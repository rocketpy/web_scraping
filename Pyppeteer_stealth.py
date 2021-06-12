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

"""
# Args:

stealth(
  page: Page,
  run_on_insecure_origins: bool = False,
  languages: [str] = ["en-US", "en"],
  vendor: str = "Google Inc."
  user_agent: str = None,
  locale: str = "en-US,en",
  mask_linux: bool = True,
  webgl_vendor: str = "Intel Inc.",
  renderer: str = "Intel Iris OpenGL Engine",
  disabled_evasions: list = [],
)

"""

"""
# List of valid evasion names to pass into disabled_evasions:

['chrome_app',
 'chrome_runtime',
 'iframe_content_window',
 'media_codecs',
 'sourceurl',
 'navigator_hardware_concurrency',
 'navigator_languages',
 'navigator_permissions',
 'navigator_plugins',
 'navigator_vendor',
 'navigator_webdriver',
 'user_agent_override',
 'webgl_vendor',
 'window_outerdimensions']
"""

