import random
import threading
import urllib.request
import requests


# Defining a function that will post on server every 15 Seconds

def thingspeak_post():
    threading.Timer(15, thingspeak_post).start()
    val=random.randint(1,30)
    URl='https://api.thingspeak.com/update?api_key='
    KEY='JP6LIEYUIR1IOI92'
    HEADER='&field1={}&field2={}'.format(val,val)
    NEW_URL=URl+KEY+HEADER
    print(NEW_URL)
    data = requests.post(NEW_URL)
    print(data)

if _name_ == '_main_':
    thingspeak_post()



'''

To send data to Thingspeak



import http.client
import urllib
import time
#import main #import the file on raspberry pi that has all the parameter values

key = "JP6LIEYUIR1IOI92"  #API
def send_car_parameters():
    while True:
        speed = 37
        acceleration = 2
        distance = 9
        params = urllib.parse.urlencode({'Crusing_speed': speed, 'Acceleration': acceleration, 'Obstacle_distance': distance}) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print(speed,"\n",acceleration,"\n",distance)
            print(response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print("connection failed")
        break
if __name__ == "__main__":
        while True:
            send_car_parameters()
'''
