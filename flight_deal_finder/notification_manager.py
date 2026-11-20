import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:

    def __init__(self):
        self.email = os.getenv("MY_EMAIL") or os.getenv("MAIL_SENDER")
        self.password = os.getenv("MY_APP_PASSWORD") or os.getenv("MAIL_PASSWORD")
        if not self.email or not self.password:
            raise RuntimeError(
                "Set MAIL_SENDER and MAIL_PASSWORD in flight_deal_finder/.env "
                "before sending email alerts."
            )

    def send_email(self, message_body):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            connection.sendmail(
                from_addr=self.email,
                to_addrs=self.email,
                msg=f"Subject: Low Price Flight Alert!\n\n{message_body}".encode("utf-8"),
            )
        print("Email alert successfully sent!")
