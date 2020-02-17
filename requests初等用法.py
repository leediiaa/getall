#import requests
#res=requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
#print(type(res))
#print(res.status_code)
#print(res.content)
#novel=res.text
#print(novel[:800])



#import requests
#res = requests.get('https://res.pandateacher.com/2018-12-18-10-43-07.png')
#发出请求，并把返回的结果放在变量res中
#pic=res.content
#把Reponse对象的内容以二进制数据的形式返回
#photo = open('ppt.jpg','wb')
#新建了一个文件ppt.jpg，这里的文件没加路径，它会被保存在程序运行的当前目录下。
#图片内容需要以二进制wb读写。你在学习open()函数时接触过它。
#photo.write(pic) 
#获取pic的二进制内容
#photo.close()
#关闭文件


#import requests
#引用requests库
#res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
#下载《三国演义》第一回，我们得到一个对象，它被命名为res
#novel=res.text
#把Response对象的内容以字符串的形式返回
#k = open('《三国演义》.txt','a+')
#创建一个名为《三国演义》的txt文档，指针放在文件末尾，追加内容
#k.write(novel)
#写进文件中     
#k.close()
#关闭文档


#import requests
#res=requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/exercise/HTTP%E5%93%8D%E5%BA%94%E7%8A%B6%E6%80%81%E7%A0%81.md')
#novel=res.text
#n=open("novel.txt","a+")
#n.write(novel)
#n.close()

#import requests
#res=requests.get('https://res.pandateacher.com/2019-01-12-15-29-33.png')
#pic=res.content
#n=open("pic.jpg","wb")
#n.write(pic)
#n.close()

import requests
res=requests.get('https://static.pandateacher.com/Over%20The%20Rainbow.mp3')
mic=res.content
n=open("mic.mp3","wb")
n.write(mic)
n.close()
