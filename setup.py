from setuptools import setup, find_packages

setup(
    name = 'movie_package',
    version = '0.0.1',
    packages = find_packages()
    requires = ['numpy', 'pandas']
    )