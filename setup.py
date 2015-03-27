try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
<<<<<<< HEAD
    'description': 'An open world text based adventure game based on skyrim',
    'author': 'Conrad Hoffman',
    'url': 'https://github.com/hezakia1/ElderText',
    'download_url': 'https://github.com/hezakia1/ElderText/archive/master.zip',
=======
    'description': 'Open world text adventure based on Skyrim',
    'author': 'Conrad Hoffman',
    'url': 'https://github.com/hezakia1/ElderText',
    'download_url': 'https://github.com/hezakia1/ElderText/archive/d17829ed4e969d7b8b205327d5bbc73109023c66.zip',
>>>>>>> 19709803bcfa68cb5acb18ed11dd7752fea728ea
    'author_email': 'conrad.r.hoffman@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['eldertext'],
    'scripts': [],
<<<<<<< HEAD
    'name': 'Elder Text'
=======
    'name': 'eldertext'
>>>>>>> 19709803bcfa68cb5acb18ed11dd7752fea728ea
}

setup(**config)
