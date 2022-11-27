#create setup.py
from setuptools import setup, find_packages
with open('requirements.txt') as f:
    required = f.read().splitlines()
setup(
    name='snowflake',
    version='1.0',
    description='Snowflake',
    author='Md Mijanur Rahman',
    author_email='md.rahmdn@fau.de',
    install_requires=required,
    packages= ['snowflake'],
    #py_modules=['snowflake'],
    )




