from twilio.rest import Client
import os
import smtplib

TWILIO_ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
MY_EMAIL = os.environ["EMAIL"]
MY_PASSWORD = os.environ["EMAIL_PASSWORD"]
MY_SMTP_SERVER = os.environ["MY_SMTP_SERVER"]
FROM_NUMBER = os.environ["FROM_NUMBER"]


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, msg, link):
        sms_text = f"{msg}\n{link}"
        message = self.client.messages \
            .create(
            body=sms_text,
            from_=FROM_NUMBER,
            to='+12025550167'
        )

        print(message.sid)

    def send_email(self, to_adds_list, msg, link):
        with smtplib.SMTP(MY_SMTP_SERVER) as server:
            server.starttls()
            server.login(user=MY_EMAIL, password=MY_PASSWORD)
            for email in to_adds_list:
                server.sendmail(from_addr=MY_EMAIL, to_addrs=email,
                                msg=f"Subject:New Low Price Flight!\n\n{msg}\n{link}".encode('utf-8'))
