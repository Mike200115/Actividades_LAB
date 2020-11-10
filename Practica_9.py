#!/usr/bin/env python3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json
import argparse

parser = argparse.ArgumentParser(description="", epilog = "", formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-c", metavar='correo', dest="correo", help="", required=True)
parser.add_argument("-a", metavar='asunto', dest="asunto", help="", required=True)
parser.add_argument("-m", metavar='mensaje', dest="mensaje", help="", required=True)


parametros = parser.parse_args()

data = {}
with open('pass.json') as f:
        data = json.load(f)
# create message object instance
msg = MIMEMultipart()

message = parametros.mensaje

# setup the parameters of the message
msg['From'] = data['user']

msg['To'] = parametros.correo
msg['Subject'] = parametros.asunto

# add in the message body
msg.attach(MIMEText(message, 'plain'))

#create server
server = smtplib.SMTP('smtp.office365.com:587')
server.starttls()

# Login Credentials for sending the mail
print(data['user'])
server.login(data['user'], data['pass'])

# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

print("successfully sent email to %s:" % (msg['To']))