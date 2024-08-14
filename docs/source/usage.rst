Usage
=====

.. _installation:

Installation
------------

To use geodisasters, first install it using pip:

.. code-block:: console

   (.venv) $ pip install geodisasters

Creating clients
----------------
To authorize against the endpoints being hosted on Rapid API you need to use your own Rapid API key.
This geopedestrian module uses client instances from the georapid module.

.. warning::
   The ``host`` parameter must target the specific host like ``"geodisasters.p.rapidapi.com"``.
   Furthermore, the factory directly access ``os.environ['x_rapidapi_key']`` and uses the specified API key as a header parameter.
   Otherwise, :py:func:`georapid.factory.EnvironmentClientFactory.create_client_with_host` will raise a :exc:`ValueError`.

For example:

.. code-block:: python

   from georapid.client import GeoRapidClient
   from georapid.factory import EnvironmentClientFactory

   host = 'geodisasters.p.rapidapi.com'
   client: GeoRapidClient = EnvironmentClientFactory.create_client_with_host(host)

For more details take a closer look at `Creating clients <https://georapid.readthedocs.io/en/latest/usage.html#creating-clients>`__.

Query the news related to natural disasters
-------------------------------------------

For example querying the named hotspots categorized by theme from yesterday:

.. code-block:: python

   from geodisasters.services import aggregate, hotspots, query
   from georapid.formats import OutFormat

   featureset_dict = hotspots(client, format=OutFormat.ESRI)
   featureset_dict

.. code-block:: python

   {'geometryType': 'esriGeometryPoint',
 'fields': [{'alias': 'location',
   'name': 'location',
   'type': 'esriFieldTypeString',
   'length': 49},
  {'alias': 'theme',
   'name': 'theme',
   'type': 'esriFieldTypeString',
   'length': 10},
  {'alias': 'count', 'name': 'count', 'type': 'esriFieldTypeSmallInteger'},
  {'alias': 'date',
   'name': 'date',
   'type': 'esriFieldTypeString',
   'length': 10}],
 'features': [{'geometry': {'x': -118.244,
    'y': 34.0522,
    'spatialReference': {'wkid': 4326}},
   'attributes': {'location': 'Los Angeles, California, United States',
    'theme': 'EARTHQUAKE',
    'count': 308,
    'date': '2024-08-13'}},
  {'geometry': {'x': 139.751, 'y': 35.685, 'spatialReference': {'wkid': 4326}},
   'attributes': {'location': 'Tokyo, Tokyo, Japan',
    'theme': 'EARTHQUAKE',
    'count': 131,
    'date': '2024-08-13'}},
  {'geometry': {'x': 36.1572,
    'y': 36.2066,
    'spatialReference': {'wkid': 4326}},
   'attributes': {'location': 'Hatay, Hatay, Turkey',
    'theme': 'EARTHQUAKE',
    'count': 99,
    'date': '2024-08-13'}},
  {'geometry': {'x': 28.9647,
    'y': 41.0186,
    'spatialReference': {'wkid': 4326}},
   'attributes': {'location': 'Istanbul, Istanbul, Turkey',
    'theme': 'EARTHQUAKE',
    'count': 82,
    'date': '2024-08-13'}},
  {'geometry': {'x': 36.3, 'y': 33.5, 'spatialReference': {'wkid': 4326}},
   'attributes': {'location': 'Damascus, Dimashq, Syria',
    'theme': 'EARTHQUAKE',
    'count': 57,
    'date': '2024-08-13'}},
  {'geometry': {'x': -122.273,
    'y': 37.8716,
    'spatialReference': {'wkid': 4326}},
   'attributes': {'location': 'Berkeley, California, United States',
    'theme': 'EARTHQUAKE',
    'count': 56,
    'date': '2024-08-13'}},
  {'geometry': {'x': 37.3825,
    'y': 37.0594,
    'spatialReference': {'wkid': 4326}},
   'attributes': {'location': 'Gaziantep, Gaziantep, Turkey',
    'theme': 'EARTHQUAKE',
    'count': 55,
    'date': '2024-08-13'}},
  {'geometry': {'x': 16, 'y': 45.8, 'spatialReference': {'wkid': 4326}},
   'attributes': {'location': 'Zagreb, Zagreb, Grad, Croatia',
    'theme': 'EARTHQUAKE',
    'count': 50,
    'date': '2024-08-13'}},
  {'geometry': {'x': 8.3858, 'y': 49.0047, 'spatialReference': {'wkid': 4326}},
   'attributes': {'location': 'Karlsruhe, Baden-WüBerg, Germany',
    'theme': 'FLOOD',
    'count': 95,
    'date': '2024-08-13'}},
  {'geometry': {'x': -65.8329,
    'y': 18.4249,
    'spatialReference': {'wkid': 4326}},
   'attributes': {'location': 'Vieques, Puerto Rico, United States',
    'theme': 'HURRICANE',
    'count': 102,
    'date': '2024-08-13'}},
  {'geometry': {'x': -65.301, 'y': 18.303, 'spatialReference': {'wkid': 4326}},
   'attributes': {'location': 'Culebra, Puerto Rico, United States',
    'theme': 'HURRICANE',
    'count': 90,
    'date': '2024-08-13'}},
  {'geometry': {'x': -80.3836,
    'y': 25.7522,
    'spatialReference': {'wkid': 4326}},
   'attributes': {'location': 'National Hurricane Center, Florida, United States',
    'theme': 'HURRICANE',
    'count': 62,
    'date': '2024-08-13'}},
  {'geometry': {'x': -80.1937,
    'y': 25.7743,
    'spatialReference': {'wkid': 4326}},
   'attributes': {'location': 'Miami, Florida, United States',
    'theme': 'HURRICANE',
    'count': 55,
    'date': '2024-08-13'}},
  {'geometry': {'x': 23.7333,
    'y': 37.9833,
    'spatialReference': {'wkid': 4326}},
   'attributes': {'location': 'Athens, AttikíR, Greece',
    'theme': 'WILDFIRE',
    'count': 368,
    'date': '2024-08-13'}}]}

Terms of use
------------
We designed the geospatial intelligence API services for research and analysis of geospatial knowledge worldwide. 
The geospatial datasets and any result being generated by these API services are available for unrestricted use for academic, commercial, or governmental use of any kind.

Redistribution
--------------
You may redistribute, republish, and mirror the geospatial datasets in any form. 
However, any use or redistribution of the geospatial datasets and results must include a citation to GEOINT API services and a link to our website `Geospatial AI <https://geospatial-ai.de>`__.
