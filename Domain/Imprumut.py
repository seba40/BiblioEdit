'''
Created on Nov 30, 2016

@idc: Sebastian
'''

class Imprumut():
    '''
    classdocs
    '''


    def __init__(self, ids,idb,idc,datai,datar):
        '''
        Constructor
        '''
        self.ids=ids
        self.idb=idb
        self.idc=idc
        self.datai=datai
        self.datar=datar
    
    def getIds(self):
        return self.ids
    
    def getIdb(self):
        return self.idb
    
    def getIdc(self):
        return self.idc
    
    def getDatai(self):
        return self.datai
    
    def getDatar(self):
        return self.datar
    
    def setIds(self,ids):
        self.ids=ids
        
    def setIdb(self,idb):
        self.idb=idb
        
    def setIdc(self,idc):
        self.idc=idc
    
    def setDatai(self,datai):
        self.datai=datai
    
    def setDatar(self,datar):
        self.datar=datar
    def __str__(self):
        return str(self.ids)+" "+str(self.idb) + " " +str(self.idc)+ " " +str(self.datai)+ " " +str(self.datar)