#Kodune töö nr 3

#Hanna-Liina Nöör 12.11.2025

# Kirjutada programm, mis lubab kasutajal valida kujundite tüübi (viisnurk, ring, ruut või suvaline) ja arvu.
# Programm joonistab seejärel antud arvu kujundeid valitud tüübiga või juhul, kui valik on “suvaline”, valib programm ise juhuslikult kujundi tüübi iga kujundi jaoks.
# Kõik kujundite joonistamise käsud peavad olema kirjutatud eraldi funktsioonidesse. Näiteks funktsioon joonista_ruut() või joonista_viisnurk().
# Pärast joonistamist peab programm pakkuma võimalust sisestada uued väärtused või väljuda programmist, jättes sisendi tühjaks.

import turtle
import random

#Kõigepealt määrame definitsioonid, et edaspidi saaks kiiremini ehk ei pea iga kord kujundeid lahti kirjutama

def joonista_viisnurk() :  
    for i in range(5) :
        turtle.forward(100)
        turtle.right(72) #360 kraadi jagatud viiega, kuna viisnurgal on viis nurka
        
def joonista_ring() :
    turtle.circle(100)

def joonista_ruut() :
    for i in range(4) :
        turtle.forward(100)
        turtle.right(90)

def joonista_suvaline() :
    kujund = random.choice(["viisnurk", "ring", "ruut"])
    if kujund == "viisnurk":
        joonista_viisnurk()
    elif kujund == "ring":
        joonista_ring()
    else:
        joonista_ruut()


while True: #lõpmatu tsükkel, programm küsib kasutajalt lõpmatult vastuseid. Googeldasin https://realpython.com/python-while-loop/
    valik = input("Millist kujundit soovite joonistada? Valikus on kas viisnurk, ring, ruut või programmi poolt suvaliselt antud kujund: ").lower() #lower() lõppu selleks, et programm ei hakkaks eristama suur- ega väiketähti
  
    if valik.strip() == "": #Selleks, et tühja väärtusega saaks tsüklit lõpetada, kasutame strip() funktsiooni. Googeldasin - https://www.mygreatlearning.com/blog/strip-in-python/
        print("Rohkem ei joonista!")
        break #Programm lõpetab küsimise
    
    arv = int(input("Mitu kujundit soovite joonistada? Palun märkige arv: "))
    
    for i in range(arv):
        
#Selleks, et kujundid ei oleks üksteise peal hunnikus, liigutame need iga kord suvalise koha peale
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        
        if valik == "viisnurk":
            joonista_viisnurk()
        elif valik == "ring":
            joonista_ring()
        elif valik == "ruut":
            joonista_ruut()
        elif valik == "suvaline":
            joonista_suvaline()
        else:
            print("Tundmatu valik")
            
    jätka = input("Soovite jätkata? Kui te ei soovi jätkata, jätke vastus tühjaks ja vajutage klahvi Enter: ")
    if jätka.strip() == "":
        print("Rohkem ei joonista!")
        break

turtle.done()