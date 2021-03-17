#!/usr/bin/python

import setuptools

setuptools.setup(
  name='openfda',
  version='1.0',
  maintainer='openFDA',
  maintainer_email='open@fda.hhs.gov',
  url='http://github.com/fda/openfda',
  python_requires='>=3.6',
  install_requires=[
    'arrow<0.16.0',
    'boto',
    'click',
    'elasticsearch>=6.0.0,<7.0.0',
    'flask',
    'leveldb',
    'luigi<=2.1.1',
    'lxml',
    'nose',
    'mock<=2.0.0',
    'coverage',
    'python-gflags',
    'requests',
    'setproctitle',
    'simplejson',
    'xmltodict',
    'dictsearch'
  ],
  description=('A research project to provide open APIs, raw data downloads, '
               'documentation and examples, and a developer community for an '
               'important collection of FDA public datasets.'),
  packages = ['openfda',
              'openfda.annotation_table',
              'openfda.faers',
              'openfda.spl',
              ],
  zip_safe=False,
  test_suite = 'nose.collector',
)
