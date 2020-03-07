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
# Functions - Main
# - - - - - - - - - - - - - - - - - - - -
def main():
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
    
    overpass_weahter.weathers_from_local_overpass_file(OPENWEATHERMAP_API_KEY, 'overpass_master_building_church.json')
    
if __name__ == '__main__':
    main()

