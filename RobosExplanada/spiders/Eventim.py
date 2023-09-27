

import scrapy

class EventimSpider(scrapy.Spider):
    name = 'EventimSpider'

    # start_urls = ['https://www.eventim.com.br/search/?affiliate=BR1&searchterm=brasilia']https://www.eventim.com.br/artist/rhcp-001/red-hot-chili-peppers-brasilia-3352005/?affiliate=BR1
    start_urls = ['https://www.eventim.com.br/artist/rhcp-001/red-hot-chili-peppers-brasilia-3352005/?affiliate=BR1']

    def __init__(self):
        self.output_file = open('eventim.txt', 'w')


    def parse(self, response):
    #     # Find and follow links to event pages
    #     event_links = response.xpath('//product-group-item[@data-qa="product-group-item-qa-3352005"]/listing-item/article/listing-cta/a/@href').get()
    #     for event_link in event_links:
    #         yield response.follow(event_link, self.parse_event)

    # def parse_event(self, response):
        title = response.xpath('//meta[@property="og:title"]/@content').get()
        local = response.xpath('//li[@data-qa="eventlisting-event-title"]/text()').get()
        day1 = response.xpath('//time[@class="event-listing-date theme-headline-color"]/text()').get()
        day =  day1.strip()
        month1 = response.xpath('//time[@class="event-listing-month"]/text()').get()
        month =  month1.strip()
        time1 = response.xpath('//time[@class="event-listing-time theme-text-color"]/text()').get()
        time2 = time1.strip()
        time = time2.lstrip(time2[:3])
        description = response.xpath('//div[@class="moretext-teaser"]/text()').getall()
       
        
        self.output_file.write(f'title: {title}\n')
        self.output_file.write(f'local: {local}\n')
        self.output_file.write(f'day: {day+ month}\n')
        self.output_file.write(f'time: {time}\n')
        self.output_file.write(f'time: {description}\n')
        yield {
            'title': title,
        }
        def closed(self, reason):
         self.output_file.close()