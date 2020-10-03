import configparser
import datetime
import MessageSender

m = MessageSender.MessageSender("Bark")
import time
# in macOS or Linux, use this.
from tkinter import messagebox

import logging

l = logging.getLogger(__name__)

from selenium import webdriver

# in Windows, use these.
# from win32api import MessageBox
# from win32con import MB_OK

# in macOS or Linux, use this.
messagebox.showinfo("警告", "本程序由ForeverOpp制作，一切后果本人概不负责。https://github.com/ForeverOpp")
# in Windows, use this.
# MessageBox(0, "本程序由ForeverOpp制作，一切后果本人概不负责。https://github.com/ForeverOpp", "警告", MB_OK)

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
rTimeS = cfg.get("common", "time")
rTimeS = str(datetime.datetime.now().date()) + " " + rTimeS + ":00"
diff = int(cfg.get("common", "diff"))
apiKey = cfg.get("common", "apiKey")
method = cfg.get("common", "method")
methodKey = cfg.get("program", method.lower())
title = cfg.get("common", "title")
content = cfg.get("common", "content")
timeout = int(cfg.get("common", "timeout"))
chromeDriver = cfg.get("common", "chromeDriver")
sTimes = int(cfg.get("program", "sTimes"))
initFlag = bool(cfg.get("program", "initFlag"))
# 获取用户列表
uList = cfg.items("userlist")
waitT = timeout
# 生成用户配置
for i in uList:
    print(i[0])
    try:
        cfg.add_section(i[0])
    except configparser.DuplicateSectionError:
        pass
    cfg.set(i[0], "sTime", datetime.datetime.now().date().__str__())
    cfg.set(i[0], "sTimes", "0")

with open("config.ini", "w+") as f:
    cfg.write(f)

l.info("配置内容：")
for i in cfg.sections():
    for j in cfg.items(i):
        l.info(j[0] + ": " + j[1])

# 配置推送服务
m.setMethod(method)
m.config({methodKey: apiKey})

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


def fillForm(uName, uPwd):
    global waitT, cfg, l
    try:
        # 配置浏览器
        b = webdriver.Chrome(executable_path=chromeDriver)
        b.minimize_window()
        b.get("https://ehall.jlu.edu.cn/infoplus/form/JLDX_BK_XNYQSB/start")
        b.find_element_by_id("username").send_keys(uName)
        b.find_element_by_id("password").send_keys(uPwd)
        b.find_element_by_id("login-submit").click()
        b.implicitly_wait(timeout)
        b.find_element_by_name("fieldCNS").click()
        b.implicitly_wait(timeout)
        b.find_element_by_xpath("/html/body/div[4]/form/div/div[1]/div[2]/ul/li[1]/a").click()
        b.implicitly_wait(timeout)
        b.find_element_by_css_selector("button.dialog_button.default.fr").click()
        b.implicitly_wait(timeout)
        # 等待动画加载完成
        time.sleep(2)
        b.find_element_by_css_selector("button.dialog_button.default.fr").click()
        b.implicitly_wait(timeout)
        # 等待读条
        time.sleep(5)
        if str(b.find_element_by_xpath("/html/body/div[4]/form/div/div[1]/div[1]/div[2]/nobr").text).find("已完成"):
            l.warning("已完成！")
            l.warning(
                m.send({"title": title, "content": content + " [" + datetime.datetime.now().date().__str__() + "]"}))
            cfg.set("program", "sTimes", str(++sTimes))
            # 成功后重置等待时间
            waitT = timeout
            b.quit()
            return False
        return True
    except:
        l.error("页面加载出错，休息%d秒重试" % waitT)
        # 休息时间每失败一次递增10秒钟，最长不超过5分钟
        if waitT>=300+timeout:
            waitT = timeout
        time.sleep(waitT)
        waitT += 10
        m.send({"title": "啊哦", "content": "出错了呢~" + " [" + datetime.datetime.now().date().__str__() + "]"})
        # 我知道这里会出问题，但是连ChromeDriver都没配置好还运行个p
        b.quit()
        return True


# 开始程序主逻辑
while True:
    if int(getDiff(rTimeS)) > diff:
        l.warning("时候未到，休息" + str(diff / 2 / 60) + "小时。")
        time.sleep(diff / 2 * 60)
        continue
    for i in uList:
        while fillForm(i[0], i[1]):
            pass

