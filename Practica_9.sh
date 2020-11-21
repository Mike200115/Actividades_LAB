#Autor: Miguel Alejandro Juarez Gonzalez
#script para leer correos de un txt y despues mandarles un mensaje predeterminado
#!/bin/bash

function py { python3 -c "$1"; }
direccion=$1


for correo in $(cat $direccion)
do
    echo "correo $correo"
    py "
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json

data = {}
with open('pass.json') as f:
    data = json.load(f)
# create message object instance
msg = MIMEMultipart()

message = 'Holaaaa' #Ingrese el mensaje que va a mandar

# setup the parameters of the message
msg['From'] = data['user']

msg['To'] = '$correo'
msg['Subject'] = 'soy el micke' #Ingrese el titulo de sus mensajes
# add in the message body
msg.attach(MIMEText(message, 'plain'))

#create server
server = smtplib.SMTP('smtp.office365.com:587')
server.starttls()

# Login Credentials for sending the mail
server.login(data['user'], data['pass'])

# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()
    "
done
