#!/usr/bin/env python2
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'spaceapi_open',
    'author': 'Loïs Postula',
    'url': 'github.com/loispostula/spaceapi_open',
    'author_email': 'lois.postula@gmail.com',
    'version': '0.1',
    'packages': ['spaceapi_open'],
    'license': 'gpl-v2',

    'scripts': [],
    'name': 'spaceapi_open',
    'entry_points': {
        'console_scripts': [
            'spaceapi_open = spaceapi_open.main:main',
        ],
    },
}

setup(**config)
