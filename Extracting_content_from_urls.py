# micawber - a small library for extracting rich content from urls

# https://pypi.org/project/micawber/
# https://github.com/coleifer/micawber/

# pip install micawber


# what does it do?
"""
micawber supplies a few methods for retrieving rich metadata about a variety of links,
such as links to youtube videos. micawber also provides functions for parsing blocks of text and
html and replacing links to videos with rich embedded content.
"""


# quick example
import micawber

# load up rules for some default providers, such as youtube and flickr
providers = micawber.bootstrap_basic()

providers.request('http://www.youtube.com/watch?v=54XHDUOHuzU')

# returns the following dictionary:
{
    'author_name': 'pascalbrax',
    'author_url': u'http://www.youtube.com/user/pascalbrax'
    'height': 344,
    'html': u'<iframe width="459" height="344" src="http://www.youtube.com/embed/54XHDUOHuzU?fs=1&feature=oembed" frameborder="0" allowfullscreen></iframe>',
    'provider_name': 'YouTube',
    'provider_url': 'http://www.youtube.com/',
    'title': 'Future Crew - Second Reality demo - HD',
    'type': u'video',
    'thumbnail_height': 360,
    'thumbnail_url': u'http://i2.ytimg.com/vi/54XHDUOHuzU/hqdefault.jpg',
    'thumbnail_width': 480,
    'url': 'http://www.youtube.com/watch?v=54XHDUOHuzU',
    'width': 459,
    'version': '1.0',
}

providers.parse_text('this is a test:\nhttp://www.youtube.com/watch?v=54XHDUOHuzU')

# returns the following string:
this is a test:
<iframe width="459" height="344" src="http://www.youtube.com/embed/54XHDUOHuzU?fs=1&feature=oembed" frameborder="0" allowfullscreen></iframe>

providers.parse_html('<p>http://www.youtube.com/watch?v=54XHDUOHuzU</p>')

# returns the following html:
<p><iframe width="459" height="344" src="http://www.youtube.com/embed/54XHDUOHuzU?fs=1&amp;feature=oembed"\
frameborder="0" allowfullscreen="allowfullscreen"></iframe></p>


# Example
import pprint
from micawber import bootstrap_oembed, ProviderException


try:
    read_input = raw_input
except NameError:
    read_input = input

def main():
    print('Please wait, loading providers from oembed.com')
    providers = bootstrap_oembed()

    while 1:
        url = read_input('Enter a url (or q to quit): ')
        if url.lower().strip() == 'q':
            break

        try:
            result = providers.request(url)
        except ProviderException:
            print('No provider found for that url :/')
        else:
            print('Data for %s\n====================================================' % url)
            pprint.pprint(result)

if __name__ == '__main__':
    print('Welcome to the example!')
    main()
