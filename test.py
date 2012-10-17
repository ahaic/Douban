
from time import sleep
class A(object):
    
    
    def __init__(self):

        self.catch()


    def catch(self):

        while True:
            
            print('call me')


        
    def get(self):
        
        sleep(2)
        print('get')

        self.catch()

        

o = A()
        
    








'''
def a(obj,index):
 #   return obj
  #  return index
    return obj[index]


try:
    a('spam',4)
except IndexError:

    print('catch Error')







pass

class A:

    r=0

    def __init__(self,x):

        self.target = x

        
        
    
        self.kk()

        
    def kk(self):

        if 2>1:

            A.r = 8
        

            
        print(A.r)

        

        print('done')
    print(r+1)

    print(self.target)

'''
