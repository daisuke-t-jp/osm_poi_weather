#!/usr/bin/python
# coding: UTF-8

import sys
import logging
import datetime
import time
import json
import urllib
import ssl
import enum

import overpy

# - - - - - - - - - - - - - - - - - - - -
# Const, Enum
# - - - - - - - - - - - - - - - - - - - -
OPENWEATHERMAP_API = 'https://api.openweathermap.org/data/2.5/weather?appid={0}&lat={1}&lon={2}'

class POIType(enum.Enum):
    church = 'church'
    station = 'station'
    townhall = 'townhall'

class OverpassMode(enum.Enum):
    local = 'local'
    server = 'server'

LOCAL_OVERPASS_FILE =  {
    POIType.church.value: 'overpass_master_building_church.json',
    POIType.station.value: 'osm_master_public_transport_station.json',
    POIType.townhall.value: 'osm_master_amenity_townhall.json',
}

# Overpass API query
# reference : https://overpass-turbo.eu/
OVERPASS_QUERY =  {
    POIType.church.value: """
                                        [out:json];
                                        area["name"~"日本"];
                                        node(area)["building"="church"];
                                        out body;
                                        """,
    POIType.station.value: """
                                        [out:json];
                                        area["name"~"日本"];
                                        node(area)["public_transport"="station"];
                                        out body;
                                        """,
    POIType.townhall.value: """
                                        [out:json];
                                        area["name"~"日本"];
                                        node(area)["amenity"="townhall"];
                                        out body;
                                        """,
}



# - - - - - - - - - - - - - - - - - - - -
# Functions
# - - - - - - - - - - - - - - - - - - - -
def overpass_nodes(poi_type, overpass_mode):
    if overpass_mode == OverpassMode.local.value:
        return overpass_json_from_local(poi_type)
    if overpass_mode == OverpassMode.server.value:
        return overpass_json_from_server(poi_type)
    
    return []


def overpass_json_from_local(poi_type):
    file = open(LOCAL_OVERPASS_FILE[poi_type], 'r')
    json_obj = json.load(file)
    file.close()
    return json_obj["elements"]

# TODO
def overpass_json_from_server(poi_type):
    logging.debug('start overpass API')

    api = overpy.Overpass()
    result = api.query(OVERPASS_QUERY[poi_type])
    nodes = result.nodes

    logging.debug('end overpass API')

    return nodes


def openweathermap_weather(api_key, lat, lon):
    url = OPENWEATHERMAP_API.format(api_key, lat, lon)
        
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as resp:
        body = json.load(resp)
    return body


def osm_poi_weather(poi_type, overpass_mode, openweahtermap_api_key):
    logging.debug('poi_type[{0}] overpass_mode[{1}]'.format(poi_type, overpass_mode))

    nodes = overpass_nodes(poi_type, overpass_mode)
    
    logging.debug('nodes len[{0}]'.format(len(nodes)))

    for node in nodes:
        weather = openweathermap_weather(openweahtermap_api_key, node['lat'], node['lon'])
        
        name = 'N/A'
        if 'name:ja' in node['tags'].keys():
            name = node['tags']['name:ja']
        elif 'name' in node['tags'].keys():
            name = node['tags']['name']
        elif 'name:en' in node['tags'].keys():
            name = node['tags']['name:en']
        
        operator = ''
        if 'operator' in node['tags'].keys():
            operator = node['tags']['operator']
        
        name2 = name
        if len(operator) > 0:
            name2 = '{0}({1})'.format(name, operator)
        
        logging.debug('{0} -> {1}'.format(name2, weather))
        time.sleep(1)   # OpenWeatherMap API free plan has limit that 60 requests in minute.

    return



def main():
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)

    # Check args.
    args = sys.argv
    if len(args) < 4 :
        logging.debug('invalid args.')
        sys.exit()
        return
    
    poi_type = args[1]
    overpass_mode = args[2]
    openweahtermap_api_key = args[3]
    
    # for api.openweathermap.org
    ssl._create_default_https_context = ssl._create_unverified_context
    
    
    osm_poi_weather(poi_type, overpass_mode, openweahtermap_api_key)

if __name__ == '__main__':
    main()
