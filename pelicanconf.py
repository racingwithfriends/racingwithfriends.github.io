AUTHOR = 'Racing with Friends'
SITENAME = 'Racing with Friends'
SITEURL = "https://racingwithfriends.com"

PATH = "content"

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

THEME = 'simple-bootstrap'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
)

# Social widget
SOCIAL = (
)

DEFAULT_PAGINATION = False

STATIC_PATHS = [
    'images',
    'static'
]
EXTRA_PATH_METADATA = {
    'static/CNAME': {'path': 'CNAME'},
}
TEMPLATE_PAGES = {
    # Custom 404 page for GitHub pages.
    '404.html': '404.html',
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True