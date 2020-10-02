#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import jieba

#创建停用词列表
def stopwordslist():
    stopwords = [line.strip() for line in open (r'D:\code\bp\visulization\dict_stopwords\stopwords-master\中文停用词表.txt',encoding = 'UTF-8').readlines()]
    return stopwords

#对句子进行中文分词 
def seg_depart(sentence):
    #对文档中的每一行进行中文分词
    print ("正在分词")
    jieba.load_userdict(r"D:\code\bp\visulization\dict_stopwords\out_dict.txt")
    sentence_depart = jieba.cut(sentence.strip())
    #创建一个停用词列表
    stopwords = stopwordslist()
    #输出结果为outstr
    outstr = ''
    #去停用词
    for word in sentence_depart:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr
    
#给出文档路径
filename = r"D:\code\bp\visulization\files\new_outtext_zhengze.txt"
outfilename = r"D:\code\bp\visulization\files\final_new_outtext_zhengze.txt"

inputs = open(filename, 'r', encoding = 'UTF-8')
outputs = open(outfilename, 'w', encoding = 'UTF-8')

#将输出结果写入seg_outtext.txt中
for line in inputs:
    line_seg = seg_depart(line)
    outputs.write(line_seg + '\n')
    #print("---------------正在分词和去停用词---------------")
outputs.close()
inputs.close()
print ("删除停用词和分词成功！")

 
    
    
    
    
    
    
    
'''
# 加载自定义词库
jieba.load_userdict(r"D:\code\bp\visulization\dict_stopwords\out_dict.txt")
path = r"D:\code\bp\visulization\files\new_outtext.txt"

#f2 = open(r"D:\code\bp\visulization\files\seg_outtext.txt",'w',encoding = "UTF-8")
with open(path,'r',encoding='utf-8') as f:
    str_doc = f.read()
    sl = jieba.cut(str_doc)
    print ("[加载自定义词库后]：", "/".join(sl))
    #f2.write(str(sl))
'''