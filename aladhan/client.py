from datetime import datetime
from time import sleep
from .location_types import Coordinates, Address, City
from .adhan import Adhan
from typing import Union
import requests


API = 'https://api.aladhan.com/v1/'


class Aladhan:

    def __init__(self, default_location: Union[Coordinates, Address, City] = None):
        """
        The main class for the API.

        - `default_location: Union[Coordinates, Address, City]=None` is the default location to use for the API, if not provided, it will be required for every method.

        Note: If `default_location` is not provided, it will be required for every method.
        """
        self.default_location = default_location

    def get_prayer_times(
        self, 
        location: Union[Coordinates, Address, City] = None, 
        year: int=None, month: int=None,
        today_only=False
    ) -> list[Adhan]:
        """
        Get the prayer times for a specific month (current month by default) and returns a list of `adhan_api.Adhan` objects.

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

        # get the location type and the ENDPOINT
        if isinstance(location, Coordinates):
            ENDPOINT = 'calendar'
            params['latitude'] = location.latitude
            params['longitude'] = location.longitude
        elif isinstance(location, Address):
            ENDPOINT = 'calendarByAddress'
            params['address'] = location.address
        elif isinstance(location, City):
            ENDPOINT = 'calendarByCity'
            params['city'] = location.city
            params['country'] = location.country
            if location.state:
                params['state'] = location.state
        else:
            raise TypeError('Invalid location type.')
        
        # today only
        if today_only:
            ENDPOINT = ENDPOINT.replace('calendar', 'timings')
        
        # send the request and get the JSON data
        response = requests.get(API + ENDPOINT, params=params)
        data = response.json()

        # loop through the data and create a list of Adhan objects
        
        # for entire month
        if not today_only:
            adhan_list = []
            for day in data['data']:
                date = datetime.strptime(day['date']['gregorian']['date'], '%d-%m-%Y')
                for salah_name, salah_time in day['timings'].items():
                    if salah_name in ['Sunrise', 'Sunset', 'Midnight', 'Lastthird', 'Firstthird', 'Imsak']:
                        continue
                    salah_time = datetime.strptime(salah_time.split(" ")[0], '%H:%M')
                    salah_time = salah_time.replace(year=date.year, month=date.month, day=date.day)
                    adhan_list.append(Adhan(salah_name, salah_time))
            return adhan_list
        
        # for today only
        else:
            adhan_list = []
            date = datetime.now()
            for salah_name, salah_time in data['data']['timings'].items():
                if salah_name in ['Sunrise', 'Sunset', 'Midnight', 'Lastthird', 'Firstthird', 'Imsak']:
                    continue
                salah_time = datetime.strptime(salah_time.split(" ")[0], '%H:%M')
                salah_time = salah_time.replace(year=date.year, month=date.month, day=date.day)
                adhan_list.append(Adhan(salah_name, salah_time))
            return adhan_list

