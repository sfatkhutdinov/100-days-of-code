import smtplib
from twilio.rest import Client
from secrets import TWILIO_PHONE_NUMBER, TWILIO_AUTH_TOKEN, TWILIO_ACCOUNT_SID, MY_PHONE_NUMBER, EMAIL, SMTP, PASSWORD

TWILIO_SID = TWILIO_ACCOUNT_SID
TWILIO_AUTH_TOKEN = TWILIO_AUTH_TOKEN
TWILIO_VIRTUAL_NUMBER = TWILIO_PHONE_NUMBER
TWILIO_VERIFIED_NUMBER = MY_PHONE_NUMBER
MAIL_PROVIDER_SMTP_ADDRESS = SMTP
MY_EMAIL = EMAIL
MY_PASSWORD = PASSWORD


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
