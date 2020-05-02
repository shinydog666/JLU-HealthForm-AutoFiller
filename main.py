"""

https://ehall.jlu.edu.cn/infoplus/form/JLDX_BK_XNYQSB/start

"""
import configparser
import datetime



# in macOS or Linux, use this.
import time
from tkinter import messagebox
# in Windows, use this.
# import win32api,win32con


# in macOS or Linux, use this.
#messagebox.showinfo("Test", "sss")
# in Windows, use this.
# win32api.MessageBox(0, "这是一个测试提醒OK消息框", "提醒",win32con.MB_OK)
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
print("读取配置文件")
cfg = configparser.ConfigParser()
cfg.read("config.ini", encoding="utf-8")
uName = cfg.get("common", "userName")
uPwd = cfg.get("common", "passWord")
rTimeS = cfg.get("common", "time")
rTimeS = str(datetime.datetime.now().date())+" "+rTimeS+":00"
diff = int(cfg.get("common","diff"))
print("配置内容：")
for i in cfg.sections():
    for j in cfg.items(i):
        print(j[0]+": "+j[1])

# 开始程序主逻辑
while(True):
    if not (int(getDiff(rTimeS)) <= diff):
        print("时候未到，休息1小时")
        time.sleep(1*60*60)
        break






