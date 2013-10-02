#!/usr/bin/python

from setuptools import setup

setup(name='pysentiment',
      version='0.1',
      description='Python sentiment analysis utilities',
      author='Zhichao HAN',
      author_email='hanzhichao@gmail.com',
      packages=['pysentiment'],
      install_requires=['pandas >= 0.10',
                        'nltk >= 2.0'],
      data_files=[('pysentiment.static', 
                   ['pysentiment/static/%s' % e for e in [
                        'HIV-4.csv', 'LM.csv', 
                        'Currencies.txt', 'DatesandNumbers.txt', 
                        'Generic.txt', 'Geographic.txt', 'Names.txt']])])