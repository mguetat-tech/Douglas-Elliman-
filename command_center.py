"""Douglas Elliman Megève — Agency Command Center CLI.

Usage:
    python command_center.py                           # Interactive menu
    python command_center.py post "Chalet 450m²..."
    python command_center.py post --fast "..."
    python command_center.py lead "Bonjour, je cherche..."
    python command_center.py campaign "..." --weeks 4
    python command_center.py market "Tendances hiver 2025"
    python command_center.py source "Chalets >€5M, quartier Jaillet"
    python command_center.py brief "3 posts publiés, 2 leads qualifiés..."
    python command_center.py visual "Chalet 480m², ski in/ski out, vue Mont-Blanc"
    python command_center.py email "Prospect belge, budget €8-12M..." --steps 4
    python command_center.py pr "Vente record €15M, chalet Mont d'Arbois"
    python command_center.py ads "Chalet 480m², ski in/ski out" --platform meta
    python command_center.py council "Faut-il baisser le prix du Chalet Étoile ?"
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

EXAMPLE_VISUAL = """
Chalet d'exception — Megève, quartier du Jaillet
Surface : 480 m² — 6 chambres en suite
Ski in / ski out direct sur les pistes du Mont d'Arbois
Vue panoramique sur le Mont-Blanc et les Aravis
Spa privatif (hammam + sauna + jacuzzi), piscine intérieure chauffée, cinéma home
Mélèze centenaire, pierre du pays, verrières contemporaines plein sud
Terrasse panoramique 80 m², cheminée double face salon/séjour
"""

EXAMPLE_EMAIL_CONTEXT = """
Prospect : M. Laurent V., entrepreneur, 45 ans, Paris (Belgique d'origine)
Intérêt : chalet familial avec piscine et ski in/ski out, budget €6–10M
Contact initial : Instagram, a commenté une publication du Chalet du Jaillet
Bien proposé : Chalet Étoile — 480m², 6 chambres, ski in/ski out, vue Mont-Blanc, €8,5M
Situation : propriété familiale depuis 2010, 3 enfants ados, skieurs confirmés
"""

EXAMPLE_PR = """
Vente record réalisée discrètement par Douglas Elliman Megève :
Chalet d'exception au Mont d'Arbois — 550m², vue à 360° — vendu €15,5M
Acquéreur : family office européen — Nouveau record au prix au m² pour Megève en 2025
Transaction réalisée hors marché, mandat exclusif, signature en 6 semaines
"""

EXAMPLE_ADS = """
Chalet Étoile — Megève, quartier du Jaillet
480m² — 6 chambres en suite — ski in/ski out Mont d'Arbois
Vue panoramique Mont-Blanc — Spa privatif — Piscine intérieure
Estimation : sur demande — Discrétion assurée — Mandat exclusif Douglas Elliman
"""

EXAMPLE_COUNCIL = (
    "Le Chalet Étoile (480m², ski in/ski out, €8,5M) est en vente depuis 3 mois "
    "sans offre sérieuse. Faut-il baisser le prix, changer la stratégie marketing, "
    "ou cibler un autre profil d'acquéreur ?"
)


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


def run_visual(center: AgencyCommandCenter, description: str) -> None:
    result = center.create_visual_brief(description)
    _separator("BRIEF VISUEL PHOTO & VIDÉO")
    print(result)


def run_email(center: AgencyCommandCenter, context: str, steps: int = 3) -> None:
    result = center.write_email_sequence(context, steps=steps)
    _separator(f"SÉQUENCE EMAIL MARKETING ({steps} EMAIL{'S' if steps > 1 else ''})")
    print(result)


def run_pr(center: AgencyCommandCenter, context: str) -> None:
    result = center.write_press_release(context)
    _separator("COMMUNIQUÉ DE PRESSE")
    print(result)


def run_ads(center: AgencyCommandCenter, description: str, platform: str = "both") -> None:
    result = center.write_ads(description, platform=platform)
    _separator(f"COPIES PUBLICITAIRES — {platform.upper()}")
    print(result)


def run_council(center: AgencyCommandCenter, question: str) -> None:
    result = center.convene_council(question)
    from council.members import MEMBERS, CHAIRMAN
    for member in MEMBERS:
        _separator(f"{member.name.upper()} — {member.title}")
        print(result["responses"][member.name])
    _separator("ÉVALUATIONS CROISÉES")
    for member in MEMBERS:
        print(f"\n── {member.name} ──")
        print(result["rankings"][member.name])
    _separator(f"SYNTHÈSE — {CHAIRMAN.name}, {CHAIRMAN.title}")
    print(result["synthesis"])


def interactive_menu(center: AgencyCommandCenter) -> None:
    menu = """
╔══════════════════════════════════════════════════════════╗
║     DOUGLAS ELLIMAN MEGÈVE — AGENCY COMMAND CENTER       ║
╚══════════════════════════════════════════════════════════╝

  ── SALES TEAM & COMMAND CENTER ──────────────────────────
  1  Créer un post Instagram
  2  Qualifier un lead entrant
  3  Planifier une campagne multi-semaines
  4  Analyse de marché
  5  Sourcing hors marché
  6  Briefing exécutif

  ── AI MARKETING SUITE ───────────────────────────────────
  7  Brief visuel (photo & vidéo)
  8  Séquence email marketing
  9  Communiqué de presse
 10  Copies publicitaires (Meta / Google Ads)

  ── CONSEIL STRATÉGIQUE ──────────────────────────────────
 11  Convoquer le conseil (4 experts + Président)

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

    elif choice == "7":
        print("\nDécrivez le bien à shooter (Entrée vide = exemple) :")
        desc = input("> ").strip() or EXAMPLE_VISUAL
        run_visual(center, desc)

    elif choice == "8":
        print("\nContexte prospect + bien (Entrée vide = exemple) :")
        context = input("> ").strip() or EXAMPLE_EMAIL_CONTEXT
        steps_str = input("Nombre d'emails [3] : ").strip()
        steps = int(steps_str) if steps_str.isdigit() else 3
        run_email(center, context, steps=steps)

    elif choice == "9":
        print("\nSujet du communiqué (Entrée vide = exemple) :")
        context = input("> ").strip() or EXAMPLE_PR
        run_pr(center, context)

    elif choice == "10":
        print("\nDécrivez le bien à promouvoir (Entrée vide = exemple) :")
        desc = input("> ").strip() or EXAMPLE_ADS
        platform = input("Plateforme — meta / google / both [both] : ").strip() or "both"
        run_ads(center, desc, platform=platform)

    elif choice == "11":
        print("\nQuestion stratégique à soumettre au conseil (Entrée vide = exemple) :")
        question = input("> ").strip() or EXAMPLE_COUNCIL
        run_council(center, question)

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

    elif command == "visual":
        description = " ".join(args[1:]) if len(args) > 1 else EXAMPLE_VISUAL
        run_visual(center, description)

    elif command == "email":
        remaining = args[1:]
        steps = 3
        if "--steps" in remaining:
            idx = remaining.index("--steps")
            if idx + 1 < len(remaining):
                steps = int(remaining[idx + 1])
                remaining = remaining[:idx] + remaining[idx + 2:]
        context = " ".join(remaining) if remaining else EXAMPLE_EMAIL_CONTEXT
        run_email(center, context, steps=steps)

    elif command == "pr":
        context = " ".join(args[1:]) if len(args) > 1 else EXAMPLE_PR
        run_pr(center, context)

    elif command == "ads":
        remaining = args[1:]
        platform = "both"
        if "--platform" in remaining:
            idx = remaining.index("--platform")
            if idx + 1 < len(remaining):
                platform = remaining[idx + 1]
                remaining = remaining[:idx] + remaining[idx + 2:]
        description = " ".join(remaining) if remaining else EXAMPLE_ADS
        run_ads(center, description, platform=platform)

    elif command == "council":
        question = " ".join(args[1:]) if len(args) > 1 else EXAMPLE_COUNCIL
        run_council(center, question)

    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
