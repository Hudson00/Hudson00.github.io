"""Cam Hudson Personal Website app's Python package configuration

Written by Cam Hudson
"""

from setuptools import setup

setup(
    name='camhudson',
    version='0.1.0',
    packages=['camhudson'],
    include_package_data=True,
    install_requires=[
        'Flask',
        'html5validator',
        'nodeenv',
        'psycopg2-binary',  # PostgreSQL adapter. TODO: Remove if not using SQL
        'requests',
    ],
    python_requires='>=3.6'
)
