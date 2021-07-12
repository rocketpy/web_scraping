#  Pyppeteer - Headless chrome/chromium automation library (unofficial port of puppeteer)

# PyPi:  https://pypi.org/project/pyppeteer2/

# pip install pyppeteer2

# Documentation: https://miyakogi.github.io/pyppeteer

# Usage
# Note: When you run pyppeteer first time, it downloads a recent version of Chromium (~100MB). 
# If you don't prefer this behavior, run pyppeteer-install command before running scripts which uses pyppeteer.


# Example: open web page and take a screenshot.

import asyncio
from pyppeteer import launch


async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://example.com')
    await page.screenshot({'path': 'example.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())


# Example: evaluate script on the page.
import asyncio
from pyppeteer import launch


async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://example.com')
    await page.screenshot({'path': 'example.png'})

    dimensions = await page.evaluate('''() => {
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio,
        }
    }''')

    print(dimensions)
    # >>> {'width': 800, 'height': 600, 'deviceScaleFactor': 1}
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())




