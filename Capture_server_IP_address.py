#  Capture server IP address by Requests

import requests

r = requests.get("http://...")
# r.ip

"""
rsp = requests.get('http://...', stream=True)
# grab the IP while you can, before you consume the body !

print(rsp.raw._fp.fp._sock.getpeername())

# consume the body, which calls the read(), after that fileno is no longer available.
print(rsp.content)
"""
