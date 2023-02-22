#INTEGRANTE A

from animal import animal
p1 = animal("jaguar", "femenino", 4, 0, "Nina")
p1.salutacio()


#integrante B
from book import book
from user import user
from university import university

print("Valores de book")

book1= book("Matematicas 1","Luis Gonzalez",20,"primaria,2",35,47)
book1.info()
book2=book("Fisica Volumen II","Laura Lopez", 13.75,"bachillerato,2", 70,200)
book2.info()

print("\nValores de user")
user1=user("Laura",20,"89282928P","Gran Via 2,Barcelona","laura123@gmail.com","Esp")

user1.salutacio()
user2=user("Pablo",44,"2672782627C","C Ferran,33,Barcelona", "Pablowww@gmail.com","Esp")

user2.salutacio()

print("\nValores de universitat")

uni1=university("Universitat de Barcelona", "Barcelona","Diagonal,Barcelona", 3,"Pública",400)

uni1.info()
uni2=university("Universitat Autonoma de Barcelona", "Barcelona","Cerdanyola del Vallès",1,"Pública",200)

uni2.info()


#modificacio atributs 
print("\nModificacion atributos")

book1.setPreu(12.75)
book2.setNom("Quimica Volumen II")



user1.setNacionalitat("italia")
user2.setCorreo("wwwPablo@gmail.com")


uni1.setGraus(95)
uni2.setRanking(2)

book1.info()
book2.info()
print("\n")
user1.salutacio()
user2.salutacio()
print("\n")
uni1.info()
uni2.info()