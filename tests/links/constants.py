from requests.structures import CaseInsensitiveDict


VALID_URLS = [
    'https://joyoftesting.com/hidden-stream',
    'https://joyoftesting.com/the-lonely-mountain',
    'https://joyoftesting.com/winters-breeze',
    'https://joyoftesting.com/fluffy-clouds',
    'https://joyoftesting.com/alaskan-waterfall',
    'https://joyoftesting.com/the-old-mill',
]

BLACKLISTED_URLS = [
    'https://angel.co/company/twitter',
    'jeff@amazon.com',
    'mailto:jeff@amazon.com',
    'http://fb.com/peter_parker-miller',
    'https://facebook.com/peter.parker',
    'https://instagram.com/disco.dude',
    'https://www.instagr.am/__disco__dude',
    'https://linkedin.com/company/dash-company.io',
    'https://linkedin.com/in/karllorey',
    'https://medium.com/does-exist/some-post-123abc',
    'https://reddit.com/u/ar-guetita',
    'https://www.snapchat.com/add/peterparker',
    'https://stackexchange.com/users/12345/lorey',
    'https://t.me/peterparker',
    'https://twitter.com/karllorey/status/1259924082067374088',
    'http://twitter.com/@karllorey',
    'https://vimeo.com/user46726126',
    'https://player.vimeo.com/video/148751763',
    'https://www.youtube.com/channel/UC3y00Z1zFPc-8Z9xg8ydC-A',
    'https://www.youtube.com/user/JPPGmbH',
    'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
    'https://youtu.be/dQw4w9WgXcQ',
    'https://youtube.com/embed/dQw4w9WgXcQ',
]

FRAMEABLE_HEADERS = CaseInsensitiveDict({
    'Date': 'Mon, 28 Jun 2021 00:45:39 GMT',
    'Server': 'Apache',
    'Accept-Ranges': 'bytes',
    'Vary': 'Accept-Encoding',
    'Content-Encoding': 'gzip',
    'Cache-Control': 'max-age=3600, must-revalidate',
    'Content-Length': '7442',
    'Keep-Alive': 'timeout=3, max=499',
    'Connection': 'Keep-Alive',
    'Content-Type': 'text/html'
})

NON_FRAMEABLE_HEADERS = CaseInsensitiveDict({
    'Date': 'Mon, 28 Jun 2021 00:45:39 GMT',
    'Server': 'Apache',
    'X-Frame-Options': 'SAMEORIGIN',
    'X-Content-Type-Options': 'nosniff',
    'Accept-Ranges': 'bytes',
    'Vary': 'Accept-Encoding',
    'Content-Encoding': 'gzip',
    'Cache-Control': 'max-age=3600, must-revalidate',
    'Content-Length': '7442',
    'Keep-Alive': 'timeout=3, max=499',
    'Connection': 'Keep-Alive',
    'Content-Type': 'text/html'
})
