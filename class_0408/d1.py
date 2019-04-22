"""web自动化测试。

接口自动化测试实战。
1. 难，  ==> 没有写代码。敲一遍。 不是学知识的，编程是一门技能，一门手艺。不是知识。《刻意练习》，《程序员修炼之道》，万维钢《学习》
2. 想不到之前已经学到的知识。
3. 上课听得明白，写代码完全不会。
4. 简历上似乎没有什么新东西可以写。 = 》 搭建了公司的自动化测试框架， python unittest
requests 接口测试。 -- 你踩过的坑越多，你简历上可以写的东西就越多。
5. 明明白白的抛出了异常，我们不知道出现了什么问题。

调试自己动代码。报错了代码。
1. 哪一行出现了错误。
2. 分析哪一行，哪个函数，使用错了啊，第三库api，数据类型不一致。语法错误。
3. 百度具体用法。selenium 原理，requests,get()，官方文档，源码。源码是我推荐的最有用的方式。


1. 多写代码，而不是多看。
2. 怎么解决问题。


web 自动化测试
手     浏览器（内容）  1. 数据是否正确， 2. 兼容性，3.交互过程

接口测试

2. 做了接口测试，为什么还要做 web 测试？ ==》 工作的目的。
bug 快速定位。  接口测试 ==》 后端接口设计问题  ==》 {'msg':'服务器挂了'}
web测试/app测试  ==》 前端 ==》 可以显示服务器挂了吗？ 不能这样的。“服务器正在升级”


1. 看到的网页内容 ==》 对应的就是一个 HTML 的文档。
2. 怎么样去判断返回内容的某一部分是否符合我们的预期。



"""

import requests
# res = requests.get('https://api.github.com')
# # header = {'user-agent'}
# print(res.text)

res = requests.get('http://localhost:5000/login')
print(res.text)

# login success
# 1. 正则表达式匹配
# 2. json ==> dict(json),  mydict["msg"]， 看起来，找起来，效率更高，更灵活，更好看

# 1.字符串  ==> find, 正则匹配

# 3. HTML ==> find, 正则匹配。 ==》 解析很多内容，效率就很成问题。
# HTML  ==> HTML 解析

# 接口 ==> 适配两种不同的实物，进行数据传输。
# 接口测试： python  =requests+接口=  后端代码
# python  =selenium + webdriver（浏览器驱动）(接口）=  浏览器（HTML）（webdriver提供了接口）


# 为什么要安装 selenium, driver

# HTML
# 手工  不认识浏览器  -  翻译器。中介 -  浏览器（谷歌，firefox, IE）
# selenium ==》 安装 selenium python 库  pip install selenium
# 安装 webdriver ==> webdriver(Chrome, firefox, IE),兼容性测试
# 驱动版本要和浏览器版本对应。
# 1. 对应的浏览器，2. 对应的浏览器版本， 3.chromedriver.exe 放到 python安装的根目录下面。

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://www.baidu.com')
# json ==> dict
# python (数据结构，数据类型，dict,类和对象，函数) 转化==>   浏览器（HTML）
















