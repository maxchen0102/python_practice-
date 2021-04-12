

print("======================")
#===========split by space 

word ="hello world "
list=word.split()
print(list)



print("======================")
#=======split by characerter 

word ="hello world "
list=word.split('o')  #以'o'為界 分成n等分
print(list)


print("======================")
#=======split後的元素之選擇  
#======切半後 只選後半部  前半部 [0 ]後半部[1]  倒數第一個為[-1]

word ="hello world "
list=word.split()[1]
print(list)


print("======================")
#=====split索引值 
# 以0開始遞增

word ="hello world "
list=word.split('o')[-1]
print(list)


print("======================")
#練習題：切割 出檔案名稱 "http://www.baidu.com/python/image/123456.jpg"


url="http://www.baidu.com/python/image/123456.jpg" 

image=url.split('/')[-1]
print(image)


print('==========')
#字串依照position切分
str = "hello world!"
splitat = 4
l, r = str[:splitat], str[splitat:]







