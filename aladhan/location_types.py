from urllib.parse import quote
from .exceptions import InvalidLocationException
from .countries import countries


def search_country(country_query: str) -> dict:
    """
    Helper function that looks up the country name based on the country query argument,
    which could be a country CLDR name, ISO 3166-1 alpha-2 or alpha-3 code.
    
    Then returns all country information in a dictionary.
    """

    key_search = None
    if len(country_query) == 2 or len(country_query) == 3:
        key_search = f"ISO3166-1-Alpha-{len(country_query)}"
        country_query = country_query.upper()
    elif len(country_query) > 3:
        key_search = "CLDR display name"
        country_query = country_query.title().replace(" Of ", " of ")
    else:
        raise InvalidLocationException("Invalid country code or name")

    for country in countries:
        if country[key_search] == country_query:
            return country
    raise InvalidLocationException("Invalid country code or name")


class Coordinates:
    
    def __init__(self, latitude: float, longitude: float):
        """A GPS coordinate object."""
        if not (longitude >= -180 and longitude <= 180 and latitude >= -90 and latitude <= 90):
            raise InvalidLocationException("Invalid coordinates")
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f"{self.latitude}, {self.longitude}"


class City:
    
    def __init__(self, city: str, country_query: str, state: str = None):
        """
        A city object that represents a city in a particular country, could contain a state or region.
        
        Args:
        - city: The name of the city.
        - country_query: The name or code of the country in ISO 3166-1 alpha-2 or alpha-3 format, or a CLDR short name. Examples: QA, QAT, Qatar.
        - state (optional): The name of the state or region where the city is located.
        
        Raises:
        - InvalidLocationException: If the city or country is not found.
        
        """
        self.city = city
        self.state = state
        self.country = search_country(country_query)

    def get_text(self) -> str:
        """Returns a string representation of the city object."""
        state_str = f", {self.state}" if self.state else ""
        return f"{self.city}{state_str}, {self.country['CLDR display name']}"
    
    def __str__(self) -> str:
        return self.get_text()


class Address:

    def __init__(self, text: str):
        """
        An address object, example of `text` argument:

        1420 Austin Bluffs Parkway, Colorado Springs, CO OR 25 Hampstead High Street, London, NW3 1RL, United Kingdom OR Sultanahmet Mosque, Istanbul, Turkey
        """
        self.text = text
    
    def url_encoded(self):
        """Returns the address in a URL encoded format."""
        return quote(self.text, safe='')

    def __str__(self):
        return self.text
