#Griffith James
#Mr. Cameron
#CTI-110 0901
#Oct 18, 2017
#M5T1 - Initials

import turtle           
wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.title("Turtle, Time!") 

#griffy stuff
griffy = turtle.Turtle()    
griffy.pensize(4)
griffy.pencolor("red")
griffy.shape("turtle")
             



griffy.forward(100)
griffy.penup()
griffy.goto(50,0)
griffy.pendown()
griffy.right(90)
griffy.forward(100)
for i in range(10):
    
    griffy.right(20)
    griffy.forward(15)
griffy.penup()
griffy.goto(200,-25)
griffy.pendown()
for i in range(10):
        griffy.left(20)
        griffy.forward(15)
griffy.penup()
griffy.pendown()
griffy.forward(80)
for i in range(9):
        griffy.left(20)
        griffy.forward(15)
griffy.penup()
griffy.pendown()
griffy.right(90)
griffy.forward(25)
griffy.backward(50)


