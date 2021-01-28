# -*- coding: utf-8 -*-
import scrapy


class BetusSpider(scrapy.Spider):
    name = 'betus'
    allowed_domains = ['www.betus.com.pa']

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url='https://www.betus.com.pa/sportsbook/nhl-ice_hockey-odds.aspx', headers={
            'User-Agent': self.user_agent
        })

    def set_user_agent(self, request):
        request.headers['User-Agent'] = self.user_agent
        return request

    # @classmethod
    # def from_crawler(cls, crawler, *args, **kwargs):
    #     spider = super(BetusSpider, cls).from_crawler(crawler, *args, **kwargs)
    #     crawler.signals.connect(spider.spider_idle, signals.spider_idle)
    #     return spider

    def parse(self, response):
        for match in response.xpath("//div[@class = 'game-tbl row']"):
            yield{
                'sitename': 'betus',
                't1': match.xpath(".//span[@id = 'homeName']/a/text()").get(),
                't2': match.xpath(".//span[@id = 'awayName']/a/text()").get(),
                'spread1': match.xpath(".//span[contains(@id,'VisitorSpread')]/text()").get(),
                'spread2': match.xpath(".//span[contains(@id,'HomeSpread')]/text()").get(),
                'line1': match.xpath(".//span[contains(@id, 'HomeMoneyLine')]/text()").get(),
                'line2': match.xpath(".//span[contains(@id, 'VisitorMoneyLine')]/text()").get()

            }

    # def spider_idle(self, spider):
    #     logging.info('waiting 30 to restart crawl')
    #     time.sleep(30)
    #     logging.info('restarting crawl')
    #     self.crawler.engine.schedule(Request(self.))
