import csv
csv_file=open('demo.csv','w',newline='',encoding='utf-8')
cfile=csv.writer(csv_file)
csv_file.close()


csv_file=open('demo.csv','r',newline='',encoding='utf-8')
reader=csv.reader(csv_file)
for row in reader:
    print(row)


#https://yiyibooks.cn/xx/python_352/library/csv.html#module-csv csv官方文档
