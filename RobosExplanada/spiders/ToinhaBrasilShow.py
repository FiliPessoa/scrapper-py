

import scrapy

class ToinhaBrasilShowSpider(scrapy.Spider):
    name = 'ToinhaBrasilShowSpider'

    # start_urls = ['https://www.toinhabrasilshow.com/eventos']https://www.toinhabrasilshow.com/evento/war-29-09-2023
    start_urls = ['https://www.toinhabrasilshow.com/evento/war-29-09-2023']

    def __init__(self):
        self.output_file = open('toinhaBrasilShow.txt', 'w')


    def parse(self, response):
    #     # Find and follow links to event pages
    #     event_links = response.xpath('//div[@class="col-6 col-xl-4"><div class="product-wrap mb-25').getall()
    #     for event_link in event_links:
    #         yield response.follow(event_link, self.parse_event)

    # def parse_event(self, response):
      
        title = response.xpath('//div[@class="fixed-div-price  "]/h2/text()').getall()




       
        
        
        self.output_file.write(f'title: {title}\n')
        self.output_file.write(f'/////\n')
        yield {
            'title': title,
        }
        def closed(self, reason):
         self.output_file.close()