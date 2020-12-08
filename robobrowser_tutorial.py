"""
RoboBrowser combines the best of two excellent Python libraries:
Requests and BeautifulSoup. RoboBrowser represents browser sessions using Requests and HTML responses using BeautifulSoup,
transparently exposing methods of both libraries
"""

# Official website: http://robobrowser.readthedocs.org/
# PyPi: https://pypi.org/project/robobrowser/

# IMPORTANT need to check version Python !!! may be max version is Python 3.4 
#  Python >= 2.6 or >= 3.3

# Installation
# mkvirtualenv robobrowser
# pip install robobrowser

import re
from robobrowser import RoboBrowser


browser = RoboBrowser(history=True)
browser.open('http://rapgenius.com/')

# search 
form = browser.get_form(action='/search')
# form                # <RoboForm q=>
form['q'].value = 'queen'
browser.submit_form(form)

# look up the first song
songs = browser.select('.song_name')
browser.follow_link(songs[0])
lyrics = browser.select('.lyrics')
lyrics[0].text  

# back to results page
browser.back()

# look up my favorite song
browser.follow_link('death on two legs')

# can also search HTML using regex patterns
lyrics = browser.find(class_=re.compile(r'\blyrics\b'))
# lyrics.text  

#  or
import re
from robobrowser import RoboBrowser


browser = RoboBrowser(user_agent='a python robot')
browser.open('https://github.com/')

# inspect the browser session
browser.session.cookies['_gh_sess']       
browser.session.headers['User-Agent']      

# search the parsed HTML
browser.select('div.teaser-icon')  
browser.find(class_=re.compile(r'column', re.I)) 

#  tools for working with forms
from robobrowser import RoboBrowser


browser = RoboBrowser()
browser.open('http://twitter.com')

# get the signup form
signup_form = browser.get_form(class_='signup')
signup_form         # <RoboForm user[name]=, user[email]=, ...

# inspect its values
signup_form['authenticity_token'].value     # 6d03597 ...

# fill it out
signup_form['user[name]'].value = 'python-robot'
signup_form['user[user_password]'].value = 'secret'

# serialize it to JSON
signup_form.serialize()         # {'data': {'authenticity_token': '6d03597...',
                                #  'context': '',
                                #  'user[email]': '',
                                #  'user[name]': 'python-robot',
                                #  'user[user_password]': ''}}

# and submit
browser.submit_form(signup_form)
