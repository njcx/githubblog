# -*- coding: utf-8 -*-

from __future__ import unicode_literals

AUTHOR = 'nJcx'
SITENAME = 'nJcx\'s Blog'
SITEURL = 'https://www.njcx.bid'  # Intentionally left blank, see ./publishconf.py

PATH = 'content'

TIMEZONE = 'Africa/Nairobi'
DEFAULT_LANG = 'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
ARTICLE_LANG_URL = 'posts/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = ARTICLE_LANG_URL

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['extras', 'images']
EXTRA_PATH_METADATA = {
    'extras/android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},
    'extras/android-chrome-512x512.png': {'path': 'android-chrome-512x512.png'},
    'extras/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'extras/browserconfig.xml': {'path': 'browserconfig.xml'},
    'extras/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extras/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'extras/favicon.ico': {'path': 'favicon.ico'},
    'extras/manifest.json': {'path': 'manifest.json'},
    'extras/mstile-150x150.png': {'path': 'mstile-150x150.png'},
    'extras/safari-pinned-tab.svg': {'path': 'safari-pinned-tab.svg'},
}

PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican-bootstrapify']

BOOTSTRAPIFY = {
    'table': ['table', 'table-striped', 'table-hover'],
    'img': ['img-fluid'],
    'blockquote': ['blockquote'],
}

# Theme settings --------------------------------------------------------------

THEME = '/Users/njcx/githubblog/alchemy'

SITESUBTITLE = ''
SITEIMAGE = '/images/profile.png width=200 height=200'
DESCRIPTION = 'Linux重度用户，Python从业人员，个人小博客，欢迎访问'

LINKS = (
    ('知乎', 'https://www.zhihu.com/people/njcxs'),
    ('FaceBook', 'https://www.facebook.com/nJcx1'),
    ('Github', 'https://github.com/njcx'),
)

ICONS = [
    ('github', 'https://github.com/njcx'),
]

PYGMENTS_STYLE = 'emacs'
RFG_FAVICONS = True

# Default value is ['index', 'tags', 'categories', 'authors', 'archives']
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'sitemap']
SITEMAP_SAVE_AS = 'sitemap.xml'
