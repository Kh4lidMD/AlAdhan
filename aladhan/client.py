from datetime import datetime
from .location_types import Coordinates, Address, City
from .adhan import Adhan
from .exceptions import *
from typing import Union
import requests


API = 'https://api.aladhan.com/v1/'
SKIP = ['Sunrise', 'Sunset', 'Midnight', 'Lastthird', 'Firstthird', 'Imsak']


class Client:


    def __init__(self, default_location: Union[Coordinates, Address, City] = None):
        """
        The main class for the API.

        - `default_location: Union[Coordinates, Address, City]=None` is the default location to use for the API, if not provided, it will be required for every method.

        Note: If `default_location` is not provided, it will be required for every method.
        """
        self.default_location = default_location


    @staticmethod
    def __set_location_params(params: dict, location: Union[Coordinates, Address, City]):
        if isinstance(location, Coordinates):
            params['latitude'] = location.latitude
            params['longitude'] = location.longitude
        elif isinstance(location, Address):
            params['address'] = location.url_encoded()
        elif isinstance(location, City):
            params['city'] = location.city
            params['country'] = location.country
            if location.state:
                params['state'] = location.state


    @staticmethod
    def __get_endpoint_by_location(location: Union[Coordinates, Address, City], endpoint: str):
        if isinstance(location, Coordinates):
            return endpoint
        if isinstance(location, Address):
            return endpoint + 'ByAddress'
        if isinstance(location, City):
            return endpoint + 'ByCity'


    @staticmethod
    def __detect_exceptions(response: requests.Response, data: dict):
        if response.status_code == 429:
            raise RateLimitedException("Rate limit exceeded.")
        if response.status_code == 400:
            raise BadRequestException(data['data'])
        if response.status_code == 500:
            raise ServerErrorException(data['message'])


    def get_calendar_times(
        self, 
        location: Union[Coordinates, Address, City] = None, 
        year: int=None, month: int=None
    ) -> list[Adhan]:
        """
        Get the prayer times for a specific month (current month by default) and returns a list of `aladhan.adhan.Adhan` objects.

        - `location: Union[Coordinates, Address, City]=None` is the location to get the prayer times for.
        - `year: int=None` is the year of the prayer times.
        - `month: int=None` is the month of the prayer times.

        Note: If `location` is not provided, the default location that was provided when initializing the class will be used.
        """

        # define parameters
        params = {}

        # figure out the location if it was in the argument or in the default location
        if location is None:
            if self.default_location is None:
                raise ValueError('No location was provided.')
            else:
                location = self.default_location

        # set year and month
        if year:
            params['year'] = year
        if month:
            params['month'] = month

        # set the location type and the ENDPOINT
        self.__set_location_params(params, location)
        ENDPOINT = self.__get_endpoint_by_location(location, 'calendar')
        
        # send the request and get the JSON data
        response = requests.get(API + ENDPOINT, params=params)
        data = response.json()
        self.__detect_exceptions(response, data)

        # loop through the data and create a list of Adhan objects
        adhan_list = []
        for day in data['data']:
            date = datetime.strptime(day['date']['gregorian']['date'], '%d-%m-%Y')
            for salah_name, salah_time in day['timings'].items():
                if salah_name in SKIP:
                    continue
                salah_time = datetime.strptime(salah_time.split(" ")[0], '%H:%M')
                salah_time = salah_time.replace(year=date.year, month=date.month, day=date.day)
                adhan_list.append(Adhan(salah_name, salah_time))
        return adhan_list


    def get_today_times(self, location: Union[Coordinates, Address, City] = None) -> list[Adhan]:
        """
        Get the prayer times for today and returns a list of 5 `aladhan.adhan.Adhan` objects.

        - `location: Union[Coordinates, Address, City]=None` is the location to get the prayer times for.

        Note: If `location` is not provided, the default location that was provided when initializing the class will be used.
        """

        # define parameters
        params = {}

        # figure out the location if it was in the argument or in the default location
        if location is None:
            if self.default_location is None:
                raise ValueError('No location was provided.')
            else:
                location = self.default_location

        # set the location type and the ENDPOINT
        self.__set_location_params(params, location)
        ENDPOINT = self.__get_endpoint_by_location(location, 'timings')
        
        # send the request and get the JSON data
        response = requests.get(API + ENDPOINT, params=params)
        data = response.json()
        self.__detect_exceptions(response, data)

        # loop through the data and create a list of Adhan objects
        adhan_list = []
        for salah_name, salah_time in data['data']['timings'].items():
            if salah_name in SKIP:
                continue
            salah_time = datetime.strptime(salah_time.split(" ")[0], '%H:%M')
            salah_time = salah_time.replace(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
            adhan_list.append(Adhan(salah_name, salah_time))
        return adhan_list


    def get_annual_times(self, location: Union[Coordinates, Address, City] = None, year: int=None) -> list[Adhan]:
        """
        Get the prayer times for a specific year (current year by default) and returns a list of `aladhan.adhan.Adhan` objects.
        
        - `location: Union[Coordinates, Address, City]=None` is the location to get the prayer times for.
        - `year: int=None` is the year of the prayer times (current year by default).
        
        Note: If `location` is not provided, the default location that was provided when initializing the class will be used.
        """
        
        # define parameters
        params = {'annual': 'true'}
        
        # figure out the location if it was in the argument or in the default location
        if location is None:
            if self.default_location is None:
                raise ValueError('No location was provided.')
            else:
                location = self.default_location
        
        # set year
        if year:
            params['year'] = year
            
        # set the location type and the ENDPOINT
        self.__set_location_params(params, location)
        ENDPOINT = self.__get_endpoint_by_location(location, 'calendar')
        
        # send the request and get the JSON data
        response = requests.get(API + ENDPOINT, params=params)
        data = response.json()
        self.__detect_exceptions(response, data)
        
        # loop through the data and create a list of Adhan objects
        adhan_list = []
        for month in data['data']:
            for day in data['data'][month]:
                date = datetime.strptime(day['date']['gregorian']['date'], '%d-%m-%Y')
                for salah_name, salah_time in day['timings'].items():
                    if salah_name in SKIP:
                        continue
                    salah_time = datetime.strptime(salah_time.split(" ")[0], '%H:%M')
                    salah_time = salah_time.replace(year=date.year, month=date.month, day=date.day)
                    adhan_list.append(Adhan(salah_name, salah_time))
        
        return adhan_list
