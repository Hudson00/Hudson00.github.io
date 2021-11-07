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
        # 'arrow',
        'boto3',
        'botocore',
        'Flask',
        # 'html5validator',
        # 'nodeenv',
        # 'requests',
    ],
    python_requires='>=3.6'
)
