# Location types

before accessing the API, you have to specify a location to get the prayer times for. In this project there is 3 types of locations you can use:

<br>

## Coordinates

Coordinates consist of latitude and longitude which are like X and Y values on the map, you can see your own coordinates by clicking [here](https://mycoordinates.xyz/). 

```py
from aladhan.location_types import Coordinates

location = Coordinates(51.507351, -0.127758)
```

<br>

## City

City location type takes the city name and the country name as parameters, country name should be in [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) alpha-2 format.

```py
from aladhan.location_types import City

location = City("London", "GB")
```

Additional `state` parameter can be used to specify the state of the city.

<br>

## Address

Address location type takes the address as a parameter, it can be a street address, a city name, a postal code or a combination of all.

According to the official API, here is some examples of valid addresses:

1420 Austin Bluffs Parkway, Colorado Springs, CO OR 25 Hampstead High Street, London, NW3 1RL, United Kingdom OR Sultanahmet Mosque, Istanbul, Turkey

```py
from aladhan.location_types import Address

location = Address("1420 Austin Bluffs Parkway, Colorado Springs, CO")
```

<br>

[Previous: Getting started](/docs/1%2C%20getting%20started.md) | [See Next: Getting prayer times](/docs/3%2C%20getting%20prayer%20times.md)
