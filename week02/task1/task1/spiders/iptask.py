# -*- coding: utf-8 -*-
import scrapy
from task1.items import Task1Item
from scrapy.selector import Selector


class IptaskSpider(scrapy.Spider):
    name = 'iptask'
    allowed_domains = ['douban.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        items=[]
        # soup = BeautifulSoup(response.text, 'html.parser')
        # title_list = soup.find_all('div', attrs={'class': 'hd'})
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        i=0
        for movie in movies:
            if i<10:
               item = Task1Item()
               movie_name = movie.xpath('div[2]/@title').extract_first().strip()
               movie_type = movie.xpath('div[2]/text()[2]').extract_first().strip()
               movie_time = movie.xpath('div[4]/text()[2]').extract_first().strip()
               print ('neirong',movie_name,movie_type,movie_time)            
               item['movie_name'] = movie_name
               item['movie_type'] = movie_type
               item['movie_time'] = movie_time
               i+=1
               items.append(item)
            else:
                break
            yield item
