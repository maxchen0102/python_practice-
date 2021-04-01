#一些python技巧練習 題目=======下的註解


#============
#建立一個for loop 和enumerate loop 去show出一個字串 "hello world  "並以空白為分割

'''
str="hello wolrd"
length=len(str)

listB=[]
for i in range(int(length/3)):
    listB.append(str[i*3:i*3+3])
print(listB)


'''
'''

str="hello wolrd"

listB=[]
listA=[]
print("====")
i=1
for index ,data in enumerate(str):
    print(index)
    listB.append(data)
    if i%3==0:
        print("====")
        print(listB)
        listA.append(listB) 
        print(listA)
        listB.clear()
        print(listB)
        i=0 
    i+=1
print("======")
print(listA)


'''
str="hello world "

list=[]
print("字串長度=",len(str))

if len(str)%3==0:
    times=int(len(str)/3)
else:
    times=int(len(str)/3)+1

for i in range(times):
    list.append([])
i=0
count=1
for index,data in enumerate(str):
    list[i].append(data)
    if count%3==0:
       i+=1
    count+=1
        
print(list)
