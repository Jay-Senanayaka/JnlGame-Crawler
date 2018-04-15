#Author: Sanjeewa B. Senanayaka
#JnlGame Crawler: Scrapes title, console, price of games

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.shell import inspect_response
from scrapy.linkextractors import LinkExtractor
from lxml import html

class QuotesSpider(CrawlSpider):
    name = "jnl"
    allowed_domains = ["jnlgame.com"]
    start_urls = [
        'https://www.jnlgame.com/collections/playstation-4-%E3%83%97%E3%83%AC%E3%82%A4%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B34?constraint=video-games',
        'https://www.jnlgame.com/collections/PlayStation-3-%E3%83%97%E3%83%AC%E3%82%A4%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B33',
        'https://www.jnlgame.com/collections/playstation-2-%E3%83%97%E3%83%AC%E3%82%A4%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B32?constraint=games-%E3%82%B2%E3%83%BC%E3%83%A0',
        'https://www.jnlgame.com/collections/playstation-vita-%E3%83%97%E3%83%AC%E3%82%A4%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3-%E3%83%B4%E3%82%A3%E3%83%BC%E3%82%BF',
        'https://www.jnlgame.com/collections/xbox-one-%E3%82%A8%E3%83%83%E3%82%AF%E3%82%B9%E3%83%9C%E3%83%83%E3%82%AF%E3%82%B9-%E3%83%AF%E3%83%B3?constraint=games-%E3%82%B2%E3%83%BC%E3%83%A0',
        'https://www.jnlgame.com/collections/xbox-360-%E3%82%A8%E3%83%83%E3%82%AF%E3%82%B9%E3%83%9C%E3%83%83%E3%82%AF%E3%82%B9-360?constraint=games-%E3%82%B2%E3%83%BC%E3%83%A0',
        'https://www.jnlgame.com/collections/nintendo-switch-%E3%83%8B%E3%83%B3%E3%83%86%E3%83%B3%E3%83%89%E3%83%BC%E3%82%B9%E3%82%A4%E3%83%83%E3%83%81?constraint=video-games',
        'https://www.jnlgame.com/collections/nintendo-3ds-%E3%83%8B%E3%83%B3%E3%83%86%E3%83%B3%E3%83%89%E3%83%BC3ds',
        'https://www.jnlgame.com/collections/nintendo-wii-u-wii-u-%E4%BB%BB%E5%A4%A9%E5%A0%82?constraint=games-%E3%82%B2%E3%83%BC%E3%83%A0',
    ]

    rules = (Rule(LinkExtractor(allow=(), restrict_xpaths=("//a[@title='Next']", )), callback="parse_page", follow=True),)

    def parse_page(self, response):
        container = response.xpath("//div[@class='block-row col-xs-12 col-sm-9 col-main']")

        for item1 in container.xpath(".//div[@class='  no_crop_image  grid-item product-item  col-xs-6 col-sm-6 col-md-4 col-lg-4 wow fadeIn']"):
            yield {
                'title': item1.xpath(".//a[@class = 'product-title']/span[@class='lang1']/text()").extract_first(),
                'console':response.xpath("//h2/span[@class='lang1']/text()").extract_first(),
                'price': item1.xpath(".//span[@class = 'money']/text()").extract_first(),
            }

