#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='stm_scheduler',
    version=open('version').read(),
    packages=find_packages(),
    long_description=open('README.md').read(),
    url='http://github.com/waxisien/stm-scheduler',
    install_requires=[
        'Flask==1.0.2',
        'Flask-Caching==1.7.2',
        'gtfs-realtime-bindings==0.0.5',
        'requests==2.31.0',
    ],
)
