from setuptools import setup

__author__ = 'Your name'


setup(
    name='pysay',
    version='0.0.2',
    packages=['pysay'],
    entry_points={
        'console_scripts': [
            'pysay=pysay:main',
        ]
    },
)
