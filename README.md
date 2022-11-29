# Al Adhan - Islamic prayer times API in Python!

Without any API keys, authentication, or registration, you can use this API to get the Islamic prayer (called salah) times for any location in the world for free using Python, this project uses the [aladhan.com official prayer times API](https://aladhan.com/prayer-times-api) (thanks to them for the great work and free API). I have made this API to convert the JSON responses from the aladhan.com API and simplify them to a Python objects and classes, so you can use them in your Python projects and they are easy to use. **This is still the alpha version, there is a lot of coming features, also note that any big changes in the API will happen at any time!** If you find any bugs or problems, please report them in the [issues](https://www.github.com/Kh4lidMD/AlAdhan/issues) page.

<br>

# Features

- Get the prayer times for any location in the world.
- Get the prayer times for any date.
- No API keys, authentication, or registration required.
- Converting the JSON responses to Python objects.
- 3 Location methods: Coordinates, City, and Address.

<br>

# Installation

The project is available on [PyPI](https://pypi.org/project/aladhan-api/), so you can install it using [pip](https://www.w3schools.com/python/python_pip.asp):

```python
pip install aladhan-api
```

If you have an older version of the API, you can update it to the latest version using:

```python
pip install aladhan-api --upgrade
```

<br>

# Documentation

See the [Wiki](https://www.github.com/Kh4lidMD/AlAdhan/wiki)

<br>

# Versioning

v3.0.0 (Alpha) **Latest**

- Changed `get_calendar` name to `get_prayer_times`.
- Added `today_only` parameter to `get_prayer_times`.
- Folder documentation removed.
- New better documentation hosted in the repository [Wiki](https://www.github.com/Kh4lidMD/AlAdhan/wiki).
- All `aladhan.location_types` objects are now available in the main import directly (e.g. `aladhan.location_types.City` _could_ be `aladhan.City`).
- Removed `ValueError` when only one of the `year` or `month` parameters is passed to `get_prayer_times`. Because the API does not return an error when one of them is missing.

v2.2.0 (Alpha)

- Added `rakat` method for the `Adhan` object, returns the number of rakat in salah.
- New Documentation.

v2.0.1 (Alpha)

- Fixed import error (renamed `aladhan/location.py` to `aladhan/location_types.py`).

v2.0.0 (Alpha)

- Changed PIP installation to `aladhan-api`.

v1.0.0 (Alpha)

- Initial release.
