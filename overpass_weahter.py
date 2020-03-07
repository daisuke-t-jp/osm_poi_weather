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
from attrdict import AttrDict


# - - - - - - - - - - - - - - - - - - - -
# Const, Enum
# - - - - - - - - - - - - - - - - - - - -
OPENWEATHERMAP_API = 'https://api.openweathermap.org/data/2.5/weather?appid={0}&lat={1}&lon={2}'
KEY_NAME = 'name'
KEY_WEATHER = 'weather'

class OverpassMode(enum.Enum):
    local       = 1
    server    = 2


# - - - - - - - - - - - - - - - - - - - -
# Functions - Overpass
# - - - - - - - - - - - - - - - - - - - -
def overpass_nodes_from_local(file_path):
    file = open(file_path, 'r')
    json_obj = json.load(file)
    file.close()
    
    nodes = json_obj["elements"]
    
    return nodes


def overpass_nodes_from_server(query):
    logging.debug('Start Overpass API')

    api = overpy.Overpass()
    result = api.query(query)
    nodes = result.nodes

    logging.debug('End Overpass API')

    return nodes



# - - - - - - - - - - - - - - - - - - - -
# Functions - OpenWeatherMap
# - - - - - - - - - - - - - - - - - - - -
def openweathermap_weather(api_key, lat, lon):
    url = OPENWEATHERMAP_API.format(api_key, lat, lon)
    
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as resp:
        body = json.load(resp)
    
    return body



# - - - - - - - - - - - - - - - - - - - -
# Functions - Nodes
# - - - - - - - - - - - - - - - - - - - -
def node_name_from_node(node):
    name = 'N/A'
    if 'name:ja' in node.tags.keys():
        name = node.tags['name:ja']
    elif 'name' in node.tags.keys():
        name = node.tags['name']
    elif 'name:en' in node.tags.keys():
        name = node.tags['name:en']
        
    operator = ''
    if 'operator' in node.tags.keys():
        operator = node.tags['operator']
        
    if len(operator) > 0:
        name = '{0}({1})'.format(name, operator)

    return name
    
    
def nodes_weather(overpass_mode, nodes, openweahtermap_api_key):
    logging.debug('nodes len[{0}]'.format(len(nodes)))

    ssl._create_default_https_context = ssl._create_unverified_context
    res = []
    
    for node in nodes:
        if overpass_mode == OverpassMode.local:
            node = AttrDict(node)
        
        # Get weather from node.
        weather = openweathermap_weather(openweahtermap_api_key, node.lat, node.lon)

        # Create weather data.        
        node_name = node_name_from_node(node)
        elm = {
            KEY_NAME: node_name,
            KEY_WEATHER: weather
        }
        res.append(elm)
        
        logging.debug('elm{0}'.format(elm))
        
        time.sleep(1.1)   # OpenWeatherMap API free plan has limit that 60 requests in minute.
    
    return  res


# - - - - - - - - - - - - - - - - - - - -
# Functions - Weathers
# - - - - - - - - - - - - - - - - - - - -
def weathers_from_local_overpass_file(openweathermap_api_key, file_path):
    logging.debug('file_path[{0}]'.format(file_path))
    
    nodes = overpass_nodes_from_local(file_path)
    weathers = nodes_weather(OverpassMode.local, nodes, openweathermap_api_key)

    return weathers
    
def weathers_from_server(openweathermap_api_key, overpass_query):
    logging.debug('overpass_query[{0}]'.format(overpass_query))
    
    nodes = overpass_nodes_from_server(overpass_query)
    weathers = nodes_weather(OverpassMode.server, nodes, openweathermap_api_key)

    return weathers
