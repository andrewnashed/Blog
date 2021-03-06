import smtplib
from dotenv import load_dotenv
import os
load_dotenv(".env.txt")
my_email = os.getenv("FROM_EMAIL")
password = os.getenv("PASSWORD")
to_email = os.getenv("TO_EMAIL")


def send_email(name, email, phone, message):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                            msg=f"Subject:hello\n\n Name:{name}\nEmail:{email}\nPhone:{phone}\nMessage:{message}")
