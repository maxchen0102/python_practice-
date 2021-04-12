print("========")
#key view as function 所以要給引述值 range(len(s))
s = [2, 3, 1, 4, 9]
sorted_s = sorted(range(len(s)), key = lambda k : s[k]) 
print(sorted_s) #output:[2, 0, 1, 3, 4]


print("======")
#以元素第二個值去排序
listC = [('e', 4), ('o', 2), ('!', 5), ('v', 3), ('l', 1)]
print(sorted(listC,key=lambda x :x[1]))

print("=======")
player_1=['B1', 'B2', 'B3', 'B5', 'C10', 'C11', 'C12', 'C13', 'C2', 'C4', 'C5', 'C6', 'C7']

list=['B12323']
