# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class Work2Pipeline:
    def process_item(self, item, spider):
        #movie = pd.DataFrame(data = item)
       # windows需要使用gbk字符集
      #  movie.to_csv('./movie2.csv',mode ='a+', encoding='gbk', index=False, header=['影片名称', '类型', '上映日期'])
        
        with open('movie2.csv', 'a+', encoding='gbk') as file:
            line = "{movie_name},{movie_type},{movie_time}\n".format(
                movie_name = item['movie_name'],
                movie_type = item['movie_type'],
                movie_time = item['movie_time'])
            file.write(line)
        return item
