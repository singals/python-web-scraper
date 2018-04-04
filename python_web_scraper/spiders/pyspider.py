import scrapy

from python_web_scraper.spiders.robots_reader import get_allowed_urls_to_scrape


class PySpider(scrapy.Spider):

    name = 'py'

    start_urls = get_allowed_urls_to_scrape()

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'python_crawler-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)