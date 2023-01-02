============
Client Class
============

This is the main class of the library, it's used to get the prayer times for a specific location and date, and other useful methods.

aladhan.Client
~~~~~~~~~~~~~~

Arguments:

- ``default_location: City | Coordinates | Address``: The location of the client. This can be a City, Coordinates or Address object (optional, default= ``None``).

Example of initializing a client with a City object:

.. code-block:: python

    >>> import aladhan
    >>>
    >>> location = aladhan.City("London", "GB")
    >>> client = aladhan.Client(location)

.. Note:: The `default_location` argument is optional. If it is not provided when the class is initialized, then the location must be provided for each method call. If `default_location` is provided both in the main class and in a method call, then the location provided in the method call will be used.

aladhan.Client.get_today_times
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Returns a list of `Adhan` objects for today's prayer times.

Arguments:

- ``location: City | Coordinates | Address``: Location of the prayer times (optional, default= ``None``).

aladhan.Client.get_calendar_times
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Returns a list of `Adhan` objects for the current month's prayer times, or you can specify the ``month`` and ``year`` arguments to get a specifc date.

Arguments:

- ``location: City | Coordinates | Address``: Location of the prayer times (optional).
- ``month: int``: Month number (optional, default= ``None``).
- ``year: int``: Year number (optional, default= ``None``).

aladhan.Client.get_annual_times
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Returns a list of `Adhan` objects for specifc year's prayer times (current year by default), which returns all the prayer times for the year, day by day.

Arguments:

- ``location: City | Coordinates | Address``: Location of the prayer times (optional, default=``None``).
- ``year: int``: Year number (optional, default= ``None``).

All the get_*_times methods have the same raises:

- ``aladhan.exceptions.InvalidLocationException``: Raised when the location is invalid.
- ``aladhan.exceptions.RateLimitedException``: Raised when the client is rate limited by the server.
- ``aladhan.exceptions.BadRequestException``: Raised when the request is invalid (e.g. invalid date).
- ``aladhan.exceptions.ServerErrorException``: Raised when the server responds with unhandled error.

aladhan.Client.api_status
~~~~~~~~~~~~~~~~~~~~~~~~~

Get the status of the API, returns a dictionary with the `status` and `code` keys, might raise an `requests.exceptions.ConnectionError` if the website is down.

Returns:

- ``dict``: A dictionary with the ``status`` and ``code`` keys.

Table of today's prayer times example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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