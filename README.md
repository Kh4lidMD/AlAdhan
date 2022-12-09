# Al Adhan - Islamic prayer times API in Python!

Without any API keys, authentication, or registration, you can use this API to get the Islamic Adhan (_a call to prayer_) times  for any location in the world for free using Python, this project uses the [aladhan.com official prayer times API](https://aladhan.com/prayer-times-api) (thanks to them for the great work and free API). I have made this API to convert the JSON responses from the aladhan.com API and simplify them to a Python objects and classes, so you can use them in your Python projects and they are easy to use. 

<img src="./thumbnail.jpg">

**This is still the alpha version, there is a lot of coming features, also note that any big changes in the API will happen at any time!** If you find any bugs or problems, please report them in the [issues](https://www.github.com/Kh4lidMD/AlAdhan/issues) page.

<br>

_Learn more about Adhan in [Wikipedia](https://en.wikipedia.org/wiki/Adhan)_

<br>

# Features

- Get the prayer times for any location in the world.
- Get the prayer times for any date.
- No API keys, authentication, or registration required.
- Converting the JSON responses to Python objects.
- 3 Location methods: Coordinates, City, and Address.
- More Adhan metadata made by the module, such as the number of rakat in salah, sunnan al rawatib rakat number, is hijri or secret salah, etc.

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

v5.0.0 (Alpha) **Latest**

- Set `threaded_wait` default argument in the `Adhan.wait` method from `True` to `False`.
- Added missing file `aladhan/exceptions.py` to the repository. which was included in the package but not in the repository.
- Changed `RateLimitException` to `RateLimitedException` (typo fix).
- Added `sunnan_al_rawatib` function to the `Adhan` object, returns a dictionary with `before` and `after` keys, each one contains the sunnan al rawatib rakat number.
  - _[English Source](https://www.wikihow.com/Pray-Sunnah-Prayers)_
  - _[Arabic Source](https://mawdoo3.com/%D9%85%D8%A7_%D9%87%D9%8A_%D8%B3%D9%86%D9%86_%D8%A7%D9%84%D8%B5%D9%84%D8%A7%D8%A9_%D8%A7%D9%84%D9%85%D8%A4%D9%83%D8%AF%D8%A9)_
- Added `__version__` attribute to the `aladhan` module, a version tuple like `(major, minor, patch)`.

v4.1.0 (Alpha)

- Added custom exceptions especially for the following return codes:
  - 400 bad request error: `BadRequestException`
  - 429 rate limited error: `RateLimitedException`
  - 500 internal server error: `ServerErrorException`

  _They're avaialble in the `aladhan.exceptions`, could be directly imported from the `aladhan` module._
- New Wiki page: [Exception Handling](https://www.github.com/Kh4lidMD/AlAdhan/wiki/Exception-Handling)

  _Started to save a copy of the Wiki pages in every release._

v4.0.0 (Alpha)

- Removed the `get_prayer_times` method, replaced with `get_today_times`, `get_calendar_times`, and `get_annual_times` methods.
- Fixed missing usage of `year` and `month` arguments in the calendar method.
- Added `callback` and `threaded_wait` arguments to the `Adhan.wait` method.
- Better code structure.
- _These Wiki pages have been updated:_
  - [_Get Prayer Times_](https://www.github.com/Kh4lidMD/AlAdhan/wiki/Get-Prayer-Times)
  - [_Adhan Object_](https://www.github.com/Kh4lidMD/AlAdhan/wiki/Adhan-Object)

v3.0.0 (Alpha)

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

<br><br>

<h3 align="center">
وَأَقِيمُوا الصَّلَاةَ وَآتُوا الزَّكَاةَ ۚ وَمَا تُقَدِّمُوا لِأَنفُسِكُم مِّنْ خَيْرٍ تَجِدُوهُ عِندَ اللَّهِ ۗ إِنَّ اللَّهَ بِمَا تَعْمَلُونَ بَصِيرٌ
<br><br>
سورة البقرة، آية : 110
</h3>
<hr>
