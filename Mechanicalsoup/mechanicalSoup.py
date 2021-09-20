# MechanicalSoup - A Python library for automating interaction with websites

# PyPi: https://pypi.org/project/MechanicalSoup/ 
# Github: https://github.com/MechanicalSoup/MechanicalSoup
# Docs: https://mechanicalsoup.readthedocs.io/en/stable/
# Examples: https://github.com/MechanicalSoup/MechanicalSoup/tree/master/examples

# pip install MechanicalSoup

"""Example usage of MechanicalSoup to get the results from the Qwant
search engine.
"""

import re
import mechanicalsoup
import html
import urllib.parse


# Connect to duckduckgo
browser = mechanicalsoup.StatefulBrowser(user_agent='MechanicalSoup')
browser.open("https://lite.qwant.com/")

# Fill-in the search form
browser.select_form('#search-form')
browser["q"] = "MechanicalSoup"
browser.submit_selected()

# Display the results
for link in browser.page.select('.result a'):
    # Qwant shows redirection links, not the actual URL, so extract
    # the actual URL from the redirect link:
    href = link.attrs['href']
    m = re.match(r"^/redirect/[^/]*/(.*)$", href)
    if m:
        href = urllib.parse.unquote(m.group(1))
    print(link.text, '->', href)

