
import datetime
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

import scrapy

class ShotgunSpider(scrapy.Spider):
    name = 'ShotgunSpider'

    # start_urls = ['https://shotgun.live/brasilia']
    start_urls = ['https://shotgun.live/pt-br/events/haus-it-4-anos-29-09']

    def __init__(self):
        self.output_file = open('shotgun.txt', 'w')


    def parse(self, response):
    #     # Find and follow links to event pages
    #     event_links = response.css('div.css-1dbjc4n.r-1habvwh.r-13qz1uu a::attr(href)').getall()
    #     for event_link in event_links:
    #         yield response.follow(event_link, self.parse_event)

    # def parse_event(self, response):
        title = response.xpath('//div/h1[contains(@class, "css-4rbku5")]/text()').get()
        local = response.css('div.css-901oao.r-jwli3a.r-c321bz.r-7cikom.r-13uqrnb.r-majxgm.r-rjixqe.r-13wfysu span::text').get()
        day = response.css('div.css-901oao.r-d8nonl.r-c321bz.r-ubezar.r-13uqrnb.r-majxgm.r-rjixqe::text').get()
        time = response.xpath('//div[@class="css-901oao r-4tuo4v r-c321bz r-1b43r93 r-13uqrnb r-b88u0q r-1ikidpy r-rjixqe r-q4m81j r-tsynxw"]/text()').getall()
        

        price2 = time[3]
        price3 =  price2.split()
        price4 = price3[1]
        price5 = price4.split(",")
        price = int(price5[0])

        time = response.xpath('//span[@class="css-901oao css-16my406 r-jwli3a r-c321bz r-ubezar r-13uqrnb r-majxgm r-rjixqe"]/text()').getall()
        splitTimeStart = time[1].split(":")
        starthour = int(splitTimeStart[0])
        startminute = int(splitTimeStart[1])
        splitTimeend = time[4].split(":")
        endhour = int(splitTimeend[0])
        endminute = int(splitTimeend[1])
        link = response.url
        descriptionparts = response.xpath('//div[@class="css-901oao r-oduq1r r-c321bz r-ubezar r-13uqrnb r-majxgm r-rjixqe"]/text()').getall()
        description = ''.join(descriptionparts)
        day_parts =  day.split()
        day_numeric = int(day_parts[1])
        month= day_parts[2]
        startdatetime =  day.split()

        month_mapping = {
    'jan': 1,
    'fev': 2,
    'mar': 3,
    'abr': 4,
    'mai': 5,
    'jun': 6,
    'jul': 7,
    'ago': 8,
    'set': 9,
    'out': 10,
    'nov': 11,
    'dez': 12,
}
        month_numeric = month_mapping.get(month)
        current_year = datetime.datetime.now().year
        # event_datetime = datetime.datetime(current_year, month_numeric, day_numeric)
        start_datetime = datetime.datetime(current_year, month_numeric, int(day_numeric), hour=starthour, minute=startminute)
        end_datetime = datetime.datetime(current_year, month_numeric, int(day_numeric), hour=endhour, minute=endminute)
       
       
        
        self.output_file.write(f'Title: {title}\n')
        self.output_file.write(f'Local: {local}\n')
        self.output_file.write(f'data: {day}\n')
        self.output_file.write(f'price: {price}\n')
        self.output_file.write(f'startTime: {time[1]}\n')
        self.output_file.write(f'endTime: {time[4]}\n')
        self.output_file.write(f'link: {link}\n')
        self.output_file.write(f'description: {starthour}\n')
        self.output_file.write(f'/////\n')

            #   Application Default credentials are automatically created.
        app = firebase_admin.initialize_app() 
        db = firestore.client()

        data = {"description": description,"startdatetime": start_datetime,"enddatetime": end_datetime,"name": title,"price": price,"site": link,}

# Add a new doc in collection 'cities' with ID 'LA'
        db.collection("approval").add(data)

        city_ref = db.collection("cities").document("BJ")

        city_ref.set({"capital": True}, merge=True)


        yield {
            'title': title,
            'local': local,
            'day': day,
            'price': price,
            'startTime': price[1],
            'endTime': price[3],
            'link': link,
            'description': description,
        }
        def closed(self, reason):
         self.output_file.close()