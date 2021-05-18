# biscuits - Fast and tasty cookies handling.

# PyPI: https://pypi.org/project/biscuits/
# Github: https://github.com/pyrates/biscuits

# pip install biscuits

#  API
# Parse a "Cookie:" header value:
from biscuits import parse
parse('some=value; and=more')
# > {'some': 'value', 'and': 'more'}

# Generate a "Set-Cookie:" header value:
from biscuits import Cookie
cookie = Cookie(name='foo', value='bar', domain='www.example.org')
str(cookie)
# > "foo=bar; Domain=www.example.org; Path=/"

