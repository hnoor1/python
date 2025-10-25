#Harjutus09
import random

for i in range(1,21): #Genereeri ja kuva arvud arvud 1-20
    if i%15 == 0:                                         #Arvud, mis jagunevad 3, lisa tekst TIK (näiteks 3 TIK)
        print(i, "TIKTAK")
    elif i%3 == 0:
        print(i,"TIK")
    elif i%5 == 0:
        print(i,"TAK")
    else:
        print(i)


