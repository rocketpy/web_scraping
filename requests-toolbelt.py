#  requests-toolbelt - A utility belt for advanced users of python-requests.


# https://pypi.org/project/requests-toolbelt/
# https://toolbelt.readthedocs.io/en/latest/

# pip install requests-toolbelt

# import requests_toolbelt


# multipart/form-data Encoder:
# The main attraction is a streaming multipart form-data object, MultipartEncoder. Its API looks like this:

from requests_toolbelt import MultipartEncoder
import requests

m = MultipartEncoder(
    fields={'field0': 'value', 'field1': 'value',
            'field2': ('filename', open('file.py', 'rb'), 'text/plain')}
    )

r = requests.post('http://httpbin.org/post', data=m,
                  headers={'Content-Type': m.content_type})


# or
from requests_toolbelt import MultipartEncoder
import requests

m = MultipartEncoder(fields={'field0': 'value', 'field1': 'value'})

r = requests.post('http://httpbin.org/post', data=m,
                  headers={'Content-Type': m.content_type})


# User-Agent constructor
from requests_toolbelt import user_agent
from requests import Session

requests_toolbelt.user_agent('mypackage', '0.0.1')

headers = {
    'User-Agent': user_agent('my_package', '0.0.1')
    }
r = requests.get('https://api.github.com/users', headers=headers)
# or
s = Session()
s.headers = {
    'User-Agent': user_agent('my_package', '0.0.1')
    }
r = s.get('https://api.github.com/users')


# Adding Extra Information to Your User-Agent String
import requests
import requests_toolbelt
from requests_toolbelt.utils import user_agent as ua

user_agent = ua.user_agent('mypackage', '0.0.1',
                           extras=[('requests', requests.__version__),
                                   ('requests-toolbelt', requests_toolbelt.__version__)])

s = requests.Session()
s.headers['User-Agent'] = user_agent


# SSLAdapter
from requests_toolbelt import SSLAdapter
import requests
import ssl

s = requests.Session()
s.mount('https://', SSLAdapter(ssl.PROTOCOL_TLSv1))


# cookies/ForgetfulCookieJar
from requests_toolbelt.cookies.forgetful import ForgetfulCookieJar

session = requests.Session()
session.cookies = ForgetfulCookieJar()

