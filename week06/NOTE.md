##  开发环境配置

web框架 Django ,流行的FastApI    展示逻辑  模型 模板 视图  views models template

DRY 代码复用原则

组件 ORM映射，等

安装pip  install  --upgrade django==2.2.13 版本  (特定版本安装)

##  创建项目和目录结构



1. 创建项目

   django-admin  startproject MyDjango  # 创建myDjango

   生成目录 manage.py 项目管理 settings.py 配置文件

2. 创建Django应用程序

   1)python manage.py startapp index  #index 应用程序的 

   python manage.py runserver 0.0.0.0：80 # 启动 服务
2) settings.py 中配置 新app index
   

3）urls.py  中 urlpatterns 中配置 应用处理的路径

​	 urlpatterns =[

​	path('admin/',admin.site.urls),

​	path('',include('index.urls')),

​	path('douban/',include('Douban.urls')),

​	]

## Settings.py的配置文件

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path))                         #读取自己脚本

开发wsgi生产模式

配置1installed_apps  不改变顺序，在尾端 加入'index' #自己注册的app

请求从上到下 ，返回从下到上  

ROOT_URL_CONF = 'MyDjango.urls'   #配置处理路径

TEMPLATE 用flask  jinjia2 配置模板

Database 

默认使用第一个 default  配置的数据库 ，可配置多个数据库

配置2数据加载的引擎，mysql   

#安装mysql 导出环境变量 配置

  static_url #设置静态文件对应的目录

##  url调度器

urlconf  处理 请求

1 传入httpRequest 对象urlconf ，root_urlconf 

2 django 加载urlconf 寻找urlpatterns ，django 依次匹配url模式

3 urlpartterns  ，通过include方式导入应用 

​	utrlpatterns=

​	[path('',views.index)]

   path("",include(index.utrls')),

   ## 模块和包

   .py结尾的文件称为模块

   包 存放多个文件的目录

   --init--.py 导入包时优先运行

定义和执行 

    from 包 import 模块  
       
    from.#从当前模块引入  from .PKg2
    # mPackage/model.py 定义可执行的模块 
    def func1():
        print('import func1')
        
    if __name__ == '__main__':
        func1()
    # python model.py  ，--name-- 会变成 model， main 函数即可以运行
    
    #运行模块中的文件的函数
    from mPackage import model as M
    m.func1()

   ## url支持变量

Django 支持对URL设置变量，URL的变量类型包括：str，int，slug，uuid，path 

  1）带变量的url path('<int:year',views.myyear),例 127.0.0.1:8000/12345.

   2) url path('<int:year/str:strings',views.myyear), 例 127.0.01:8000/striabc  ,

 生产模式会返回问题和匹配顺序

   3）url正则 re_path('(?P<year>[0-9]{4}).html',name ='urlyear'),例 2020.html

   4) 自定义过滤去

 	

​	 regitster_converters.intconverter(convter.foutgitYearconveter,'yyyy')

  	class inconverter:

   ​	regex='[0-9]+'

   ​	def to_python(self,value):	

   ​	 return int(vlaue)

   ​    def  to_int

   ## view 视图处理

   response 与render  ：render 将response 再次封装

   render 返回请求内容到指定页面，

   redirect 用户密码的跳转

get_object_or_404() 如果不存在返回404

   ## 使用ORM创建数据库

数据库表=python类， 数据库字段= 类属性

```
from django.db import models
class Person(models.Model):
  id= models.InterField(primary_key=True)
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
```

通过中间脚本将类转化为实际的数据表明 makemigration  ，migrate

```
> python manage.py makemigrations 
> python manage.py migrate
```

在MyDjango的init文件中导入pymysql 文件

```
# XmDjango/init.py
import pymysql
pymysql.install_as_Mysqldb()
> export  PATH=$PATH:/usr/local/mysql/bin
```

[doc.djangoproject.com] 中查询model字段类型、字段选项设置方法

使用shell 对数据表进行读写

```
> python manage.py shell
from index.models import *
n=Name()
n.name ='红楼梦'
n.author ='曹雪芹'
n.stars=9.6
n.save()
#使用ORM框架 api 实现
from index.models import *
Name.objects.create(name='红楼梦'，author='曹雪芹'，stars='9.6')
```

### Django模板开发

模板变量 {{variables}}

从URL获取模板变量{% url 'urlyear' 2020 %}

读取静态资源内容{% static "css/header.css" %}

for 遍历标签{% for type in type_list %}{% endfor %}

if 判断标签{% if name.type == type.type %}{% end if %}  ​       

## URLconf 与Model

1. 创建一个新的Douban APP

   ```
   >python manage.py startapp Douban
   ```

2. setting 中配置 Douban

3. urls.py 中的urlpatterns 中配置路径

   ```
   path('douban/',include('Douban.urls'))
   ```

4.  编写douban 中urls.py 指定访问路径（需自己创建urls.py)

5.  通过数据库表创建models.py

   ```
   >python manage.py inspectdb>models.py
   ```

   ###     

   

   

   

   

   

