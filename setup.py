__author__ = 'roy'

import os

from setuptools import setup, find_packages

ROOT = os.path.abspath(os.path.dirname(__file__))

README = open(os.path.join(ROOT, 'README.rst')).read()
CHANGES = open(os.path.join(ROOT, 'CHANGES.md')).read()

requires = [
    'nose',
]


setup(name='nose-logpertest',
      version='0.0.1',
      description='Logging nose plugin to create log per test',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: Apache Software License",
          "Operating System :: OS Independent",
          "Topic :: Software Development :: Testing",
      ],
      license='Apache Software License',
      author='Roy Klinger',
      author_email='roy@taykey.com',
      url='https://github.com/taykey/nose-logpertest',
      packages=find_packages(),
      keywords='nosetest logging',
      include_package_data=False,
      zip_safe=False,
      entry_points="""\
      [nose.plugins.0.10]
      logpertest = nose_logpertest:LogPerTest
      """,
      install_requires=requires)