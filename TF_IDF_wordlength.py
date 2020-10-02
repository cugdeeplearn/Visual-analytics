#-*-coding:utf-8-*-
# -*- coding: utf-8 -*-
from collections import defaultdict
import math
import operator
 
"""
函数说明:创建数据样本
Returns:
    dataset - 实验样本切分的词条
"""

word_length = {} 
max_word_length = [] 
def loadDataSet():
    dataset = []    
    with open (r'D:\code\bp\visulization\files\fenci\hand_crafted_pro\final\final_segword0828.txt', 'r', encoding = 'utf8') as f:
        all_line = f.readlines()
        for line in all_line:
            line = line.strip('\n\ufeff')
            words = line.split(' ')
            dataset.append(words)
        for list in dataset:
            del(list[len(list)-1])
        for list in dataset:
            for i in list: 
                word_length.setdefault(i,len(i))
    max_word_length.append (max(word_length.values()))                  
    #print (dataset)
    return dataset,word_length,max_word_length
"""
函数说明：特征选择TF-IDF算法
Parameters:
     list_words:词列表
Returns:
     dict_feature_select:特征选择词字典
"""
'''
def values_function(dict):
    values = []
    for v in dict.values():
        values.append(format(v))
    return values
'''
def feature_select(list_words):
    #总词频统计
    doc_frequency=defaultdict(int)
    for word_list in list_words:
        for i in word_list:
            doc_frequency[i]+=1
 
    #计算每个词的TF值
    word_tf={}  #存储每个词的tf值
    for i in doc_frequency:
        word_tf[i]=doc_frequency[i]/sum(doc_frequency.values())
 
    #计算每个词的IDF值
    doc_num=len(list_words)
    word_idf={} #存储每个词的idf值
    word_doc=defaultdict(int) #存储包含该词的文档数
    for i in doc_frequency:
        for j in list_words:
            if i in j:
                word_doc[i]+=1
    for i in doc_frequency:
        word_idf[i]=math.log(doc_num/(word_doc[i]+1))
    
    #print (doc_frequency)
    #计算每个词的TF*IDF的值
    word_tf_idf={}
    for i in doc_frequency:
        word_tf_idf[i] = word_tf[i]*word_idf[i]
        #word_tf_idf[i] = round(word_tf_idf[i], 3)
    #print (word_tf_idf)
    
    #计算TF-IDF-Wordlength 
    word_tf_idf_word_length = {}
    for i in doc_frequency:
        word_tf_idf_word_length [i] = word_tf_idf[i] + word_length[i]/max_word_length[0]
        word_tf_idf_word_length [i] = round(word_tf_idf_word_length [i], 3)
    
    '''    
    word_tf_idf_word_length=[]
    value_list = values_function(word_tf_idf)
    for i in range(len(word_tf_idf)):
        word_tf_idf_word_length.append (float(value_list[i])  + float(word_length[i]/max_word_length[0]))
        #word_tf_idf_word_length[i] = round(word_tf_idf_word_length[i], 3)
    print (word_tf_idf_word_length)
    '''
    # 对字典按值由大到小排序
    dict_feature_select=sorted(word_tf_idf_word_length.items(),key=operator.itemgetter(1),reverse=True)
    #dict_feature_select=sorted(word_tf_idf.items(),key=operator.itemgetter(1))
    return dict_feature_select
 
if __name__=='__main__':
    data_list, word_length, max_word_length=loadDataSet() #加载数据
    #print (data_list)
    #print (word_length)
    #print (max_word_length)

    features=feature_select(data_list) #所有词的TF-IDF值
    #print(features)
    print(len(features))
    fw=open(r'D:\code\bp\visulization\files\fenci\hand_crafted_pro\final\final_segword0828-tf-idf-wordlength.txt','w',encoding = 'utf8')
    for line in features:
        for a in line:
            fw.write(str(a))
            fw.write('\t')
        fw.write('\n')
    fw.close()