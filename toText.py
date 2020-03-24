import numpy as np
import xlrd #打开excel文件

if __name__ == '__main__':

    '''
    此代码是为了将xls 某一列 生成 对应的txt
    更改xls（excel表格文件） 名字在 14行
    更改生成的txt文件在 20行
    更改excel列 在23行 5为 职业 4为 要求
    '''


    data= xlrd.open_workbook('Simple_spider_QD.xls')#打开Excel文件读取数据
    sh=data.sheet_by_name("简单爬虫")##通过工作簿名称获取
    print(sh.nrows)
    print(sh.ncols)
    n=0
    i=0
    file=open("jobqdzyq.txt",'wb')
    for n in range(sh.nrows):
        print(n)
        text=sh.cell_value(n,4).encode('utf-8')
        text=text
        file.write(text+b'\n')