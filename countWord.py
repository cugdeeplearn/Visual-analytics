#!/usr/bin/env python
# encoding:utf-8

import matplotlib
import random
import matplotlib.pyplot as plt
import numpy as np
#from matplotlib.font_manager import *
#myfont = FontProperties(fname=r'C:\Windows\Fonts\simhei.ttf',size=12)

N = 10
words = []
counts = []

with open(r'D:\code\bp\visulization\files\TF_IDF_wordlength_sta_0830.txt','r',encoding = "UTF-8") as f:
    lines = f.readlines()
    for line in lines:
        value = [s for s in line.split('\t')]
        words.append(value[0])
        #counts.append(int(value[1]))
        counts.append(value[1])

# 中文乱码和坐标轴负号处理。
matplotlib.rc('font', family='SimHei', weight='bold')
plt.rcParams['axes.unicode_minus'] = False
 
#城市数据。
city_name = words[:N]
city_name.reverse()

 
data = counts[:N]
data = [float(_) for _ in data]
data.reverse()

#绘图。
fig, ax = plt.subplots(figsize = (5,5))
b = ax.barh(range(len(city_name)), data, color='#6699CC')
 
#为横向水平的柱图右侧添加数据标签。
for rect in b:
    w = rect.get_width()
    ax.text(w, rect.get_y()+rect.get_height()/2, '%.3f' %
            w, ha='left', va='center')
 
ax.xaxis.set_ticks(np.arange(0, 1.3, 0.1)) 
#设置Y轴纵坐标上的刻度线标签。
ax.set_yticks(range(len(city_name)))
ax.set_yticklabels(city_name)
#ax.set_xlabel(u"TF-IDF",fontproperties=myfont)

#plt.title('TF-IDF', loc='center', fontsize='25',
#          fontweight='bold', color='black')

plt.show()