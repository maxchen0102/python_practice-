

from collections import defaultdict
from typing import OrderedDict 


''' 
wd = "initially"

df= defaultdict(int )
 
for key in wd : 
    df[key ]+=1 
print(list(df.items()))
''' 


'''
rdt= OrderedDict()
rdt[1]='one' 
rdt[2]='two'
rdt[3]='three' 
print(rdt)
''' 

'''
st1={23,24,26} 
st2={23,24,33,45 } 

print(st1 |st2 ) 
print(st1 -st2 )
print(st2-st1)
print(st1&st2)
print(st1^st2)

''' 

total=['hellow','gg']#全部人的名單 
#total 為宇集 

print({len(item) for item in total }) 

st1=set([1,2,3,4]) 
st2=set([5,6,7,8])

print(st1-st2)



