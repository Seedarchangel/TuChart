# !/usr/bin/env python
# -*- coding: utf-8 -*-



import codecs
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'tuchart'
DESCRIPTION = 'Graphing app for Chinese stocks. '
URL = 'https://github.com/Seedarchangel/TuChart'
EMAIL = 'rzli2@illinois.com'
AUTHOR = 'Rong Zhou Li'


REQUIRED = [
"pyecharts==0.2.0","tushare","qtpy"
    # 'requests', 'maya', 'records',
]



here = os.path.abspath(os.path.dirname(__file__))




about = {}
with open(os.path.join(here, NAME, '__version__.py')) as f:
    exec (f.read(), about)


class PublishCommand(Command):
    """Support setup.py publish."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.sep.join(('.', 'dist')))
        except FileNotFoundError:
          pass
        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPi via Twine…')
        os.system('twine upload dist/*')

        sys.exit()


setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    #long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=('tests',)),

    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    classifiers=[
      
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    # $ setup.py publish support.
    cmdclass={
        'publish': PublishCommand,
    },
)
