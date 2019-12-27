import urllib.request 
from html.parser import HTMLParser


req = request.urlopen("http://www.  .com")

# .read()  return HTML data of the webpage
# .getcode()  return the status code 

# HTML parsing
class HtmlParser(parser):
    def error(self, message):
        pass
        
parser = HtmlParser()
f = open("file_name.html")
if f.mode == 'r':  # file opened
    content = f.read()
    parser.feed(content)
    
    
# JSON parsing
import json

json_data = json.loads(response)


# XML parsing 
import xml.dom.minidom

doc = minidom.parse("file_name.xml")
