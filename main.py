import elsofeladat
import masodik
import harmadik

"""
print("1. FELADAT")
paros=elsofeladat.beker()
print(paros)


print("1.FELADAT/B:")
paros_szamok_lista=elsofeladat.harom_paros()
print(paros_szamok_lista)


print("1.FELADAT/C:")
harom_paros=elsofeladat.harom_paros
min=elsofeladat.legkisebb(harom_paros)
print(f"A legkisebb szám a listából: {harom_paros[min]}")

paros_szamok_lista=elsofeladat.harom_paros()
print(paros_szamok_lista)

elsofeladat.legkisebb()

lista = masodik.a_feladat()
print(lista)

db=masodik.ketjegyuek_szama(lista)
print(f"{db} db kétjegyű szám van a listában")

parososszeg=masodik.paros_osszege(lista)
print(f"A páros számok összege: {parososszeg}")

paratlanosszeg=masodik.paratlan_osszege(lista)
print(f"A páratlan számok összege: {paratlanosszeg}")

if parososszeg > paratlanosszeg:
    print(f"A páros számok összege({parososszeg}) nagyobb, mint a páratlan számok ({paratlanosszeg}) összege. ")
else:
    print(f"A páratlan számok összege ({paratlanosszeg}) nagyobb, mint a páros számok ({parososszeg}) összege. ")"""


lista=harmadik.beolvas()

csapatok_szama=harmadik.csapatok_sz(lista)
print(f"Az adott listában összesen {csapatok_szama}db csapat van")