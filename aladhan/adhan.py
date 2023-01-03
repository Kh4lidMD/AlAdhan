from time import sleep
from datetime import datetime
import threading


class Adhan:

    def __init__(self, name: str, datetime_obj: datetime):
        """
        Returns an Adhan object with useful methods.

        - `name` is the name of the salah capitalized. (e.g. 'Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha')
        - `datetime_obj` is a datetime object for the salah time.
        """
        self.name = name.capitalize()
        self.datetime_obj = datetime_obj

        if self.name not in ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']:
            raise ValueError('Invalid salah name.')

    def readable_timing(self, show_time=True, show_date=True, _24h=False, arabic=False) -> str:
        """
        Returns a readable timing for the salah from the datetime object.

        - `show_time: bool=True` to show the time or not.
        - `show_date: bool=True` to show the date in the YYYY/MM/DD format or not.
        - `_24h: bool=False` display the time in 24h format.
        - `arabic: bool=False` display the time in Arabic (change English numbers to Arabic and PM/AM to ص/م).

        Note: the date comes first, then the time if both are shown.
        """

        if show_date and show_time: format_ = '%Y/%m/%d %H:%M (%p)'
        elif show_date: format_ = '%Y/%m/%d'
        elif show_time: format_ = '%H:%M (%p)'
        else: format_ = ''

        if _24h:
            format_ = format_.replace('(%p)', '').strip()
        else:
            format_ = format_.replace('%H', '%I')

        if arabic:
            arabic_nums = {
                "1": "١",
                "2": "٢",
                "3": "٣",
                "4": "٤",
                "5": "٥",
                "6": "٦",
                "7": "٧",
                "8": "٨",
                "9": "٩",
                "0": "٠"
            }
            result = self.datetime_obj.strftime(format_)
            for a, e in arabic_nums.items():
                result = result.replace(a, e)
            result = result.replace('AM', 'ص').replace('PM', 'م')
            return result
        else:
            return self.datetime_obj.strftime(format_)

    def wait(self, callback=None, threaded_wait=False, *args, **kwargs) -> threading.Thread or None:
        """
        Wait until the salah time has passed.
        
        - `callback: callable=None` is a function to be called when the salah time has passed.
        - `threaded_wait: bool=True` to wait in a separate thread or not, this is useful if you want to do other things while waiting and having a callback function.
        """ 
        def wait_function():
            while True:
                if datetime.now() >= self.datetime_obj:
                    break
                sleep(1)
            if callback:
                callback(*args, **kwargs)

        if threaded_wait:
            thread = threading.Thread(target=wait_function, name=f'Wait thread for {self.name} at {self.readable_timing()}')
            thread.start()
            return thread
        else:
            wait_function()

    def is_passed(self) -> bool:
        """Returns `True` if the salah time has passed, `False` otherwise."""
        return datetime.now() >= self.datetime_obj

    def is_hijri(self) -> bool:
        """Figure out if the salah is hijri (هجرية) or not."""
        return self.name in ['Isha', 'Fajr', 'Maghrib']

    def is_secret(self) -> bool:
        """Figure out if the salah is secret (سرية) or not."""
        return self.name in ['Dhuhr', 'Asr']

    def rakat(self) -> int:
        """Returns the number of rak'at for the salah."""
        if self.name == 'Fajr': return 2
        elif self.name == 'Dhuhr': return 4
        elif self.name == 'Asr': return 4
        elif self.name == 'Maghrib': return 3
        elif self.name == 'Isha': return 4

    def get_en_name(self) -> str:
        """Returns the English name of the salah."""
        return self.name
    
    def get_ar_name(self, tashkeel: bool=False, include_al: bool=True) -> str:
        """
        Returns the Arabic name of the salah.
        
        - `tashkeel: bool=False` to include tashkeel or not (e.g. مَغْرِبٌ).
        - `include_al: bool=True` to include the definite article (ال) or not (e.g. العشاء instead of عشاء).
        """
        
        translate = {
            "Fajr":    {"ar": "فجر", "tashkeel_ar": "فَجْرٌ"},
            "Dhuhr":   {"ar": "ظهر", "tashkeel_ar": "ظُهْرٌ"},
            "Asr":     {"ar": "عصر", "tashkeel_ar": "عَصْرٌ"},
            "Maghrib": {"ar": "مغرب", "tashkeel_ar": "مَغْرِبٌ"},
            "Isha":    {"ar": "عشاء", "tashkeel_ar": "عَشَاءٌ"}
        }
        
        name = translate[self.name]['ar']
        if tashkeel:
            name = translate[self.name]['tashkeel_ar']
        if include_al:
            name = 'ال' + name

        return name

    def sunnan_al_rawatib(self) -> dict:
        """Returns a dictionary with the number of sunnah prayers `before` and `after` the salah."""
        if self.name == 'Fajr': return {'before': 2,'after': 0}
        elif self.name == 'Dhuhr': return {'before': 4, 'after': 2}
        elif self.name == 'Asr': return {'before': 0, 'after': 0}
        elif self.name == 'Maghrib': return {'before': 0, 'after': 2}
        elif self.name == 'Isha': return {'before': 0, 'after': 2}

    def __str__(self):
        return f'{self.name} at {self.readable_timing()}'
