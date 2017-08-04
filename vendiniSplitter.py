
import ssl
import pdfkit
from random import *
import os
import os.path
from bs4 import BeautifulSoup
import urllib.request
import pdfkit
import urllib

ssl._create_default_https_context = ssl._create_unverified_context



url = input('enter tickets url: ') #get url of tickets page from user then write the html to a var
with urllib.request.urlopen(url) as response:
   html = response.read()





soup = BeautifulSoup (html, 'html.parser') #make the soup

i = 0
num = 0

imgUrl =""

for img in soup.find_all('img'): #add path to ticketagent sit for images that had local paths


    if img['src'][0] != 'h' and img['src'][2] != 'w' :
                if  img['src'][2] != 't':
                        imgUrl = 'https://ticketagent.vendini.com' + img['src']
                        img['src'] = os.path.basename(img['src'])
                        if img['src'][0] == 'b' and img['src'][1] == 'a' and img['src'][2] == 'r':
                            img['src'] = str(num+1) +'.png'
                            num = num + 1
                        if img['src'][0] == 'i':
                            img['src'] = str(num+1) + '.png'
                            num = num + 1
                        print(imgUrl)
                        imgForSave = urllib.request.urlopen(imgUrl)
                        localFile = open(img['src'],'wb')
                        localFile.write(imgForSave.read())
                        localFile.close()

		# print(img['src'])



for p in soup.find_all('p'):
    if p['style'] == 'margin:0;padding:0;text-align:right;font-family:Verdana,Arial,Helvetica,sans-serif;font-size:9px;height:30px;':
        p['style'] = 'margin:0em;padding:0;text-align:center;font-family:Verdana,Arial,Helvetica,sans-serif;font-size:9px;height:30px;'



divs = soup.find_all("div", id="etickets") #write all divs with id etickets to var

options = {
    'orientation':'Landscape',
    'page-size': 'B7',
    'zoom': '6'

}

for each in divs: #write each div to a html file, then convert to pdf


    i = i + 1

    filename = 'page' + str(i) + '.html'
    filenamePdf = 'ticket' + str(i) + '.pdf'
    # print(filename)
    Html_file = open(filename,"w")
    Html_file.write('<!DOCTYPE HTML><html><head><meta charset="utf-8"></head>' + str(each) + '</html>')
    #pdfkit.from_file(filename, filenamePdf)


    Html_file.close()
    Html_file = open(filename,"r")
    tempSoup = BeautifulSoup (Html_file, 'html.parser') #make the soup
    # for img in tempSoup.find_all('img'):
    #     img['align'] = 'center'
    pdfkit.from_file( filename, filenamePdf, options=options)
