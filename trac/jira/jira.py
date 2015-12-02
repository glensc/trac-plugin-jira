# -*- coding: utf-8 -*-
#
# Copyright (C) 2008-2015 Elan Ruusamäe <glen@pld-linux.org>
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution. The terms
# are also available at http://trac.edgewall.com/license.html.
#
# Author: Elan Ruusamäe <glen@pld-linux.org>

from trac.core import implements, Component
from trac.wiki import IWikiSyntaxProvider
import trac

if [int(x) for x in trac.__version__.split('.')] >= [0, 11]:
	# trac 0.11
	from genshi.builder import tag
else:
	# trac 0.10
	from trac.util.html import html as tag

class TracJiraLink(Component):
	implements(IWikiSyntaxProvider)

	ticket_regexp = r"\b[A-Z]+?-(?P<id>\d+)\b"

	# IWikiSyntaxProvider methods
	def get_wiki_syntax(self):
		jira_url = self.env.config.get('jira', 'url')

		def ticket(formatter, match, fullmatch):
			return tag.a(tag.span(u'\u200b', class_="icon"), match, class_="ext-link", href=jira_url % int(fullmatch.group('id')))

		if jira_url:
			yield (self.ticket_regexp, ticket)
		else:
			self.log.warn('url not set in configuration. Jira links disabled')

	def get_link_resolvers(self):
		return []
