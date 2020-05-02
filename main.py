"""

https://ehall.jlu.edu.cn/infoplus/form/JLDX_BK_XNYQSB/start

"""
import configparser
import datetime

import MessageSender
m = MessageSender.MessageSender("Bark")


# in macOS or Linux, use this.
import time
from tkinter import messagebox
import logging
l = logging.getLogger(__name__)

from selenium import webdriver
# in Windows, use this.
import win32api,win32con



# in macOS or Linux, use this.
#messagebox.showinfo("Test", "sss")
# in Windows, use this.
win32api.MessageBox(0, "这是一个测试提醒OK消息框", "提醒",win32con.MB_OK)
"""

自定义函数区

"""
def getDiff(rTimeS):
    rTime = datetime.datetime.strptime(rTimeS, "%Y-%m-%d %H:%M:%S")
    nTime = datetime.datetime.now()
    if rTime > nTime:
        result = (rTime - nTime).seconds / 60
    else:
        result = (nTime - rTime).seconds / 60
    return result




"""

主程序区

"""
# 初始化

# 配置日志输出
l.setLevel(level=logging.INFO)
handler = logging.FileHandler("log.txt", encoding='utf-8')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s, [%(levelname)s]: %(message)s')
handler.setFormatter(formatter)
l.addHandler(handler)

# 读取配置文件
l.info("读取配置文件")
cfg = configparser.ConfigParser()
cfg.read("config.ini", encoding="utf-8")
uName = cfg.get("common", "userName")
uPwd = cfg.get("common", "passWord")
rTimeS = cfg.get("common", "time")
rTimeS = str(datetime.datetime.now().date()) + " " + rTimeS + ":00"
diff = int(cfg.get("common", "diff"))
apiKey = cfg.get("common", "apiKey")
method = cfg.get("common", "method")
methodKey = cfg.get("program", method.lower())
title = cfg.get("common", "title")
content = cfg.get("common", "content")
#m.send({"title": title, "content": content})

l.info("配置内容：")
for i in cfg.sections():
    for j in cfg.items(i):
        l.info(j[0] + ": " + j[1])

# 配置推送服务
m.setMethod(method)
m.config({methodKey: apiKey})












# 开始程序主逻辑
while(True):
    if not (int(getDiff(rTimeS)) <= diff):
        l.warning("时候未到，休息1小时")
        time.sleep(1*60*60)
        break
    m.send({"title": title, "content": content + " [" + datetime.datetime.now().date().__str__() + "]"})





