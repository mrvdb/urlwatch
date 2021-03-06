#!/usr/bin/python
# -*- coding: utf-8 -*-
# Minimalistic, automatic setup.py file for Python modules
# Copyright (c) 2008-2016 Thomas Perl <thp.io/about>

from setuptools import setup

import os
import re

PACKAGE_NAME = 'urlwatch'
DEPENDENCIES = ['minidb', 'PyYAML', 'requests']

# Assumptions:
#  1. Package name equals main script file name (and only one script)
#  2. Main script contains docstring + dunder-{author, license, url, version}
#  3. Data files are in "share/", will be installed in $(PREFIX)/share
#  4. Packages are in "lib/", no modules

main_py = open('lib/%s/__init__.py' % PACKAGE_NAME).read()
m = dict(re.findall("\n__([a-z]+)__ = '([^']+)'", main_py))
docs = re.findall('"""(.*?)"""', main_py, re.DOTALL)

m['name'] = PACKAGE_NAME
m['author'], m['author_email'] = re.match(r'(.*) <(.*)>', m['author']).groups()
m['description'], m['long_description'] = docs[0].strip().split('\n\n', 1)
m['download_url'] = m['url'] + PACKAGE_NAME + '-' + m['version'] + '.tar.gz'

m['scripts'] = [PACKAGE_NAME]
m['package_dir'] = {'': 'lib'}
m['packages'] = ['.'.join(dirname.split(os.sep)[1:]) for dirname, _, files in os.walk('lib') if '__init__.py' in files]
m['data_files'] = [(dirname, [os.path.join(dirname, fn) for fn in files]) for dirname, _, files in os.walk('share')]
m['install_requires'] = DEPENDENCIES

setup(**m)
