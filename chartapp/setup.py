import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='chartapp',
    version='0.1',
    packages=find_packages(exclude=['demo', 'demo.*']),
    include_package_data=True,
    license='MIT',
    description='simple chartapp for linechart and piechart/donutchart',
    long_description=README,
    author='Firdan Machda',
    author_email='firdan.machda@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: ',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
