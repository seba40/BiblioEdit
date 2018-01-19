'''
Created on Nov 30, 2016

@author: Sebastian
'''

class ClientRep():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.cl=[]
    
    def add(self,x):
        self.cl.append(x)
    
    def delete(self,x):
        self.cl.remove(x)    
    def change(self,x):
        for i in range (0,len(self.cl)):
            if self.cl[i].getIds()==x.getIds():
                self.cl[i]=x

    
    def getRep(self):
        return self.cl