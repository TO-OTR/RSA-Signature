# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 19:28:25 2021

@author: to_ot
"""

def home_mod_expnoent(x,y,n): #exponentiation modulaire
    res = 1
    while y != 0:
        if (y & 1) == 1:
            res = (res * x) % n
        y >>= 1
        x = (x*x) % n
    return res

def home_ext_euclide(y,b): #algorithme d'euclide étendu pour la recherche de l'exposant secret
    # b mod y = da
    q = []
    t = [0,1]
    pgcd,q = home_pgcd_plus(y,b,q)
    if pgcd != 1:
        return -1
    for i in range(0,len(q)-1):#v2 = v0 -q1v1
        t[0], t[1] = t[1], t[0]-q[i]*t[1]
    return t[1]%y

def home_pgcd_plus(y,b,q):
    if(b==0): 
        return y,q
    else:
        q.append(y//b)
        return home_pgcd_plus(b,y%b,q)

def home_pgcd(a,b): #recherche du pgcd
    if(b==0): 
        return a 
    else: 
        return home_pgcd(b,a%b)


def home_string_to_int(x): # pour transformer un string en int
    z=0
    for i in reversed(range(len(x))):
        z=int(ord(x[i]))*pow(2,(8*i))+z #ord(c) -> Ackii
    return(z)


def home_int_to_string(x): # pour transformer un int en string
    txt=''
    res1=x
    while res1>0:
        res=res1%(pow(2,8))
        res1=(res1-res)//(pow(2,8))
        txt=txt+chr(res)
    return txt


def mot10char(): #entrer le secret
    secret=input("donner un secret unlimited si CBC&MD5, autrement moins de 25 si 32bit, moins de 50 si 64bit: ")
    while (len(secret)>100000):
        secret=input("c'est beaucoup trop long, 10 caractères S.V.P : ")
    return(secret)