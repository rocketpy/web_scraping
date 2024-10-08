# shot-scraper - A command-line utility for taking automated screenshots of websites.

# https://github.com/simonw/shot-scraper


# Quick installation
"""
You can install the shot-scraper CLI tool using pip:

pip install shot-scraper

# Now install the browser it needs:
shot-scraper install

# Taking your first screenshot
You can take a screenshot of a web page like this:

shot-scraper https://datasette.io/
This will create a screenshot in a file called datasette-io.png.
"""

# Taking a screenshots:
"""
To take a screenshot of a web page and write it to datasette-io.png run this:

shot-scraper https://datasette.io/
If a file called datasette-io.png already exists the filename datasette-io.1.png will be used instead.

You can use the -o option to specify a filename:

shot-scraper https://datasette.io/ -o datasette.png
Use -o - to write the PNG image to standard output:

shot-scraper https://datasette.io/ -o - > datasette.png
If you omit the protocol http:// will be added automatically, and any redirects will be followed:

shot-scraper datasette.io -o datasette.png

# Adjusting the browser width and height
The browser window used to take the screenshots defaults to 1280px wide and 780px tall.

You can adjust these with the --width and --height options (-w and -h for short):

shot-scraper https://datasette.io/ -o small.png --width 400 --height 800
If you provide both options, the resulting screenshot will be of that size.
If you omit --height a full page length screenshot will be produced (the default).
"""
