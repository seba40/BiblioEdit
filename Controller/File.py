from Controller.Controller import control
import io  # @UnusedImport
class File():
    '''
    classdocs
    '''

    def save(self,path):
        self.f=open(path, 'w')
        self.f.write(str(len(control.rCarte.cr))+'\n')
        for i in range(0,len(control.rCarte.cr)):
            self.f.write(str(control.rCarte.cr[i].getIds())+'  ')
            self.f.write(str(control.rCarte.cr[i].getTitle())+'  ')
            self.f.write(str(control.rCarte.cr[i].getAuthor())+'  ')
            self.f.write(str(control.rCarte.cr[i].getDesc())+'  ')
            self.f.write(str(control.rCarte.cr[i].getImage()))



            self.f.write('\n')
        self.f.write(str(len(control.rClient.cl))+'\n')
        for i in range(0,len(control.rClient.cl)):
            self.f.write(str(control.rClient.cl[i].getIds())+'  ')
            self.f.write(str(control.rClient.cl[i].getName())+'  ')
            self.f.write(str(control.rClient.cl[i].getCnp()))
            self.f.write('\n')
        self.f.write(str(len(control.rImprumut.im))+'\n')
        for i in range(0,len(control.rImprumut.im)):
            self.f.write(str(control.rImprumut.im[i].getIds())+'  ')
            self.f.write(str(control.rImprumut.im[i].getIdb())+'  ')
            self.f.write(str(control.rImprumut.im[i].getIdc())+'  ')
            self.f.write(str(control.rImprumut.im[i].getDatai())+'  ')
            self.f.write(str(control.rImprumut.im[i].getDatar()))
            self.f.write('\n')

        self.f.flush()
    def open(self,path):
        self.f=open(path,'r')
        self.index=self.f.readline()
        self.carte=[]
        self.client=[]
        self.entry=[]
        control.rCarte.cr=[]
        control.rClient.cl=[]
        control.rImprumut.im=[]

        for i in range(0,int(self.index)):  # @UnusedVariable

            self.string=self.f.readline()
            self.string=self.string.replace('\n','')
            self.carte=self.string.split('  ')
            self.ids=int(self.carte[0])
            self.title=self.carte[1]
            self.author=self.carte[2]
            self.desc=self.carte[3]
            self.img=self.carte[4]
            control.add_Carte(self.ids, self.title, self.author,self.desc,self.img)
            
            
        self.index=self.f.readline()    
        for i in range(0,int(self.index)):  # @UnusedVariable
            self.string=self.f.readline()
            self.string=self.string.replace('\n','')
            self.client=self.string.split('  ')
            self.ids=int(self.client[0])
            self.name=self.client[1]
            self.cnp=self.client[2]
            control.add_Client(self.ids, self.name, self.cnp)

        self.index=self.f.readline()
        for i in range(0,int(self.index)):  # @UnusedVariable
            self.string=self.f.readline()
            self.string=self.string.replace('\n','')
            self.entry.append(self.string)
            self.entry=self.string.split('  ')
            self.ids=int(self.entry[0])
            self.idb=int(self.entry[1])
            self.idc=int(self.entry[2])
            self.datai=self.entry[3]
            self.datar=self.entry[4]
            control.add_Imprumut(self.ids, self.idb, self.idc, self.datai, self.datar)
    def openDesc(self,path):
        self.f=open(path,'r')
        text=self.f.readlines()
        return text

