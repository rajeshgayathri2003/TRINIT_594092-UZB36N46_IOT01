'''

To send data to Thingspeak

'''

import httplib
import urllib
import time
import main #import the file on raspberry pi that has all the parameter values

key = "JP6LIEYUIR1IOI92"  #API
def send_car_parameters():
    while True:
        speed = speedometer()
        acceleration = accelerometer()
        distance = ultra()
        params = urllib.urlencode({'Crusing_speed': speed, 'Acceleration': acceleration, 'Obstacle_distance': distance}) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print(speed,"\n",acceleration,"\n",distance)
            print response.status, response.reason
            data = response.read()
            conn.close()
        except:
            print "connection failed"
        break
if __name__ == "__main__":
        while True:
            send_car_parameters()
