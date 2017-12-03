import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site): # Takes a website to scrape as a parameter.
        self.site = site

    def scrape(self): # Used to scrape data from the passed in site in init.
        r = urllib.request.urlopen(self.site) # Makes a request to a website and returns a Response object with stored
                                              # HTML.
        html = r.read() # When read() is executed on r, all of the data is stored in html variable.
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)

        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                print("\n"+url)

news = "https://news.google.com/"

Scraper(news).scrape()
