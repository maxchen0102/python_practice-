
# 抓資料
import numpy as np 
import bs4 
import urllib.request as req 



def getData(url):
    print("=======================")
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15"
    })
    with req.urlopen(request) as response: # using with to open this page 
        data=response.read().decode("utf-8")  # decode this page by utf-8 then store in data 
    #print(data)
    # 解析資料 

    root=bs4.BeautifulSoup(data,"html.parser")  # using beautiful to parser html file then store in root 
   
    titles=root.find_all("div",class_="title")  
    
    for i in titles: 
        print(i.find('a').get("href"))

    
    for title in titles: 
        if title.a!=None:
            print(title)
            print(title.a.string) #  title is under tag a  and unser tag title 
    nextlink=root.find('a',string="‹ 上頁")
    
    return nextlink["href"]

url="https://www.ptt.cc/bbs/studyabroad/index.html"    
count=0 
while(count<1):
    url="http://www.ptt.cc"+getData(url)
    count+=1 
    
    print("===========================")
    