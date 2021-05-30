from app.settings import DEFAULT_FROM_EMAIL, EMAIL_HOST_PASSWORD, APP_URL
from django.utils.crypto import get_random_string
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class BaseMailer:
    def __init__(self, to_email, subject, message):
        self.to_email = to_email
        self.subject = subject
        self.message = message
        self.mail = Mail(
            subject=self.subject,
            plain_text_content=self.message,
            from_email=DEFAULT_FROM_EMAIL,
            to_emails=self.to_email,
        )

    def send_email(self):
        try:
            sg = SendGridAPIClient(EMAIL_HOST_PASSWORD)
            sg.send(self.mail)
        except Exception as e:
            print(e)


class RegisterMailer(BaseMailer):
    def __init__(self, to_email):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        numbers = "0123456789"
        chars = alphabet + alphabet.upper() + numbers
        self.registration_code = get_random_string(
            length=6, allowed_chars=chars)
        link = f"{APP_URL}/validation/"
        subject = f"[CTRLCO] Validación de registro"
        body = (
            f"Hola {to_email}:\n\nSu código de registro es: "
            f"{self.registration_code}\n\nPara poder registrarse en "
            f"el administrador de propiedades haga click en el siguiente enlace y "
            f"coloque su código de registro: {link}\n"
            f"\n\nSi no ha intentado registrarse en el Administrador de propiedades de CtrlCo"
            f", por favor ignore este email.\n\nAtte.\n"
            f"Equipo CtrlCo"
        )
        super().__init__(to_email, subject=subject, message=body)
