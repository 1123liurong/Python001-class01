# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pandas
class SpidersPipeline:
    def process_item(self, item, spider):
        m_name = item['movie_name']
        m_type = item['movie_type']
        m_time = item['movie_time']
        movie = pd.DataFrame(data = item)
        print (m_name,m_type,m_time)
       # windows需要使用gbk字符集
        movie.to_csv('./movie2.csv',mode ='a', encoding='gbk', index=False, header=['影片名称', '类型', '上映日期'])
      #  output = f'|{m_name}|\t|{m_type}|\t|{m_time}|\n\n'
      #  with open('./movie2.csv', 'a+', encoding='gbk') as article:
            # article.write(output)
        return item
         