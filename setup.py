#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='build',
    version='0.0.2',
    project_urls={'homepage': 'https://github.com/FFY00/python-build'},
    author='Filipe Laíns',
    author_email='lains@archlinux.org',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ],
    packages=['build'],
    install_requires=[
        'toml'
        'pep517',
        'packaging',
        'importlib-metadata; python_version < "3.8"',
    ],
)
