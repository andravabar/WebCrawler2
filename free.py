import smtplib, ssl
from bot import thisDict
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "stock.webcrawler2@gmail.com"  # Enter your address
receiver_email = "andra.vabar@gmail.com"  # Enter receiver address
password = input("Type your password and press enter: ")
message = f"""\
Subject: Price Alert (+/-5%)
{thisDict["NTU1L"].get("positive")}
This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
