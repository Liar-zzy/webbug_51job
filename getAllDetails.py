from xml import etree
import requests
import lxml
import xlwt
import time
from bs4 import BeautifulSoup as bs

def getADetails(url_old):

    '''
    根据传进来的单个招聘信息的url 获取网站的详细信息
    :param url_old:
    :return:
    '''

    #print("GetADetails")

    url = url_old.format(1)
    try:
        #print("simple")
        header = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(url, header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding

        #print("bs")
        soup = bs(r.text, "lxml")
        # print(soup)
        body_all = soup.select(
            'body > div.tCompanyPage > div.tCompany_center.clearfix > div.tCompany_main > div:nth-child(1) > div >p')
        # print(body_all)

        job_body = ''
        for item in body_all:
            # print(item.get_text())
            job_body = job_body + item.get_text()
        #print(job_body)

        job_name = ''
        body_2 = soup.select(
            'body > div.tCompanyPage > div.tCompany_center.clearfix > div.tCompany_main > div:nth-child(1) > div > div.mt10 > p:nth-child(1) > a')
        #print(len(body_2))
        i = 0
        for item in body_2:
            i = i + 1
            if i == 1:
                job_name = job_name + item.get_text()
            else:
                job_name = job_name + "," + item.get_text()
        #print(job_name)

        return job_body,job_name;
    except:
        return "失败"
    time.sleep(5)

if __name__ == '__main__':
    getADetails("https://jobs.51job.com/nanjing/96480575.html?s=01&t=0")

