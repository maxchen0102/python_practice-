


word='''<html><body><h1>Of course NIU CSIE is the best</h1></body></html>'''


word_1=word.split(sep="<h1>")
word_2=word_1[1].split(sep="</h1>") 
word_3=word_2[0]

print(word_3)

print(word_3[word_3.index('best'):word_3.index('best')+4:])

print(word_3[word_3.index('NIU CS'):word_3.index('NIU CS')+6])


print(word_3[word_3.index('o'):word_3.index('t')+1:3])



#==================== 

#用index取出字元位址 然後用字串的方式直接去設定前後取出的位址 然後印出 
# 

