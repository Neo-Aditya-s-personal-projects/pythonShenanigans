from turtle import *

speed(10)
color('black')
bgcolor('black')
#pensize(5)

b = 200
forward(b * 2)
sub = 5
c = 255
color('cyan')
while b > 0:
   pencolor("#{:02x}{:02x}{:02x}".format(abs(255-c), abs(128-c), abs(128-b)))
   left(b)
   forward(b)
   forward(b)
   forward(b)
   b = b - 1
   c -= sub
   if c == 0 or c == 255:
    sub*=-1

pensize(0)
exit = input("Enter 1 to exit")
while exit != '1':
    exit = input("")