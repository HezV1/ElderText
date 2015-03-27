try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Open world text adventure based on Skyrim',
    'author': 'Conrad Hoffman',
    'url': 'https://github.com/hezakia1/ElderText',
    'download_url': 'https://github.com/hezakia1/ElderText/archive/d17829ed4e969d7b8b205327d5bbc73109023c66.zip',
    'author_email': 'conrad.r.hoffman@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['eldertext'],
    'scripts': [],
    'name': 'eldertext'
}

setup(**config)
