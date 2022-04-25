from setuptools import setup, find_packages

import modules

setup(
    name=modules.__package_name__,
    version=modules.__version__,
    packages=find_packages(),
)
