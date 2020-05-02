"""

https://ehall.jlu.edu.cn/infoplus/form/JLDX_BK_XNYQSB/start

"""
import configparser
from tkinter import messagebox
# import win32api,win32con
messagebox.showinfo("Test","sss")
# win32api.MessageBox(0, "这是一个测试提醒OK消息框", "提醒",win32con.MB_OK)
cfg = configparser.ConfigParser()
cfg.read("config.ini", encoding="utf-8")

