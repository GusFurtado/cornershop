from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'cornershop',
  packages = ['cornershop'],
  version = '0.1.0',
  license = 'MIT',
  description = "A Python wrapper for Cornershop by Uber's API.",
  long_description = long_description,
  long_description_content_type = 'text/markdown', 
  author = 'Gustavo Furtado',
  author_email = 'gustavofurtado2@gmail.com',
  url = 'https://github.com/GusFurtado/cornershop',
  download_url = 'https://github.com/GusFurtado/cornershop/archive/0.1.0.tar.gz',

  keywords = [
    'python',
    'api',
    'wrapper',
    'uber',
    'delivery',
    'cornershop' 
  ],

  install_requires = [
    'requests'
  ],

  classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Other Audience',
    'Topic :: Other/Nonlisted Topic',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6'
  ]
)