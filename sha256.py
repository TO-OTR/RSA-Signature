# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 19:48:43 2021

@author: to_ot
"""

import MathWork as MW
import hashlib
import binascii


#voici les éléments de la clé d'Alice
x1a=5041901504594532739647823671795674168764781963651928746817637721 #p
x2a=3519515844892517921589158908425412501259054259751250142510592837 #q
na=x1a*x2a  #n
phia=((x1a-1)*(x2a-1))//MW.home_pgcd(x1a-1,x2a-1)
ea=65539 #exposant public
da=MW.home_ext_euclide(phia,ea) #exposant privé

#voici les éléments de la clé de bob
x1b=1052456273541519052754912597542159752451295426523386415487954397 #p
x2b=8010942103422233250095259520184485912517624159728275641272341643 #q
nb=x1b*x2b # n
phib=((x1b-1)*(x2b-1))//MW.home_pgcd(x1b-1,x2b-1)
eb=80141 # exposants public
db=MW.home_ext_euclide(phib,eb) #exposant privé


print("Vous êtes Bob, vous souhaitez envoyer un secret à Alice")
print("voici votre clé publique que tout le monde a le droit de consulter")
print("n =",nb)
print("exposant :",eb)
print("voici votre précieux secret")
print("d =",db)
print("*******************************************************************")

print("Voici aussi la clé publique d'Alice que tout le monde peut conslter")
print("n =",na)
print("exposent :",ea)
print("*******************************************************************")

print("il est temps de lui envoyer votre secret ")
print("*******************************************************************")
x=input("appuyer sur entrer")
secret=MW.mot10char()
print("*******************************************************************")
print("voici la version en nombre décimal de ",secret," : ")
num_sec=MW.home_string_to_int(secret)
print(num_sec)
print("voici le message chiffré avec la publique d'Alice : ")
chif=MW.home_mod_expnoent(num_sec, ea, na)
print(chif)
print("*******************************************************************")
print("On utilise la fonction de hashage MD5 pour obtenir le hash du message",secret)
Bhachis0=hashlib.sha256(secret.encode(encoding='UTF-8',errors='strict')).digest() #MD5 du message
print("voici le hash en nombre décimal ")
Bhachis1=binascii.b2a_uu(Bhachis0)
Bhachis2=Bhachis1.decode() #en string
Bhachis3=MW.home_string_to_int(Bhachis2)
print(Bhachis3)
print("voici la signature avec la clé privée de Bob du hachis")
signe=MW.home_mod_expnoent(Bhachis3, db, nb)
print(signe)
print("*******************************************************************")
print("Bob envoie \n \t 1-le message chiffré avec la clé public d'Alice \n",chif,"\n \t 2-et le hash signé \n",signe)
print("*******************************************************************")
x=input("appuyer sur entrer")
print("*******************************************************************")
print("Alice déchiffre le message chiffré \n",chif,"\nce qui donne ")
dechif=MW.home_int_to_string(MW.home_mod_expnoent(chif, da, na))
print(dechif)
print("*******************************************************************")
print("Alice déchiffre la signature de Bob \n",signe,"\n ce qui donne  en décimal")
designe=MW.home_mod_expnoent(signe, eb, nb)
print(designe)
print("Alice vérifie si elle obtient la même chose avec le hash de ",dechif)
Ahachis0=hashlib.sha256(dechif.encode(encoding='UTF-8',errors='strict')).digest()
Ahachis1=binascii.b2a_uu(Ahachis0)
Ahachis2=Ahachis1.decode()
Ahachis3=MW.home_string_to_int(Ahachis2)
print(Ahachis3)
print("La différence =",Ahachis3-designe)
if (Ahachis3-designe==0):
    print("Alice : Bob m'a envoyé : ",dechif)
else:
    print("oups")