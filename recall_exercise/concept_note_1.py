

#============================================================================== 
# 1  what is mean of    list[i]
#============================================================================== 
#二維陣列的列=i 


#============================================================================== 
# 2 what is mean of this code 
'''
 for j in range(0:3):
        list[i].append(eval(input("give me a number "))) 
''' 
#============================================================================== 
# 二維陣列的每一列 加上值 ＝給行值  
# [[1,2,3],[4,5,6]] should be vies as 立體 
#============================================================================== 

#============================================================================== 
# 3 要怎麼去產生2維list 的關鍵 
#==============================================================================  
'''
list=[]
for i in range(row_number):
    list.append([]) 
''' 

#==============================================================================  
#4  串列的複製 和一班變數的複製的差別 哪個是call by referance or call by value 
#==============================================================================  
# 一般list 是 call by referance       
# 變數是 call by value 

#==============================================================================  
# 5  list  shallow copy  和deep copy 的差別  
#==============================================================================  
# shallow copy equal to call by referance 
# deep copy equal to call by reference 

#==============================================================================  
#6 copy function 在什麼情況下deep 和shallow copy是同樣的結果
#==============================================================================  
# 如果list 中沒有list 的話 無論是deepcopy 和shallow copy 都會是call by referance  
#就是都是複製一個新的位址 
# 且如果只list 中lsit 的值  才會使用 call by reference 
#==============================================================================  
