# -*- coding: utf-8 -*-

import re
import os
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

here = os.path.dirname(__file__)

version_regex = re.compile(r".*__version__ = '(.*?)'", re.S)
version_script = os.path.join(here, 'sphinxcontrib', 'gravatar', '__init__.py')
version = version_regex.match(open(version_script, 'r').read()).group(1)

long_description = '\n'.join([
    open(os.path.join(here, "README.rst")).read(),
    open(os.path.join(here, "AUTHORS.rst")).read(),
    open(os.path.join(here, "HISTORY.rst")).read(),
])

install_requires = ['Sphinx>=1.2']

tests_require = [
    "pytest-cov",
    "pytest",
    "mock",
]

classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    'Framework :: Sphinx',
    'Framework :: Sphinx :: Extension',
    'Topic :: Documentation',
    'Topic :: Utilities',
]

setup(
    name='sphinxcontrib-gravatar',
    version=version,
    url='https://github.com/tell-k/sphinxcontrib-gravatar',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-gravatar',
    license='BSD',
    author='tell-k',
    author_email='ffk2005 at gmail.com',
    description='Sphinx "gravatar" extension',
    long_description=long_description,
    zip_safe=False,
    classifiers=classifiers,
    platforms='any',
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_require,
    cmdclass={'test': PyTest},
    namespace_packages=['sphinxcontrib'],
)
