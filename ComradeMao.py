import os
import requests
from bs4 import BeautifulSoup as soup
import language_check
import time
import random

tool = language_check.LanguageTool('en-US')
#Declare the file we want to store to

def WebScrape( myUrl, fileName, startPage, endPage):

    if os.path.exists(fileName):
        print("Append TO existing file")
        f= open(fileName,"a+",encoding="utf-8")
    else:
        print("Create new file")
        f= open(fileName,"w+",encoding="utf-8")
    #myUrl = 'https://comrademao.com/mtl/all-attributes-martial-path/all-attributes-martial-path-chapter-'

    for page in range(startPage, endPage):
        #traverse the Site
        print(page)
        srhUrl =  myUrl + str(page) + "/"
        try:
            uClient =  requests.get(srhUrl)
            uClient.encoding = "utf-8"
            html_content = soup(uClient.content, 'html.parser')

            Body = html_content.findAll("article",{"class":'status-publish'})

            translatedBody = Body[0].findAll("p")
            transaltedText = translatedBody[0].find_all("p",class_=False)
            count = 0
            for transdiv in transaltedText:
                temp  = transdiv.text
                temp = temp.replace("\t", "").replace("\r", "").replace("\n", "")
                temp = temp.replace("„","\"").replace("”","\"").replace("“","\"").replace("”","\"")
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
            print("Completed page")
        except:
            continue
        num = random.randint(5, 8)

        time.sleep(num)

    f.close()


if __name__ == '__main__':
        srtPage = 201
        endPage = 593
        fileName = "all_attributes_martial_path.txt"
        myUrl = 'https://comrademao.com/mtl/all-attributes-martial-path/all-attributes-martial-path-chapter-'
        WebScrape(myUrl, fileName, srtPage, endPage)
        
