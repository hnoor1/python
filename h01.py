import turtle

#Hanna-Liina Nöör 09.10.2025

#see on kujundite liigutamine
turtle.penup()
turtle.goto(-400,200)
turtle.pendown()

#see on kolmnurk!
for i in range(3):
    turtle.fd(200)
    turtle.left(120)

#see on ruudu tagasi liigutamine
turtle.penup()
turtle.goto(0,0)
turtle.pendown()

#see on ruut
for i in range(4): #tsükkel 4x
    turtle.fd(150) #fd on forward
    turtle.left(90)

#liigume
turtle.penup()
turtle.goto(-100,-300)
turtle.pendown()

#see on minu nime esitäht - Liina
turtle.fd(200)
turtle.right(90)
turtle.fd(50)
turtle.left(90)
turtle.bk(250)
turtle.left(90)
turtle.fd(300)
turtle.right(90)
turtle.fd(50)
turtle.right(90)
turtle.fd(250)










turtle.done()
