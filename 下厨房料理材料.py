import requests
from bs4 import BeautifulSoup
res_foods = requests.get('http://www.xiachufang.com/explore/')
bs_foods = BeautifulSoup(res_foods.text,'html.parser')
tag_name = bs_foods.find_all('p',class_='name')
tag_ingredients = bs_foods.find_all('p',class_='ing ellipsis')
list_all = []
for x in range(len(tag_name)):
    list_food = [tag_name[x].text[18:-14],tag_name[x].find('a')['href'],tag_ingredients[x].text[1:-1]]
    # 提取信息，封装为列表。注意此处[18:-14]切片和之前不同，是因为此处使用的是<p>标签，而之前是<a>
    list_all.append(list_food)
print(list_all)
