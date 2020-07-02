# -*- coding: utf-8 -*-
import scrapy
from work2.items import Work2Item 
from scrapy.selector import Selector


class MoviesSpider(scrapy.Spider):
    #定义爬虫的名字
    name = 'movies'
    #允许访问的范围
    allowed_domains = ['maoyan.com']
    #第一次发起的请求的页面
    start_urls = ['https://maoyan.com/films?showType=3']

    #解析函数
    def parse(self, response):
        
       
       # 打印网页的url
        print(response.url)
        # 打印网页的内容
        # print(response.text)
        items=[]
        # soup = BeautifulSoup(response.text, 'html.parser')
        # title_list = soup.find_all('div', attrs={'class': 'hd'})
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        i=0
        for movie in movies:

            if i<10:
               item = Work2Item()
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