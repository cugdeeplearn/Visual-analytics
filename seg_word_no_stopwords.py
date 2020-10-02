'''
#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import jieba

#给出文档路径
filename = r"D:\code\bp\visulization\files\new_outtext_zhengze_out28.txt"
outfilename = r"D:\code\bp\visulization\files\new_outtext_zhengze_out28_seg.txt"

#inputs = open(filename, 'r', encoding = 'UTF-8')
outputs = open(outfilename, 'w', encoding = 'UTF-8')

jieba.load_userdict(r"D:\code\bp\visulization\dict_stopwords\out_dict.txt")
#将输出结果写入seg_outtext.txt中
with open (filename,'r', encoding = 'UTF-8') as f:
    outstr = ''
    line_content = f.read()
    line_seg = jieba.cut(line_content)
    #去停用词
    for word in line_seg:
        outstr += word
        if word != '\n'
            outstr += " "   
    outputs.write(outstr)
outputs.close()
f.close()
print ("删除停用词和分词成功！")
'''

#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import jieba

#给出文档路径
filename = r"D:\code\bp\visulization\files\new_outtext_zhengze_out28-1.txt"
outfilename = r"D:\code\bp\visulization\files\new_outtext_zhengze_out28-1_seg1.txt"

#inputs = open(filename, 'r', encoding = 'UTF-8')
outputs = open(outfilename, 'w', encoding = 'UTF-8')

jieba.load_userdict(r"D:\code\bp\visulization\dict_stopwords\out_dict.txt")
#将输出结果写入seg_outtext.txt中
with open (filename,'r', encoding = 'UTF-8') as f:
    outstr = ''
    line_content = f.read()
    line_seg = jieba.cut(line_content)
    #去停用词
    for word in line_seg:
        outstr += word
        if word != '\n':
            outstr += " "   
    outputs.write(outstr)
outputs.close()
f.close()
print ("删除停用词和分词成功！")   