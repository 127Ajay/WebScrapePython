from multiprocessing import Process
import requests
from bs4 import BeautifulSoup as soup
import language_check
import time
import random

tool = language_check.LanguageTool('en-US')
#Declare the file we want to store to

def WebScrape(startPage, endPage):
    fileName = 'super_magic_god_of_harry_potter_langCheck'+ str(startPage) + '_' + str(endPage) +'.txt'
    f= open(fileName,"w+",encoding="utf-8")

    myUrl = 'http://lnmtl.com/chapter/super-magic-god-of-harry-potter-chapter-'


    for page in range(startPage, endPage):
        #traverse the Site
        print(page)
        srhUrl =  myUrl + str(page) + "/"
        uClient =  requests.get(srhUrl)
        uClient.encoding = "utf-8"
        html_content = soup(uClient.content, 'html.parser')

        Body = html_content.findAll("div",{"class":'chapter-body'})

        translatedBody = Body[0].findAll("sentence",{"class":'translated'})
        count = 0
        for transdiv in translatedBody:
            temp  = transdiv.text
            temp = temp.replace("\t", "").replace("\r", "").replace("\n", "")
            temp = temp.replace("„","\"").replace("”","\"")
            matches = tool.check(temp)
            #print(len(matches))
            if(len(matches) > 0):
                temp = language_check.correct(temp, matches)
            #print(temp)
            if count == 0:
                f.write(temp)
                f.write("\n")
                count += 1
            else:
                f.write(temp)
            f.write("\n")


        f.write("\n\n")
        # f1.write("\n\n")
        print("Completed page")

        num = random.randint(5, 8)

        time.sleep(num)

    f.close()


if __name__ == '__main__':
    proc = []
    i=1
    while i < 796:
        srtPage = 0
        endPage = 0
        if i > 750:
            srtPage = i
            endPage = i + 45
        else:
            srtPage = i
            endPage = i + 50
        print(str(srtPage) + '-' + str(endPage))
        p = Process(target=WebScrape, args=(srtPage,endPage))       
        proc.append(p)
        i += 50 
        
    for p in proc: 
        print(p)
        p.start()
        p.join()
