import turtle as r
import colorsys
r.title('StudyMuch')
r.bgcolor("black")
r.tracer(5)
r.pensize(2)
h=0

for i in range(200):
    c=colorsys.hsv_to_rgb(h,0.8,1)
    r.pencolor(c)
    h += 0.008
    r.right(121)
    r.circle(-i*0.4, 120)
    r.circle(i*0.5, 120)
    r.circle(-i*0.4, 110)
    r.circle(i*0.5, 110)
r.done()    