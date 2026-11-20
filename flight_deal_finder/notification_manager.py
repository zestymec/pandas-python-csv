import os
import smtplib
from dotenv import load_dotenv

load_dotenv()


class NotificationManager:

    def __init__(self):
        self.email = os.getenv("MY_EMAIL")
        self.password = os.getenv("MY_APP_PASSWORD")

    def send_email(self, message_body):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()  # Connection ko encrypt/secure karta hai
            connection.login(user=self.email, password=self.password)
            connection.sendmail(
                from_addr=self.email,
                to_addrs=self.email,  # Apne hi email par alert bhej rahe hain
                msg=f"Subject:Low Price Flight Alert!\n\n{message_body}".encode("utf-8"),
            )
        print("Email alert successfully sent!")