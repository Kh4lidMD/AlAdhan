from urllib.parse import quote


class Coordinates:

    def __init__(self, latitude: float, longitude: float):
        """A GPS coordinate object."""
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f"{self.latitude}, {self.longitude}"


class City:

    def __init__(self, city: str, country: str, state: str = None):
        """A city object, `country` argument is the name of the country in ISO 3166-1 alpha-2 country code (2 characters)."""
        self.city = city
        self.country = country
        self.state = state
    
    def __str__(self):
        if self.state:
            return f"{self.city}, {self.state}, {self.country}"
        else:
            return f"{self.city}, {self.country}"


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
