"""
Envoi d'emails personnalisés aux contacts acquéreurs et vendeurs.
Utilise les templates définis ci-dessous + données de project_deals.md
"""
import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Configuration (charger depuis variables d'environnement en production)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = ""  # À configurer
SENDER_NAME = "Douglas Elliman — Immobilier Luxe"

TEMPLATES = {
    "suivi_visite": {
        "subject": "{prenom}, merci pour notre rencontre",
        "body": """Bonjour {prenom},

C'était un plaisir de vous faire découvrir {bien} aujourd'hui.

J'espère que cette visite vous a donné une bonne idée du potentiel de ce bien.
N'hésitez pas à revenir vers moi pour toute question.

Je reste disponible pour organiser une seconde visite ou vous présenter \
d'autres opportunités correspondant à vos critères.

Bien cordialement,
{signature}"""
    },
    "nouvelle_opportunite": {
        "subject": "Opportunité off-market — {marche}",
        "body": """Bonjour {prenom},

Je pense à vous en découvrant une opportunité qui correspond \
parfaitement à vos critères.

Il s'agit d'un {description} à {ville}.

Ce bien n'est pas encore sur le marché public — je vous en parle \
en avant-première.

Souhaitez-vous en savoir plus ? Je peux vous envoyer la fiche \
confidentielle ou organiser une visite privée.

Bien cordialement,
{signature}"""
    },
    "relance_froide": {
        "subject": "Le marché {marche} en ce moment",
        "body": """Bonjour {prenom},

J'espère que vous allez bien.

Je voulais partager avec vous quelques observations sur le marché \
{marche} ce printemps : {observations_marche}

Si votre projet est toujours d'actualité, je serais ravi d'en discuter.

Bien cordialement,
{signature}"""
    }
}


def send_email(to_email, to_name, template_name, variables):
    """Envoie un email personnalisé à partir d'un template."""
    template = TEMPLATES.get(template_name)
    if not template:
        raise ValueError(f"Template '{template_name}' introuvable")

    variables.setdefault("signature", f"{SENDER_NAME}\n+33 X XX XX XX XX")

    subject = template["subject"].format(**variables)
    body = template["body"].format(**variables)

    msg = MIMEMultipart()
    msg["From"] = f"{SENDER_NAME} <{SENDER_EMAIL}>"
    msg["To"] = f"{to_name} <{to_email}>"
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain", "utf-8"))

    # Décommenter pour envoi réel (nécessite SENDER_EMAIL configuré)
    # with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    #     server.starttls()
    #     server.login(SENDER_EMAIL, os.environ["GMAIL_APP_PASSWORD"])
    #     server.send_message(msg)

    print(f"[{datetime.now().strftime('%H:%M')}] Email '{template_name}' → {to_email}")
    print(f"  Objet : {subject}\n")


def run_campaign(contacts_file, template_name, common_vars=None):
    """Lance une campagne email sur une liste de contacts."""
    with open(contacts_file) as f:
        contacts = json.load(f)

    for contact in contacts:
        variables = {**contact, **(common_vars or {})}
        send_email(
            to_email=contact["email"],
            to_name=contact["prenom"],
            template_name=template_name,
            variables=variables
        )


if __name__ == "__main__":
    # Exemple d'utilisation
    send_email(
        to_email="exemple@email.com",
        to_name="Jean",
        template_name="nouvelle_opportunite",
        variables={
            "prenom": "Jean",
            "marche": "Megève",
            "description": "chalet ski-in/ski-out 6 chambres avec spa",
            "ville": "Megève",
        }
    )
