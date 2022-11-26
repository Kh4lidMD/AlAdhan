# Getting prayer times

After defining the location, you can either put it in the `Aladhan` class or pass manually to each method.

```py
from aladhan import Aladhan
from aladhan.location_types import City

location = City("Doha", "QA")
aladhan = Aladhan(location)
```

If you specify it in the main class, this will be the default location for all methods.

<br>

## `get_calendar`

This method returns a list of `Adhan` objects for a specific month (current month by default).

```py
for adhan in aladhan.get_calendar():
    print(adhan)
```

Output:
```
Fajr at 2022/01/01 05:30 AM
Dhuhr at 2022/01/01 12:30 PM
Asr at 2022/01/01 03:30 PM
Maghrib at 2022/01/01 05:00 PM
Isha at 2022/01/01 06:30 PM
till the end of the month...
```

<br>

[Previous: Location types](/docs/2%2C%20location%20types.md) | [Next: Adhan object](/docs/4%2C%20adhan%20object.md)
