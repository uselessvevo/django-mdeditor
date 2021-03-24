# -*- coding:utf-8 -*-
import os
from codecs import open
from setuptools import find_packages, setup


with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as readme:
    long_description = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-mdeditor',
    version='0.1.19-forked',
    packages=find_packages(exclude=[
        'mdeditor_demo',
        'mdeditor_demo_app',
        'mdeditor_demo_app.*',
    ]),
    include_package_data=True,
    license='GPL-3.0 License',
    description='A simple Django app to edit markdown text.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/pylixm/django-mdeditor',
    author='DeanWu',
    author_email='pyli.xm@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
    ]
)
