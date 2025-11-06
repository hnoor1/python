#Harjutus 10

# Koostage Pythoni programm, mis küsib kasutajalt arve ükshaaval. 
# Programm peaks jätkama arvude küsimist ja nende vastuvõtmist seni, kuni kasutaja jätab sisestuse tühjaks (st vajutab sisestusklahvi ilma midagi kirjutamata).
# Programm peab kasutama while-tsüklit arvude küsimiseks ja nende salvestamiseks.
# Pärast seda, kui kasutaja lõpetab arvude sisestamise peab programm arvutama ja väljastama kõikide sisestatud arvude keskmise väärtuse.

loop = 1

while loop:
    arv = input("Lisa arv: ")
    if arv=="":
        break #töötab ka loop = 0
