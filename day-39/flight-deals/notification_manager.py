from twilio.rest import Client
from secrets import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, MY_PHONE_NUMBER

TWILIO_SID = TWILIO_ACCOUNT_SID
TWILIO_AUTH_TOKEN = TWILIO_AUTH_TOKEN
TWILIO_VIRTUAL_NUMBER = TWILIO_PHONE_NUMBER
TWILIO_VERIFIED_NUMBER = MY_PHONE_NUMBER


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
