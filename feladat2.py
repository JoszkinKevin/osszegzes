#Módosítsd úgy a fenti programot, hogy a program csak a páros számokat adja össze!

import random
lista = []


for i in range(5):
    szam = random.randrange(1 , 11)
    lista.append(szam)


osszeg = 0
for i in lista:
    if  i % 2 == 0:
        osszeg = osszeg + i


print(osszeg)
print(lista)