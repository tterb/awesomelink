MAX_REDIRECT_COUNT = 4
CLIENT_ERROR_CODE_MIN = 400
SERVER_ERROR_CODE_MAX = 512

VISITED_LINKS_COOKIE = 'awsmlnk_viewed'

AWESOMELINK_DNE_ERROR = 'AwesomeLink does not exist'
AWESOMELINK_UNAPPROVED_ERROR = 'AwesomeLink is awaiting approval'
AWESOMELINK_UNIQUE_ERROR = 'AwesomeLink with the provided URL already exists'
BLACKLIST_URL_ERROR = '%(domain)s links are not very awesome'
INVALID_RATING_ERROR = 'Invalid \'rating\' parameter value'
MAX_REDIRECT_ERROR = 'The provided URL exceeded the maximum number of redirects'
URL_INVALID_ERROR = '\'%(url)s\' is not a valid URL'
URL_STATUS_ERROR = 'The provided URL returned an error'
INVALID_PARAM_ERROR = 'Invalid \'{param}\' parameter: \'{value}\''

AWESOMLINK_ORDER_BY = {'rating', 'clicks', 'created', 'updated'}

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
