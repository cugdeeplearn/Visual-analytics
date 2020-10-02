'''
# coding:utf-8
import numpy as np
import pandas as pd
import jieba.analyse
import os


# 获取关键词
def Get_file_keywords(dir):
    try:
        formated_data = []  # 每篇文章关键词的二维数组
        set_key_list = []  # 所有关键词的列表
        fo = open('D:\\code\\bp\\visulization\\files\\fenci\\seg_outtext.txt', 'r', encoding='UTF-8')
        keywords = fo.read()
        for home, dirs, files in os.walk(dir):
            for filename in files:
                fullname = os.path.join(home, filename)
                f = open(fullname, 'r', encoding='UTF-8')
                sentence = f.read()
                words = " ".join(jieba.analyse.extract_tags(sentence=sentence, topK=30, withWeight=False, allowPOS=('n')))  # TF-IDF分词
                words = words.split(' ')
                formated_data.append(words)
                for word in words:
                    if word in keywords:
                        set_key_list.append(word)
                    else:
                        words.remove(word)
        set_word = list(set(set_key_list))  # 所有关键词的集合
        return formated_data, set_word
    except Exception as reason:
        print('出现错误：', reason)


# 初始化矩阵
def build_matirx(set_word):
    edge = len(set_word) + 1  # 建立矩阵，矩阵的高度和宽度为关键词集合的长度+1
    #matrix = np.zeros((edge, edge), dtype=str) # 另一种初始化方法
    matrix = [['' for j in range(edge)] for i in range(edge)]  # 初始化矩阵
    matrix[0][1:] = np.array(set_word)
    matrix = list(map(list, zip(*matrix)))
    matrix[0][1:] = np.array(set_word)  # 赋值矩阵的第一行与第一列
    return matrix


# 计算各个关键词的共现次数
def count_matrix(matrix, formated_data):
    for row in range(1, len(matrix)):
        # 遍历矩阵第一行，跳过下标为0的元素
        for col in range(1, len(matrix)):
            # 遍历矩阵第一列，跳过下标为0的元素
            # 实际上就是为了跳过matrix中下标为[0][0]的元素，因为[0][0]为空，不为关键词
            if matrix[0][row] == matrix[col][0]:
                # 如果取出的行关键词和取出的列关键词相同，则其对应的共现次数为0，即矩阵对角线为0
                matrix[col][row] = str(0)
            else:
                counter = 0  # 初始化计数器
                for ech in formated_data:
                    # 遍历格式化后的原始数据，让取出的行关键词和取出的列关键词进行组合，
                    # 再放到每条原始数据中查询
                    if matrix[0][row] in ech and matrix[col][0] in ech:
                        counter += 1
                    else:
                        continue
                matrix[col][row] = str(counter)
    return matrix


def main():
    formated_data, set_word = Get_file_keywords('D:\\code\\bp\\visulization\\files\\fenci')
    print(set_word)
    #print(5244)
    print(formated_data)
    matrix = build_matirx(set_word)
    matrix = count_matrix(matrix, formated_data)
    data1 = pd.DataFrame(matrix)
    data1.to_csv('D:\\code\\bp\\visulization\\files\\fenci\\data.csv', index=0, columns=None, encoding='utf_8_sig')


main()
'''
import concurrent.futures
from collections import Counter
import pandas as pd

tokens = []
'''
for _ in range(10):
    tokens.extend(['lazy', 'old', 'fart', 'lying', 'on', 'the', 'bed'])
'''
with open(r'D:\code\bp\visulization\files\fenci\Co occurrence matrix_input.txt','r',encoding='utf8')as f:
	# print(f.readlines())
    for line in f.readlines():
        for s in line.split():
            value = str(s)
            tokens.append(value)
    #print (words)
    #counts.append(int(value[1]))
    #rows = zip(words)

def cooccurrances(idx, tokens, window_size):

    # beware this will backfire if you feed it large files (token lists)
    window = tokens[idx:idx+window_size]    
    first_token = window.pop(0)

    for second_token in window:
        yield first_token, second_token

def harvest_cooccurrances(tokens, window_size=3, n_workers=5):
    l = len(tokens)
    harvest = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=n_workers) as executor:
        future_cooccurrances = {
            executor.submit(cooccurrances, idx, tokens, window_size): idx
            for idx
            in range(l)
        }
        for future in concurrent.futures.as_completed(future_cooccurrances):
            try:
                harvest.extend(future.result())
            except Exception as exc:
                # you may want to add some logging here
                continue


    return harvest

def count(harvest):
    return [
        (first_word, second_word, count) 
        for (first_word, second_word), count 
        in Counter(harvest).items()
    ]


harvest = harvest_cooccurrances(tokens, 3, 5)
counts = count(harvest)

print(counts)

#print(counts[1])

counts_1 = []
#counts = list(counts)
for i in range(len(counts)):
    if counts[i][2] != 1:
        counts_1.append(counts[i])
    

print("删除权重为1的共现单词:",counts_1)

list1 = []
list2 = []
list3 = []
for j in counts_1:
    list1.append(j[0])
    list2.append(j[1])
    list3.append(j[2])    
dataframe = pd.DataFrame({"Source":list1,"Target":list2,"Weight":list3})
dataframe.to_csv(r'D:\code\bp\visulization\files\weight_test0828.csv',index=False,sep=',',encoding='UTF-8-sig')