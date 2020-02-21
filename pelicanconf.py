#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime


AUTHOR = 'LocoBOTS'
#SITEURL = 'http://yoursite.com'
SITENAME = 'LocoBOTS'
SITETITLE = 'LocoBOTS'
SITESUBTITLE = 'Núcleo de desenvolvimento em robótica'
SITEDESCRIPTION = 'Dê asas aos Locos e eles darão vidas às máquinas'
SITELOGO = 'https://avatars3.githubusercontent.com/u/40442965?s=400&v=4'
#FAVICON = SITEURL + '/images/favicon.ico'
RELATIVE_URLS = True
BROWSER_COLOR = 'black'
PYGMENTS_STYLE = 'monokai'
STATIC_PATHS = ['images', 'static']
CUSTOM_CSS = 'static/custom.css'


ROBOTS = 'index, follow'

THEME = 'Flex'
PATH = 'content'
#OUTPUT_PATH = 'blog/'
TIMEZONE = 'America/Sao_Paulo'

I18N_TEMPLATES_LANG = 'pt_BR'
DEFAULT_LANG = 'pt_BR'
OG_LOCALE = 'pt_BR'
LOCALE = 'pt_BR'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True
PAGES_SORT_ATTRIBUTE = 'date'

LINKS_IN_NEW_TAB = 'external'

# Blogroll
LINKS = (('BLOG', '/'),)
         
# Social widget
SOCIAL = (('facebook', 'https://www.facebook.com/locobots'),
          ('instagram', 'https://www.instagram.com/locobots.ufop/'),
          ('github', 'https://www.github.com/locobots'),
          ('linkedin', 'https://www.linkedin.com/company/n%C3%BAcleo-de-desenvolvimento-em-rob%C3%B3tica-locobots/about/')
          )
#MENUITEMS = (('Archives', '/archives.html'),
#             ('Categories', '/categories.html'),
#     Archives        ('Tags', '/tags.html'),)

#CC_LICENSE = {
#    'name': 'Creative Commons Attribution-ShareAlike',
#    'version': '4.0',
#    'slug': 'by-sa'
#}

COPYRIGHT_YEAR = datetime.now().year

DEFAULT_PAGINATION = 6
