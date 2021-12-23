# https://github.com/YoongiKim/AutoCrawler

# How to use
"""
-    Install Chrome

-    pip install -r requirements.txt

-    Write search keywords in keywords.txt

-    Run "main.py"

-    Files will be downloaded to 'download' directory.
"""

#  Arguments

# usage:
"""
python3 main.py [--skip true] [--threads 4] [--google true] [--naver true] [--full false] [--face false] [--no_gui auto] [--limit 0]

--skip true        Skips keyword if downloaded directory already exists. This is needed when re-downloading.

--threads 4        Number of threads to download.

--google true      Download from google.com (boolean)

--naver true       Download from naver.com (boolean)

--full false       Download full resolution image instead of thumbnails (slow)

--face false       Face search mode

--no_gui auto      No GUI mode. (headless mode) Acceleration for full_resolution mode, but unstable on thumbnail mode.
                   Default: "auto" - false if full=false, true if full=true
                   (can be used for docker linux system)
                   
--limit 0          Maximum count of images to download per site. (0: infinite)
--proxy-list ''    The comma separated proxy list like: "socks://127.0.0.1:1080,http://127.0.0.1:1081".
                   Every thread will randomly choose one from the list.
"""

