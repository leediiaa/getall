import requests,random, csv,smtplib,schedule,time
from bs4 import BeautifulSoup
from urllib.request import quote
from email.mime.text import MIMEText
from email.header import Header


#movie=input('你想看什么电影？')
#gbkmovie = movie.encode('gbk')
#urlsearch = 'http://s.ygdy8.com/plus/so.php?typeid=1&keyword='+quote(gbkmovie)

account = input('请输入你的邮箱：')
password = input('请输入你的密码：')
receiver=input('请输入收件人的邮箱：')

def movies_book():
    csv_file=open('movieTop.csv', 'w', newline='',encoding='utf-8')
    writer = csv.writer(csv_file)
    for x in range(10):
        url = 'https://movie.douban.com/top250?start=&#39; + str(x*25) + '&filter='
        res = requests.get(url)
        bs = BeautifulSoup(res.text, 'html.parser')
        bs = bs.find('ol', class_="grid_view")
    for titles in bs.find_all('li'):
        title = titles.find('span', class_="title").text
        list1 = [title]
        writer.writerow(list1)
    csv_file.close()

def three_movies():
    csv_file=open('movieTop.csv','r',newline='',encoding='utf-8')
    csv_file.read()
    return movies,link



def send_email():
    qqmail.login(account,password)
    mailhost='smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost,25)
    message = MIMEText(content, 'plain', 'utf-8')
    subject = '电影链接'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print ('邮件发送成功')
    except:
        print ('邮件发送失败')
    qqmail.quit()
def job():
    print('开始一次任务')
    movies,link=three_movies()
    send_email(tem,weather)
    print('任务完成')

schedule.every().day.at("05:30").do(job) 
while True:
    schedule.run_pending()
    time.sleep(1)
