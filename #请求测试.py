#请求测试
import requests
import json

def request_h(url):
    headers = {
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63040026)",
        "X-Requested-With": "XMLHttpRequest",
        
        "Referer": "http://jc.ncu.edu.cn/?code=3udUa91k_xCo4oIb1IiBUU4ryxhVuPrjp7JmepNU7_M&state=STATE",
        "token": "eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJlY2hpc2FuIiwic3ViIjoiNTEwNjExODA1MSIsImlhdCI6MTYzNTUyMTY2NH0.T6xZDk4G1nufskRnZCD5pKDmH-ZywORafhYdsI30whlhXk8nVSKA4-ueImHRK2I2HBdu6uWCOMBX8drYk8yCsQ",
        "Connection":"keep-alive",
        "Host": "jc.ncu.edu.cn",
    }
    r = requests.get(url,headers=headers,json=None)
    return r

if __name__ == '__main__':
    url = 'http://jc.ncu.edu.cn/gate/student/getPreSignInfo'
    res = request_h(url)
    print(res.text)

