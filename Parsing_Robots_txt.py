import urllib.robotparser as urobot
import urllib.request
from bs4 import BeautifulSoup


url = "https://..."

rp = urobot.RobotFileParser()

rp.set_url(url + "/robots.txt")
rp.read()

if rp.can_fetch("*", url):
    site = urllib.request.urlopen(url)
    sauce = site.read()
    soup = BeautifulSoup(sauce, "html.parser")
    actual_url = site.geturl()[:site.geturl().rfind('/')]

    my_list = soup.find_all("a", href=True)
    for i in my_list:
        # rather than != "#" you can control your list before loop over it
        if i != "#":
            newurl = str(actual_url)+"/"+str(i)
            try:
                if rp.can_fetch("*", newurl):
                    site = urllib.request.urlopen(newurl)
                    # do what you want on each authorized webpage
            except:
                pass
else:
    print("cannot scrap")

