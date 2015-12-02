# -*- coding: utf-8 -*-
from setuptools import setup

setup(
	name='TracJiraLink',
	version='0.1',
	author='Elan Ruusamäe',
	author_email='glen@pld-linux.org',
	description='Automatically create links for Jira Issue Id-s.',
	url='https://github.com/glensc/trac-plugin-jira',
	license='BSD-like',
	packages=['trac.jira'],
	entry_points = {'trac.plugins': ['trac.jira = trac.jira']}
)
