import os

from setuptools import setup, find_packages

ROOT = os.path.abspath(os.path.dirname(__file__))

README = open(os.path.join(ROOT, 'README.rst')).read()

requires = [
    'nose',
]


setup(name='nose-logpertest',
      version='0.0.1',
      description='logging plugin to create log per test',
      long_description=README,
      classifiers=[
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Software Development :: Testing",
      ],
      license='MIT',
      author='Roy Klinger',
      author_email='roy@taykey.com',
      url='',
      packages=find_packages(),
      keywords='nosetest logging',
      include_package_data=True,
      zip_safe=False,
      entry_points="""\
      [nose.plugins.0.10]
      logpertest = nose_logpertest:LogPerTest
      """,
      install_requires=requires)