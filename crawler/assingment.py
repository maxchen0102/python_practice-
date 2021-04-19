#載入模組 

import requests
import bs4 
import csv

import time 
import datetime #載入python基本的日期和時間類型的模組

#datetime.timedelta物件代表兩個時間之間的時間差，並將兩個date物件相減

time1 = datetime.timedelta(days = 1)
today = datetime.date.today() #透過此函式取得當天的日期
yesterday = today - time1
time_yesterday = yesterday.strftime("%m/%d")
time_today = today.strftime("%m/%d")#用strftime()方法, 將datetime及date轉成字串.


#這邊使用payload 去向server傳送請求 並且使用headers 讓我們在抓取資料的時候不要被系統發現是用程式去抓的

#可以看到表單是以POST的形式傳送，確認預設的值是'yes'，
#所以接下來我們要帶著建立的session，以POST的方式帶著參數登入，再用cookie以GET的方式帶著參數進入主頁。

payload = {"from": "https://www.ptt.cc/bbs/Gossiping/index.html","yes": "yes"} 
my_headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63"}
rs = requests.Session() 
rs.post("https://www.ptt.cc/ask/over18", data = payload, headers = my_headers) 


#起始頁面網址為11/14和11/15日間的那個頁面(會往前開始抓)
url="https://www.ptt.cc/bbs/Gossiping/index38820.html" 


#取出每個文章的資料  

link = [] #建立link[]串列 去儲存所抓出來的網址


def get_date(url): 
    response = rs.get(url, headers=my_headers)
    soup = bs4.BeautifulSoup(response.text, "html.parser")           #透過BeautifulSoup並用"html.parser"去解析此網站
    titles = soup.find_all("div", class_ = "title")          #抓取連結
    date = soup.find("div", class_="date").text             #抓取日期
    print("anothor")  
    for i in titles:                         #用title當文章數量的計數器 去一一檢視日期 
        if date == "11/14":                   #檢索我們所要抓取的日期 如果符合 就此篇文章的連接 放進link串列中 讓我們之後去做排序
            if(i.a):                           #使用.a是避免已經被刪除的文章
                link.append("https://www.ptt.cc/" + i.find("a").get("href"))
    
    nextlink_2=soup.select('div.btn-group > a')           # 由籤div.btn.group 到標籤a 
    up_page_href = nextlink_2[3]['href'] #在標籤div.btn.group下[0]是看板連結 [1]是精華區連結[2]是最舊[3]是上頁[4]是下頁[5]是最新
    return  up_page_href  #回傳上一頁的網址 讓遞迴成功
    
  

page =100 #設定要往後抓取的頁數 


for i in range(1,page):
    url = "https://www.ptt.cc/"+get_date(url)  #設定一個遞迴 去把上一頁的網址再丟入函式中 去抓取


push = [] #設定一個push的串列 去儲存蓋樓數

score = [[0 for j in range(2)] for k in range(3000)] #設定一個雙重陣列去儲存排序的網址和蓋樓數 方便去比對
for j in range(len(link)):  #把迴圈的range設定成我們擁有的網址的數量  
    response = rs.get(str(link[j]), headers = my_headers)
    soup = bs4.BeautifulSoup(response.text, "html.parser") #再做一次網頁的解析
    push = soup.find_all("div", class_ = "push") #把蓋樓的數量存到變數push中
    
    score[j][0] = len(push) #取出蓋樓數量 並存入score list的0位置
    score[j][1] = link[j] #把link存入score list的1位置
    score.sort(key=lambda x:x[0], reverse =True) #使用python的串列排序的函式sort    

  
    

with open("C:/Users/acer_PC/Desktop/python_crawler/text20.csv", "a", newline="", encoding='utf-8-sig')as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['爬取時間',"作者:", "標題", "時間", "內文", "IP位址"])
    
    for n in range(10): #用迴圈印出抓取之前10個推需文數最多的文章
        response = rs.get(score[n][1], headers = my_headers)
        soup = bs4.BeautifulSoup (response.text, "html.parser") #再對網站做一次解析
        header = soup.find_all("span", "article-meta-value") 

        author = header[0].text #存入作者  這邊分別使用header[]是因為他分別存在article-meta-value下 
        title = header[2].text #存入標題
        date = header[3].text #存入日期

        main_container = soup.find(id = "main-container",) #抓出內文
        content = main_container.text.replace("\u6ca1", "  ") 
       
        ip1 = soup.find(id = "main-container") 
        ip2 = ip1.text.split("※ 發信站: 批踢踢實業坊(ptt.cc), 來自:")[1]  #使用字串分割split
        ip = ip2.split("※ 文章網址:")[0]#[0]=false代表此字串後面的不留,[1]代表留下
        
        all_content = content
        pre_content = all_content.split("--")[0]
        texts = pre_content.split('\n')
        contents = texts[2:]
        final_contents = "\n".join(contents)

        writer.writerow([time_today,author, title, date,final_contents, ip]) #寫入csv檔





print("OK")
    


