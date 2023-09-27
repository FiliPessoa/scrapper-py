

import scrapy

class IngressoDigitalSpider(scrapy.Spider):
    name = 'IngressoDigitalSpider'

    start_urls = ['https://www.ingressodigital.com/list.php?busca=S&txt_busca=bras%C3%ADlia&txt_busca_m=']
    # start_urls = ['https://www.ingressodigital.com/evento/9435/Murilo_Couto__Ideias_Soltas']


    def __init__(self):
        self.output_file = open('ingressoDigital.txt', 'w')


    def parse(self, response):
        # Find and follow links to event pages
        hrefs = response.xpath('//div[@class="item-content"]/h2/a/@href').getall()

        for href in hrefs:
            # Construct the full URL by adding the prefix
            full_url = "https://www.ingressodigital.com/" + href.lstrip('./')

            yield response.follow(full_url, self.parse_event)

    def parse_event(self, response):
        title = response.xpath('//div[@class="eventWhere radiusid"]/h2/text()').get()
        local2 = response.xpath('//ul[@class="eventDetails"]/li[i[@class="fa fa-map-marker"]]/p/text()').get()
        local = local2.strip()
        daytocut = response.xpath('//div[contains(@onclick, "show_hora")]/@onclick').get()
        day = daytocut.lstrip('show_hora')
        time = response.xpath('//label[@class="form-check-label"]/text()').get()
        price = response.xpath('//ul[@class="eventDetails"]/li[i[@class="fa fa-ticket"]]/p/text()').get()
        link = response.url
        description = response.xpath('//div[@class="placeAbout"]/p/text()').getall()
        
        
        self.output_file.write(f'title: {title}\n')
        self.output_file.write(f'local: {local}\n')
        self.output_file.write(f'day: {day}\n')
        self.output_file.write(f'time: {time}\n')
        self.output_file.write(f'price: {price}\n')
        self.output_file.write(f'link: {link}\n')
        self.output_file.write(f'description: {description}\n')
        self.output_file.write(f'/////\n')
        yield {
            'title': title,
        }
        def closed(self, reason):
         self.output_file.close()