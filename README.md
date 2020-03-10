# overpass_weather

## Overview

[overpass_weather.py](overpass_weahter.py) is get weather with POI data.

This module run at step.

1. Get OSM nodes from [Overpass API](https://wiki.openstreetmap.org/wiki/Overpass_API) or Overpass local file.
1. Get weather with node from [OpenWeatherMap API](https://openweathermap.org/current) (You must need API key)


## Python dependency
 
Using Python 3.x.

Install packages.

```sh
$ pip3 install overpy
$ pip3 install attrdict
```


## Usage

There are two ways to get Overpass API data.

### Using Overpass API

```py
    # overpass_weahter.weathers_with_overpass_api(query, openweathermap_api_key, openweathermap_api_interval_seconds)
    weathers = overpass_weahter.weathers_with_overpass_api("""
                                            [out:json];
                                            node["building"="cathedral"];
                                            out body;
                                            """,
                                            OPENWEATHERMAP_API_KEY,
                                            0.1)

    for weather in weathers:
        # ...
```

### Using Overpass data(local file)

```py
    # overpass_weahter.weathers_with_overpass_file(overpass_file_path, openweathermap_api_key, openweathermap_api_interval_seconds)
    weathers = overpass_weahter.weathers_with_overpass_file('overpass_building_cathedral.json',
                                            OPENWEATHERMAP_API_KEY,
                                            0.1)

    for weather in weathers:
        # ...
```


## Example

See [test](test).

```sh
$ cd test/
$ python3 test.py

2020-03-09 23:54:38,076 DEBUG test.py:40 - test_overpass_api() : start test_overpass_api() - - - - - - - - - -
2020-03-09 23:56:06,709 DEBUG test.py:27 - test_dump_weather() : osm_id[100090862] name[Dom St. Blasien] lat[47.7600646] lon[8.1300061] temp[280.04] pressure[1017] humidity[71]
2020-03-09 23:56:06,709 DEBUG test.py:27 - test_dump_weather() : osm_id[474375860] name[Собор Успения Пресвятой Богородицы] lat[50.9799235] lon[39.3167911] temp[286.99] pressure[1019] humidity[66]
2020-03-09 23:56:06,709 DEBUG test.py:27 - test_dump_weather() : osm_id[592838468] name[N/A] lat[4.8092301] lon[-74.3537103] temp[289.15] pressure[1030] humidity[67]

...

2020-03-08 18:01:15,056 DEBUG test.py:92 - test_overpass_file() : start test_overpass_file() - - - - - - - - - -
2020-03-09 23:57:14,733 DEBUG test.py:27 - test_dump_weather() : osm_id[100090862] name[Dom St. Blasien] lat[47.7600646] lon[8.1300061] temp[280.04] pressure[1017] humidity[71]
2020-03-09 23:57:14,733 DEBUG test.py:27 - test_dump_weather() : osm_id[262567942] name[Catedral Primada de Bogotá] lat[4.5978998] lon[-74.0751863] temp[289.15] pressure[1030] humidity[67]
2020-03-09 23:57:14,733 DEBUG test.py:27 - test_dump_weather() : osm_id[474375860] name[Собор Успения Пресвятой Богородицы] lat[50.9799235] lon[39.3167911] temp[286.99] pressure[1019] humidity[66]

...

```

