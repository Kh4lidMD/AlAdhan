================
Get Prayer Times
================

We can get today's prayer times, all current month prayer times, or annual prayer times using ``get_calendar_times``, ``get_today_times``, or ``get_annual_times`` methods. All of them returns a list of ``Adhan`` objects with some useful methods.

aladhan.Client.get_today_times
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Returns a list of `Adhan` objects for today's prayer times.

Arguments:

- ``location: City | Coordinates | Address``: Location of the prayer times (optional, default= ``None``).

aladhan.Client.get_calendar_times
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Returns a list of `Adhan` objects for the current month's prayer times, or you can specify the ``month`` and ``year`` arguments to get a specifc date.

Arguments:

- ``location: City | Coordinates | Address``: Location of the prayer times (optional).
- ``month: int``: Month number (optional, default= ``None``).
- ``year: int``: Year number (optional, default= ``None``).

aladhan.Client.get_annual_times
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Returns a list of `Adhan` objects for specifc year's prayer times (current year by default), which returns all the prayer times for the year, day by day.

Arguments:

- ``location: City | Coordinates | Address``: Location of the prayer times (optional, default=``None``).
- ``year: int``: Year number (optional, default= ``None``).

All the methods above have the same raises:

- ``aladhan.exceptions.InvalidLocationException``: Raised when the location is invalid.
- ``aladhan.exceptions.RateLimitedException``: Raised when the client is rate limited by the server.
- ``aladhan.exceptions.BadRequestException``: Raised when the request is invalid (e.g. invalid date).
- ``aladhan.exceptions.ServerErrorException``: Raised when the server responds with unhandled error.

aladhan.Client.api_status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get the status of the API, returns a dictionary with the `status` and `code` keys, might raise an `requests.exceptions.ConnectionError` if the website is down.

Returns:

- ``dict``: A dictionary with the ``status`` and ``code`` keys.

Example
~~~~~~~

Let's get today's prayer times for Doha, Qatar, and print them as a table:

.. code-block:: python

    import aladhan

    location = aladhan.City("Doha", "QA") # Doha, Qatar
    client = aladhan.Client(location)

    adhans = client.get_today_times()

    print("Today's Prayer Times for Doha, Qatar")
    print("======================================")
    for adhan in adhans:
        print("{: <15} | {: <15}".format(adhan.get_en_name(), adhan.readable_timing(show_date=False)))
    
Output:

.. code-block:: text

    Today's Prayer Times for Doha, Qatar
    ======================================
    Fajr            | 04:51 AM
    Dhuhr           | 12:30 PM
    Asr             | 03:45 PM
    Maghrib         | 06:20 PM
    Isha            | 07:40 PM