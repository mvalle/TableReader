try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'TableReader is a library to write quick scripts to read data in a tabular format',
    'author': 'mvalle',
    'version': '0.1',
    'install_requires': ['xlrd'],
    'packages': ['tablereader'],
    'scripts':[],
    'name': 'tablereader'
}

setup(**config)
