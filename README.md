# freq_words


利用Spark MLlib中的fp_growth统计twitter中出现的频繁项集

1.py_preparation.py主要是数据预处理，去噪（标点，stopwords等）

2.test_pre.py主要是去掉难以处理的未知编码（第一步很难处理），分词。

3.py_fpgrowth.py则为Spark程序，负责调用fp_growth算法处理前两步得到的数据文件


部分结果：（有一些错别字目前还未做处理）

FreqItemset(items=[u'phone'], freq=23)
FreqItemset(items=[u'repli'], freq=34)
FreqItemset(items=[u'repli', u'thank'], freq=24)
FreqItemset(items=[u'quick'], freq=29)
FreqItemset(items=[u'quick', u'thank'], freq=23)
