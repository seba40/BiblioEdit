'''
Created on Nov 30, 2016

@author: Sebastian
'''

class CarteRep():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.cr=[]
    
    def add(self,x):
        self.cr.append(x)
    
    def delete(self,x):
        self.cr.remove(x)
    def change(self,x):
        for i in range (0,len(self.cr)):
            if self.cr[i].getIds()==x.getIds():
                self.cr[i]=x
    def getRep(self):
        return self.cr