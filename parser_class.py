import urllib.request
import urllib
import os
from html.parser import HTMLParser

import time

start_time = time.ctime()

class DoubanHtmlParser(HTMLParser):
    url = []
    def handle_starttag(self,tag,attrs):
             
        if tag =='img':
            
            for name,value in attrs:
                
                if name =='src':
                    self.url.append(str(value))





class DoubanImageParser(DoubanHtmlParser):

    url=[]
    web_url=[]
    new_url=[]
    image_name=[]
    
    
    
    def __init__(self,album,path = "D:/Photos"):
        
        self.album=album
         
        self.get_photo_info()
        print('finished...')
        


    def get_photo_info(self):
        '''
            generate urls for each page
            



        '''
        online_number = self.album.split('/')[4]
        album_number = self.album.split('/')[6]
        self.home_album ="http://www.douban.com/online/"+online_number
        
        t= urllib.request.urlopen(self.home_album).read().decode('utf8')

        s_tart = t.find(">全部")+3
        e_nd  = t.find("张")
        total_photos = t[s_tart:e_nd]
        print("the amount of photos are: ",total_photos)
        pages = int(int(total_photos)/30+1)
        print("total pages are : ", pages)
        start=0
        end = (pages-1)*30
        
 
        
        
        while start <=end:
            n=start
            self.web_url.append(self.album+"?start="+str(n))
            
    
            start=start+30
        print(' all urls are reday to be used -and stored in \'web_url\' -------\n')
# ----------get pics--------------------------------------

        for r in DoubanImageParser.web_url:
            page = urllib.request.urlopen(r)
            text=page.read().decode("utf8")
            myparser.feed(text)
        print('parser finished------\n')
        
        k=0
        url = [ii for ii in DoubanHtmlParser.url if len(ii)==61]
        print('start print image urls .............')
        for i in url:
            k=k+1
            print(k,':',"http://img3.douban.com/view/photo/photo/public/p"+i[-13:-4]+'.jpg')

            self.get_image_name('http://www.douban.com/online/10776262/photo/'+i[-13:-4])
        print(start_time,'-----',time.ctime())

# ------------------------------------------------


    
    def get_image_name(self,image_url):
        page = urllib.request.urlopen(image_url)
        text=page.read().decode("utf8")
        j=-1
   
        for i in text:
            j=j+1
            if i == '自':
                break

        p=0
        for k in text[j:]:
            p+=1    
            if k =='上':

                break

        image_name = self.image_name.append(text[j+1:p+j-1])
        print(image_name,'++++++++++++++++++++')






  

myparser = DoubanHtmlParser()

   
db=DoubanImageParser('http://www.douban.com/online/10776262/album/45239925/')
