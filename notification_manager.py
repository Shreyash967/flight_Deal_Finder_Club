import os
import smtplib 
from dotenv import load_dotenv
# Using a .env file to retrieve the phone numbers and tokens.
load_dotenv()

class NotificationManager:

    def __init__(self):
        self.gmail = os.getenv("gmail")
        self.password = os.getenv("password")
        

    def send_mail(self, message_body ,email ):
        for recipient in email:
            with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
                connection.starttls()
                connection.login(user=self.gmail,password=self.password)
                connection.sendmail(
                    from_addr=self.gmail,
                    to_addrs=recipient,
                    msg=f"Subject:Flight Club Notification\n\n{message_body}"
                )