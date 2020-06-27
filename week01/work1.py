# 使用requests库获取豆瓣影评

from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs
import requests

ua = UserAgent()

#设置User_agent,cookie 防止被反爬
user_agent = ua.random
header = {
    'Cookie':'uuid_n_v=v1; uuid=26FBFE10B62711EA95E3C92BBC8FF0192F9CF699BF99461CBA685840EB0D7813; __guid=17099173.2848318422711892500.1593008985397.3293; _lxsdk_cuid=172e6bc1c4cc8-0d91da3e772f0b-376b4502-1fa400-172e6bc1c4cc8; _lxsdk=26FBFE10B62711EA95E3C92BBC8FF0192F9CF699BF99461CBA685840EB0D7813; mojo-uuid=33491ae3bdd2ba95faebe92470e4a720; _lx_utm=utm_source%3Dso.com%26utm_medium%3Dorganic; _csrf=8b7d8bf2de1f48fa0155e99f415e71373bf4b85c46411470a0f0c717b0344fb8; mojo-session-id={"id":"17c714391ab1030cc50dae096d9b7e7d","time":1593263137369}; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593008987,1593097703,1593121921,1593263137; monitor_count=6; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593263822; mojo-trace-id=11; __mta=210597546.1593008989026.1593263779240.1593263821897.25; _lxsdk_s=172f5e224f9-1f4-1b1-1a6%7C%7C11',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
#猫眼网站的排名地址
myurl = 'https://maoyan.com/films?showType=3'
response = requests.get(myurl,headers=header)
#打印请求返回状态码
print(f'返回码是: {response.status_code}')

bs_info = bs(response.text, 'html.parser')

# Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
mylist = []
#获取电影名称，类型，上映时间
for tags in bs_info.find_all('div',attrs = {'class':'movie-hover-info'} ):
    film_name =''
    film_type =''
    for tag2s in tags.find_all('div', attrs = {'class':'movie-hover-title'}):
        film_name  = tag2s.get('title')
        film_type_tmp = tag2s.find('span',attrs={'class':'hover-tag'})
        if film_type_tmp is not None:
            if film_type_tmp.text =='类型:':
               film_type= tag2s.text.split(':')[1].strip()
    film_time = tags.find('div',attrs={'class':'movie-hover-title movie-hover-brief'}).text.split(':')[1].strip()
    print(film_name,film_type,film_time)
    mylist.append([film_name,film_type,film_time])

import pandas as pd
#使用pandas 整理数据到文件
movie = pd.DataFrame(data = mylist[:10])

# windows需要使用gbk字符集
movie.to_csv('./movie1.csv', encoding='gbk', index=False, header=['影片名称', '类型', '上映日期'])