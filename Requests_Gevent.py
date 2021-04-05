#  GRequests allows you to use Requests with Gevent to make asynchronous HTTP Requests easily.

# PyPi:  https://pypi.org/project/grequests/
# Github:  https://github.com/spyoungtech/grequests

# pip install grequests

# Example
import grequests

urls = ['http://www.heroku.com',
        'http://tablib.org',
        'http://httpbin.org',
        'http://python-requests.org',
        'http://kennethreitz.com'
       ]

# Create a set of unsent Requests:
rs = (grequests.get(u) for u in urls)

# Send them all at the same time:
grequests.map(rs)
# [<Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>]


