import jieba
from wordcloud import WordCloud
from wordcloud import WordCloud
import PIL .Image as image
import numpy as np
import jieba
import xlrd


def trans_CN(text):
    word_list = jieba.cut(text)    # 分词后在单独个体之间加上空格
    result = " ".join(word_list)
    return result;





if __name__ == "__main__":
    '''
    此代码是为了生成点云：
    1.需要爬虫得到的xls数据，这个在之前已经完成。
    2.需要运行toText.py 读取xls对应列数据 生成txt
    3.运行此代码 将生成的txt读入 生成词云
    
    '''

    #此处job.txt 需与xls转化生成的txt名字对应
    with open("jobqdzyq.txt", encoding= 'utf-8') as fp:

        text = fp.read()
        text = trans_CN(text)  # print(text)
        mask = np.array(image.open("1.png"))
        wordcloud = WordCloud(
            mask=mask,
            font_path="C:\\Windows\\Fonts\\msyh.ttc"
        ).generate(text)
        image_produce = wordcloud.to_image()
        image_produce.show()
