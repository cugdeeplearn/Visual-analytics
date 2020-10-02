#!/usr/bin/env python
# encoding:utf-8
import io
import sys
#reload(sys) # Python2.5 初始化后删除了 sys.setdefaultencoding 方法，我们需要重新载入 
#sys.setdefaultencoding('utf-8') 
#print (sys.getdefaultencoding())
# 打开文件
fr=io.open(r'D:\code\bp\visulization\files\fenci\hand_crafted_pro\final\final_segword0828.txt','r', encoding='utf-8')
# 读取文件所有行
content=fr.readlines()
contentLines=''
 
characers=[]#存放不同字的总数
rate={}#存放每个字出现的频率

#读取停用词，创建停用词表

#stwlist = [line.strip() for line in io.open ('stopwords.txt','r', encoding='utf-8').readlines()]



# 依次迭代所有行
for line in content:
    # 去除空格
    #line=line.strip()
    #如果是空行，则跳过
    if len(line)==0:
        continue
    contentLines = contentLines + line
    # 统计每一字出现的个数
    for db in line.split():
        #if db.strip() not in stwlist and len(db)>1:
            if not db in characers:
                characers.append(db)
	    # 如果是字符第一次出现 加入到字典中
            if db not in rate:
                rate[db]=1
        #出现次数加一
            rate[db]+=1

 
# 对字典进行倒数排序 从高到低 其中e表示dict.items()中的一个元素，
# e[1]则表示按 值排序如果把e[1]改成e[0]，那么则是按键排序，
# reverse=False可以省略，默认为升序排列
rate=sorted(rate.items(), key=lambda e:e[1], reverse=True)

# write
 #打开一个文本将统计好的词频存放进去
with io.open(r'D:\code\bp\visulization\files\TF-IDF0830_have_stopwordspython.txt', 'w', encoding='utf-8') as fw:
	for i in rate:
		fw.write(i[0]+'   '+str(i[1])+'\n')
fw.close()


print('全文共有%d个字'%len(contentLines))
print('一共有%d个不同的字'%len(characers))
print()
for i in rate:
    print("[",i[0],"] 共出现 ",  i[1], "次")
 
fr.close()
