import anthropic
from .agents import ContentStrategist, Copywriter, HashtagSpecialist, LeadQualifier


class AISalesTeam:
    """Douglas Elliman Megève — AI Sales Team coordinator.

    Orchestrates four specialist agents:
    - ContentStrategist  : defines the Instagram content angle
    - Copywriter         : writes the caption
    - HashtagSpecialist  : generates optimised hashtags
    - LeadQualifier      : scores and responds to incoming inquiries
    """

    def __init__(self) -> None:
        client = anthropic.Anthropic()
        self.strategist = ContentStrategist(client)
        self.copywriter = Copywriter(client)
        self.hashtag_specialist = HashtagSpecialist(client)
        self.lead_qualifier = LeadQualifier(client)

    def create_instagram_post(
        self, property_description: str, skip_strategy: bool = False
    ) -> dict[str, str]:
        """Run the full pipeline: strategy → caption → hashtags.

        Returns a dict with keys: strategy (optional), caption, hashtags.
        """
        result: dict[str, str] = {}

        if not skip_strategy:
            print("📋 Stratégie de contenu…")
            result["strategy"] = self.strategist.plan(property_description)

        print("✍️  Rédaction de la légende…")
        result["caption"] = self.copywriter.write(
            property_description,
            strategy=result.get("strategy", ""),
        )

        print("🏷️  Génération des hashtags…")
        result["hashtags"] = self.hashtag_specialist.generate(
            property_description,
            caption=result.get("caption", ""),
        )

        return result

    def qualify_lead(self, inquiry: str) -> str:
        """Qualify an incoming prospect inquiry."""
        print("🔍 Qualification du lead…")
        return self.lead_qualifier.qualify(inquiry)
