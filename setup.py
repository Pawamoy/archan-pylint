#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
Setup script.

Uses setuptools.
Long description is a concatenation of README.rst and CHANGELOG.rst.
"""

from __future__ import absolute_import, print_function

import io
import re
from glob import glob
from os.path import basename, dirname, join, splitext

from setuptools import find_packages, setup


def read(*names, **kwargs):
    """Read a file in current directory."""
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


setup(
    name='archan-pylint',
    version='0.1.0',
    license='ISC',
    description='Archan plugin for Pylint (number of messages per module).',
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S)
        .sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    author=u'Timothee Mazzucotelli',
    author_email='timothee.mazzucotelli@gmail.com',
    url='https://github.com/Pawamoy/archan-pylint',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ],
    keywords=[
        'archan', 'pylint'
    ],
    install_requires=[
        'archan', 'pylint'
    ],
    entry_points={
        'archan': [
            'archan_pylint.PylintProvider = archan_pylint:PylintProvider'  # noqa
        ]
    },
)
