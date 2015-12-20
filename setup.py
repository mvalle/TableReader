try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'TableReader is a library to write quick scripts to read data in a tabular format',
    'author': 'mvalle',
    'version': '0.3',
    'install_requires': ['xlrd>=0.8.0', 'ezodf'],
    'setup_requires': ['pytest-runner'],
    'tests_requrie': ['pytest'],
    'packages': ['tablereader'],
    'scripts':[],
    'name': 'tablereader'
}

setup(**config)
