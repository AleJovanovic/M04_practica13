class user:
    def __init__(self,nom,edat,dni,adreça,correo,nacionalitat):
        self.nom=nom
        self.edat=edat
        self.dni=dni
        self.adreça=adreça
        self.correo=correo
        self.nacionalitat=nacionalitat

    
    def getNom(self):
        return self.nom

    def setNom(self,nom):
        self.nom=nom

    def getEdat(self):
        return self.edat

    def setEdat(self,edat):
        self.edat=edat

    def getDNI(self):
        return self.dni

    def setDNI(self,dni):
        self.dni=dni
    
    def getAdreça(self):
        return self.adreça

    def setAdreça(self,adreça):
        self.adreça=adreça

    def getCorreo(self):
        return self.correo

    def setCorreo(self,correo):
        self.correo=correo

    def getNacionalitat(self):
        return self.nacionalitat

    def setNacionalitat(self,n):
        self.nacionalitat=n

    
    def salutacio(self):
        print(self.nom,self.edat,self.dni,self.adreça,self.correo,self.nacionalitat)

