==================
Exception Handling
==================

You can handle exceptions by importing them directly from the ``aladhan`` module, this page describes what each exception is for, and when it's raised.

aladhan.BadRequestException
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This exception is raised when the API returns a 400 bad request error, this happens when the API is unable to process the request, for example, some of the parameters are missing, or invalid.

.. code-block:: python

    import aladhan

    location = aladhan.City("ABC", "EFG") # Invalid city and country
    client = aladhan.Client(location)

    print(client.get_today_times()) # Raises BadRequestException

aladhan.RateLimitedException
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This exception is raised when the API returns a 429 Too Many Requests error, this happens when the API is being used too much, and the rate limit is reached.

According to the API, on this `source <https://community.islamic.network/d/2-is-there-a-rate-limit-on-the-apis>`_:

.. code-block:: bash

    For the AlAdhan API in each region, each IP is allowed approximately 14 requests per second.

This could happen if you're calling the API too fast.

aladhan.ServerErrorException
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This exception is raised when the API returns a 500 Internal Server Error error, this means that the API got a non-handled error, and it's unable to process the request.

Which is very common in the API due to unhandled errors.

aladhan.InvalidLocationException
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Exception raised when a invalid location is provided, e.g invalid coordinates.

.. code-block:: python

    >>> import aladhan
    >>> 
    >>> location = aladhan.Coordinates(0, 1000)
    Traceback (most recent call last):
        File "...", line 1, in <module>
        File "...\location_types.py", line 10, in __init__
            raise InvalidLocationException("Invalid coordinates")
    aladhan.exceptions.InvalidLocationException: Invalid coordinates
