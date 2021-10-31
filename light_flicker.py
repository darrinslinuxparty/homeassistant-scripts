#! /bin/python3
# importing the requests library
import requests
import random
import argparse
import time
from time import sleep

parser = argparse.ArgumentParser(description='Short sample app')
parser.add_argument('--key', action="store", dest='key')
parser.add_argument('--entity', action="store", dest='entity')
parser.add_argument('--duration', action="store", dest='duration')
parser.add_argument('--brightness', action="store", dest='brightness')
args = parser.parse_args()


# defining the api-endpoint 
on_api_endpoint = "http://192.168.0.18:8123/api/services/light/turn_on"
off_api_endpoint = "http://192.168.0.18:8123/api/services/light/turn_off"

    
header = {'Content-Type': 'application/json',
          'Accept': 'application/json',
          'Authorization': 'Bearer ' + args.key}

# data to be sent to api
red = 255
green = 0
blue = 0
off_data = {"entity_id": str(args.entity)}
on_data = {"entity_id": str(args.entity),
           "brightness_pct": int(args.brightness)}

now = time.time()
timer = 0
while timer <= int(args.duration):
    sleep_int = round(random.uniform(0.00, .10), 2)
    response = requests.post(off_api_endpoint, json=off_data, headers=header)
    print(response)
    print("r=" + str(red) + ",g=" + str(green) + ",b=" + str(blue)) 
    print("sleep_int=" + str(sleep_int)) 
    sleep(sleep_int)

    sleep_int = round(random.uniform(0.00, 1.50), 2)
    response = requests.post(on_api_endpoint, json=on_data, headers=header)
    print(response)
    print("r=" + str(red) + ",g=" + str(green) + ",b=" + str(blue))
    print("sleep_int=" + str(sleep_int))  
    sleep(sleep_int)

    end = time.time()
    timer = round(end - now)
    print(timer)
     
