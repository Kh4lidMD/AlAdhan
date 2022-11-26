# Al Adhan - Islamic prayer times API in Python!

Without any API keys, authentication, or registration, you can use this API to get the Islamic prayer times for any location in the world for free using Python, this project uses the [aladhan.com official prayer times API](https://aladhan.com/prayer-times-api) (thanks to them for the great work and free API).

<br>

I have made this API to convert the JSON responses from the aladhan.com API and simplify them to a Python objects and classes, so you can use them in your Python projects and they are easy to use.

<br>

**This is still the alpha version, there is a lot of coming features, also note that any big changes in the API will happen at any time!**

<br>

If you find any bugs or problems, please report them in the [issues](https://www.github.com/Kh4lidMD/AlAdhan/issues) page.

<br>

# Features

- Get the prayer times for any location in the world.
- Get the prayer times for any date.
- No API keys, authentication, or registration required.
- Converting the JSON responses to Python objects.
- 3 Location methods: Coordinates, City, and Address.

<br>

# Installation

The project is available on [PyPI](https://pypi.org/project/aladhan-api/), so you can install it using pip:

```python
pip install aladhan-api
```

If you have an older version of the API, you can update it to the latest version using:

```python
pip install aladhan-api --upgrade
```

<br>

# Documentation

Not available yet, but coming soon.<br>

<br>

# Versioning

v2.0.1 (Alpha)

- Fixed import error (renamed `aladhan/location.py` to `aladhan/location_types.py`

v2.0.0 (Alpha)

- Changed PIP installation to `aladhan-api`

v1.0.0 (Alpha)

- Initial release.
