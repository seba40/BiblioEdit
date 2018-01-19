
class Carte():
    '''
    classdocs
    '''


    def __init__(self, ids,title,author,desc,image):
        '''
        Constructor
        '''
        self.ids=ids
        self.title=title
        self.author=author
        self.desc=desc
        self.image=image
    
    def getIds(self):
        return self.ids
    
    def getTitle(self):
        return self.title
    
    def getAuthor(self):
        return self.author
    def getDesc(self):
        return self.desc
    def getImage(self):
        return self.image
    
    def setIds(self,ids):
        self.ids=ids
        
    def setTitle(self,title):
        self.title=title
        
    def setAuthor(self,author):
        self.author=author
    def setDesc(self,desc):
        self.desc=desc
    def setImage(self,image):
        self.image=image
    def __str__(self):
        return str(self.ids)+" "+str(self.title) + " " +str(self.author)
