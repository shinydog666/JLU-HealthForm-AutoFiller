@echo off
cd %~dp0
rd /s /q build
rd /s /q dist
del *.spec
pyinstaller -i ./fav.ico -w -F main.py --onefile
xcopy /y dist\*.exe .
rd /s /q build
rd /s /q dist
del *.spec