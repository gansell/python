# file: setup_hand.py

from distutils.core import setup
from distutils.extension import Extension

name = 'count_ext'
version = '1.0'

sources = ['count.c', 'count_ext.c']          #1

setup(name = name, version = version,         #2
      ext_modules=[Extension(name, sources)])