# 吉林大学健康填报自动填表程序
## 声明：
  1. 本程序不应用于任何非吉林大学允许的行为，本程序不会对填报内容做任何修改，仅确认已填好的表格内容并发送。
  2. 使用者应对自己的填报内容进行负责，本程序仅辅助实现填报，对于使用本程序造成的一切后果本人不予负责。  
## 使用方法
  1. 修改config.ini中的userName和passWord字段，其中username为用户名，即去掉@mails.jlu.edu.cn后的邮箱名；
  password为密码。
  2. 右键管理员运行install.bat即可开机启动，如果不想开机启动也可以直接运行程序。
  3. 如果需要自定义浏览器位置，请修改b = webdriver.Chrome()一行，改为Chrome
  4. 请在[这里](http://npm.taobao.org/mirrors/chromedriver/) 下载对应浏览器版本的ChromeDriver，放到Python安装目录下（Python目录一般已经加入
  到Path变量中，这里是为了方便，如果需要放到其它目录请将对应目录加入Path变量）。
  
## 已知问题
  1. 闰年、闰月的时候可能会出问题，就像今年各大软件出现的问题一样。
