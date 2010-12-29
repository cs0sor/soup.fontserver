from setuptools import setup, find_packages
import sys, os
import os
import sys

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()


version = '0.1'

setup(name='soup.fontserver',
      version=version,
      description="@@FontFace server",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Simon Oram',
      author_email='simon@electrosoup.co.uk',
      url='http://www.electrosoup.co.uk',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""\
      [paste.app.factory]
      app = sorg.fontserver.fontserver.run:app
      """,
      )