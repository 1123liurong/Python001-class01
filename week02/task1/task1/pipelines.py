# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class Task1Pipeline:

    def __init__(self):
        self.conn = pymysql.connect('localhost', 'root', 'python', 'sqldb', charset = 'utf8mb4')
        self.cursor = self.conn.cursor()
        self.cursor.execute('select VERSION()')
        result=self.cursor.fetchone()
        print (result)
        #打印是否链接成功
 
    def process_item(self, item, spider):
        insert_sql = """
            insert into movie_info(movie_name, movie_type, moive_time)
            VALUES (%s, %s, %s)
        """
        
        value = (item['movie_name'],item['movie_type'],item['movie_time'])   
        self.cursor.execute(insert_sql,value)        
        self.conn.commit()
        # 插入数据到mysql，并提交
        return item
