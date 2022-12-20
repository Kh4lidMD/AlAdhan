===================
Initializing Client
===================

:code:`aladhan.Client` is the main class of the library. 

Arguments:

- ``default_location: City | Coordinates | Address``: The location of the client. This can be a City, Coordinates or Address object (optional, default= ``None``).

Example of initializing a client with a City object:

.. code-block:: python

    >>> import aladhan
    >>>
    >>> location = aladhan.City("London", "GB")
    >>> client = aladhan.Client(location)

.. Note:: The `default_location` argument is optional. If it is not provided when the class is initialized, then the location must be provided for each method call. If `default_location` is provided both in the main class and in a method call, then the location provided in the method call will be used.