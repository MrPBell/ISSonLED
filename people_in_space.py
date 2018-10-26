##############################################################
# P Bell - Where is ISS on 12 x 8 grid
# v1.01
# October 2018
# long range = -180 to +180
# lat range = -52 to +52 (not -90 to 90 but ISS range of ISS)
# Matrix = 12 x 8
##############################################################

import requests
from time import sleep
import json
#from gpiozero import LEDBarGraph

import turtle
screen = turtle.Screen()
screen.setup(720,360)
screen.setworldcoordinates(-180,-90,180,90)
screen.title("ISS tracker")
screen.bgpic("mapFromRpi.gif")
screen.update()
screen.register_shape("issFromRpi.gif")
iss=turtle.Turtle()
iss.shape("issFromRpi.gif")
iss.setheading(90)
iss.penup()
screen.update()


req = requests.get("http://api.open-notify.org/iss-now.json", auth=('xxxx', 'xxxxxx'))
print ("Status response =",req.status_code)
print ("Text is",req.text)

response = req.json()
print ("Response = ", response)

timestamp = response['timestamp']
print ("Time is",timestamp)

lat = 8-int(abs(float(response['iss_position']['latitude'])+52)/(104/9))
print ("Latitude is",lat)

long = int(abs(float(response['iss_position']['longitude'])+180)/(360/13))
print ("Longitude is",long)

def makeBlankMatrix():
    global matrix
    matrix = []
    for i in range(8):
      row = []
      for j in range(12):
        row.append(0)
      matrix.append(row)
            
makeBlankMatrix()
for row in matrix:
    print(row)
    
while True:
    sleep(5)
    print("------------")
    print("Lat",lat)
    print("Long",long)
    req = requests.get("http://api.open-notify.org/iss-now.json", auth=('user', 'pass'))
    response = req.json()
    isslat = response['iss_position']['latitude']
    isslong = response['iss_position']['longitude']
    lat = 8-int(abs(float(response['iss_position']['latitude'])+52)/(104/9))
    long = int(abs(float(response['iss_position']['longitude'])+180)/(360/13))
    makeBlankMatrix()
    matrix[lat-1][long-1] = 1
    iss.goto(int(float(isslong)),int(float(isslat)))
    screen.update()
    for row in matrix:
        print(row)

'''
url = "http://api.open-notify.org/astros.json"
r = requests.get(url)
data = r.json()
people = data['number']
print(people)
'''
