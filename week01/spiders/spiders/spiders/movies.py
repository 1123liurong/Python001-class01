# -*- coding: utf-8 -*-
import scrapy
from spiders.items import SpidersItem
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
        
        #pass
       # soup = BeautifulSoup(response.text,'html.parser')
        item = SpidersItem()
      # item['movie_name'] 
       # 打印网页的url
        print(response.url)
        # 打印网页的内容
        # print(response.text)

        # soup = BeautifulSoup(response.text, 'html.parser')
        # title_list = soup.find_all('div', attrs={'class': 'hd'})
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        for movie in movies:
        #     title = i.find('a').find('span',).text
        #     link = i.find('a').get('href')
            # 路径使用 / .  .. 不同的含义　
            movie_name= movie.xpath('./div/span[@class="name"]/text()')
            movie_type = movie.xpath('./div[2]/text()')
            movie_time = movie.xpath('./div[4]/text()')


            item['movie_name'] = movie_name.extract()
            item['movie_type'] = movie_type.extract().strip()
            item['movie_time'] = movie_time.extract().strip()
            print (movie_name)
            print (movie_time.extract().strip())
        
        yield item