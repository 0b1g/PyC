import requests
import re

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
}

r = requests.get("http://cxrc.kjt.zj.gov.cn/ContactInfoSelected03.aspx",headers=headers)
result = re.findall("<td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td>",r.text)
print(result)
# print(r.text)