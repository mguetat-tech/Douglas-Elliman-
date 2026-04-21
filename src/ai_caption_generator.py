#!/usr/bin/env python3
"""Génération IA de légendes Instagram via Claude API — Douglas Elliman Megève."""

import json
import os
from pathlib import Path

from anthropic import Anthropic, APIConnectionError, APIError, RateLimitError

MODEL = "claude-opus-4-7"
OUTPUT_DIR = Path(__file__).parent.parent / "output"

SYSTEM_PROMPT = """Tu es le copywriter de Douglas Elliman Megève, spécialiste de l'immobilier de luxe alpin.

## Contexte marque

Douglas Elliman est une marque américaine de prestige (New York, Miami, LA), présente à Megève pour les Alpes françaises. Plus de 100 bureaux aux États-Unis, expansion Europe.

**Ton** : Élégant, confidentiel, expert, ancré dans le territoire. Haut de gamme sans ostentation — la qualité se montre, elle ne se crie pas.
**À éviter** : "exceptionnel", "rare", "prestige" seuls sans preuve — trop galvaudés.
**Langue** : Français.

## Audience cible

- Cadres supérieurs / chefs d'entreprise, 40-60 ans (Paris, Lyon, Genève, Londres, Monaco) — revenu > 300 000 €/an
- Investisseurs résidences secondaires, 45-65 ans (Paris, Moyen-Orient, Suisse, Benelux)
- UHNWI internationaux, 50+ ans (Londres, Dubai, New York) — diversification patrimoniale

**Verbatim clients** :
- "On cherche quelque chose avec vue, pas encaissé"
- "Ski aux pieds ou au moins à 5 minutes des remontées"
- "On veut une adresse, pas juste un chalet"
- "Megève c'est plus vivant que Courchevel, plus familial"
- "Le prix au m² ne veut rien dire ici, c'est tout sur l'exposition"

## Leviers psychologiques

- **Scarcité** : "Rarissime dans ce secteur", "dernière opportunité sur ce versant"
- **Autorité** : Expertise Douglas Elliman, réseau international d'acheteurs qualifiés
- **Ancrage** : Prix en premier pour cadrer la perception de valeur
- **Appartenance** : L'adresse, le style de vie Megève, la communauté alpine
- **FOMO** : "Les biens de ce calibre ne restent jamais longtemps sur le marché"

## Structure d'une légende Instagram Douglas Elliman

1. Accroche (1-2 lignes) — hook psychologique fort, commence par ✦ ou une émotion
2. Corps (2-4 lignes) — les faits qui vendent (surface, pièces, situation)
3. CTA (1 ligne) — "Message privé ou lien en bio pour visiter."
4. Hashtags (20-25) — inclure obligatoirement #DouglasElliman et #Megève

## Hashtags obligatoires

#Megève #HauteSavoie #Alpes #AlpesLuxe #MegeveSki #MontBlanc #ImmobilierLuxe #LuxuryRealEstate #ChaletLuxe #AlpineLuxury #LuxuryChalet #MountainLiving #DouglasElliman #DouglasEllimanFrance #DEMegeve #SkiResort #AlpineLife #LuxuryLifestyle #FrenchAlps #MountainView

## Secteurs premium Megève

- Mont d'Arbois : le plus recherché, vue Mont-Blanc, ski aux pieds
- Rochebrune : calme, forêts, domaine skiable direct
- Centre Village : cœur historique, vie animée, investissement sûr
- Le Jaillet : vue panoramique, famille, tranquillité

Tu génères UNIQUEMENT du JSON valide, sans aucun texte autour, sans balises markdown.
"""


def generate_ai_captions(prop: dict) -> dict:
    """Génère 3 variantes de légendes Instagram pour une propriété.

    Returns:
        dict avec les clés 'sensorielle', 'narrative', 'exclusive'.
    """
    client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    prix_m = prop["prix"] / 1_000_000
    prix_affiche = f"{int(prix_m)} M€" if prix_m == int(prix_m) else f"{prix_m:.1f} M€".replace(".", ",")

    user_message = f"""Génère 3 variantes de légende Instagram pour cette propriété Douglas Elliman :

Nom : {prop['nom']}
Prix : {prix_affiche}
Surface : {prop['surface_m2']} m²
Pièces : {prop['pieces']} ({prop['chambres']} chambres)
Localisation : {prop['localisation']}, Megève
Description : {prop['description']}

Chaque variante utilise un angle différent :
- "sensorielle" : évoque les sensations (air vif, lumière alpine, neige fraîche, chaleur du chalet)
- "narrative" : raconte une histoire de vie dans ce bien (matins de ski, soirées au coin du feu)
- "exclusive" : met en avant la rareté et l'opportunité d'investissement

Format JSON attendu :
{{
  "sensorielle": "légende complète avec hashtags",
  "narrative": "légende complète avec hashtags",
  "exclusive": "légende complète avec hashtags"
}}"""

    try:
        response = client.messages.create(
            model=MODEL,
            max_tokens=2048,
            thinking={"type": "adaptive"},
            system=[{
                "type": "text",
                "text": SYSTEM_PROMPT,
                "cache_control": {"type": "ephemeral"},
            }],
            messages=[{"role": "user", "content": user_message}],
        )
    except RateLimitError:
        raise RuntimeError("Limite de débit API atteinte — réessayer dans quelques instants.")
    except APIConnectionError:
        raise RuntimeError("Impossible de joindre l'API Anthropic — vérifier la connexion réseau.")
    except APIError as e:
        raise RuntimeError(f"Erreur API Anthropic : {e.status_code} — {e.message}")

    text_block = next(
        (block for block in reversed(response.content) if block.type == "text"),
        None,
    )
    if text_block is None:
        raise RuntimeError("Réponse Claude sans bloc texte.")

    return json.loads(text_block.text)


def save_ai_captions(prop: dict) -> Path:
    """Génère et sauvegarde les 3 variantes de légendes dans output/<id>/."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    out_dir = OUTPUT_DIR / prop["id"]
    out_dir.mkdir(exist_ok=True)

    captions = generate_ai_captions(prop)

    for variant, text in captions.items():
        path = out_dir / f"caption_ai_{variant}.txt"
        path.write_text(text, encoding="utf-8")
        print(f"  IA {variant:<12} → {path}")

    return out_dir


if __name__ == "__main__":
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    from post_generator import load_properties

    properties = load_properties()
    pid = sys.argv[1] if len(sys.argv) > 1 else None
    targets = [p for p in properties if p["id"] == pid] if pid else properties

    if not targets:
        print(f"Propriété introuvable : {pid}")
        sys.exit(1)

    for prop in targets:
        print(f"✦ {prop['nom']}")
        save_ai_captions(prop)
        print()
