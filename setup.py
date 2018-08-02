from pip.req import parse_requirements

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

install_reqs = parse_requirements('requirements.txt')
reqs = [str(ir.req) for ir in install_reqs]

config ='description': 'Insight',
	'author_email': 'rolan86@gmail.com',
	'version': '0.1',
	'install_requires': reqs,
	'packages': ['Insight'],
	'scripts': [],
	'name': 'insight'
}

setup(**config)
