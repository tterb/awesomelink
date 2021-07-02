
MAX_REDIRECT_COUNT = 4
CLIENT_ERROR_CODE_MIN = 400
SERVER_ERROR_CODE_MAX = 512

# Because assholes will use any opportunity for self-promotion
BLACKLIST_DOMAINS = [
    {
        'name': 'AngelList',
        'pattern': r'(?:https?:)?\/\/angel\.co',
    }, {
        'name': 'Email',
        'pattern': r'(?:mailto:)?(?P<email>[A-z0-9_.+-]+@[A-z0-9_.-]+\.[A-z]+)',
    }, {
        'name': 'Instagram',
        'pattern': r'(?:https?:)?\/\/(?:www\.)?(?:instagram\.com|instagr\.am)',
    }, {
        'name': 'LinkedIn',
        'pattern': r'(?:https?:)?\/\/(?:[\w]+\.)?linkedin\.com',
    }, {
        'name': 'Facebook',
        'pattern': r'(?:https?:)?\/\/(?:www\.)?(?:facebook|fb)\.com',
    }, {
        'name': 'Medium',
        'pattern': r'(?:https?:)?\/\/medium\.com',
    }, {
        'name': 'Reddit',
        'pattern': r'(?:https?:)?\/\/(?:[a-z]+\.)?reddit\.com',
    }, {
        'name': 'SnapChat',
        'pattern': r'(?:https?:)?\/\/(?:www\.)?snapchat\.com',
    }, {
        'name': 'StackExchange',
        'pattern': r'(?:https?:)?\/\/(?:www\.)?stackexchange\.com',
    }, {
        'name': 'Telegram',
        'pattern': r'(?:https?:)?\/\/(?:t(?:elegram)?\.me|telegram\.org)',
    }, {
        'name': 'Twitter',
        'pattern': r'(?:https?:)?\/\/(?:[A-z]+\.)?twitter\.com',
    }, {
        'name': 'Vimeo',
        'pattern': r'(?:https?:)?\/\/(?:[A-z]+\.)?vimeo\.com',
    }, {
        'name': 'YouTube',
        'pattern': r'(?:https?:)?\/\/(?:[A-z]+\.)?(?:youtube\.com|youtu\.be)',
    },
]
