#  urllib3 is a powerful, user-friendly HTTP client

#  Docs:  https://urllib3.readthedocs.io/en/latest/user-guide.html
#  pip install urllib3

import urllib3

http = urllib3.PoolManager()
r = http.request('GET', 'http://')
r.status
# 200
r.data


