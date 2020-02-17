import gevent,time,requests
from gevent import monkey
monkey.patch_all()
#假设有1000个网址
start = time.time()
url_list = ['https://www.baidu.com/',
'https://www.sina.com.cn/',
'http://www.sohu.com/',
'https://www.qq.com/',
'https://www.163.com/',
'http://www.iqiyi.com/',
'https://www.tmall.com/',
'http://www.ifeng.com/'
……
]

def crawler(url_list):
#定义一个crawler()函数。
    for url in url_list:
        r = requests.get(url)
        print(url,time.time()-start,r.status_code)

tasks_list = [ ]
#创建空的任务列表。
for i in range(5):
    task = gevent.spawn(crawler,url_list[i*200:(i+1)*200])
    #用gevent.spawn()函数创建5个任务。
    tasks_list.append(task)
    #往任务列表添加任务。

gevent.joinall(tasks_list)
end = time.time()
print(end-start)
