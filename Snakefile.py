# 获取定位信息的.py
import requests
import json
url = "https://restapi.amap.com/v3/geocode/regeo?location=109.67538,37.14258&key=a0599c316b9533a47162b9044a64f659&extensions=base"
headers = {
    "Accept-Encoding": "gzip, deflate, br",
    "User-Agent": "Mozilla/5.0",
    "content-type": "application/json",
    "Referer": "https://servicewechat.com/wxd2bebfc67ee4a7eb/45/page-frame.html",
    "Connection": "keep-alive",
    "Host": "restapi.amap.com"

}
r = requests.get(url, headers=headers)
print(r.json())
