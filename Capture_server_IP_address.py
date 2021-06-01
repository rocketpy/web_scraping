#  Capture server IP address by Requests

import requests

r = requests.get("http://...")
# r.ip

# For Python 3, need change  ip = r.raw._fp.fp.raw._sock.getpeername()
"""
rsp = requests.get('http://...', stream=True)
# grab the IP while you can, before you consume the body !

print(rsp.raw._fp.fp._sock.getpeername())

# consume the body, which calls the read(), after that fileno is no longer available.
print(rsp.content)
"""

# or 
"""
with requests.get("https://httpbin.org", stream=True) as response:
    ip21 = response.raw.connection.sock.getsockname()
    print(ip21)
    # ('192.168.100.104', 58254)
    
    ip22 = response.raw.connection.sock.getpeername()
    print(ip22)
    # ('52.3.177.149', 443)
"""

#
