import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq
import csv

#网站：https://scrape.center/ spa3

base_url = "https://spa3.scrape.center/api/movie/?"
headers = {
    "Host": 'spa3.scrape.center',
    "X-Requested-With": 'XMLHttpRequest',
    "user-agen": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36",
    "cookie": "__jda=122270672.1673142548861134128172.1673142549.1673142549.1673142549.1; __jdc=122270672; __jdv=122270672|direct|-|none|-|1673142548863; __jdu=1673142548861134128172; wlfstk_smdl=97bshjd7zzwh6bp1w4a0ox4t5zptl7ov; TrackID=1iuKKsz2-150mYJV7GxdU8RufBvVN7gtJEb8j4Z9JdwrQo98D6xES2Ky2QeEY9--39Oub4vRbFBlp23JrnIZRq0PYPIrbmH6Sx8D4EYfE8yQ; thor=B26B88A9E54E26035958BF29BBA2BCEBE031680B37DB35CE3526574F5E85F46BB7C1D0BDE989873D1C7FFF5693CF552D7943983FBB7687609F44F4BEC269757261DA9229C29BB68872F7F3EFF39FF961F040A83689952367D8EECB2A521983A0F4C46857E87CFE9EFBCFD3A202A25B474433B5C071A1C4181E839EA651F75B49B6D62BEA181A1239D4162C0DFF31F949A3C7E5FB8805341F860B6BA3B20E2632; pinId=LCv2-fjTam1WnWZXhrytXrV9-x-f3wj7; pin=jd_42d8ae804c055; unick=jd_159667ciw; ceshi3.com=201; _tp=%2BKJIUIBVuvcVYC%2BmTW6wdRGtVWVaTH4X7jb8lZa5w5I%3D; _pst=jd_42d8ae804c055; areaId=15; ipLoc-djd=15-1213-0-0; __jdb=122270672.5.1673142548861134128172|1.1673142549; 3AB9D23F7A4B3C9B=NQFTWJRT5ENG3C5YHQQU6WEAKRZJQKGSC7EF7YSGKNUARXH34Q6ODXLM5V2E4H4G276UOO2RP42UUVDXWRHFO3W4GY"
}

def get_page(offset):
    params = {
        'limit': '10',
        'offset': 'offset' + '0'
    }
    url = base_url + urlencode(params)#转化成参数形式：https://spa3.scrape.center/api/movie/?limit=10&offset=offset0
    print(url)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)

def parse_page(json):
    if json:
        for i in range(0,10):
            ids = json.get('results')[i].get('id') #get方法可以获取字典中名字为results中的数据，[]数组，获取字典中第一个数据
            names = json.get('results')[i].get('name') #其中第一个数据为字典，则再用get方法获取字典中id值
            alias = json.get('results')[i].get('alias')
            categories = json.get('results')[i].get('categories')
            regions = json.get('results')[i].get('regions')
            actors=[]
            for j in range(0,5): #演员名单有多个，遍历获取前5个用数组存储
                actors.append(json.get('results')[i].get('actors')[j].get('name'))
            print(actors)
            scores = json.get('results')[i].get('score')
            ranks = json.get('results')[i].get('rank')
            minutes = json.get('results')[i].get('minute')
            dramas = json.get('results')[i].get('drama')
            published_ats = json.get('results')[i].get('published_at')
            WriteCSV(ids,names,alias,categories,regions,actors,scores,ranks,minutes,dramas,published_ats)

def WriteCSV(ids,names,alias,categories,regions,actors,scores,ranks,minutes,dramas,published_ats):
    with open("C:\\AllSoftWare\\tools\\Pycharm\\python_practice\\PaChong\PyExer\\Ajax_exer.csv","a+",encoding='utf-8',newline="") as f:
        writer = csv.writer(f)
        writer.writerow([ids,names,alias,categories,regions,actors,scores,ranks,minutes,dramas,published_ats])

if __name__ == '__main__':
    for offset in range(0, 1): #遍历多少页
        json = get_page(offset) #得到json格式数据
        parse_page(json)
