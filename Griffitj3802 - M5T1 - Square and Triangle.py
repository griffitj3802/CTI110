#Griffith James
#Mr. Cameron
#CTI-110 0901
#Oct 18, 2017
#M5T1 - Turtle Graphics




import turtle           
wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.title("Turtle Time!") 

#griffy stuff
griffy = turtle.Turtle()    
griffy.pensize(4)
griffy.pencolor("red")
griffy.shape("turtle")


for i in range(3):
    griffy.forward(90)          
    griffy.left(120)            

griffy.left(90)
for i in range(4):
    griffy.forward(80)          
    griffy.left(90)             


# end commands
wn.mainloop()           
