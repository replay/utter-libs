#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='utter_libs',
      version='0.1',
      author='Mauro Stettler',
      author_email='mauro.stettler@gmail.com',
      license='MIT',
      description='Shared libs that are used by utter projects',
      py_modules=['utter_libs'],
      packages=find_packages())
