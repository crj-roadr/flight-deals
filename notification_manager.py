from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()

# Your Account SID and Auth Token from console.twilio.com
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token  = os.getenv("TWILIO_AUTH_TOKEN")


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        self.fromPhoneNumber = os.getenv("TWILIO_ROADR_NUMBER")
        self.toPhoneNumber = "+13468576623"

    def send_sms(self, body: str) -> None:

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to=self.toPhoneNumber,
            from_=self.fromPhoneNumber,
            body=body)

        print(message.status)