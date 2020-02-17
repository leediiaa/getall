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
    name = item.find('h3').find('a') 
    point=item.find('p')
    price=item.find(class_='price_color')
    print(name.text,point['class'],price.text)
