import random  
import numpy as np
import pandas as pd
from pyecharts.charts import WordCloud
import matplotlib.pyplot as plt
from PIL import Image,ImageSequence
from wordcloud import WordCloud,ImageColorGenerator

def DrawWordcloud():
    image = Image.open(r'D:\code\bp\visulization\files\椭圆2.jpg')#作为背景形状的图
    graph = np.array(image)
    #参数分别是指定字体、背景颜色、最大的词的大小、使用给定图作为背景形状
    wc = WordCloud(font_path = r'D:\code\bp\visulization\files\simsun.ttf', background_color = 'White', max_words = 200, mask = graph)
    words = []
    counts = []
    with open(r'D:\code\bp\visulization\files\TF-IDF.txt','r',encoding = "UTF-8") as f:
        lines = f.readlines()
        for line in lines:
            value = [str(s) for s in line.split()]
            words.append(value[0])
            counts.append(int(value[1]))
    dic = dict(zip(words, counts))#词频以字典形式存储
    wc.generate_from_frequencies(dic)#根据给定词频生成词云
    image_color = ImageColorGenerator(graph)
    plt.imshow(wc)
    plt.axis("off")#不显示坐标轴
    plt.show()
    wc.to_file('Wordcloud.png')#保存的图片命名为Wordcloud.png
if __name__=='__main__':
    DrawWordcloud()
