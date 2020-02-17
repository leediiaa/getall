import requests,bs4
from urllib.request import quote
#quote()函数，可以帮我们把内容转为标准的url格式，作为网址的一部分打开
a=input('请输入你想要下载的电影名：')
url='http://s.ygdy8.com/plus/so.php?typeid=1&keyword='+quote(a.encode('gbk'))
res=requests.get(url)
bs=bs4.BeautifulSoup(res.text,'html.parser')
bs=bs.find('div',class_="co_content8")
bs=bs.find('td').find('a')['href']
url='https://www.ygdy8.com/'+bs
res=requests.get(url)
bt=bs4.BeautifulSoup(res.text,'html.parser')
bt=bt.find('div',class_="co_content8").find('table').find('a')['href']
print(bt)

