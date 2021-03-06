from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-edem',
    version=version,
    description="projekt E-Demokracia",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Dominik',
    author_email='kapisinsky@microcomp.sk',
    url='edem.microcomp.sk',
    license='GPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.edem'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    #entry_points='''
    #    [ckan.plugins]
    #    # Add plugins here, e.g.
    #    edem =ckanext.edem.plugin:EdemCustomPlugin
    #''',
    entry_points={
        'babel.extractors': [
                    'ckan = ckan.lib.extract:extract_ckan',
                    ],
        'ckan.plugins' : [
                    'edem =ckanext.edem.plugin:EdemCustomPlugin',
                    ]
        }

    
)
