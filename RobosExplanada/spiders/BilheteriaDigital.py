

import scrapy

class BilheteriaDigitalSpider(scrapy.Spider):
    name = 'BilheteriaDigitalSpider'

    start_urls = ['https://www.bilheteriadigital.com/DF']

    def __init__(self):
        self.output_file = open('bilheteriaDigital.txt', 'w')


    def parse(self, response):
        # Find and follow links to event pages
        event_links = response.xpath('//li[@class="box-li-evento"]/a/@href').getall()
        for event_link in event_links:
            yield response.follow(event_link, self.parse_event)

    def parse_event(self, response):
      
        title = response.xpath('normalize-space(substring-after(//title/text(), "| Ingressos "))').get()
        local = response.xpath('//span[@class="span-local-evento"]/text()').get()
        day = response.xpath('//div[@class="data-evento-ingressos"]/b/text()').getall()
        month = response.xpath('//div[@class="calendario-evento col-md-2 col-sm-2 col-xs-2 col-lg-2"]/div[2]/text()').get()
        time = response.xpath('//div[@class="col-xs-10  col-lg-10 col-md-10 col-sm-10"]/text()').get()
        link = response.url
        descriptiontext = response.xpath('//div[@class="panel-body  informacoes-adicionais-evento"]/descendant-or-self::text()').getall()
        description = ' '.join(descriptiontext).strip()


       
        
        self.output_file.write(f'title: {title}\n')
        self.output_file.write(f'local: {local}\n')
        self.output_file.write(f'day: {day,month}\n')
        self.output_file.write(f'time: {time}\n')
        self.output_file.write(f'link: {link}\n')
        self.output_file.write(f'description: {description}\n')
        self.output_file.write(f'/////\n')
        yield {
            'title': title,
            'time': time,
            'day': month,
            'day': link,
            
        }
        def closed(self, reason):
         self.output_file.close()