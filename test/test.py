#!/usr/bin/python
# coding: UTF-8

import sys
import logging
import enum

sys.path.append('../')
import overpass_weahter



# - - - - - - - - - - - - - - - - - - - -
# Const, Enum
# - - - - - - - - - - - - - - - - - - - -
OPENWEATHERMAP_API_KEY = '<YOU MUST BE SET>'



# - - - - - - - - - - - - - - - - - - - -
# Functions - Tests
# - - - - - - - - - - - - - - - - - - - -
def test_dump_weather(weather):
    openweathermap_weather = weather[overpass_weahter.KEY_OPENWEATHERMAP_CURRENT_WEATHER_DATA]
    
    logging.debug('name[{0}] lat[{1}] lon[{2}] temp[{3}] pressure[{4}] humidity[{5}]'.format(
        weather[overpass_weahter.KEY_NAME],
        weather[overpass_weahter.KEY_LAT],
        weather[overpass_weahter.KEY_LON],
        openweathermap_weather['main']['temp'],
        openweathermap_weather['main']['pressure'],
        openweathermap_weather['main']['humidity']))
    
    return


def test_overpass_api():
    logging.debug('start test_overpass_api() - - - - - - - - - -')
    
    try:
        weathers = overpass_weahter.weathers_with_overpass_api("""
                                            [out:json];
                                            node["building"="cathedral"];
                                            out body;
                                            """,
                                            OPENWEATHERMAP_API_KEY,
                                            0.1)
                                            
        '''
        weathers = overpass_weahter.weathers_with_overpass_api("""
                                            [out:json];
                                            area["name"~"日本"];
                                            node(area)["building"="church"];
                                            out body;
                                            """,
                                            OPENWEATHERMAP_API_KEY,
                                            0.1)
        '''
    
        '''
        overpass_weahter.weathers_with_overpass_api("""
                                            [out:json];
                                            area["name"~"日本"];
                                            node(area)["amenity"="townhall"];
                                            out body;
                                            """,
                                            OPENWEATHERMAP_API_KEY,
                                            0.1)
        '''
    
        '''
        overpass_weahter.weathers_with_overpass_api("""
                                            [out:json];
                                            area["name"~"日本"];
                                            node(area)["public_transport"="station"];
                                            out body;
                                            """,
                                            OPENWEATHERMAP_API_KEY,
                                            0.1)
        '''

        for weather in weathers:
            test_dump_weather(weather)
        
    except Exception as exp: 
        logging.error('exception[{0}]'.format(exp))

    return


def test_overpass_file():
    logging.debug('start test_overpass_file() - - - - - - - - - -')
    
    try:
        weathers = overpass_weahter.weathers_with_overpass_file('overpass_building_cathedral.json', OPENWEATHERMAP_API_KEY, 0.1)
        # weathers = overpass_weahter.weathers_with_overpass_file('overpass_japan_building_church.json', OPENWEATHERMAP_API_KEY, 0.1)
        # weathers = overpass_weahter.weathers_with_overpass_file('overpass_japan_amenity_townhall.json', OPENWEATHERMAP_API_KEY, 0.1)
        # weathers = overpass_weahter.weathers_with_overpass_file('overpass_japan_public_transport_station.json', OPENWEATHERMAP_API_KEY, 0.1)

        for weather in weathers:
            test_dump_weather(weather)
        
    except Exception as exp: 
        logging.error('exception[{0}]'.format(exp))
        
    return



# - - - - - - - - - - - - - - - - - - - -
# Functions - Main
# - - - - - - - - - - - - - - - - - - - -
def main():
    logging.basicConfig(format='%(asctime)s %(levelname)s %(filename)s:%(lineno)s - %(funcName)s() : %(message)s', level=logging.DEBUG)
        
    test_overpass_api()
    test_overpass_file()
    
if __name__ == '__main__':
    main()

