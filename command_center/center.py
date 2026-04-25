import anthropic
from ai_sales_team.team import AISalesTeam
from ai_marketing_suite.suite import AIMarketingSuite
from .agents import MarketAnalyst, CampaignPlanner, DealSourcer, BriefingOfficer


class AgencyCommandCenter:
    """Douglas Elliman Megève — AI Agency Command Center.

    Central hub that orchestrates the full AI team:

    From ai_sales_team     : ContentStrategist, Copywriter, HashtagSpecialist, LeadQualifier
    From command_center    : MarketAnalyst, CampaignPlanner, DealSourcer, BriefingOfficer
    From ai_marketing_suite: VisualDirector, EmailMarketingWriter, PRWriter, AdCopyWriter

    Entry points
    ────────────
    create_post(description)               Single Instagram post pipeline
    plan_campaign(description, weeks)      Multi-week editorial calendar
    analyze_market(topic)                  Strategic market intelligence
    qualify_lead(inquiry)                  Score & respond to a prospect
    source_deals(criteria)                 Off-market acquisition strategy
    executive_brief(context)               Weekly command briefing
    create_visual_brief(description)       Photo/video shoot brief
    write_email_sequence(context, steps)   Prospect nurture email sequence
    write_press_release(context)           Press release
    write_ads(description, platform)       Meta & Google ad copy
    """

    def __init__(self) -> None:
        client = anthropic.Anthropic()
        # Sales team (existing agents)
        self._sales_team = AISalesTeam()
        # Marketing suite
        self._marketing_suite = AIMarketingSuite()
        # Command center agents
        self._market_analyst = MarketAnalyst(client)
        self._campaign_planner = CampaignPlanner(client)
        self._deal_sourcer = DealSourcer(client)
        self._briefing_officer = BriefingOfficer(client)

    # ── Delegation to AI Sales Team ───────────────────────────────────────

    def create_post(self, description: str, fast: bool = False) -> dict[str, str]:
        """Full single-post pipeline: strategy → caption → hashtags."""
        return self._sales_team.create_instagram_post(description, skip_strategy=fast)

    def qualify_lead(self, inquiry: str) -> str:
        """Score an incoming prospect and suggest a personalised response."""
        return self._sales_team.qualify_lead(inquiry)

    # ── Command Center exclusives ─────────────────────────────────────────

    def plan_campaign(self, description: str, weeks: int = 2) -> str:
        """Plan a multi-week Instagram campaign for a property listing."""
        print(f"📅 Planification d'une campagne {weeks} semaine(s)…")
        return self._campaign_planner.plan(description, weeks=weeks)

    def analyze_market(self, topic: str) -> str:
        """Produce a strategic market intelligence report."""
        print("📊 Analyse de marché en cours…")
        return self._market_analyst.analyze(topic)

    def source_deals(self, criteria: str) -> str:
        """Generate an off-market property sourcing strategy."""
        print("🤝 Élaboration de la stratégie d'acquisition…")
        return self._deal_sourcer.source(criteria)

    def executive_brief(self, context: str) -> str:
        """Synthesise agency activities into an executive briefing."""
        print("📋 Rédaction du briefing exécutif…")
        return self._briefing_officer.brief(context)

    # ── Delegation to AI Marketing Suite ──────────────────────────────────

    def create_visual_brief(self, property_description: str) -> str:
        """Generate a photography/videography brief for a property shoot."""
        return self._marketing_suite.create_visual_brief(property_description)

    def write_email_sequence(self, context: str, steps: int = 3) -> str:
        """Write a personalized email nurture sequence for a prospect."""
        return self._marketing_suite.write_email_sequence(context, steps=steps)

    def write_press_release(self, context: str) -> str:
        """Write a press release for a property listing or agency news."""
        return self._marketing_suite.write_press_release(context)

    def write_ads(self, property_description: str, platform: str = "both") -> str:
        """Create paid advertising copy for Meta and/or Google Ads."""
        return self._marketing_suite.write_ads(property_description, platform=platform)
