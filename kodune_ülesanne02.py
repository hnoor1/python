#Kodune ülesanne nr 2
#Hanna-Liina Nöör 28.10.2025

#Vaja on joonistada kujund nr 12 (https://www.metshein.com/wp-content/uploads/2023/10/python-turtle-KT-scaled.jpg)

import turtle
turtle.speed(0)
#Kujund koosneb 12 kolmnurgast, selle sees on ühtlasi ka kuusnurk

# turtle.forward(100) #ühe kolmnurga tegemine ilma tsüklita, for-tsükliga tehes saab nelja rea asemel hakkama kahe reaga
    # turtle.right(60)
    # turtle.backward(100)
    # turtle.right(60)
    # turtle.forward(100)

#teeme kuus kolmnurka, mis moodustavad tähe kujundi, tähe sisse moodustub tühi kuusnurk
for kolmnurk in range(6): 
    #ühe kolmnurga tegemine
    for kolmnurk in range(3): 
        turtle.forward(100)
        turtle.left(120)        
    #kui üks kolmnurk on tehtud, saab teha kuus samasugust kolmnurka
    turtle.forward(100)  
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