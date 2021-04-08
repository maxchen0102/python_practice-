

#======== 加減運算==========

# normal function form 
def max(m,n):
    return m if m>n else n 
# print(max(3,2)) 

#lambada function form 
final_number= lambda m,n: m if m>n else n  # m,n are parameter  

print(final_number(5,1)) 

#==========相乘=====

multiple=lambda x,y: x*y  

a=multiple(5,5)
print(multiple(5,20))
print(a)

