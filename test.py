#!/usr/bin/python
# coding: UTF-8

import sys
import logging
import enum

import overpass_weahter



# - - - - - - - - - - - - - - - - - - - -
# Const, Enum
# - - - - - - - - - - - - - - - - - - - -
OPENWEATHERMAP_API_KEY = '<YOU MUST BE SET>'



# - - - - - - - - - - - - - - - - - - - -
# Functions - Tests
# - - - - - - - - - - - - - - - - - - - -
def test_overpass_api():
    # TODO: Dump weathers.
    overpass_weahter.weathers_with_overpass_api("""
                                        [out:json];
                                        area["name"~"日本"];
                                        node(area)["building"="church"];
                                        out body;
                                        """,
                                        OPENWEATHERMAP_API_KEY,)

    '''
    overpass_weahter.weathers_with_overpass_api("""
                                        [out:json];
                                        area["name"~"日本"];
                                        node(area)["amenity"="townhall"];
                                        out body;
                                        """,
                                        OPENWEATHERMAP_API_KEY)

    overpass_weahter.weathers_with_overpass_api("""
                                        [out:json];
                                        area["name"~"日本"];
                                        node(area)["public_transport"="station"];
                                        out body;
                                        """,
                                        OPENWEATHERMAP_API_KEY)
    '''
    return


def test_overpass_file():
    # TODO: Dump weathers.
    weathers = overpass_weahter.weathers_with_overpass_file('overpass_master_building_church.json', OPENWEATHERMAP_API_KEY)
    # overpass_weahter.weathers_with_overpass_file('overpass_master_amenity_townhall.json', OPENWEATHERMAP_API_KEY)
    # overpass_weahter.weathers_with_overpass_file('overpass_master_public_transport_station.json', OPENWEATHERMAP_API_KEY)
    return



# - - - - - - - - - - - - - - - - - - - -
# Functions - Main
# - - - - - - - - - - - - - - - - - - - -
def main():
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
        
    test_overpass_api()
    test_overpass_file()
    
if __name__ == '__main__':
    main()

