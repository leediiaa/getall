import requests, random, bs4,csv
csv_file=open('movie.csv','w',newline='',encoding='utf-8')
writer=csv.writerow(['序号','电影名','评分','推荐语','链接'])
for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    res = requests.get(url)
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    bs = bs.find('ol', class_="grid_view")
    for titles in bs.find_all('li'):
        num = titles.find('em',class_="").text
        title = titles.find('span', class_="title").text
        comment = titles.find('span',class_="rating_num").text
        url_movie = titles.find('a')['href']

        if titles.find('span',class_="inq") != None:
            tes = titles.find('span',class_="inq").text
            writer.writerow([num,title,comment,url_movie])
            print(num + '.' + title + '——' + comment + '\n' + '推荐语：' + tes +'\n' + url_movie)
        else:
            writer.writerow([num,title,comment,url_movie])
            print(num + '.' + title + '——' + comment + '\n' +'\n' + url_movie)
csv_file.close()
