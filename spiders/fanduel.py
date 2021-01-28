import scrapy
from scrapy_splash import SplashRequest


class FanduelSpider(scrapy.Spider):
    name = 'fanduel'
    allowed_domains = ['sportsbook.fanduel.com']

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    
    script = '''
        function main(splash, args)
            splash.private_mode_enabled = false
            splash:set_user_agent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
            assert(splash:go(args.url))
            assert(splash:wait(.5))
            return splash:html()
        end

    '''


    def set_user_agent(self, request):
        request.headers['User-Agent'] = self.user_agent
        return request
    
    def start_requests(self):
        yield SplashRequest(url="http://sportsbook.fanduel.com/sports/navigation/1550.1/10329.3", callback=self.parse, endpoint="execute",args={
            'lua_source': self.script
            })
    
    def parse(self, response):
        for match in response.xpath("//div[@class='layout coupon-event big3-event ICE HOCKEY']"):
            yield{
                'sitename': 'fanduel',
                't1': match.xpath(".//div[contains(@class,'eventTitle')][1]/span[@class='name']/text()").get(),
                't2': match.xpath(".//div[contains(@class,'eventTitle')][2]/span[@class='name']/text()").get(),
                'spread1': '',# match.xpath(".//div[@class='layout coupon-event big3-event ICE HOCKEY']//div[@class='market points']//div[@class='flex'][1]//div[contains(@class, 'currenthandicap') or contains(@class, 'selectionprice')]/text()").get(),
                'spread2': '',# match.xpath(".//span[contains(@id,'HomeSpread')]/text()").get(),
                # these are currently incorrect
                'line1': match.xpath(".//div[@class='market money']//div[@class='flex'][1]//div[@class='selectionprice']/text()").get(),
                'line2': match.xpath(".//div[@class='market money']//div[@class='flex'][2]//div[@class='selectionprice']/text()").get()

            }

        
