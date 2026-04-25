"""Douglas Elliman Megève — Agency Command Center CLI.

Usage:
    python command_center.py                        # Interactive menu
    python command_center.py post "Chalet 450m²..."
    python command_center.py post --fast "..."
    python command_center.py lead "Bonjour, je cherche..."
    python command_center.py campaign "Chalet 450m²..." --weeks 4
    python command_center.py market "Tendances saison hiver 2025"
    python command_center.py source "Chalets >€5M, moins de 10 ans, quartier Jaillet"
    python command_center.py brief "3 posts publiés, 2 leads qualifiés, 1 visite organisée"
"""

import sys
from dotenv import load_dotenv
from command_center import AgencyCommandCenter

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

EXAMPLE_MARKET = "Tendances du marché des chalets de luxe à Megève pour la saison hiver 2025-2026."

EXAMPLE_SOURCE = "Chalets de plus de €5M construits avant 2010, quartiers Jaillet ou Mont d'Arbois."

EXAMPLE_BRIEF = """
Cette semaine : 3 posts Instagram publiés (chalet Jaillet, appartement centre, chalet Mont d'Arbois).
2 leads qualifiés dont 1 acheteur belge très sérieux (budget €8-12M, visite confirmée).
1 bien hors marché identifié — propriétaire potentiellement vendeur d'ici 6 mois.
Engagement Instagram +18% vs semaine précédente.
"""


def _separator(title: str) -> None:
    print(f"\n{'='*60}")
    print(title)
    print("=" * 60)


def run_post(center: AgencyCommandCenter, description: str, fast: bool = False) -> None:
    result = center.create_post(description, fast=fast)
    if "strategy" in result:
        _separator("STRATÉGIE DE CONTENU")
        print(result["strategy"])
    _separator("LÉGENDE INSTAGRAM")
    print(result["caption"])
    _separator("HASHTAGS")
    print(result["hashtags"])


def run_lead(center: AgencyCommandCenter, inquiry: str) -> None:
    result = center.qualify_lead(inquiry)
    _separator("QUALIFICATION DU LEAD")
    print(result)


def run_campaign(center: AgencyCommandCenter, description: str, weeks: int = 2) -> None:
    result = center.plan_campaign(description, weeks=weeks)
    _separator(f"PLAN DE CAMPAGNE ({weeks} SEMAINE{'S' if weeks > 1 else ''})")
    print(result)


def run_market(center: AgencyCommandCenter, topic: str) -> None:
    result = center.analyze_market(topic)
    _separator("ANALYSE DE MARCHÉ")
    print(result)


def run_source(center: AgencyCommandCenter, criteria: str) -> None:
    result = center.source_deals(criteria)
    _separator("STRATÉGIE D'ACQUISITION HORS MARCHÉ")
    print(result)


def run_brief(center: AgencyCommandCenter, context: str) -> None:
    result = center.executive_brief(context)
    _separator("BRIEFING EXÉCUTIF")
    print(result)


def interactive_menu(center: AgencyCommandCenter) -> None:
    menu = """
╔══════════════════════════════════════════════════════════╗
║     DOUGLAS ELLIMAN MEGÈVE — AGENCY COMMAND CENTER       ║
╚══════════════════════════════════════════════════════════╝

  1  Créer un post Instagram
  2  Qualifier un lead entrant
  3  Planifier une campagne multi-semaines
  4  Analyse de marché
  5  Sourcing hors marché
  6  Briefing exécutif
  0  Quitter

"""
    print(menu)
    choice = input("Votre choix : ").strip()

    if choice == "0":
        print("À bientôt.")
        return

    elif choice == "1":
        print("\nDécrivez le bien (Entrée vide = exemple) :")
        desc = input("> ").strip() or EXAMPLE_PROPERTY
        fast = input("Mode rapide sans stratégie ? (o/N) : ").strip().lower() == "o"
        run_post(center, desc, fast=fast)

    elif choice == "2":
        print("\nCollez l'inquiry du prospect (Entrée vide = exemple) :")
        inquiry = input("> ").strip() or EXAMPLE_INQUIRY
        run_lead(center, inquiry)

    elif choice == "3":
        print("\nDécrivez le bien (Entrée vide = exemple) :")
        desc = input("> ").strip() or EXAMPLE_PROPERTY
        weeks_str = input("Nombre de semaines [2] : ").strip()
        weeks = int(weeks_str) if weeks_str.isdigit() else 2
        run_campaign(center, desc, weeks=weeks)

    elif choice == "4":
        print("\nSujet d'analyse (Entrée vide = exemple) :")
        topic = input("> ").strip() or EXAMPLE_MARKET
        run_market(center, topic)

    elif choice == "5":
        print("\nCritères de sourcing (Entrée vide = exemple) :")
        criteria = input("> ").strip() or EXAMPLE_SOURCE
        run_source(center, criteria)

    elif choice == "6":
        print("\nActivités à synthétiser (Entrée vide = exemple) :")
        context = input("> ").strip() or EXAMPLE_BRIEF
        run_brief(center, context)

    else:
        print("Choix invalide.")


def main() -> None:
    args = sys.argv[1:]
    center = AgencyCommandCenter()

    if not args:
        interactive_menu(center)
        return

    command = args[0]

    if command == "post":
        remaining = args[1:]
        fast = "--fast" in remaining
        remaining = [a for a in remaining if a != "--fast"]
        description = " ".join(remaining) if remaining else EXAMPLE_PROPERTY
        run_post(center, description, fast=fast)

    elif command == "lead":
        inquiry = " ".join(args[1:]) if len(args) > 1 else EXAMPLE_INQUIRY
        run_lead(center, inquiry)

    elif command == "campaign":
        remaining = args[1:]
        weeks = 2
        if "--weeks" in remaining:
            idx = remaining.index("--weeks")
            if idx + 1 < len(remaining):
                weeks = int(remaining[idx + 1])
                remaining = remaining[:idx] + remaining[idx + 2:]
        description = " ".join(remaining) if remaining else EXAMPLE_PROPERTY
        run_campaign(center, description, weeks=weeks)

    elif command == "market":
        topic = " ".join(args[1:]) if len(args) > 1 else EXAMPLE_MARKET
        run_market(center, topic)

    elif command == "source":
        criteria = " ".join(args[1:]) if len(args) > 1 else EXAMPLE_SOURCE
        run_source(center, criteria)

    elif command == "brief":
        context = " ".join(args[1:]) if len(args) > 1 else EXAMPLE_BRIEF
        run_brief(center, context)

    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
