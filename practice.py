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
listB=[]
listC=[]

for i in range(len(str)):
    list.append([])

for index,data in enumerate(str):
    list[0].append(data)
print(list)
