import urllib.request
import requests
import threading
import json

import random


# Defining a function that will post on server every 15 Seconds

def thingspeak_post():
    threading.Timer(15,thingspeak_post).start()
    val1=random.uniform(0,3)
    val2=random.uniform(85,95)
    val3=random.uniform(5,25)
    URl='https://api.thingspeak.com/update?api_key='
    KEY='JP6LIEYUIR1IOI92'
    HEADER='&field1={}&field2={}&field3={}'.format(val1,val2,val3)
    NEW_URL=URl+KEY+HEADER
    print(NEW_URL)
    data=urllib.request.urlopen(NEW_URL)
    print(data)

def read_data_thingspeak():
    threading.Timer(15,read_data_thingspeak).start()
    URL='https://api.thingspeak.com/channels/2030393/fields/1&2&3.json?api_key='
    KEY='NH5FT0QRWOPXD8T3'
    HEADER='&results=2'
    NEW_URL=URL+KEY+HEADER
    print(NEW_URL)

    get_data=requests.get(NEW_URL).json()
    print(get_data)
    channel_id=get_data['channel']['id']
    feild_1=get_data['feeds']
    for i in feild_1:
        if float(i["field1"]) > 1.4705:
            print("START DECELERATING")
        if float(i["field2"]) > 90:
            print("REDUCE SPEED")
        if float(i["field3"]) < 15:
            print("OBSTACLE AHEAD SLOW DOWN")


    t=[]
    for x in feild_1:
        #print(x['field1'])
        t.append(x['field1'])

if __name__ == '__main__':
    thingspeak_post()
    read_data_thingspeak()

