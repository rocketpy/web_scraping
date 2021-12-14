"""
Authentication implementations are subclasses of AuthBase, and are easy to define.
Requests provides two common authentication scheme implementations in requests.auth: HTTPBasicAuth and HTTPDigestAuth.
"""

from requests.auth import AuthBase


class PizzaAuth(AuthBase):
    """Attaches HTTP Pizza Authentication to the given Request object."""
    def __init__(self, username):
        # setup any auth-related data here
        self.username = username

    def __call__(self, r):
        # modify and return the request
        r.headers['X-Pizza'] = self.username
        return r
        
        
# we can make a request using our Pizza Auth:    
requests.get('http://pizzabin.org/admin', auth=PizzaAuth('kenneth'))
# <Response [200]>
