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
        'Flask-SQLAlchemy==2.4.0',
        'SQLAlchemy==1.3.3',
        'gtfs-realtime-bindings==0.0.5',
        'requests==2.22.0',
    ],
)
