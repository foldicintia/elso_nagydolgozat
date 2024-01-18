"""
1. feladat:    7 pont
a)	Kérj be 1 páros számot a felhasználótól. (1 pont)
Amennyiben nem páros számot ad meg a felhasználó, akkor kérd be újra a számot, addig, amíg páros számot nem ad meg!  (1 pont)
A bekéréshez írj egy függvényt beker(), amely bekéri a kívánt feltételeknek megfelelő számot. . (1 pont)

b)  Az előző metódus felhasználásával - és kiegészítésével - kérj be 3 páros számot a felhasználótól. 
A program minden lépésben írja ki, hogy hányadik számot kéri be,   az alábbi minta szerint: . (2 pont)

c)	Az előző metódusnak legyen visszatérési értéke, mely a bekért számmal tér vissza, és azt beleteszi egy listába! Írj metódust, mely 
megkeresi a három bekért szám közül a legkisebbet! A legkisebb számot a program írja ki a konzolra és azt is, hogy hányadiknak 
adta meg a felhasználó! . (2 pont)
"""

def beker():
    paros_szam:int = int(input("Kérek egy páros számot: "))
    i=0
    while not (paros_szam % 2 == 0):
        print("Ez nem páros. Páros számot kérek.")
        paros_szam: int = int(input("Kérek egy páros számot: "))   
    return paros_szam

def harom_paros(): 
    paros_szamok_lista=[]
    for i in range(0,3,1):
        paros_szam:int = int(input(f"Kérem az {i+1}. páros számot: "))
        while not (paros_szam % 2 == 0):
            print("Ez nem páros. Páros számot kérek.")
            paros_szam: int = int(input(f"Kérem az {i+1}. páros számot: "))
        paros_szamok_lista.append(paros_szam)
    return paros_szamok_lista

def legkisebb(paros_szamok_lista):
    min=paros_szamok_lista[0]
    for i in range(0,len(paros_szamok_lista),1):
        if paros_szamok_lista[i] < min:
            min==paros_szamok_lista[i]
    return min


    
