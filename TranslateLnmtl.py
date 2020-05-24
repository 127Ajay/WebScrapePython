import requests
from bs4 import BeautifulSoup as soup
from textblob import TextBlob
import time
import random

#Declare the file we want to store to
f1= open("super_magic_god_of_harry_potter41.txt","w+",encoding="utf-8")

myUrl = 'http://lnmtl.com/chapter/super-magic-god-of-harry-potter-chapter-'

for page in range(41,795):
    #traverse the Site
    print(page)
    srhUrl =  myUrl + str(page) + "/"
    uClient =  requests.get(srhUrl)
    uClient.encoding = "utf-8"
    html_content = soup(uClient.content, 'html.parser')

    Body = html_content.findAll("div",{"class":'chapter-body'})

    OrgBody = Body[0].findAll("sentence",{"class":'original'})
    count = 0
    for orgdiv in OrgBody:
        temp  = orgdiv.text
        temp = temp.replace("\t", "").replace("\r", "").replace("\n", "")
        temp = temp.replace("„","\"").replace("”","\"")
        blob = TextBlob(temp)
        try:
            x = blob.translate(to='en')
        except Exception as e:
            print(e)
            x = blob
        print(x)
        if count == 0:
            f1.write(str(x))
            f1.write("\n")
            count += 1
        else:
            f1.write(str(x))
        f1.write("\n")

    f1.write("\n\n")
    print("Completed page")

    num = random.randint(5, 8)

    time.sleep(num)

f1.close()