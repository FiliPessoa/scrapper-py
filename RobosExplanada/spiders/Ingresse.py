

import scrapy

class IngresseSpider(scrapy.Spider):
    name = 'IngresseSpider'

    # //start_urls = ['https://www.ingresse.com/busca'] https://www.ingresse.com/quadradinho-do-pericles
    start_urls = ['https://www.ingresse.com/quadradinho-do-pericles']
    def __init__(self):
        self.output_file = open('ingresse.txt', 'w')


    def parse(self, response):
    #     # Find and follow links to event pages
    #     event_links = response.xpath('//div[@class="col-xs-12 col-sm-6 col-md-4 col-lg-3 ng-scope"]/div/a/@href').getall()
    #     print (event_links)
    #     for event_link in event_links:
    #         yield response.follow(event_link, self.parse_event)
    
    # def parse_event(self, response):
        hrefs = response.xpath('//div[@class="col-xs-12 col-sm-6 col-md-4 col-lg-3 ng-scope"]/div/a/@href').getall()
        title = response.xpath('title/text()').get()


       
        
        self.output_file.write(f'Title: {title}\n')
        yield {
        }
        def closed(self, reason):
         self.output_file.close()