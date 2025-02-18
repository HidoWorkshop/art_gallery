AUTHOR = 'hidolio'
SITENAME = 'Hido Gallery'
SITEURL = ""
# https://hidoworkshop.github.io/art_gallery/
RELATIVE_URLS = True

PATH = "content"

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("pixiv", "https://www.pixiv.net/users/15766039"),
)

# Social widget
SOCIAL = (
    ("x", "https://x.com/HidoLido"),
)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing


THEME = 'themes/Flex'  # 需要先下载主题到 themes 目录

# 指定包含静态文件的目录
STATIC_PATHS = ['images', 'videos', 'extra']

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/robots.txt': {'path': 'robots.txt'},
}





