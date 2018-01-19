'''
Created on Nov 30, 2016

@author: Sebastian
'''

class ImprumutRep():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.im=[]
    
    def add(self,x):
        self.im.append(x)
    
    def delete(self,x):
        self.im.remove(x)
    def change(self,x):
        for i in range (0,len(self.im)):
            if self.im[i].getIds()==x.getIds():
                self.im[i]=x

    
    def getRep(self):
        return self.im