import anthropic
from .agents import VisualDirector, EmailMarketingWriter, PRWriter, AdCopyWriter


class AIMarketingSuite:
    """Douglas Elliman Megève — AI Marketing Suite.

    Orchestrates four specialist marketing agents:

    - VisualDirector       : photography & videography shoot briefs
    - EmailMarketingWriter : personalized prospect email sequences
    - PRWriter             : press releases for properties and agency news
    - AdCopyWriter         : paid advertising copy (Meta Ads & Google Ads)

    Entry points
    ────────────
    create_visual_brief(description)          Photo/video shoot brief
    write_email_sequence(context, steps)      Prospect nurture email sequence
    write_press_release(context)              Press release
    write_ads(description, platform)          Meta & Google ad copy
    """

    def __init__(self) -> None:
        client = anthropic.Anthropic()
        self._visual_director = VisualDirector(client)
        self._email_writer = EmailMarketingWriter(client)
        self._pr_writer = PRWriter(client)
        self._ad_copywriter = AdCopyWriter(client)

    def create_visual_brief(self, property_description: str) -> str:
        """Generate a photography/videography brief for a property shoot."""
        print("📸 Création du brief visuel…")
        return self._visual_director.brief(property_description)

    def write_email_sequence(self, context: str, steps: int = 3) -> str:
        """Write a personalized email nurture sequence for a prospect."""
        print(f"📧 Rédaction d'une séquence de {steps} email(s)…")
        return self._email_writer.write(context, steps=steps)

    def write_press_release(self, context: str) -> str:
        """Write a press release for a property listing or agency news."""
        print("📰 Rédaction du communiqué de presse…")
        return self._pr_writer.write(context)

    def write_ads(self, property_description: str, platform: str = "both") -> str:
        """Create paid advertising copy for Meta and/or Google Ads."""
        print(f"📣 Création des copies publicitaires ({platform})…")
        return self._ad_copywriter.write(property_description, platform=platform)
