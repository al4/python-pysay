from setuptools import setup

__author__ = 'Your name'


setup(
    name='pysay',
    version='0.0.3',
    description='Simple tutorial from al4.co.nz',
    author='Your Name',
    author_email='you@domain',
    license='MIT',
    url='https://github.com/al4/python-pysay',
    packages=['pysay'],
    entry_points={
        'console_scripts': [
            'pysay=pysay:main',
        ]
    },
)
