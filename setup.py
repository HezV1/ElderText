import ez_setup
ez_setup.use_setuptools()

try:
    from setuptools import setup, find_packages
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
    'entry_points': {'console_scripts': [
        'eldertext = eldertext.__main__:main']},
    'name': 'eldertext'
}

setup(**config)
