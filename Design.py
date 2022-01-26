import turtle

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.speed(0)
color = ('green','blue','yellow','red','white')
for i in range (102):
    t.color(color[1%5])
    t.left(144)
    t.forward(i*2)
    t.rt(72)
