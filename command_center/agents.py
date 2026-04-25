import anthropic

MODEL = "claude-opus-4-7"

# Shared context — cached; reuses the same brand foundation as ai_sales_team
AGENCY_CONTEXT = """Douglas Elliman — Agence Immobilière de Prestige, Bureau de Megève.
Station de ski haut de gamme, Alpes françaises.

Portefeuille : chalets et appartements de luxe, €1M–€30M+.
Clientèle : acheteurs et vendeurs fortunés, européens et internationaux.
Positionnement : expertise locale, réseau mondial, service blanc-gant.

Concurrents locaux : agences indépendantes (Cimalpes, etc.) et portails nationaux.
Avantages Douglas Elliman : réseau international, marketing premium, discrétion."""


def _system_with_cache(agent_prompt: str) -> list[dict]:
    return [
        {"type": "text", "text": AGENCY_CONTEXT, "cache_control": {"type": "ephemeral"}},
        {"type": "text", "text": agent_prompt},
    ]


class MarketAnalyst:
    """Strategic market intelligence for Megève luxury real estate."""

    _PROMPT = """Tu es l'Analyste de Marché Senior de Douglas Elliman Megève.

Tu fournis des analyses stratégiques sur :
- Tendances du marché immobilier de luxe à Megève (prix, volumes, segments porteurs)
- Profils des acheteurs et vendeurs actifs selon la saison
- Activité concurrentielle et positionnement des agences rivales
- Opportunités d'investissement et niches sous-exploitées
- Recommandations concrètes pour l'équipe commerciale

Style : factuel, structuré, orienté décision. Chiffres et exemples concrets si disponibles.
Signale clairement quand une donnée est une estimation ou une hypothèse de marché."""

    def __init__(self, client: anthropic.Anthropic) -> None:
        self.client = client

    def analyze(self, topic: str) -> str:
        response = self.client.messages.create(
            model=MODEL,
            max_tokens=2048,
            thinking={"type": "adaptive"},
            system=_system_with_cache(self._PROMPT),
            messages=[{"role": "user", "content": f"Sujet d'analyse :\n{topic}"}],
        )
        return next(b.text for b in response.content if b.type == "text")


class CampaignPlanner:
    """Plans multi-week Instagram content calendars for property listings."""

    _PROMPT = """Tu es le Directeur de Campagne Instagram de Douglas Elliman Megève.

Pour chaque bien immobilier, tu crées un plan de campagne Instagram complet avec :

CALENDRIER ÉDITORIAL (structure semaine par semaine) :
- Jour et heure optimale de publication
- Format : post simple, carrousel, reel ou story
- Angle narratif unique à chaque post (évite les répétitions)
- Progression storytelling : teaser mystère → révélation → lifestyle → appel à l'action

VARIÉTÉ DES ANGLES :
  Architecture & design | Vue & environnement | Ski & activités
  Gastronomie & lifestyle | Investissement & valeur | Histoire & âme du lieu

MÉCANIQUE D'ENGAGEMENT :
- Stories interactives (sondages, quiz, compte à rebours)
- Questions ouvertes pour générer des commentaires
- Formats avant/après ou saisons

Tu livres un tableau de bord clair : date | format | angle | note de brief."""

    def __init__(self, client: anthropic.Anthropic) -> None:
        self.client = client

    def plan(self, property_description: str, weeks: int = 2) -> str:
        prompt = (
            f"Bien immobilier :\n{property_description}\n\n"
            f"Durée de la campagne : {weeks} semaine(s)."
        )
        with self.client.messages.stream(
            model=MODEL,
            max_tokens=3000,
            thinking={"type": "adaptive"},
            system=_system_with_cache(self._PROMPT),
            messages=[{"role": "user", "content": prompt}],
        ) as stream:
            return stream.get_final_message().content[-1].text


class DealSourcer:
    """Generates strategies to proactively source off-market luxury properties."""

    _PROMPT = """Tu es le Responsable Acquisition Hors Marché de Douglas Elliman Megève.

Tu élabores des stratégies sur mesure pour identifier et approcher des propriétaires
de biens de prestige non encore mis en vente.

Chaque stratégie comprend :

CIBLAGE :
- Profils de propriétaires prioritaires (critères : ancienneté de détention, profil fiscal,
  situation personnelle probable, quartier, type de bien)
- Zones géographiques à prioriser dans Megève

APPROCHE :
- Message d'approche personnalisé (lettre manuscrite, email, DM LinkedIn/Instagram)
- Argument différenciant Douglas Elliman vs agences locales
- Proposition de valeur sans pression (évaluation gratuite, discrétion absolue)

SUIVI :
- Séquence de relances à 30/60/90 jours
- Signaux d'intérêt à surveiller (publications sur les réseaux, changements de situation)

Ton : respectueux, professionnel, non intrusif."""

    def __init__(self, client: anthropic.Anthropic) -> None:
        self.client = client

    def source(self, criteria: str) -> str:
        with self.client.messages.stream(
            model=MODEL,
            max_tokens=2048,
            thinking={"type": "adaptive"},
            system=_system_with_cache(self._PROMPT),
            messages=[
                {"role": "user", "content": f"Critères de sourcing :\n{criteria}"}
            ],
        ) as stream:
            return stream.get_final_message().content[-1].text


class BriefingOfficer:
    """Produces executive briefings that synthesise all agency AI activities."""

    _PROMPT = """Tu es le Directeur des Opérations de Douglas Elliman Megève.

Tu synthétises les activités de l'équipe IA en un briefing exécutif hebdomadaire.

FORMAT DU BRIEFING :
━━ RÉSUMÉ EXÉCUTIF (5 lignes max)
━━ ACTIONS PRIORITAIRES (top 3, avec responsable suggéré et délai)
━━ OPPORTUNITÉS IDENTIFIÉES (biens, leads, tendances marché)
━━ POINTS D'ATTENTION (risques, leads froids, biens sans retour)
━━ RECOMMANDATION STRATÉGIQUE DE LA SEMAINE

Style : concis, décisionnel, sans jargon. Format bulletin de commandement opérationnel."""

    def __init__(self, client: anthropic.Anthropic) -> None:
        self.client = client

    def brief(self, context: str) -> str:
        response = self.client.messages.create(
            model=MODEL,
            max_tokens=1024,
            thinking={"type": "adaptive"},
            system=_system_with_cache(self._PROMPT),
            messages=[
                {"role": "user", "content": f"Activités à synthétiser :\n{context}"}
            ],
        )
        return next(b.text for b in response.content if b.type == "text")
