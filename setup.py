#!/usr/bin/env python
from setuptools import find_packages, setup

with open('README.rst', 'r') as f:
    README = f.read()

setup(
    name='airgun',
    version='0.0.1',
    description='TBD',
    long_description=README,
    author=u'RedHat QE Team',
    url='https://bitbucket.org/Balah/airgun',
    packages=find_packages(exclude=['tests*']),
    package_data={'': ['LICENSE']},
    include_package_data=True,
    license='GNU GPL v3.0',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux'
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ),
)
