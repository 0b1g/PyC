import requests
from lxml import etree
import csv

def Crawler():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
    }
    baseurl = "https://www.qidian.com/rank/hotsales/"
    for i in range(5):
        baseurl = "https://www.qidian.com/rank/hotsales/page{}/".format(i+1)
        response = requests.get(url=baseurl, headers=headers)
        html = response.text
        html = etree.HTML(html)
        book_names = html.xpath('//h2/a/text()')
        book_authors = html.xpath('//p[@class="author"]/a[@class="name"]//text()')
        book_type1s = html.xpath('//p[@class="author"]/a[@target="_blank" and @data-eid="qd_C42"]//text()')
        book_type2s = html.xpath('//p[@class="author"]/a[@class="go-sub-type"]//text()')
        book_states = html.xpath('//p[@class="author"]/span//text()')
        book_infos = html.xpath('//p[@class="intro"]//text()')
        for book_name,book_author,book_type1,book_type2,book_state,book_info in zip(book_names,book_authors,book_type1s,book_type2s,book_states,book_infos):
            WriteCSV(book_name,book_author,book_type1,book_type2,book_state,book_info)
        # print(book_name)
        # print(book_author)
        # print(book_type1)
        # print(book_type2)
        # print(book_state)
        # print(book_info)

def WriteCSV(book_name,book_author,book_type1,book_type2,book_state,book_info):
    with open("C:\\AllSoftWare\\qidian.csv","a+",encoding='utf-8',newline="") as f:
        writer = csv.writer(f)
        writer.writerow([book_name, book_author, book_type1,book_type2,book_state,book_info])

if __name__ == '__main__':
    Crawler()