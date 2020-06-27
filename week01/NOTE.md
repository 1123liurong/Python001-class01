学习笔记
1 request命令
  user_agent 可以通过 from fake_useragent import UserAgent 导入获取到 header
  如果被反爬可以使用F2 -network -选择网页地址 查看cookie内容
2 bs 命令 from bs4 import beatifullsoup as bs
  对要找的网页研究不够，一开始想到的方法是翻页，但是python去重复的功能还不太会用，还要多次请求，参考了其它同学的作业后，找到方法
3 pandas 命令
  直接转2维数组到csv ，pd.Dataframe = {data=mylist[:10] 取前10条记录

初学还是感到python的方便，花了好几天时间，
 浪费时间的地方
 1 作业看了好几遍，才保证明确题目，一开始找错了要爬的网页
 2 函数不是很熟悉，做一步要看一步例题代码，下载和按装也出了好多问题，要是没有助教和老师的指导提示，感觉会绕不出来，上课还是很有好处的
  