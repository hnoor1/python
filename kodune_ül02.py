#Kodune ülesanne nr 2 - kujund nr 12 (https://www.metshein.com/wp-content/uploads/2023/10/python-turtle-KT-scaled.jpg)
#Hanna-Liina Nöör 28.10.2025

import turtle

# turtle.forward(100) #ühe kolmnurga tegemine ilma tsüklita
    # turtle.right(60)
    # turtle.backward(100)
    # turtle.right(60)
    # turtle.forward(100)

turtle.speed(0)

#Kujundi nr 12 saamiseks tuleb teha kolmnurgad.Selleks kasutan tsükleid.

for kolmnurk in range(3):
    turtle.forward(100) 
    turtle.left(120)
    
for kolmnurk in range(3):
    turtle.backward(100)
    turtle.left(120)
    
for kolmnurk in range(3):
    turtle.left(120)
    turtle.backward(100)
turtle.forward(100)

for kolmnurk in range(3):
    turtle.left(120)
    turtle.backward(100)

turtle.left(60)
turtle.backward(100)

for kolmnurk in range(3):
    turtle.left(120)
    turtle.backward(100)

for kolmnurk in range(3):
    turtle.backward(100)
    turtle.left(120)
    
for kolmnurk in range(3):
    turtle.backward(100)
    turtle.right(120)

turtle.left(60)

for kolmnurk in range(3):
    turtle.backward(100)
    turtle.left(120)

turtle.backward(100)
turtle.right(120)

for kolmnurk in range(3):
    turtle.forward(100) 
    turtle.left(120)
    
turtle.backward(100)

for kolmnurk in range(3):
    turtle.forward(100)
    turtle.right(120)
    
turtle.backward(100)
turtle.left(60)
turtle.forward(100)
    
    
turtle.done()