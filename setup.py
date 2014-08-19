import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-typeahead-textinput',
    version='0.3',
    packages=['django_typeahead_textinput'],
    include_package_data=True,
    license='MIT License',
    description='Typeahead Autocomplete for textfields and textinput widgets in Django',
    long_description=README,
    url='http://www.fh-brandenburg.de',
    author='Daniel Weis',
    author_email='weisd@fh-brandenburg.de',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
)