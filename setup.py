# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='dailytao',
    version='0.1',
    description='Daily Tao chapters from the command line',
    long_description=readme,
    author='Mike Adams',
    author_email='adams.mj@me.com',
    url='https://github.com/M1keadams/dailytao',
    license=license,
    entry_points = {
        'console_scripts': ['dailytao=dailytao.command_line:main'],
    },
    packages=['dailytao'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: System Administrators',
        'Topic :: Other/Nonlisted Topic',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)

