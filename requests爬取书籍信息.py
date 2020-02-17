import requests # 调用requests库
from bs4 import BeautifulSoup # 调用BeautifulSoup库
res = requests.get('http://books.toscrape.com/')
# 返回一个response对象，赋值给res
html = res.text
# 把res的内容以字符串的形式返回
soup = BeautifulSoup( html,'html.parser') 
# 把网页解析为BeautifulSoup对象
items = soup.find_all(class_='nav nav-list') # 通过定位标签和属性提取我们想要的数据
for item in items:
    p1 = item.find('li') # 在列表中的每个元素里，匹配标签<h2>提取出数据
    print(type(p1)) # 打印提取出的数据类型
    print(p1.text,'\n')

import requests # 调用requests库
from bs4 import BeautifulSoup # 调用BeautifulSoup库
res = requests.get('http://books.toscrape.com/catalogue/category/books/travel_2/index.html')
# 返回一个response对象，赋值给res
html = res.text
# 把res的内容以字符串的形式返回
soup = BeautifulSoup( html,'html.parser') 
# 把网页解析为BeautifulSoup对象
items = soup.find_all(class_='product_pod') # 通过定位标签和属性提取我们想要的数据
for item in items:
    name2 = item.find('h3') # 在列表中的每个元素里，匹配标签<h2>提取出数据
    name=name2.find('a')
    point1=item.find('p')
    point=point1.find(p['class'])
    price=item.find('product_price').find('price_color')
    print(type(name)) # 打印提取出的数据类型
    print(name.text,' ',point,' ',price.text,'\n')


