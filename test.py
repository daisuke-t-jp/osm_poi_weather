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
# Functions
# - - - - - - - - - - - - - - - - - - - -
def test_local():
    overpass_weahter.weathers_from_local_overpass_file(OPENWEATHERMAP_API_KEY, 'overpass_master_building_church.json')
    # overpass_weahter.weathers_from_local_overpass_file(OPENWEATHERMAP_API_KEY, 'overpass_master_amenity_townhall.json')
    # overpass_weahter.weathers_from_local_overpass_file(OPENWEATHERMAP_API_KEY, 'overpass_master_public_transport_station.json')
    return


def test_server():
    overpass_weahter.weathers_from_server(OPENWEATHERMAP_API_KEY, """
                                        [out:json];
                                        area["name"~"日本"];
                                        node(area)["building"="church"];
                                        out body;
                                        """)
    return
'''
    overpass_weahter.weathers_from_server(OPENWEATHERMAP_API_KEY, """
                                        [out:json];
                                        area["name"~"日本"];
                                        node(area)["amenity"="townhall"];
                                        out body;
                                        """)

    overpass_weahter.weathers_from_server(OPENWEATHERMAP_API_KEY, """
                                        [out:json];
                                        area["name"~"日本"];
                                        node(area)["public_transport"="station"];
                                        out body;
                                        """)
'''


def main():
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
    
    test_local()
    test_server()
    
if __name__ == '__main__':
    main()

