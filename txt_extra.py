﻿from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
#from mailmerge import MailMerge
import os

# text_path = r'photo-words.pdf'
def parse(pdf_path,text_path):
    '''解析PDF文本，并保存到TXT文件中'''
    with open(pdf_path, 'rb') as fp:
        # 用文件对象创建一个PDF文档分析器
        parser = PDFParser(fp)

    # 创建一个PDF文档
    doc = PDFDocument()

    # 连接分析器，与文档对象
    parser.set_document(doc)
    doc.set_parser(parser)

    # 提供初始化密码，如果没有密码，就创建一个空的字符串
    doc.initialize()

    # 检测文档是否提供txt转换，不提供就忽略
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:

        # 创建PDF，资源管理器，来共享资源
        rsrcmgr = PDFResourceManager()

        # 创建一个PDF设备对象
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)

        # 创建一个PDF解释其对象
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        #content 用于保存文本信息
        content = []
        #content_test 用于标记文本信息方便查找
        content_test=[]
        # 循环遍历列表，每次处理一个page内容
        # doc.get_pages() 获取page列表
        for page in doc.get_pages():
            index = 0
            interpreter.process_page(page)

            # 接受该页面的LTPage对象
            layout = device.get_result()
            # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象
            # 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等
            # 想要获取文本就获得对象的text属性，
         
            for x in layout:
                if isinstance(x, LTTextBoxHorizontal):
                    with open(text_path, 'a', encoding='utf-8') as f:
                        results = x.get_text()
                        f.write(results + '\n')

if __name__ == '__main__':
    folder = "D:\\code\\bp\\visulization\\files"
    os.chdir(folder)
    pdf_path = './辽宁省鞍山市黑石砬子铁矿床补充勘探报告.pdf'
    text_path = './outtext.txt'
    parse(pdf_path,text_path)

