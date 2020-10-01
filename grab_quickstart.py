#  grab is a python framework for building web scrapers
#  official docs:  https://grablab.org/docs/
#  installing:  pip install -U Grab  , also need install the lxml and pycurl libraries !!!

from grab import Grab


gr = Grab()
resp = gr.go('http://...com/')

#  make a HEAD request
g = Grab()
g.setup(method='head')
resp = g.go('http://google.com/robots.txt')
print(len(resp.body))
print(resp.headers['Content-Length'])


#  set some methods
"""
g.setup(method='put')
g.setup(method='delete')
g.setup(method='options')
g.setup(method='head')
"""

