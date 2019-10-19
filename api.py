# import json
# import requests

# country = input('Entra nom pais\n')
# APIKEY = ''

# response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=' + country + '&APPID=' + APIKEY) # Obtenim l'objecte response

# weather = json.loads(response.text) # Li passem l'atribut text de l'objecte response al mètode loads de la classe json

# txt = json.dumps(weather)

# print(weather)


import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='hola@hola.com',
    to_emails='magurlat@gmail.com',
    subject='Ajhjh',
    html_content='<strong>Please send us your password</strong>')
try:
    sg = SendGridAPIClient('')
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(str(e))