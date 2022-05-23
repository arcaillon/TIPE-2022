from turtle import *
import math as m
t = Turtle()

# tracé de la lentille
t.color('blue')
t.circle(100,180)
t.seth(270)
t.fd(200)
t.setpos(0,100)
t.seth(0)
t.pu()
t.fd(50*m.sqrt(3))
t.seth(90)
t.pd()
t.fd(50)
t.seth(10000000)
t.fd(100)

#tracé des rayons
t.color('red')
l = [k*50/11+100 for k in range(-5,6)]
t.pu()
for i in l :
    t.setpos(-10,i)
    t.pd()
    t.seth(0)
    t.fd(200)
    t.pu()

bye()