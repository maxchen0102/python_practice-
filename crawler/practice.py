


import bs4 

web = """
<html><head><title>Hello World</title></head>
<body><h2>Test Header</h2>
<p>This is a test.</p>
<a id="link1" href="/my_link1">Link 1</a>
<a id="link2" href="/my_link2">Link 2</a>
<p>Hello, <b class="boldtext">Bold Text</b></p>
</body></html>
"""

data=bs4.BeautifulSoup(web ,"html.parser")

tag_a= data.find_all(["a",'b'])
title= data.find("title")

print(title )

for i in tag_a :
    print(i.get("id")) 
print("done")