import turtle as trtl
painter = trtl.Turtle()



#house square structure walls thingy idk????
painter.fillcolor("bisque")
painter.begin_fill()
for each in range(3):
  painter.forward(100)
  painter.right(90)

painter.forward(100)
painter.end_fill()

#roof
painter.fillcolor("darkred")
painter.begin_fill()
painter.right(45)
painter.forward(71)
painter.right(90)
painter.forward(71)
painter.end_fill()

#door
painter.fillcolor("brown")
painter.penup()
painter.goto((40,-100))
painter.right(225)
painter.pendown()
painter.begin_fill()
painter.forward(30)
painter.right(90)
painter.forward(20)
painter.right(90)
painter.forward(30)
painter.end_fill()
painter.backward(15)
painter.right(90)
painter.forward(5)
painter.penup()
painter.goto((0,0))


#window
painter.goto((85,-30))
painter.pendown()
painter.fillcolor("lightblue")
painter.begin_fill()
for each in range(4):
  painter.forward(15)
  painter.left(90)

painter.end_fill()
painter.forward(7.5)
painter.left(90)
painter.forward(15)
painter.penup()
painter.goto((85,-37.5))
painter.right(90)
painter.pendown()
painter.forward(15)
painter.penup()
painter.goto((-25,-100))


#mustang car
painter.pendown()
painter.right(90)
painter.forward(35)
painter.left(90)
painter.forward(30)
painter.right(25)
painter.forward(30)
painter.left(25)
painter.forward(45)
painter.left(25)
painter.forward(30)
painter.right(25)
painter.forward(30)
painter.left(90)
painter.forward(8)
painter.right(90)
painter.forward(2)
painter.left(90)
painter.forward(20)
painter.left(90)
painter.forward(2)
painter.right(90)
painter.forward(5)
painter.left(90)
painter.forward(35)
painter.begin_fill()
painter.fillcolor("black")
painter.circle(-10)
painter.forward(80)
painter.circle(-10)
painter.end_fill()
painter.forward(45)
painter.penup()
painter.goto((-30,-90))

#to do: color car and make door maybe, sun, stick figs



#something?
wn = trtl.Screen()
wn.mainloop()
