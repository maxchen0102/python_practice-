
stock_price=dict(apple=128.10,ibm=145.22,google=2344.17,Tesla=670.94,intel=56.85,facebook=315.02,amazon=3270.54,HP=34.45
                 ,cisco=51.31, microsoft= 246.67, oracle =79.19) 

print(" for 迴圈") 
dict={}
for k,v  in stock_price.items():  
    if v>300: 
        dict[k]=v
print(dict )

print("字典生成式")
print({k for k,v in stock_price.items() if v>300})

    
print("=========================================================================")