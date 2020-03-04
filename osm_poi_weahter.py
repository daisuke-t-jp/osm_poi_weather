#!/usr/bin/python
# coding: UTF-8

import logging
import datetime
import time
import json
import urllib
import ssl
import enum

import overpy

CONNECTION_RETRY = 3
OPENWEATHERMAP_API = "https://api.openweathermap.org/data/2.5/weather?appid={0}&lat={1}&lon={2}"

class POIType(enum.Enum):
    station = 'station'
    townhall = 'townhall'

class OverpassMode(enum.Enum):
    local = 'local'
    server = 'server'


def node_overpass_json_from_local():
    file = open("overpass.json", 'r')
    json_obj = json.load(file)
    file.close()
    return json_obj["elements"]



def node_overpass_json_from_server():
    logging.debug('Start API')

    # https://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%3Barea%5B%22name%22%7E%22%E6%97%A5%E6%9C%AC%22%5D%3Bnode%5B%22public%5Ftransport%22%3D%22station%22%5D%28area%29%3Bout%3B%0A
    api = overpy.Overpass()

    for i in range(1, CONNECTION_RETRY + 1):
        try:
            result = api.query("""
                [out:json];
                area["name"~"日本"];
                node(area)["public_transport"="station"];
                out body;
                """
            )
        except Exception as exp:
            logging.debug(exp.args)
            sleep(i * 5)
        else:
            break

    logging.debug('End API')

    return result.nodes



def openweathermap_api_key():
    file = open("openweathermap_api_key.txt", 'r')
    key = file.read()
    file.close()
    return key



def openweathermap_weather(api_key, lat, lon):
    url = OPENWEATHERMAP_API.format(api_key, lat, lon)
    logging.debug('URL[{0}]'.format(url))
    
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as resp:
        body = json.load(resp)
    return body



def main():
    ssl._create_default_https_context = ssl._create_unverified_context

    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
    
    api_key = openweathermap_api_key()
    
    nodes = node_overpass_json_from_local()
    logging.debug('node num[{0}]'.format(len(nodes)))
    
    for node in nodes:
        weather = openweathermap_weather(api_key, node['lat'], node['lon'])
        
        name = 'N/A'
        if 'name:ja' in node['tags'].keys():
            name = node['tags']['name:ja']
        elif 'name' in node.keys():
            name = node['tags']['name']
        elif 'name:en' in node.keys():
            name = node['tags']['name:en']

        operator = 'N/A'
        if 'operator' in node['tags'].keys():
            operator = node['tags']['operator']
        
        logging.debug('{0}({1}) -> {2}'.format(name, operator, weather))
    


if __name__ == '__main__':
    main()
