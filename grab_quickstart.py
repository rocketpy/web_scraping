#  grab is a python framework for building web scrapers
#  official docs:  https://grablab.org/docs/
#  installing:  pip install -U Grab  , also need install the lxml and pycurl libraries !!!

from grab import Grab


gr = Grab()
resp = gr.go('http://...com/')
