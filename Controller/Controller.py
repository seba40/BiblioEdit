from Repository.CarteRep import CarteRep
from Repository.ClientRep import ClientRep
from Repository.ImprumutRep import ImprumutRep
from Domain.Carte import Carte
from Domain.Client import Client
from Domain.Imprumut import Imprumut
import copy

class Control():
    '''
    classdocs
    '''
    def __init__(self):
        self.rCarte=CarteRep()
        self.rClient=ClientRep()
        self.rImprumut=ImprumutRep()
        self.top=ClientRep()
        self.top2=CarteRep()
        self.idbook=1
        self.idclient=1
        self.identry=1
        self.opened={'bx':0,'dx':0,'fx':0,'cx':0,'gx':0,'bk':0,'window':0}

    def add_Carte(self,ids,title,author,desc,image):
        if ids!=0:
            self.opt=Carte(ids,title,author,desc,image)
            self.rCarte.add(self.opt)
            self.idbook+=1
        else:
            ids=self.idbook
            self.opt=Carte(ids,title,author,desc,image)
            self.rCarte.add(self.opt)
            self.idbook+=1
        
    def add_Client(self,ids,nume,cnp):
        if ids!=0:
            self.opt=Client(ids,nume,cnp)
            self.rClient.add(self.opt)
            self.idclient+=1
        else:
            ids=self.idclient
            self.opt=Client(ids,nume,cnp)
            self.rClient.add(self.opt)
            self.idclient+=1



    def add_Imprumut(self,ids,idb,idc,datai,datar):
        if ids!=0:
            self.opt=Imprumut(ids,idb,idc,datai,datar)
            self.rImprumut.add(self.opt)
            self.identry+=1
        else:
            ids=self.identry
            self.opt=Imprumut(ids,idb,idc,datai,datar)
            self.rImprumut.add(self.opt)
            self.identry+=1


    def delete_Carte(self,opt,el):
        if opt==1:
            for i in self.rCarte.cr:
                if i.getIds()==int(el):
                    self.rCarte.delete(i)
        if opt==2:
            for i in self.rCarte.cr:
                if i.getTitle()==el:
                    self.rCarte.delete(i)
        if opt==3:
            i=0
            while i < len(self.rCarte.cr):
                if self.rCarte.cr[i].getAuthor()==el:
                    self.rCarte.delete(self.rCarte.cr[i])
                else:
                    i+=1



        
    def delete_Client(self,opt,el):
        if opt==1:
            for i in self.rClient.cl:
                if i.getIds()==int(el):
                    self.rClient.delete(i)
        if opt==2:
            for i in self.rClient.cl:
                if i.getName()==el:
                    self.rClient.delete(i)
        if opt==3:
            i=0
            while i < len(self.rClient.cl):
                if self.rClient.cl[i].getCnp()==el:
                    self.rClient.delete(self.rClient.cl[i])
                else:
                    i+=1
    def delete_Imprumut(self,el):
        for i in self.rImprumut.im:
            if i.getIds()==int(el):
                self.rImprumut.delete(i)


    def change_Carte(self,ids,title,author,desc,image):
        self.opt=Carte(ids,title,author,desc,image)
        self.rCarte.change(self.opt)
    def change_Client(self,ids,nume,cnp):
        self.opt=Client(ids,nume,cnp)
        self.rClient.change(self.opt)
    def change_Imprumut(self,ids,idb,idc,datai,datar):
        self.opt=Imprumut(ids,idb,idc,datai,datar)
        self.rImprumut.change(self.opt)
    def stat_topr(self):
        self.ord=[]
        for i in range(0,self.rClient.cl[len(self.rClient.cl)-1].getIds()):  # @UnusedVariable
            self.ord.append(0)
        for i in range(0,len(self.rImprumut.im)):  # @UnusedVariable
            self.ord[int(self.rImprumut.im[i].getIdc())-1]+=1
        self.top.cl=copy.deepcopy(self.rClient.cl)
        self.aux=0
        for i in range(0,len(self.top.cl)-1):
            for j in range(i+1,len(self.top.cl)):
                if(self.ord[int(self.top.cl[i].getIds()-1)]<self.ord[int(self.top.cl[j].getIds()-1)]):
                    self.aux=self.top.cl[i]
                    self.top.cl[i]=self.top.cl[j]
                    self.top.cl[j]=self.aux
    def stat_topb(self):
        self.ord=[]
        for i in range(0,self.rCarte.cr[len(self.rCarte.cr)-1].getIds()):  # @UnusedVariable
            self.ord.append(0)
        for i in range(0,len(self.rImprumut.im)):  # @UnusedVariable
            self.ord[int(self.rImprumut.im[i].getIdb())-1]+=1
        self.aux=0
        self.top2.cr=copy.deepcopy(self.rCarte.cr)

        for i in range(0,len(self.top2.cr)-1):
            for j in range(i+1,len(self.top2.cr)):
                if(self.ord[int(self.top2.cr[i].getIds()-1)]<self.ord[int(self.top2.cr[j].getIds()-1)]):
                    self.aux=self.top2.cr[i]
                    self.top2.cr[i]=self.top2.cr[j]
                    self.top2.cr[j]=self.aux

        
        
control=Control()        
        
    
