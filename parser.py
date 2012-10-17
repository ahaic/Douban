from html.parser import HTMLParser
import urllib.request
import urllib
import os
image_name =[]

album = input('plz enter url \n')

                                   #"http://www.douban.com/online/10698791/album/41048682/"
print("album = ", album)

online_number = album.split('/')[4]
album_number = album.split('/')[6]

home_album = "http://www.douban.com/online/"+online_number  # home_album: the url that show how many pics

# -------   find the number of total photos --------------
t = urllib.request.urlopen(home_album).read().decode('utf8')

s_tart = t.find("全部")+2
e_nd  = t.find("张")

#   t[%s:%s %(t.find("全部")+2,t.find("张")]
total_photos = t[s_tart:e_nd]
print("the amount of photos are: ",total_photos)

# -------   find the number of total photos --------------

pages = int(int(total_photos)/30+1)

print("total pages are : ", pages)
start=0
end = (pages-1)*30
path = "D:/Photos"
 
web_url = []   # store the pages of url
new_url = []
while start <=end:
    n=start
    web_url = web_url+[album+"?start="+str(n)]
    
    start=start+30
    
    
global url
url = []



class MyHTMLParser(HTMLParser):
    
      
   
    def handle_starttag(self,tag,attrs):
             
        if tag =='img':
            
            for name,value in attrs:
                
                if name =='src':
                    url.append(str(value))
                  
#     ----------------start------------------------------------

def get_image_name(image_url):
    
    page = urllib.request.urlopen(image_url)
    text=page.read().decode("utf8")
    j=-1
#    print(len(text))
    for i in text:
        j=j+1
        if i == '自':
#            print('start',j)
            break
#print('jj',j)
#print(text[j:])
    p=0
    for k in text[j:]:
        p+=1
    
        if k =='上':
#            print('end',p+j)
            break

    image_name.append(text[j+1:p+j-1])
    

#get_image_name('http://www.douban.com/online/10698791/photo/726568228')    
        


#--------------------------------------end---------------------

             
print("start printing image url","hoho")           

            

myparser = MyHTMLParser()

for r in web_url:
    page = urllib.request.urlopen(r)
    text=page.read().decode("utf8")
    myparser.feed(text)

k=0

p_p = []    # store the number like " photo/public/p801104999.jpg" ----------  801104999

for i in url:
    if len(i)==61:
        new_url.append(i)
        
        new_url[-1][-13:-4]
        print(len(new_url),":","http://img3.douban.com/view/photo/photo/public/p"+new_url[-1][-13:-4]+'.jpg')
        
        
        
       
            
            
        
        
'''
for ii in new_url:
    k=k+1
    p_p.append(ii[-13:-4])
    print(k,":","http://img3.douban.com/view/photo/photo/public/p"+ii[-13:-4]+'.jpg')
'''

#    get_image_name("http://www.douban.com/online/"+online_number+"/photo/"+ii[-13:-4])
    
#    print(image_name[k-1])

    #urllib.request.urlretrieve("http://img3.douban.com/view/photo/photo/public/p"+ii[-13:-4]+".jpg","D:/jk/"+str(k)+".jpg")

    #print('done---',k )
                      
  

    
