import firebase_admin
from firebase_admin import credentials
from fcm_django.models import FCMDevice

cred = credentials.Certificate("fb-credentials.json")
default_app = firebase_admin.initialize_app(
    cred
)


class BaseNotification:
    def __init__(self, user, title, message):
        self.user = user
        self.title = title
        self.message = message

    def send_notification(self):
        try:
            device = FCMDevice.objects.filter(user=self.user).first()
            if device:
                result = device.send_message(
                    title=self.title, body=self.message, sound=True
                )
                return result
        except Exception as e:
            print(e)


class MessageNotification(BaseNotification):
    def __init__(self, user):
        title = "Nuevo aviso"
        message = ("Nuevo aviso")
        print(message)
        super().__init__(user, title=title, message=message)
