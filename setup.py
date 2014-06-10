# coding=utf-8

import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-satchmo-grappelli',
    version='0.2',
    packages=['satchmo_grappelli'],
    include_package_data=True,
    license='MIT License',  # example license
    description='Skin for satchmo',
    long_description=README,
    url='https://github.com/lvelezsantos/django-satchmo-grappelli',
    author='Luis Velez',
    author_email='lvelezsantos@gmail.com',
    classifiers=[
        "Development Status :: Beta",
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        "Framework :: Django",

    ],
)
