# Adhan object

As a result of the `get_calendar` method, you will get a list of `Adhan` objects. Here is a full list of attributes:

<br>

## Adhan.readable_timing

Returns the prayer time in a readable format.

Arguments:

- `show_time: bool=True` to show the time or not.
- `show_date: bool=True` to show the date in the YYYY/MM/DD format or not.
- `_24h: bool=False` display the time in 24h format.
- `arabic: bool=False` display the time in Arabic (change English numbers to Arabic and PM/AM to ص/م).

Returns:

- `str`

Raises:

- Nothing

Note: the date comes first, then the time if both are shown.

<br>

## Adhan.wait

Wait until the prayer time is reached in a loop.

Arguments:

- Nothing

Returns:

- `None`

Raises:

- Nothing

<br>

## Adhan.is_passed

Check if the prayer time is passed or not.

Arguments:

- Nothing

Returns:

- `bool`

Raises:

- Nothing

<br>

## Adhan.is_hijri

Check if the date is Hijri (هجرية) or not.

Arguments:

- Nothing

Returns:

- `bool`

Raises:

- Nothing

<br>

## Adhan.is_secret

Check if the prayer time is secret (سرية) or not.

Arguments:

- Nothing

Returns:

- `bool`

Raises:

- Nothing

<br>

## Adhan.rakat

Returns the number of rakat for the prayer.

Arguments:

- Nothing

Returns:

- `int`

Raises:

- Nothing

<br>

## Adhan.get_name

Get the name of the prayer time.

Arguments:

- `lang: str='en'` set this to `ar` to get the Arabic name.

Returns:

- `str`

Raises:

- Nothing

<br>

[Previous: Getting prayer times](/docs/3%2C%20getting%20prayer%20times.md)
