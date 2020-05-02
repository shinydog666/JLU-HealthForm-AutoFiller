@echo off
cd %~dp0
echo "正在安装服务..."
sc create JLUHealthFormAutoFiller binpath=%~dp0main.exe start=auto
sc description JLUHealthFormAutoFiller "吉林大学健康填报自动填表程序服务"