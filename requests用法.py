#import requests
#from bs4 import BeautifulSoup
#url = 'https://localprod.pandateacher.com/python-manuscript/crawler-html/spder-men0.0.html'
#res = requests.get (url)
#print(res.status_code)
#soup = BeautifulSoup(res.text,'html.parser')
#item = soup.find('div') #使用find()方法提取首个<div>元素，并放到变量item里。
#print(type(item)) #打印item的数据类型
#print(item)       #打印item


#import requests # 调用requests库
#from bs4 import BeautifulSoup # 调用BeautifulSoup库
#res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')# 返回一个Response对象，赋值给res
#html = res.text# 把Response对象的内容以字符串的形式返回
#soup = BeautifulSoup( html,'html.parser') # 把网页解析为BeautifulSoup对象
#items = soup.find_all(class_='books') # 通过匹配标签和属性提取我们想要的数据
#print(items) # 打印items
#for item in items:
#    print('想找的数据都包含在这里了：\n',item) # 打印item
#print(type(items)) #打印items的数据类型

import requests # 调用requests库
from bs4 import BeautifulSoup # 调用BeautifulSoup库
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
# 返回一个response对象，赋值给res
html = res.text
# 把res的内容以字符串的形式返回
soup = BeautifulSoup( html,'html.parser') 
# 把网页解析为BeautifulSoup对象
items = soup.find_all(class_='books') # 通过定位标签和属性提取我们想要的数据
for item in items:
    kind = item.find('h2') # 在列表中的每个元素里，匹配标签<h2>提取出数据
    title = item.find(class_='title') #在列表中的每个元素里，匹配属性class_='title'提取出数据
    brief = item.find(class_='info') #在列表中的每个元素里，匹配属性class_='info'提取出数据
    print(kind,'\n',title,'\n',brief) # 打印提取出的数据
    print(type(kind),type(title),type(brief)) # 打印提取出的数据类型
    print(kind.text,'\n',title.text,'\n',title['href'],'\n',brief.text)

import requests # 调用requests库
from bs4 import BeautifulSoup # 调用BeautifulSoup库
res = requests.get('https://wordpress-edu-3autumn.localprod.forc.work/all-about-the-future_04/')
# 返回一个response对象，赋值给res
html = res.text
# 把res的内容以字符串的形式返回
soup = BeautifulSoup( html,'html.parser') 
# 把网页解析为BeautifulSoup对象
items = soup.find_all(class_='comment-content') # 通过定位标签和属性提取我们想要的数据
for item in items:
    p1 = item.find('p') # 在列表中的每个元素里，匹配标签<h2>提取出数据
    print(type(p1)) # 打印提取出的数据类型
    print(p1.text,'\n')

