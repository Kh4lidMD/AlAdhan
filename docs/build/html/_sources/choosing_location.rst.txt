===================
Choosing a location
===================

Before using the module, you have to choose a location to get the prayer times for. And this API will not determine your location by itself, but you have to define it, in order to define a location, you have to import a location object. There is 3 types of locaton objects:

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

City is a location object that is defined by a city name and a country alpha-2 code.

Arguments:

- ``city (str)``: The name of the city (required)
- ``country (str)``: The alpha-2 code of the country (required)
- ``state (str)``: The name of the state (optional, default=``None``)

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