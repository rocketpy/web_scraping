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

# Optionally, in the event of a timeout or any other exception during the connection of the request, you can add an exception handler !
def exception_handler(request, exception):
    print("Request failed")

reqs = [grequests.get('http://httpbin.org/delay/1', timeout=0.001),
        grequests.get('http://fakedomain/'),
        grequests.get('http://httpbin.org/status/500')
       ]
grequests.map(reqs, exception_handler=exception_handler)
# Request failed
# Request failed
# [None, None, <Response [500]>]

