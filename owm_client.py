#!/usr/bin/env python3

# Soubor: owm_client.py
# Popis: 1. projekt (varianta 2) do predmetu IPK
# Autor: Jan Havlin (xhavli47@stud.fit.vutbr.cz)
# Datum: 14. 3. 2019

import socket
import sys
import json

if (len(sys.argv) != 3):
    sys.exit('Error: Invalid amount of arguments')

HOST = 'api.openweathermap.org'
PORT = 80
KEY = sys.argv[1]
CITY = sys.argv[2]
REQUEST = 'GET /data/2.5/weather?q='+CITY+'&APPID='+KEY+'&units=metric HTTP/1.1\r\nHost: '+HOST+'\r\n\r\n'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(REQUEST.encode())
    data = s.recv(1024)

code = data.decode().split()[1]
if (code != '200'):
    sys.exit('Error: Request returned code '+code)

datajson = json.loads(data.decode().splitlines()[11])

print(datajson['name'])
print(datajson['weather'][0]['description'])
print('temp:', datajson['main']['temp'], '°C')
print('humidity:', datajson['main']['humidity'], '%')
print('pressure:', datajson['main']['pressure'], 'hPa')

windspeed = int(datajson['wind']['speed']) * 3.6
print('wind-speed:', windspeed, 'km/h')
if (windspeed == 0):
    print('wind-deg: -')
else:
    print('wind-deg:', datajson['wind']['deg'])
