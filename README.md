# overpass_weather

## Overview

`overpass_weather.py` is get weather with POI data.

This module run at step.

1. Get OSM nodes from [Overpass API](https://wiki.openstreetmap.org/wiki/Overpass_API) or Overpass local file.
2. Get weather with node from [OpenWeatherMap API](https://openweathermap.org/current) (You must need API key)


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
    weathers = overpass_weahter.weathers_with_overpass_api("""
                                            'overpass_building_cathedral.json',
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

2020-03-08 17:59:11,984 DEBUG test.py:38 - test_overpass_api() : start test_overpass_api() - - - - - - - - - -
2020-03-08 18:01:15,051 DEBUG test.py:26 - test_dump_weather() : name[Dom St. Blasien] lat[47.7600646] lon[8.1300061] temp[276.57] pressure[1022] humidity[74]
2020-03-08 18:01:15,051 DEBUG test.py:26 - test_dump_weather() : name[Catedral Primada de Bogotá] lat[4.5978998] lon[-74.0751863] temp[286.15] pressure[1026] humidity[76]
2020-03-08 18:01:15,051 DEBUG test.py:26 - test_dump_weather() : name[Собор Успения Пресвятой Богородицы] lat[50.9799235] lon[39.3167911] temp[285.94] pressure[1020] humidity[64]

...

2020-03-08 18:01:15,056 DEBUG test.py:92 - test_overpass_file() : start test_overpass_file() - - - - - - - - - -
2020-03-08 18:03:05,688 DEBUG test.py:26 - test_dump_weather() : name[Dom St. Blasien] lat[47.7600646] lon[8.1300061] temp[276.93] pressure[1022] humidity[69]
2020-03-08 18:03:05,688 DEBUG test.py:26 - test_dump_weather() : name[Catedral Primada de Bogotá] lat[4.5978998] lon[-74.0751863] temp[286.15] pressure[1026] humidity[76]
2020-03-08 18:03:05,688 DEBUG test.py:26 - test_dump_weather() : name[Собор Успения Пресвятой Богородицы] lat[50.9799235] lon[39.3167911] temp[285.94] pressure[1020] humidity[64]

...

```

