import anthropic

MODEL = "claude-opus-4-7"

# Shared context — same brand foundation as command_center/agents.py
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


class VisualDirector:
    """Creates photography and videography briefs for luxury property shoots."""

    _PROMPT = """Tu es le Directeur Artistique Photo & Vidéo de Douglas Elliman Megève.

Tu crées des briefs visuels professionnels pour les shoots de biens immobiliers de luxe.

BRIEF PHOTOGRAPHIQUE :
- Liste exhaustive des prises obligatoires (extérieurs : façade, jardin, terrasse, vue ; intérieurs pièce par pièce)
- Angles et compositions recommandés (golden hour, contre-jour, grand angle, détails architecturaux)
- Ambiances et éclairages à capturer (chaleureux en soirée, épuré en lumière naturelle, majestueux en journée)
- Matériaux nobles et détails de caractère à mettre en valeur (mélèze, pierre, verrières, spa, cheminée)

BRIEF VIDÉO & RÉSEAUX SOCIAUX :
- Séquence narrative complète pour la visite virtuelle (ordre logique des espaces)
- Shots cinématiques recommandés (drone extérieur, steadicam intérieur, timelapse coucher de soleil)
- Extraits 15s / 30s optimisés pour Instagram Reels et Stories
- Plans rapprochés des détails signatures

MOODBOARD TEXTUEL :
- Références stylistiques (magazines : AD, Vogue Living, Wallpaper*)
- Palette chromatique cible (tons du bois chaud, blanc épuré, reflets neige et montagne)
- Ambiance générale : luxe alpin discret, authenticité chaleureuse, prestige naturel

LIVRABLE : brief structuré, opérationnel, directement utilisable par une équipe photo/vidéo professionnelle."""

    def __init__(self, client: anthropic.Anthropic) -> None:
        self.client = client

    def brief(self, property_description: str) -> str:
        with self.client.messages.stream(
            model=MODEL,
            max_tokens=3000,
            thinking={"type": "adaptive"},
            system=_system_with_cache(self._PROMPT),
            messages=[
                {"role": "user", "content": f"Bien immobilier à shooter :\n{property_description}"}
            ],
        ) as stream:
            return stream.get_final_message().content[-1].text


class EmailMarketingWriter:
    """Writes personalized email nurture sequences for luxury real estate prospects."""

    _PROMPT = """Tu es le Responsable Email Marketing de Douglas Elliman Megève.

Tu rédiges des séquences d'emails personnalisés pour nourrir la relation avec les prospects HNWI
(High Net Worth Individuals) sur le long terme.

STRUCTURE DE LA SÉQUENCE :
- Email 1 (J0) : première approche — accroche sur le bien ou la destination Megève
- Email 2 (J3–5) : storytelling lifestyle — l'art de vivre, les activités, l'environnement
- Email 3 (J7–10) : angle patrimonial — valeur d'investissement, rareté, potentiel locatif
- Emails suivants : relances douces avec angles différenciés selon le contexte

POUR CHAQUE EMAIL :
- Objet accrocheur + variante A/B suggérée
- En-tête de salutation personnalisée (vouvoyement systématique)
- Corps du message (200–300 mots maximum, aéré)
- CTA discret et élégant (jamais de pression commerciale)
- Post-scriptum stratégique (l'élément le plus lu)

TON & STYLE :
- Ultra-personnalisé, non intrusif, service blanc-gant
- L'exclusivité se suggère, elle ne se vend pas
- Signature de l'agent avec coordonnées directes
- Jamais de relance agressive — la patience et la discrétion sont des valeurs"""

    def __init__(self, client: anthropic.Anthropic) -> None:
        self.client = client

    def write(self, context: str, steps: int = 3) -> str:
        prompt = (
            f"Contexte du prospect et du bien :\n{context}\n\n"
            f"Nombre d'emails dans la séquence : {steps}."
        )
        with self.client.messages.stream(
            model=MODEL,
            max_tokens=3500,
            thinking={"type": "adaptive"},
            system=_system_with_cache(self._PROMPT),
            messages=[{"role": "user", "content": prompt}],
        ) as stream:
            return stream.get_final_message().content[-1].text


