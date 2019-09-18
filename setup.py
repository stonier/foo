#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup


setup(
    name="foo",
    version='0.1.0',
    packages=find_packages(
        exclude=['doc*', 'tests*', 'graveyard*', 'scripts*']
    ),
    data_files=[
        ('share/foo', ['package.xml']),
    ],
    package_data={},
    install_requires=[],
    extras_require={},
    author='Me',
    maintainer='me@gmail.com',
    url='https://github.com/me/me',
    keywords=['ROS', 'behaviour-trees'],
    zip_safe=True,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries'
    ],
    description=(
        "test package"
    ),
    license='BSD',
    test_suite='tests',
    tests_require=[],  # using vanilla py unit tests
)
