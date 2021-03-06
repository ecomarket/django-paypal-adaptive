#!/usr/bin/env python

from setuptools import setup, find_packages

import paypal

setup(
    name='django-paypal-adaptive',
    version=".".join(map(str, paypaladaptive.__version__)),
    author='Greg McGuire',
    author_email='greg@buzzcar.com',
    maintainer='Greg McGuire',
    maintainer_email="greg@buzzcar.com",
    url='http://github.com/gmcguire/django-paypal-adaptive',
    install_requires=[
        'Django>=1.2',
        'South>=0.7.3',
        'python-money>=0.5.0',
    ],
    description = 'A pluggable Django application for integrating PayPal Adaptive Payments',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)