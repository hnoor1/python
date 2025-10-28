#Kodune ülesanne nr 2 - kujund nr 12 (https://www.metshein.com/wp-content/uploads/2023/10/python-turtle-KT-scaled.jpg)
#Hanna-Liina Nöör 28.10.2025

import turtle
turtle.speed()
#kujud koosneb 12 kolmnurgast, selle sees on ühtlasi ka kuusnurk

# turtle.forward(100) #ühe kolmnurga tegemine ilma tsüklita
    # turtle.right(60)
    # turtle.backward(100)
    # turtle.right(60)
    # turtle.forward(100)

for kolmnurk in range(6): #teeme kuus kolmnurka, mis moodustavad tähe kujundi, tähe sisse moodustub tühi kuusnurk
    for kolmnurk in range(3): #ühe kolmnurga tegemine
        turtle.forward(100)
        turtle.left(120)        
    turtle.forward(100)  #kui üks kolmnurk on tehtud, saab teha kuus samasugust kolmnurka
    turtle.right(60)
    
#liigume kuusnurga sisse ülejäänud kolmnurkade joonistamiseks
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