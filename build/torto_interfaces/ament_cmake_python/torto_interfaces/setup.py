from setuptools import find_packages
from setuptools import setup

setup(
    name='torto_interfaces',
    version='0.0.0',
    packages=find_packages(
        include=('torto_interfaces', 'torto_interfaces.*')),
)
