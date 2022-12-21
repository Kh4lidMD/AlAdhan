============
Adhan Object
============

Let's get some ``Adhan`` objects:

.. code-block:: python

    import aladhan

    # initialize the client
    location = aladhan.City("Doha", "QA")
    client = aladhan.Client(location)

    # get the today's adhan times using aladhan.Client.get_today_times
    # this will return 5 Adhan objects
    times = client.get_today_times()

Here is a full list of all the attributes of the ``Adhan`` object:

aladhan.Adhan.readable_timing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Returns the prayer time in a human readable format.

Arguments:

- ``show_time (bool)``: to show the time or not (optional, default= ``True``)
- ``show_date (bool)``: to show the date in the YYYY/MM/DD format or not (optional, default= ``True``)
- ``_24h (bool)`` display the time in 24h format (optional, default= ``False``)
- ``arabic (bool)`` display the time in Arabic (change English numbers to Arabic and PM/AM to ص/م) (optional, default= ``False``)

Example:

.. code-block:: python

    >>> some_adhan = calendar[2]
    >>>
    >>> print(some_adhan.readable_timing())
    >>> # 2021/07/03 11:00 AM
    >>>
    >>> print(some_adhan.readable_timing(show_time=False))
    >>> # 2021/07/03
    >>>
    >>> print(some_adhan.readable_timing(show_date=False))
    >>> # 11:00 AM
    >>>
    >>> print(some_adhan.readable_timing(_24h=True))
    >>> # 2021/07/03 11:00

aladhan.Adhan.wait
~~~~~~~~~~~~~~~~~~

Wait until the salah time has passed, and do a callback if provided.

Arguments:

- ``callback (callable)``: a function to call when the salah time has passed (optional, default= ``None``)
- ``threaded_wait (bool)``: to wait in a separate thread or not, this is useful if you want to do other things while waiting and having a callback function (optional, default= ``False``)
- ``*args``: arguments to pass to the callback function (optional)
- ``**kwargs``: keyword arguments to pass to the callback function (optional)

aladhan.Adhan.is_passed
~~~~~~~~~~~~~~~~~~~~~~~

Check if the salah time has passed or not.

Returns:

- ``bool``: ``True`` if the salah time has passed, ``False`` otherwise.

aladhan.Adhan.is_hijri
~~~~~~~~~~~~~~~~~~~~~~

Check if the salah is hijri (هجرية) or not.

Returns:

- ``bool``: ``True`` if the salah is hijri, ``False`` otherwise.

aladhan.Adhan.is_secret
~~~~~~~~~~~~~~~~~~~~~~~

Check if the salah is secret (سرية) or not.

Returns:

- ``bool``: ``True`` if the salah is secret, ``False`` otherwise.

aladhan.Adhan.rakat
~~~~~~~~~~~~~~~~~~~

Get the number of rakat of the salah.

Returns:

- ``int``: the number of rakat of the salah.

aladhan.Adhan.get_en_name
~~~~~~~~~~~~~~~~~~~~~~~~~

Returns the English name of the salah.

Returns:

- ``str``: the English name of the salah.

aladhan.Adhan.get_ar_name
~~~~~~~~~~~~~~~~~~~~~~~~~

Returns the Arabic name of the salah.

Arguments:

- ``tashkeel (bool)``: to add tashkeel to the Arabic name or not (optional, default= ``False``)
- ``include_al (bool)``: to include the definite article (ال) or not (e.g. العشاء instead of عشاء) (optional, default= ``False``)

Returns:

- ``str``: the Arabic name of the salah.

aladhan.Adhan.sunnan_al_rawatib
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Returns the sunnan al rawatib rakat number before and after the salah in a dict.

Returns:

- ``dict``: a dict with the keys ``before`` and ``after`` and the values are the rakat numbers.

