import re
#import pkuseg
#from pyhanlp import *
#HanLP.Config.ShowTermNature = False
#import pandas as pd

def readFile(path):
    str_doc = ""
    f2 = open('D:/code/bp/visulization/files/new_outtext.txt','w',encoding = "UTF-8")
    #f3 = open('D:/code/bp/visulization/files/new_outtext无空格.txt','w',encoding = "UTF-8")
    with open(path,'r',encoding='utf-8') as f:
        #str_doc = f.read()
        lines = f.readlines()
    '''  
    #去除空行
    str_doc = re.sub(r"\n+", "\n",out_str)
    '''
    a = ''
    for line in lines:
        a += line.strip()#去除换行
        c = a.split()#将a分割成每个字符串
        b = ''.join(c)#将c的每个字符不以任何符号直接连接
        
    f2.write(b.replace(r"。",'。\n'))
    #f2.write(b)
    
    #分词
    '''
    seg = pkuseg.pkuseg(model_name='default')  # 程序会自动下载所对应的细领域模型
    for word in str3:
        text = seg.cut(word)              # 进行分词
        print(text)
    '''
    '''
    for word in str3:
        text = HanLP.segment(word)
        print(text)
    '''
    '''
    data ={
            'Description':str_out_list[::-1],
            'Width':str4[::-1]
          }
    # list转dataframe
    df = pd.DataFrame(data)
    
    # 保存到本地excel
    df.to_excel(r"D:\code\bp\pmt\dem\infor_extract\outfiles\outdes.xlsx", index=True)
    '''


if __name__ == '__main__': 
    path= r'D:\code\bp\visulization\files\outtext.txt'
    readFile(path)