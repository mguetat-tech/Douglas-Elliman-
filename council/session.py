import anthropic
from concurrent.futures import ThreadPoolExecutor, as_completed

from .members import MEMBERS, CHAIRMAN, AGENCY_CONTEXT, CouncilMember

MODEL = "claude-opus-4-7"


def _system(member: CouncilMember) -> list[dict]:
    return [
        {"type": "text", "text": AGENCY_CONTEXT, "cache_control": {"type": "ephemeral"}},
        {"type": "text", "text": member.prompt},
    ]


def _stage1_response(client: anthropic.Anthropic, member: CouncilMember, question: str) -> str:
    with client.messages.stream(
        model=MODEL,
        max_tokens=1024,
        thinking={"type": "adaptive"},
        system=_system(member),
        messages=[{"role": "user", "content": question}],
    ) as stream:
        return stream.get_final_message().content[-1].text


def _stage2_ranking(
    client: anthropic.Anthropic,
    member: CouncilMember,
    question: str,
    responses: dict[str, str],
) -> str:
    letters = list("ABCD")
    names = list(responses.keys())
    anon = "\n\n".join(
        f"Membre {letters[i]} :\n{responses[names[i]]}" for i in range(len(names))
    )
    prompt = (
        f"Question posée au conseil :\n{question}\n\n"
        f"Réponses anonymisées de tes collègues :\n\n{anon}\n\n"
        "Classe ces réponses de la meilleure à la moins bonne (A, B, C, D) "
        "et justifie brièvement ton classement. Sois objectif et critique même "
        "envers les idées qui rejoignent les tiennes."
    )
    response = client.messages.create(
        model=MODEL,
        max_tokens=512,
        system=_system(member),
        messages=[{"role": "user", "content": prompt}],
    )
    return next(b.text for b in response.content if b.type == "text")


def _stage3_synthesis(
    client: anthropic.Anthropic,
    question: str,
    responses: dict[str, str],
    rankings: dict[str, str],
) -> str:
    member_map = {m.name: m.title for m in MEMBERS}
    responses_text = "\n\n".join(
        f"**{name}** ({member_map[name]}) :\n{text}"
        for name, text in responses.items()
    )
    rankings_text = "\n\n".join(
        f"**{name}** :\n{text}" for name, text in rankings.items()
    )
    prompt = (
        f"Question soumise au conseil :\n{question}\n\n"
        f"━━ RÉPONSES DES MEMBRES ━━\n\n{responses_text}\n\n"
        f"━━ ÉVALUATIONS CROISÉES ━━\n\n{rankings_text}\n\n"
        "Synthétise ces perspectives en une recommandation finale claire "
        "et actionnable pour Douglas Elliman Megève."
    )
    with client.messages.stream(
        model=MODEL,
        max_tokens=1500,
        thinking={"type": "adaptive"},
        system=_system(CHAIRMAN),
        messages=[{"role": "user", "content": prompt}],
    ) as stream:
        return stream.get_final_message().content[-1].text


class CouncilSession:
    """Three-stage multi-expert deliberation: respond → rank → synthesize."""

    def __init__(self) -> None:
        self._client = anthropic.Anthropic()

    def deliberate(self, question: str) -> dict:
        """Run full council deliberation and return structured results."""

        # Stage 1 — parallel responses
        print(f"⚖️  Le conseil délibère… ({len(MEMBERS)} membres consultés)")
        responses: dict[str, str] = {}
        with ThreadPoolExecutor(max_workers=len(MEMBERS)) as executor:
            futures = {
                executor.submit(_stage1_response, self._client, m, question): m.name
                for m in MEMBERS
            }
            for future in as_completed(futures):
                name = futures[future]
                responses[name] = future.result()
                print(f"  ✓ {name}")

        # Preserve declaration order
        responses = {m.name: responses[m.name] for m in MEMBERS}

        # Stage 2 — parallel peer rankings
        print("🔍  Évaluation croisée en cours…")
        rankings: dict[str, str] = {}
        with ThreadPoolExecutor(max_workers=len(MEMBERS)) as executor:
            futures = {
                executor.submit(_stage2_ranking, self._client, m, question, responses): m.name
                for m in MEMBERS
            }
            for future in as_completed(futures):
                name = futures[future]
                rankings[name] = future.result()
                print(f"  ✓ {name}")

        rankings = {m.name: rankings[m.name] for m in MEMBERS}

        # Stage 3 — chairman synthesis
        print("🏛️  Synthèse du Président du Conseil…")
        synthesis = _stage3_synthesis(self._client, question, responses, rankings)

        return {
            "question": question,
            "responses": responses,
            "rankings": rankings,
            "synthesis": synthesis,
        }
