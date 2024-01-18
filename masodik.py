"""
2. feladat:    13 pont
a)	Írass ki a konzolra 13 db  [- 40, 150] zárt intervallumba eső véletlen számot. A generált értékeket tárold lista adatszerkezetben (2 pont)

b)	Készíts ketjegyuek_szama(lista) metódust, mely megmondja, hogy  hány kétjegyű szám van a listában! 
A függvény visszatérési értéke legyen a darabszám! (3 pont)

c)	Készíts  paros_osszege(lista) metódust, mely megmondja, hogy  listában lévő páros számok összegét!  
A függvény visszatérési értéke legyen a párosok összege! (3 pont)

d)	Készíts paratlan_osszege(lista)  metódust, mely megmondja, hogy  listában lévő páratlan számok összegét!  
A függvény visszatérési értéke legyen a páratlanok összege! (3 pont)

e)	Írd ki a konzolra, hogy a párosok összege, vagy a páratlanok összege nagyobb-e? (2 pont)
"""

import random

def a_feladat():
    lista=[]
    for i in range(0,13,1):
        szam:int = random.randint(-40,150)
        lista.append(szam)
    return lista

def ketjegyuek_szama(lista):
    db=0
    for i in range(0,len(lista),1):
        if lista[i] > 9 and lista[i] < 100:
            db+=1
    return db

def paros_osszege(lista):
    parososszeg=0
    for i in range(0,len(lista),1):
        if lista[i] % 2 == 0:
            parososszeg+=lista[i]
    return parososszeg

def paratlan_osszege(lista):
    paratlanosszeg=0
    for i in range(0,len(lista),1):
        if lista[i] % 2 != 0:
            paratlanosszeg+=lista[i]
    return paratlanosszeg


