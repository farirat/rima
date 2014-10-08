from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='rima',
      version=version,
      description="Minimalist Python REST API Framework",
      long_description="""\
      Minimalist Python REST API Framework
""",
      classifiers=[
          "Development Status :: 1 - Planning",
          "Environment :: Web Environment",
          "Intended Audience :: Information Technology",
          "License :: OSI Approved :: Apache Software License",
          "Natural Language :: English",
          "Operating System :: POSIX :: Linux",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.4",
          "Topic :: Internet",
          "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Server",
      ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='REST API',
      author='Ghassen Telmoudi',
      author_email='ghassen.telmoudi@gmail.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          "tornado",
          "mongoengine",
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
