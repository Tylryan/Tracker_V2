#!/usr/bin/python3

from setuptools import setup, find_packages

setup(
    name='tracker-cli',
    version='0.0.2',
    description='Tracks and analyzes users tasks',
    author='Tyler Ryan',
    author_email='tlrrn5@gmail.com',
    url='https://github.com/Tylryan/Tracker_V2',
    # find_packages(exclude=('modules','you','want','to','exclude'))
    install_requires=['pandas', 'matplotlib'],
    packages=find_packages(),
    entry_points={
        'console_scripts': ['tracker-cli=tracker_cli.main:main']
    }
)
