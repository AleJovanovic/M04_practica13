class book:
    def __init__(self, nom, autor, preu, curs, copies, pagines):
        self.nom=nom
        self.autor=autor
        self.preu=preu
        self.curs=curs
        self.copies=copies
        self.pagines=pagines   

    def getNom(self):
        return self.nom
    def setNom(self,nom):
        self.nom=nom

    def getAutor(self):
        return self.autor
    def setAutor(self,autor):
        self.autor=autor

    def getPreu(self):
        return self.preu    
    def setPreu(self,preu):
        self.preu=preu

    def getCurs(self):
        return self.curs
    def setCurs(self,curs):
        self.curs=curs 

    def getCopies(self):
        return self.copies  
    def setCopies(self,copies):
        self.copies=copies 

    def getPagines(self):
        return self.pagines
    def setPagines(self,pagines):
        self.pagines=pagines   
    
    
    def info(self):
        
        print(self.nom,self.autor,self.preu,self.curs,self.copies,self.pagines)
