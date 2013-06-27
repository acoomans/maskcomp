from setuptools import setup

config = {
	'name': 'Maskcomp',
	'version': '0.1',
	'description': 'Compares images with a mask',
	'license': 'LICENSE.txt',
	'url': '',
	'download_url': '',
	'author': 'Arnaud Coomans',
	'install_requires': ['PIL'],
	'packages': ['maskcomp'],
	'scripts': ['bin/mcomp.py'],
	'data_files' : [('uiautomation', ['extras/uiautomation/screen.js'])],
	'zip_safe': False
}

setup(**config)