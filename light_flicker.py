#! /bin/python3
import requests
import random
import argparse
import time

parser = argparse.ArgumentParser(description='Script for controlling Home Assistant Light service to flicker a light')
parser.add_argument('--ip', action="store", dest='ip',
                    help='The ip of the Home Assistant Server')
parser.add_argument('--key', action="store", dest='key',
                    help='The api key for the user on the Home Assistant Server')
parser.add_argument('--entity', action="store", dest='entity',
                    help='The entity name for the light that will be affected(e.g light.kitchen_1)')
parser.add_argument('--duration', action="store", dest='duration',
                    help='The duration in seconds (e.g 60)')
parser.add_argument('--brightness', action="store", dest='brightness',
                    help='An integer for the brightness percentage with 100 as max brightness')
parser.add_argument('--debug', action="store_true", dest='debug',
                    help='Enables debug output. Used when run from the command line to see values')
args = parser.parse_args()


# defining the api-endpoint 
on_api_endpoint = "http://" + args.ip + ":8123/api/services/light/turn_on"
off_api_endpoint = "http://" + args.ip + ":8123/api/services/light/turn_off"

# Header info
header = {'Content-Type': 'application/json',
          'Accept': 'application/json',
          'Authorization': 'Bearer ' + args.key}

# data to be sent to api
off_data = {"entity_id": str(args.entity)}
if args.brightness == "":
    on_data = {"entity_id": str(args.entity),
               "brightness_pct": int(args.brightness)}
else:
    on_data = {"entity_id": str(args.entity)}

# Debug Function
def debug():
    if args.debug == True:
        print(response.json())
        print("sleep_int=" + str(sleep_int))
        print(timer)

# Main loop args and loop
now = time.time()
timer = 0
while timer <= int(args.duration):
    # Off-to-on flicker logic
    sleep_int = round(random.uniform(0.00, .10), 2)
    response = requests.post(off_api_endpoint, json=off_data, headers=header)
    debug()
    time.sleep(sleep_int)

    # On-to-off flicker logic
    sleep_int = round(random.uniform(0.00, 1.50), 2)
    response = requests.post(on_api_endpoint, json=on_data, headers=header)
    debug()
    time.sleep(sleep_int)

    # Duration time logic
    end = time.time()
    timer = round(end - now)
    debug()
