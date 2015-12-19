try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Table reader lib',
    'author': 'Table Reader',
    'url': 'example.com',
    'download_url': 'example.com',
    'author_email': 'email@example.com',
    'version': '0.1',
    'install_requires': [],
    'packages': ['tablereader'],
    'scripts':[],
    'name': 'tablereader'
}

setup(**config)
