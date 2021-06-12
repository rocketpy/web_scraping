# pyppeteer-stealth 

# PyPi: https://pypi.org/project/pyppeteer-stealth/
# Github: https://github.com/MeiK2333/pyppeteer_stealth

# pip install pyppeteer-stealth

# Test for bots : https://bot.sannysoft.com/

# Usage

import asyncio
from pyppeteer import launch
from pyppeteer_stealth import stealth

async def main():
    browser = await launch(headless=True)
    page = await browser.newPage()

    await stealth(page)  # <-- Here

    await page.goto("https://bot.sannysoft.com/")
    await browser.close()
asyncio.get_event_loop().run_until_complete(main())


