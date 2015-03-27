try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'An open world text based adventure game based on skyrim',
    'author': 'Conrad Hoffman',
    'url': 'https://github.com/hezakia1/ElderText',
    'download_url': 'https://github.com/hezakia1/ElderText/archive/master.zip',
    'author_email': 'conrad.r.hoffman@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['eldertext'],
    'scripts': [],
    'name': 'Elder Text'
}

setup(**config)
