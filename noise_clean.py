# ecoding=utf-8
#ifn = r"D:\\code\\bp\\visulization\\files\\new_outtext.txt"
ifn = r"D:\\code\\bp\\visulization\\files\\new_outtext.txt"
ofn = r"D:\\code\\bp\\visulization\\files\\new_outtext_zhengze_out28-1.txt"

infile = open(ifn,'r',encoding = 'utf8')
outfile = open(ofn,'w+',encoding = 'utf8') # 在使用write()函数的时候，如果文件打开模式带 b，那写入文件内容时，str (参数)要用 encode 方法转为 bytes 形式，否则报错。

for eachline in infile.readlines():
    #去掉文本行里面的空格、\t、数字（其他有要去除的也可以放到' \t1234567890'里面）
    lines = filter(lambda ch: ch not in '\t1234567890%）（ -  m.－/ °,+×()~=△．′①②±≥＞≤③#$?_“”、《》Ⅱ^·ⅦⅢ：T％℃″″＜√∑……④—【】*Ⅰk～○ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz∈φ﹪g : ;；μπωΦγδ，。', eachline) 
    lines = list(lines)
    #print (lines)
    lines = "".join(lines)
    #outfile.write(lines.replace(r"。",'。\n'))
    outfile.write(lines) # 写入train_output.txt(此处是一股脑的全写进去，并没有做任何的分行处理)

infile.close()
outfile.close()