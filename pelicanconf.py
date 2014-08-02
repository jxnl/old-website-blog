#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jason Liu'
SITENAME = 'jxnl.co'
SITEURL = 'jxnl.github.io'

STATIC_PATHS = ['images']
# EXTRA_PATH_METADATA = {'extra/CNAME': {'path', 'CNAME'}}

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{slug}/index.html'

DISPLAY_PAGES_ON_MENU = True

ABOUT_PAGE = SITEURL+"/pages/about.html"

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

GITHUB_USERNAME, TWITTER_USERNAME = "jxnl", "jxnlco"
DRIBBBLE_USERNAME = 'jxnl'
DISQUS_USERNAME = 'jxnlgithub'
SHOW_ARCHIVES = True

MARKUP = ('md', 'ipynb')
THEME = './themes/middle'

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb']

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
