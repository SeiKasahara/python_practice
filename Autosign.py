#AutoSign.py

import threading
import requests
from threading import Thread
import time
import datetime
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def request_h(url,json,token):
    headers = {
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63040026)",
        "X-Requested-With": "XMLHttpRequest",
        
        "Referer": "http://jc.ncu.edu.cn/?code=3udUa91k_xCo4oIb1IiBUU4ryxhVuPrjp7JmepNU7_M&state=STATE",
        "token": token,
        "Connection":"keep-alive",
        "Host": "jc.ncu.edu.cn",
    }
    while True:
        r = requests.post(url, headers=headers, json=None)
        print(r.text)
        time.sleep(60*60*24)

def send_email():
    smtp_server = 'smtp.qq.com'

    sender = '1325054302@qq.com'
 # 发送方密码（或授权密码）
    password = 'qduuacxjamwqfefd'
 # 收件方邮箱
    receiver = 'fortheapocalypse@hotmail.com'
 # 邮件标题
    subject = '自动打卡系统测试'
 # 邮件内容
    mail_msg = '打卡成功' + '\n'+ str(datetime)

 # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，html 设置文本格式为html格式  第三个 utf-8 设置编码
    message = MIMEText(mail_msg, 'plain', 'utf-8')  # 发送内容 （文本内容，发送格式，编码格式）
 # 发送地址
    message['From'] = sender
 # 接受地址
    message['To'] = receiver
 # 邮件标题
    message['Subject'] = Header(subject,'utf-8')
    
    print('123')
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtp_server)
        smtp.login(sender,password)
        smtp.sendmail(sender,receiver,message.as_string())
        print('success:邮件发送成功')
    except smtp.SMTPException:
        print('error:邮件发送失败')
    finally:
        smtp.quit()
        

if __name__ == '__main__':
   null=""
   url = 'http://jc.ncu.edu.cn/gate/student/getPreSignInfo'
   jsons = [{"code":"0","message":"success","data":{"id":"11422963","userId":"5106118051","signDate":"2021-10-29 20:41:54","inChina":"是","addressProvince":"江西省","addressCity":"南昌市","addressInfo":"南昌大学前湖校区","temperatureStatus":"正常","temperature":0.0,"isIll":"否","closeHb":"否","closeIll":"否","ip":"223.104.170.60","ipToAddress":"江西省-南昌市","isGraduate":"否","isIsolate":"否","isolatePlace":"无","healthStatus":"无异常","closeHbNew":null,"closeHrb":null,"closeBj":null,"closeJl":null,"closeOther":null,"closeGx":null,"closeBjSix":null,"closeOtherSix":null,"closeServen":null,"allowGetIn":"是"}}]
   tokens = ["eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJlY2hpc2FuIiwic3ViIjoiNTEwNjExODA1MSIsImlhdCI6MTYzNTUyMTY2NH0.T6xZDk4G1nufskRnZCD5pKDmH-ZywORafhYdsI30whlhXk8nVSKA4-ueImHRK2I2HBdu6uWCOMBX8drYk8yCsQ"]
   threads = []
   n = 0
   for js in jsons:
      t = Thread(target=request_h, args=(url,js,tokens[n]))
      n += 1
      t.start()
      threads.append(t)

   for t in threads:
      t.join()
