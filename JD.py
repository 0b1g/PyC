import requests
from lxml import etree
import csv

def Crawler():
    headers = {
        "user-agen": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36",
        "cookie":"__jda=122270672.1673142548861134128172.1673142549.1673142549.1673142549.1; __jdc=122270672; __jdv=122270672|direct|-|none|-|1673142548863; __jdu=1673142548861134128172; wlfstk_smdl=97bshjd7zzwh6bp1w4a0ox4t5zptl7ov; TrackID=1iuKKsz2-150mYJV7GxdU8RufBvVN7gtJEb8j4Z9JdwrQo98D6xES2Ky2QeEY9--39Oub4vRbFBlp23JrnIZRq0PYPIrbmH6Sx8D4EYfE8yQ; thor=B26B88A9E54E26035958BF29BBA2BCEBE031680B37DB35CE3526574F5E85F46BB7C1D0BDE989873D1C7FFF5693CF552D7943983FBB7687609F44F4BEC269757261DA9229C29BB68872F7F3EFF39FF961F040A83689952367D8EECB2A521983A0F4C46857E87CFE9EFBCFD3A202A25B474433B5C071A1C4181E839EA651F75B49B6D62BEA181A1239D4162C0DFF31F949A3C7E5FB8805341F860B6BA3B20E2632; pinId=LCv2-fjTam1WnWZXhrytXrV9-x-f3wj7; pin=jd_42d8ae804c055; unick=jd_159667ciw; ceshi3.com=201; _tp=%2BKJIUIBVuvcVYC%2BmTW6wdRGtVWVaTH4X7jb8lZa5w5I%3D; _pst=jd_42d8ae804c055; areaId=15; ipLoc-djd=15-1213-0-0; __jdb=122270672.5.1673142548861134128172|1.1673142549; 3AB9D23F7A4B3C9B=NQFTWJRT5ENG3C5YHQQU6WEAKRZJQKGSC7EF7YSGKNUARXH34Q6ODXLM5V2E4H4G276UOO2RP42UUVDXWRHFO3W4GY"
    }
    url = "https://order.jd.com/center/list.action?search=0&d=2022&s=4096"

    session = requests.Session()        #session会话维持
    response = session.get(url=url, headers=headers)
    html = response.text
    html = etree.HTML(html)
    order_times = html.xpath('//span[@class="dealtime"]//text()')   #购买订单时间
    order_ids = html.xpath('//span[@class="number"]/a//text()')      #订单号
    order_things =html.xpath('//div[@class="p-name"]/a[@target="_blank"]//text()')      #物品名称
    order_prices =html.xpath('//div[@class="amount"]//span[1]//text()') #选择span标签下的第一个标签span[1]，价格
    for order_time,order_id,order_thing,order_price in zip(order_times,order_ids,order_things,order_prices):
        WriteCSV(order_time,order_id,order_thing,order_price)

def WriteCSV(order_time,order_id,order_thing,order_price):
    with open("C:\\AllSoftWare\\tools\\Pycharm\\python_practice\\PaChong\PyExer\\JD01.csv","a+",encoding='utf-8',newline="") as f:
        writer = csv.writer(f)
        writer.writerow([order_time, order_id, order_thing, order_price])

if __name__ == '__main__':
    Crawler()