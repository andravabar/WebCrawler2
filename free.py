import smtplib, ssl
from bot import thisDict
userChangePos = 3
userChangeNeg = -3

def getStockChange(thisDict):
    response = ""
    for e in thisDict:
        if thisDict[e]['positive'] is not None:
            if int(float(thisDict[e]['positive'].strip("%").replace(",", "."))) > userChangePos:
                response += e + " " + thisDict[e]['positive'] + " "

        if thisDict[e]['negative'] is not None:
            if int(float(thisDict[e]['negative'].strip("%").replace(",", "."))) < userChangeNeg:
                response += e + " " + thisDict[e]['negative'] + " "
    return response
# getStockChange(thisDict)
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "stock.webcrawler2@gmail.com"  # Enter your address
receiver_email = "andra.vabar@gmail.com"  # Enter receiver address
password = input("Type your password and press enter: ")
message = f"""\
Subject: Price Alert (+/-5%)
{getStockChange(thisDict)}
This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
