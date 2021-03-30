

#============
#建立一個for loop 和enumerate loop 去show出一個字串 "hello world  "並以空白為分割

 '''
str="hello wolrd"
list=list(str.split(' '))

print(list)

i=0
for x in list:
    print(i,x)
    i+=1
print("====")
for index ,data in enumerate(list):
    print(index ,data)
'''


