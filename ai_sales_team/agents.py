import anthropic

MODEL = "claude-opus-4-7"

# Shared brand context — cached across all agents to reduce token costs
MEGEVE_CONTEXT = """Douglas Elliman est une agence immobilière de prestige internationale.
Bureau de Megève — station de ski haut de gamme dans les Alpes françaises.

Marché :
- Chalets et appartements de luxe à Megève et environs
- Prix : généralement €1M et au-delà
- Clientèle : acheteurs et vendeurs européens et internationaux fortunés
- Atouts : ski in/ski out, vue sur le Mont-Blanc, gastronomie étoilée, spa, art de vivre alpin

Ton : élégant, sophistiqué, aspirationnel. Jamais trop commercial.
Langue : français en priorité, anglais pour la clientèle internationale."""


def _system_with_cache(agent_prompt: str) -> list[dict]:
    """Build system prompt with shared brand context cached."""
    return [
        {
            "type": "text",
            "text": MEGEVE_CONTEXT,
            "cache_control": {"type": "ephemeral"},
        },
        {"type": "text", "text": agent_prompt},
    ]


class ContentStrategist:
    """Plans Instagram content strategy for a property listing."""

    _PROMPT = """Tu es le Stratège de Contenu Instagram pour Douglas Elliman Megève.

Pour chaque bien immobilier, tu définis :
- Format recommandé : post simple, carrousel, reel ou story
- Angle narratif principal (lifestyle, exclusivité, vue, investissement, ski, etc.)
- Émotions à cibler chez l'acheteur idéal
- Meilleur moment de publication (jour/heure)
- Appel à l'action principal

Sois concis et actionnable."""

    def __init__(self, client: anthropic.Anthropic) -> None:
        self.client = client

    def plan(self, property_description: str) -> str:
        response = self.client.messages.create(
            model=MODEL,
            max_tokens=1024,
            thinking={"type": "adaptive"},
            system=_system_with_cache(self._PROMPT),
            messages=[
                {"role": "user", "content": f"Bien à promouvoir :\n{property_description}"}
            ],
        )
        return next(b.text for b in response.content if b.type == "text")


class Copywriter:
    """Writes compelling Instagram captions for luxury property listings."""

    _PROMPT = """Tu es le Rédacteur Expert de Douglas Elliman Megève.

Tu crées des légendes Instagram captivantes pour des propriétés de luxe.

Chaque légende :
- Hook fort dès la première ligne
- Peint un lifestyle aspirationnel sans énumérer des specs techniques
- Inclut un appel à l'action discret (« Contactez-nous en privé », « Lien en bio »)
- Fait entre 150 et 300 mots
- Est rédigée en français ; propose une version anglaise courte en dessous si pertinent

Style : luxueux, authentique, évocateur."""

    def __init__(self, client: anthropic.Anthropic) -> None:
        self.client = client

    def write(self, property_description: str, strategy: str = "") -> str:
        content = f"Bien :\n{property_description}"
        if strategy:
            content += f"\n\nStratégie de contenu :\n{strategy}"

        with self.client.messages.stream(
            model=MODEL,
            max_tokens=1024,
            system=_system_with_cache(self._PROMPT),
            messages=[{"role": "user", "content": content}],
        ) as stream:
            return stream.get_final_message().content[0].text


class HashtagSpecialist:
    """Generates optimised Instagram hashtag sets."""

    _PROMPT = """Tu es le Spécialiste Hashtags Instagram de Douglas Elliman Megève.

Pour chaque post, génère 20 hashtags organisés en 3 groupes :
- 5 haute portée (>500K posts) — visibilité large
- 8 moyenne portée (10K–500K) — audience qualifiée
- 7 niche (<10K) — ultra-ciblé, meilleur taux d'engagement

Couvre : Megève/Alpes françaises, immobilier luxe, lifestyle montagne, ski, Douglas Elliman.

Retourne uniquement les hashtags, groupés et prêts à copier-coller."""

    def __init__(self, client: anthropic.Anthropic) -> None:
        self.client = client

    def generate(self, property_description: str, caption: str = "") -> str:
        content = f"Bien : {property_description}"
        if caption:
            content += f"\n\nLégende (extrait) : {caption[:300]}"

        response = self.client.messages.create(
            model=MODEL,
            max_tokens=512,
            system=_system_with_cache(self._PROMPT),
            messages=[{"role": "user", "content": content}],
        )
        return next(b.text for b in response.content if b.type == "text")


class LeadQualifier:
    """Qualifies incoming prospect inquiries and suggests follow-up actions."""

    _PROMPT = """Tu es le Qualificateur de Leads pour Douglas Elliman Megève.

Tu analyses une demande entrante (DM Instagram, commentaire, email) et fournis :
1. Score : Froid / Tiède / Chaud / Très Chaud
2. Profil estimé (acheteur résidence principale, secondaire, investisseur, etc.)
3. Besoins identifiés
4. Prochaines étapes recommandées pour l'équipe commerciale
5. Suggestion de réponse personnalisée (français et/ou anglais selon le contexte)

Critères : budget apparent, urgence, sérieux de la démarche, adéquation avec l'offre Megève."""

    def __init__(self, client: anthropic.Anthropic) -> None:
        self.client = client

    def qualify(self, inquiry: str) -> str:
        response = self.client.messages.create(
            model=MODEL,
            max_tokens=1024,
            thinking={"type": "adaptive"},
            system=_system_with_cache(self._PROMPT),
            messages=[{"role": "user", "content": f"Demande à qualifier :\n{inquiry}"}],
        )
        return next(b.text for b in response.content if b.type == "text")
