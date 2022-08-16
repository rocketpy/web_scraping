#  requests-toolbelt - A utility belt for advanced users of python-requests.


# https://pypi.org/project/requests-toolbelt/
# https://toolbelt.readthedocs.io/en/latest/

# pip install requests-toolbelt


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

