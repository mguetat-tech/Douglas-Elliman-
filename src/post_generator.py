#!/usr/bin/env python3
"""Générateur de posts Instagram pour Douglas Elliman Megève."""

import json
import re
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
TEMPLATES_DIR = Path(__file__).parent / "templates"
OUTPUT_DIR = Path(__file__).parent.parent / "output"

HASHTAGS = [
    "#Megève", "#HauteSavoie", "#Alpes", "#AlpesLuxe", "#MegeveSki", "#MontBlanc",
    "#ImmobilierLuxe", "#LuxuryRealEstate", "#ChaletLuxe", "#AlpineLuxury",
    "#LuxuryChalet", "#MountainLiving", "#DouglasElliman", "#DouglasEllimanFrance",
    "#DEMegeve", "#SkiResort", "#AlpineLife", "#LuxuryLifestyle", "#FrenchAlps",
    "#MountainView",
]


def format_price(prix: int) -> str:
    """Formate un prix en millions avec virgule française."""
    millions = prix / 1_000_000
    if millions == int(millions):
        return f"{int(millions)} M€"
    return f"{millions:.1f} M€".replace(".", ",")


def load_properties() -> list[dict]:
    path = DATA_DIR / "properties.json"
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def generate_caption(prop: dict) -> str:
    """Génère la légende Instagram pour une propriété."""
    prix_affiche = format_price(prop["prix"])
    lines = [
        f"✦ {prop['nom']} ✦",
        "",
        prop["description"],
        "",
        f"✦ {prix_affiche}  ✦ {prop['surface_m2']} m²  ✦ {prop['pieces']} pièces",
        f"📍 {prop['localisation']}, Megève",
        "",
        "Pour plus d'informations, contactez-nous en message privé ou via le lien en bio.",
        "",
        " ".join(HASHTAGS),
    ]
    return "\n".join(lines)


def render_html(prop: dict) -> str:
    """Remplace les variables du template HTML par les données de la propriété."""
    template_path = TEMPLATES_DIR / "post_template.html"
    html = template_path.read_text(encoding="utf-8")

    prix_affiche = format_price(prop["prix"])
    image_url = prop.get("image_url") or ""

    if image_url:
        image_block = f'<img src="{image_url}" alt="{prop["nom"]}" />'
        html = re.sub(
            r"\{\{#if image_url\}\}.*?\{\{/if\}\}",
            image_block,
            html,
            flags=re.DOTALL,
        )
    else:
        placeholder_block = '<div class="image-placeholder"><span class="placeholder-icon">🏔️</span></div>'
        html = re.sub(
            r"\{\{#if image_url\}\}.*?\{\{/if\}\}",
            placeholder_block,
            html,
            flags=re.DOTALL,
        )

    replacements = {
        "{{nom}}": prop["nom"],
        "{{prix_affiche}}": prix_affiche,
        "{{surface_m2}}": str(prop["surface_m2"]),
        "{{pieces}}": str(prop["pieces"]),
        "{{chambres}}": str(prop["chambres"]),
        "{{localisation}}": prop["localisation"],
        "{{description}}": prop["description"],
    }
    for key, value in replacements.items():
        html = html.replace(key, value)

    return html


def generate_post(property_id: str | None = None) -> None:
    """Génère le post Instagram (légende + HTML) pour une ou toutes les propriétés."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    properties = load_properties()

    targets = (
        [p for p in properties if p["id"] == property_id]
        if property_id
        else properties
    )

    if not targets:
        print(f"Propriété introuvable : {property_id}")
        return

    for prop in targets:
        prop_id = prop["id"]
        out_dir = OUTPUT_DIR / prop_id
        out_dir.mkdir(exist_ok=True)

        caption = generate_caption(prop)
        caption_path = out_dir / "caption.txt"
        caption_path.write_text(caption, encoding="utf-8")

        html = render_html(prop)
        html_path = out_dir / "post.html"
        html_path.write_text(html, encoding="utf-8")

        print(f"✓ {prop['nom']}")
        print(f"  Légende → {caption_path}")
        print(f"  Visuel  → {html_path}")
        print()


if __name__ == "__main__":
    import sys
    pid = sys.argv[1] if len(sys.argv) > 1 else None
    generate_post(pid)
