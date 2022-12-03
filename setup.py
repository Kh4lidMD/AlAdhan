from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="aladhan-api",
    version="4.1.0",
    author="Khaled Mahmoud",
    author_email="KhalidYBel@gmail.com",
    description="A Python package to calculate Islamic prayer times for any location in the world.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.github.com/Kh4lidMD/AlAdhan",
    packages=find_packages(),
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Natural Language :: Arabic',
        'Natural Language :: English',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License'
    ]
)
