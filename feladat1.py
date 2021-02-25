#Készíts egy programot, amely [1;10] intervallumon generál 5 darab véletlen egész számot, és ezeket tárolja el egy listában! 
#A program adja össze a lista elemeit, írja ki a képernyőre az összegüket és a lista elemeit!

import random
lista = []

for i in range(5):
    a = random.randrange(1 , 11)
    lista.append(a)


osszeg = 0
for i in lista:
    osszeg = osszeg + i

print(osszeg)
print(lista)