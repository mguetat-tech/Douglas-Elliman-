"""Douglas Elliman Megève — AI Sales Team CLI.

Usage:
    # Generate a full Instagram post (strategy + caption + hashtags)
    python main.py post "Chalet 450m², 6 chambres, ski in/ski out, vue Mont-Blanc, ~€8M"

    # Skip strategy step for a faster caption+hashtags only
    python main.py post --fast "Description du bien..."

    # Qualify an incoming lead / inquiry
    python main.py lead "Bonjour, je cherche un chalet 4-5 chambres avec vue..."

    # Run with example data
    python main.py
"""

import sys
from dotenv import load_dotenv
from ai_sales_team import AISalesTeam

load_dotenv()

EXAMPLE_PROPERTY = """
Chalet d'exception — Megève, quartier du Jaillet
Surface : 480 m² — 6 chambres en suite
Ski in / ski out direct sur les pistes du Mont d'Arbois
Vue panoramique sur le Mont-Blanc et les Aravis
Spa privatif, piscine intérieure chauffée, cinéma home
Matériaux nobles : mélèze centenaire, pierre du pays, verrières contemporaines
Estimation : sur demande
"""

EXAMPLE_INQUIRY = """
Bonjour, j'ai vu vos publications sur Instagram et je suis très intéressé par Megève.
Je cherche quelque chose de vraiment exclusif pour ma famille — 4 à 5 chambres minimum,
avec de la vue et idéalement proche des pistes. Budget assez flexible.
Je suis disponible pour une visite en janvier si possible. Merci.
"""


def _separator(title: str) -> None:
    print(f"\n{'='*60}")
    print(title)
    print("=" * 60)


def run_post(description: str, fast: bool = False) -> None:
    team = AISalesTeam()
    result = team.create_instagram_post(description, skip_strategy=fast)

    if "strategy" in result:
        _separator("STRATÉGIE DE CONTENU")
        print(result["strategy"])

    _separator("LÉGENDE INSTAGRAM")
    print(result["caption"])

    _separator("HASHTAGS")
    print(result["hashtags"])


def run_lead(inquiry: str) -> None:
    team = AISalesTeam()
    result = team.qualify_lead(inquiry)
    _separator("QUALIFICATION DU LEAD")
    print(result)


def main() -> None:
    args = sys.argv[1:]

    if not args:
        # Demo mode
        print("=== DEMO : Création de post Instagram ===")
        run_post(EXAMPLE_PROPERTY)
        return

    command = args[0]

    if command == "post":
        remaining = args[1:]
        fast = "--fast" in remaining
        remaining = [a for a in remaining if a != "--fast"]
        description = " ".join(remaining) if remaining else EXAMPLE_PROPERTY
        run_post(description, fast=fast)

    elif command == "lead":
        inquiry = " ".join(args[1:]) if len(args) > 1 else EXAMPLE_INQUIRY
        run_lead(inquiry)

    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
