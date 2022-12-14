===================
Choosing a location
===================

Before using the module, you must specify a location to get prayer times for. The API does not automatically determine your location, so you must define it by using a location object. There are three types of location objects:

aladhan.Coordinates
~~~~~~~~~~~~~~~~~~~

Coordinates (latitude and longitude) are like X and Y coordinates on a map, you can see your own coordinates by clicking `here <https://mycoordinates.xyz/>`_.

Arguments:

- ``latitude (float)``: The latitude of the location (required)
- ``longitude (float)``: The longitude of the location (required)

Raises:

- ``InvalidLocationException``: If the latitude or longitude is invalid.

Example:

.. code-block:: python

    import aladhan

    location = aladhan.Coordinates(51.507351, -0.127758)

aladhan.City
~~~~~~~~~~~~

City is a location object that is defined by a city name and a country, state is optional.

Arguments:

- ``city (str)``: The name of the city (required)
- ``country (str)``: The name or code of the country in ISO 3166-1 alpha-2 or alpha-3 format, or a CLDR short name. Examples: QA, QAT, Qatar (required)
- ``state (str)``: The name of the state or region where the city is located (optional, default= ``None``)

Raises:

- ``InvalidLocationException``: If the country is invalid.

Example:

.. code-block:: python

    import aladhan

    location = aladhan.City("London", "GB") # London, United Kingdom
    # or
    location = aladhan.City("London", "GB", "England") # London, England, United Kingdom

aladhan.Address
~~~~~~~~~~~~~~~

Address location type takes the address as a parameter, it can be a street address, a city name, a postal code or a combination of all. According to the official aladhan.com prayer times API, here is a list of valid addresses:

1420 Austin Bluffs Parkway, Colorado Springs, CO OR 25 Hampstead High Street, London, NW3 1RL, United Kingdom OR Sultanahmet Mosque, Istanbul, Turkey

Arguments:

- ``address (str)``: The address (required)

Example:

.. code-block:: python

    import aladhan

    location = aladhan.Address("1420 Austin Bluffs Parkway, Colorado Springs, CO")