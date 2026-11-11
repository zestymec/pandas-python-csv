# import os
# import smtplib
# from email.message import EmailMessage
# from pathlib import Path



# SMTP_HOST = "smtp.gmail.com"
# SMTP_PORT = 587

# load_dotenv(Path(__file__).with_name(".env"))


# def required_setting(name: str) -> str:
#     value = os.getenv(name)
#     if not value:
#         raise RuntimeError(
#             f"Missing required environment variable: {name}. "
#             "Fill in your values in the .env file."
#         )
#     return value


# def send_email() -> None:
#     sender = required_setting("MAIL_SENDER")
#     password = required_setting("MAIL_PASSWORD")
#     recipient = required_setting("MAIL_RECIPIENT")

#     message = EmailMessage()
#     message["Subject"] = "Hello"
#     message["From"] = sender
#     message["To"] = recipient
#     message.set_content("This is the body")

#     with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as connection:
#         connection.starttls()
#         connection.login(user=sender, password=password)
#         connection.send_message(message)


# if __name__ == "__main__":
#     send_email()



import datetime as dt 

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=2026, month=11 , day = 11 , hour=15 , minute= 45)
print(date_of_birth)