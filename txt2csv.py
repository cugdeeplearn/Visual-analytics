'''
import pandas as pd

data = open(r'D:\code\bp\visulization\files\TF-IDF.txt','r',encoding='UTF-8')
res = []
for i in data:
    d = [x for x in i.strip().split(' ')]
    res.append(d)
save = pd.DataFrame(columns=['label','frequency'], index = None, data=list(res)) #columns列名，index索引名，data数据
# print(save)
fh = open(r'D:\code\bp\visulization\files\kuang_test.csv','w+')
save.to_csv(fh)
fh.close()
'''
import csv
import pandas as pd

line_words =[]
#counts =[]

with open(r'D:\code\bp\visulization\files\seg_outtext.txt','r',encoding='utf8')as f:
	# print(f.readlines())
    for line in f.readlines():
        line_words.append(line)
    rows = zip(line_words)
dataframe = pd.DataFrame({"label":line_words})
dataframe.to_csv(r'D:\code\bp\visulization\files\line_test.csv',index=False,sep=',',encoding='UTF-8-sig')




'''
#-*-coding:utf-8 -*-
import csv
import pandas as pd

words =[]
#counts =[]

with open(r'D:\code\bp\visulization\files\seg_outtext.txt','r',encoding='utf8')as f:
	# print(f.readlines())
    for line in f.readlines():
        for s in line.split():
            value = str(s)
            words.append(value)
    print (words)
    #counts.append(int(value[1]))
    rows = zip(words)
dataframe = pd.DataFrame({"label":words})
dataframe.to_csv(r'D:\code\bp\visulization\files\kuang_test.csv',index=False,sep=',',encoding='UTF-8-sig')    
'''
'''
with open(r'D:\code\bp\visulization\files\kuang_test.csv', "w+", newline="",encoding='UTF-8') as f:
    writer = csv.writer(f)
    writer.writerow(["标签"])
    for row in rows:  
        writer.writerow(words)
'''
