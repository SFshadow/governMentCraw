#先爬取a标签里面的js
from bs4 import BeautifulSoup
import csv


# 记录第一次字符出现的位置
def getStrInfo1(str, target):
    count = 0
    for index, value in enumerate(str):
        if target == value:  return count
        count += 1

#读取html
page=input("循环次数：")

for p in range(int(page)):
    p=p+1;
    path = f'js{p}.html'
    htmlfile = open(path, 'r', encoding='utf-8')
    htmlhandle = htmlfile.read()
    soup = BeautifulSoup(htmlhandle, "html.parser")
    res=soup.find_all('cell')
    file = open(f"demo{p}.csv", mode="w", newline="",
                encoding="utf-8")  # 创建一个demo的csv文件，模式是write，编码是utf-8,newline的作用是两行不会空的太多
    w = csv.writer(file)  # 将file加入到writer函数中，生成一个写入工具

    count=1
    total=0
    rate=100
    if(p==page):rate=input("请输入最后一页的条数：")
    rate=int(rate)



    for r in res:


        string = str(res[count])
        print(string)
        first=getStrInfo1(string,"'")+1
        last=getStrInfo1(string,",")-1
        w.writerow([string[int(first):int(last)]])
        count+=23
        total+=1
        # if count  == (15*(rate-1)+1):break
        if total  == rate:break

    file.close()
    print(total)