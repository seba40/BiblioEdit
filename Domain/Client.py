'''
Created on Nov 30, 2016

@author: Sebastian
'''

class Client():
    '''
    classdocs
    '''


    def __init__(self, ids,name,cnp):
        '''
        Constructor
        '''
        self.ids=ids
        self.name=name
        self.cnp=cnp
    
    def getIds(self):
        return self.ids
    
    def getName(self):
        return self.name
    
    def getCnp(self):
        return self.cnp
    
    def setIds(self,ids):
        self.ids=ids
        
    def setName(self,name):
        self.name=name
        
    def setCnp(self,cnp):
        self.cnp=cnp
    def __str__(self):
        return str(self.ids)+" "+str(self.name) + " " +str(self.cnp)