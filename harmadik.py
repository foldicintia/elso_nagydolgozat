"""
3. feladat:     16pont
A stadionok.txt forrásállomány, Forma-1-es verseny pilótáinak adatait tartalmazza, a feladatok megoldása során ezeket az adatokat használd!
A stadionok.txt állomány szerkezete:
•	a stadion neve: Pl.: Metropolitan Park
•	a stadion helyszínének városa: Pl.: New York
•	a stadionnak hányas csapata: Pl.: 1
•	mikor léptek előszőr pályára: pl.: 1984-05-13
•	mikor léptek utoljára pályára: pl.: 1985-08-23
                
d)	Olvasd be a stadionok.txt fájlból az a stadionok adatait és tárolja el megfelelő nevű listákban! 
Ügyelj arra, hogy az állományok első sora az adatok fejlécét tartalmazza! (10 pont)

e)	Írasd ki a csapatok darabszámát a konzolra!(1p)

f)	Határozd meg és írd ki a minta szerint, hogy mely csapatok találhatók New York-ban! 
A kiírásban a stadion neve és a csapatok száma szerepeljen (5p)
"""
from Stadionok import Stadionok

def beolvas():
    stadionok_lista=[]
    fajl=open("stadionok.txt","r",encoding="utf-8")
    fajl.readline()
    fajl_lista=fajl.readlines()
    fajl.close()

    for i in range(0,len(fajl_lista),1):
        aktsor=fajl_lista[i].strip().split(";")
        nev = int(aktsor[0])
        helyszin = int(aktsor[1])
        csapat_szam = int(aktsor[2])
        elso_palyara = int(aktsor[3])
        ut_palyara = int(aktsor[4])
        stadion=Stadionok(nev,helyszin,csapat_szam,elso_palyara,ut_palyara)
        stadionok_lista.append(stadion)

def csap_db(lista):
    csapatok_szama = 0
    for i in range(0,len(lista),1):
        csapatok_szama+=lista[i].csapat_szam

    return csapatok_szama

def newyork(lista):
    newyorki_cs=[]
    for i in range(0,len(lista),1):
        if lista[i].helyszin == "New York":
            newyorki_cs.append(lista[i])

    return newyorki_cs