#index/urls.py
from django.urls import path,re_path,register_converter
from . import views,converters

register_converter(converters.IntConverter,'myint')
register_converter(converters.FourDigitYearConverter,'yyyy')
urlpatterns =[
    #path('',views.index),
    # 带变量的url
    # #path('<int:year>',views.year),#只接受整数，否则返回ERROR 404
    # path('<int:year>/<str:name',views.name),
    # # 正则匹配
    # # re_path('(?P<year>[0-9]{4}.html',views.myyear,name='urlyear'),#传入year进行匹配

    # #自定义过滤器
    # path('<yyyy:year>',views.myyear), #通过register_converter 定义
    path('shorts',views.short),
]