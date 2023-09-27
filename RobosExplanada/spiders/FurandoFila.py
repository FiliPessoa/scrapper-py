

import scrapy

class FurandoFilaSpider(scrapy.Spider):
    name = 'FurandoFilaSpider'

    start_urls = ['https://furandoafila.com.br/pesquisa.php?busca=S&txt_busca=distrito+federal']

    def __init__(self):
        self.output_file = open('furandoFila.txt', 'w')


    def parse(self, response):
        # Find and follow links to event pages
        event_links = response.xpath('//div[@class="prs_upcom_movie_content_box_inner"]/h2/a/@href').getall()
        for event_link in event_links:
            yield response.follow(event_link, self.parse_event)

    def parse_event(self, response):
        title = response.xpath('//meta[@property="og:title"]/@content').get()
        day = response.xpath('//div[@class="prs_es_left_map_section_wrapper dado-event"]/h3/text()').get()
        smalltexts = smalltexts = response.xpath('//div[@class="smalltext"]/ul/li/text()').getall()
        local=smalltexts[0]
        time=smalltexts[2]
        price = response.xpath('//div[@class="st_dtts_sb_ul float_left"]/ul/li/text()[contains(., "R$")][contains(., "Taxa")]').get()
        link = response.url
        description = response.xpath('//div[@class="prs_es_tabs_event_sche_img_cont_wrapper"]/p/text()').getall()



       
        
        self.output_file.write(f'title: {title}\n')
        self.output_file.write(f'day: {day}\n')
        self.output_file.write(f'time: {time}\n')
        self.output_file.write(f'local: {local}\n')
        self.output_file.write(f'price: {price}\n')
        self.output_file.write(f'link: {link}\n')
        self.output_file.write(f'description: {description}\n')
        self.output_file.write(f'/////\n')
        yield {
            'title': title,
        }
        def closed(self, reason):
         self.output_file.close()