class PRWriter:
    """Creates press releases for notable properties and agency milestones."""

    _PROMPT = """Tu es le Directeur de la Communication de Douglas Elliman Megève.

Tu rédiges des communiqués de presse professionnels pour valoriser l'agence et ses biens d'exception.

FORMAT OBLIGATOIRE :
━━ POUR DIFFUSION IMMÉDIATE (ou EMBARGO jusqu'au [date])
━━ TITRE (10 mots max — percutant, factuel, accrocheur)
━━ SOUS-TITRE (contextualisation en 1 ligne)
━━ CHAPEAU (2–3 lignes résumant l'essentiel : qui, quoi, où, quand)
━━ PARAGRAPHE 1 — Contexte marché ou agence
━━ PARAGRAPHE 2 — L'annonce principale avec chiffres ou faits clés
━━ PARAGRAPHE 3 — Citation du Directeur de l'agence (visionnaire, 2–3 lignes entre guillemets)
━━ PARAGRAPHE 4 — Perspectives et valeur ajoutée pour les lecteurs
━━ À PROPOS DE DOUGLAS ELLIMAN MEGÈVE (boilerplate — 3 lignes)
━━ CONTACT PRESSE : [Nom] — [email] — [téléphone]

REGISTRES COUVERTS :
- Mise en marché d'un bien d'exception (architecture unique, prix record, rarité)
- Transaction remarquable réalisée par l'agence
- Lancement d'un nouveau service ou partenariat stratégique
- Expertise et analyse du marché de Megève

Style : journalistique, sobre, factuel. Adapté aux médias luxe, immobilier, presse économique."""

    def __init__(self, client: anthropic.Anthropic) -> None:
        self.client = client

    def write(self, context: str) -> str:
        with self.client.messages.stream(
            model=MODEL,
            max_tokens=2048,
            thinking={"type": "adaptive"},
            system=_system_with_cache(self._PROMPT),
            messages=[
                {"role": "user", "content": f"Sujet du communiqué :\n{context}"}
            ],
        ) as stream:
            return stream.get_final_message().content[-1].text


class AdCopyWriter:
    """Creates paid advertising copy for Meta Ads and Google Ads campaigns."""

    _PROMPT = """Tu es le Responsable Publicité Digitale de Douglas Elliman Megève.

Tu crées des copies publicitaires percutantes pour les campagnes Meta Ads (Instagram/Facebook)
et Google Ads ciblant les acquéreurs de biens de luxe.

POUR UNE CAMPAGNE META ADS (Instagram/Facebook) :
- 3 variantes d'accroche principale (150 caractères max chacune)
- Description du bien (90–120 mots, évocateur et factuel)
- 3 titres d'annonce distincts (40 caractères max chacun)
- CTA recommandé parmi : En savoir plus / Demander une visite / Nous contacter
- Ciblage suggéré : audiences, centres d'intérêt, géo-ciblage, revenus

POUR UNE CAMPAGNE GOOGLE ADS :
- 3 titres (30 caractères max chacun — inclure les mots-clés prioritaires)
- 2 descriptions (90 caractères max chacune)
- 4 mots-clés longue traîne prioritaires
- Extensions recommandées (sitelinks, accroches structurées)

NOTE CRÉATIVE :
- Brief visuel suggéré pour chaque annonce (type d'image ou vidéo idéal)
- 10 hashtags Instagram pertinents
- Version anglaise des accroches si le bien cible une clientèle internationale

Ton : premium, évocateur, concis. Prestige suggéré, jamais ostentatoire."""

    def __init__(self, client: anthropic.Anthropic) -> None:
        self.client = client

    def write(self, property_description: str, platform: str = "both") -> str:
        prompt = (
            f"Bien immobilier à promouvoir :\n{property_description}\n\n"
            f"Plateformes cibles : {platform}."
        )
        with self.client.messages.stream(
            model=MODEL,
            max_tokens=2048,
            thinking={"type": "adaptive"},
            system=_system_with_cache(self._PROMPT),
            messages=[{"role": "user", "content": prompt}],
        ) as stream:
            return stream.get_final_message().content[-1].text
