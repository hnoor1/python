#Kodune ülesanne nr 2
#Hanna-Liina Nöör 29.10.2025

#Vaja on joonistada kujund nr 12 (https://www.metshein.com/wp-content/uploads/2023/10/python-turtle-KT-scaled.jpg)

import turtle
turtle.speed(0)
#Kujund koosneb 12 kolmnurgast, selle sees on ühtlasi ka kuusnurk

#teeme kuus kolmnurka, mis moodustavad tähe kujundi, tähe sisse moodustub tühi kuusnurk
for kolmnnurk in range(6):
    #ühe kolmnurga tegemine
    for kolmnurk in range(3):
        turtle.forward(100)
        turtle.left(120)
    #kui üks kolmnurk on tehtud, saab teha kuus samasugust kolmnurka
    turtle.forward(100)
    turtle.right(60)

#liigume tekkinud kuusnurga sisse ülejäänud kolmnurkade joonistamiseks
turtle.right(60)
turtle.forward(100)

#teeme kuusnurga sisse kuus kolmnurka
for kolmnurk in range(6):
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.right(180)
    
turtle.done()