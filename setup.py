# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'anuket',
    'geoalchemy',
    'psycopg2',
    ]

tests_require = [
    'WebTest',
    ]

setup(name='begotemp',
    version='0.1a',
    description='Begotemp alpha stage application',
    long_description=README + '\n\n' +  CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
    author='LDPL - Laboratoire Départemental de Préhistoire du Lazaret',
    author_email='opensource@lazaret.unice.fr',
    url='http://github.com/miniwark/begotemp',
    license='LICENSE.txt',
    keywords='web wsgi pyramid',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    tests_require=tests_require,
    test_suite="begotemp",
    entry_points = """\
    [paste.app_factory]
    main = begotemp:main
    """,
    )
