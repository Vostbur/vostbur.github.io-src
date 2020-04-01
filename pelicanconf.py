#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Vostbur'
SITENAME = 'Little things'
SITESUBTITLE = 'A personal blog.'
SITEURL = ''
THEME = 'theme/blue-penguin'

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = 'Russian'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/Vostbur'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# additional menu items
MENUITEMS = (
    ('GitHub', 'https://github.com/Vostbur'),
)
