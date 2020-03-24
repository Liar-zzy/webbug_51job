import random
from xml import etree
import requests
from lxml import etree
import xlwt
import time
from getAllDetails import getADetails


# 获取url 并实现一次爬虫
def get_url():

    urls = []
    p = 45

    for i in range(1,p):

        url="https://search.51job.com/list/070200,000000,0000,00,9,99,%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE,2," + \
                str(i) + \
            ".html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="

        simple_spider(url)
        s = random.randint(5, 30)
        time.sleep(s)


# 在excel中 增加一个sheet用于存储当前数据
def add_sheet(sheet_name, row_titles):
     sheet_info = workbook.add_sheet(sheet_name,cell_overwrite_ok=True)
     for i in range(0,len(row_titles)):
          sheet_info.write(0,i,row_titles[i])
     return  sheet_info


# 尝试进行一次爬取数据
def simple_spider(url):
     try:
          header = {'User-Agent':'Mozilla/5.0'}
          r = requests.get(url,header)
          r.raise_for_status()
          r.encoding = r.apparent_encoding
          get_data(r.text)
     except:
         return "失败"


# 解析网页数据
def get_data(text):
    html = etree.HTML(text)
    # 使用xpath格式获取数据
    divs = html.xpath('//*[@id="resultList"]/div[@class="el"]')

    for div in divs:
        job_title = div.xpath('./p/span/a/@title')
        job_company = div.xpath('./span[1]/a/@title')
        job_address = div.xpath('./span[2]/text()')
        job_salary = div.xpath('./span[3]/text()')
        job_href = div.xpath('./p/span/a/@href')

        job_title = job_title[0] if len(job_title) > 0 else ''
        job_company = job_company[0] if len(job_company) > 0 else ''
        job_address = job_address[0] if len(job_address) > 0 else ''
        job_salary = job_salary[0] if len(job_salary) >0 else ''
        job_href = job_href[0] if len(job_href) >0 else ''

        job_info = []  # 存储数据
        job_info.append(job_title)
        job_info.append(job_company)
        job_info.append(job_address)
        job_info.append(job_salary)

        # 读取职位的网页 将该网页继续解析 得到求职页面具体信息
        #job_info.append(job_href)

        job_body,job_name = getADetails(job_href)

        #print(job_body)

        #print(job_name)

        job_info.append(job_body)
        job_info.append(job_name)
        write_excel(job_info, 'Simple_spider_NJ2.xls')  # 写进sheet
        job_info = []  # 每写一次都需要清空
        time.sleep(1)


# 将数据写入excel
def write_excel(data, execl_name, count=[]):
    count.append(1)
    print('采集了{}条数据'.format(len(count)))
    for j in range(0, len(data)):
        data_sheet.write(len(count), j, data[j])
    workbook.save(execl_name)


def main():
    global workbook, data_sheet
    rowTitle = ['职务名称','公司名','公司地址','工资','网站要求','职能类别']
    #rowTitle = ['职务名称', '公司名', '公司地址', '工资', '网站']
    workbook = xlwt.Workbook(encoding='utf-8')  # 创建一个Excel
    data_sheet = add_sheet('简单爬虫', rowTitle)  # 给excel文件添加一个sheet 一般是先想好要存的数据标题是什么
    get_url()


if __name__ == '__main__':
    main()
