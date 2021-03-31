# write a program which can transter string to list every three character
# by using enumerate function 
#show your final list 


str="hello world " # 定義原始字串

list=[]
print("字串長度=",len(str)) 

if len(str)%3==0: #計算字串長度 去開二維串列空間 
    times=int(len(str)/3)
else:
    times=int(len(str)/3)+1 #如果有餘數 就直接在開一個空間 

for i in range(times): #開二維串列數
    list.append([])
i=0
count=1      #計數器 每3個字元 就換成下一個二維串列儲存
for index,data in enumerate(str): #enumerate函數 
    list[i].append(data) #加入 append 輸入字元 
    if count%3==0: 
       i+=1
    count+=1
        
print(list)# 輸出字串 
