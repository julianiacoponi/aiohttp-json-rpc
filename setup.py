#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='aiohttp-json-rpc',
      version='0.1.1',
      author='Florian Scherf',
      url='https://github.com/pengutronix/aiohttp-json-rpc/tree/doc',
      author_email='f.scherf@pengutronix.de',
      license='Apache 2.0',
      install_requires=['aiohttp>=0.17.0'],
      packages=['aiohttp_json_rpc'],
      zip_safe=False)
