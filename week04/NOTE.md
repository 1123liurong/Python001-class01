学习笔记
1. pandas 基本操作
  可进行的运算方式列相加
	df['A']+df['C']
   具体操作文档 https://pandas.pydata.org/docs/user_guide/computation.html#method-summary
2. pandas 数据的分组及聚合
   统计数据的分组操作
   df2.groupby('type').count()
   统计分组的数值和
   df2.groupby('type').aggregate('type':'count','feb':'sum')
   构建数据
   pd.dataframe 

   agg,transform 区别
   pvoit_table 数据透视表
3 jieba 分词与提取关键词
  cut ，cut for search 方法分词
  tfidf 算法 topk设置权重值,提取关键词使用
	tfidf=jieba.analyse.extract_tags(text)
  textrank 
  问题1 不是真正的关键词，stop_words.txt 可以将非需要的关键词过滤掉，使用配置文件来拼接配置
  问题2 需要的词不认识，user_dict 设置 词+设置权重+词性
        动态加载jieba.add_word('极客大学')
	jieba.del_word('极客大学')删除
	jieba.suggest_freq('中出',True) 将错分的词分开

     