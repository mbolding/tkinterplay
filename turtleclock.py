#!/usr/bin/env python
#Turtle Analogue Clock
#Tim Street
#version 1.6
#2017-06-23
#SHOWS GMT NOT BST

import turtle
import time

print("Python Turtle Analogue Clock")
print("By T Street")

#Deal with different time zones
ok = False
while not(ok):
 print("\nFor example, for British summer time enter 1")
 offset = int(input("Enter offset from GMT (-11 to 11) :"))
 if offset >= -11 and offset <= 11:
  ok = True

wn = turtle.Screen()
wn.title("TURTLE CLOCK")

SCALE = 0.5 # size of clock scale factor (try 2.0 to 0.5)

#create dial
mark = turtle.Turtle()
mark.speed(200)
mark.shape("circle")
for i in range(60):
      if i % 5 == 0:
            mark.pensize(10)
            mark.penup()
            mark.forward(200*SCALE)
            mark.pendown()
            mark.forward(10*SCALE)
            mark.penup()
            mark.backward(210*SCALE)
      else:
            mark.pensize(5)
            mark.penup()
            mark.forward(200*SCALE)
            mark.pendown()
            mark.forward(5*SCALE)
            mark.penup()
            mark.backward(205*SCALE)
      mark.right(6)


update = True #controls whether minute and hour hand should update (once per minute)
updateSecond = True # controls whether the second hanbd should update
while True:
      b = time.gmtime(time.time()) # current GMT
      m = b.tm_min # remember the current minute
      s = b.tm_sec # rember the current second
      if update:
            #hour hand
            hour = turtle.Turtle()
            hour.left(90)
            hour.speed(100*SCALE)
            hour.pensize(10)
            hour.shape("blank")
            hour.right(((b.tm_hour + offset) % 12) * 30 + b.tm_min * 0.5 )
            hour.backward(30*SCALE)
            hour.forward(160*SCALE)

            #minute hand
            minute = turtle.Turtle()
            minute.speed(100)
            minute.shape("blank")
            minute.left(90)
            minute.pensize(6)
            minute.right((b.tm_min) * 6)
            minute.backward(30*SCALE)
            minute.forward(180*SCALE)

            update = False

      if updateSecond:
            #second hand
            second = turtle.Turtle()
            second.speed(100)
            second.shape("blank")
            second.color("red")
            second.left(90)
            second.pensize(3)
            second.right((b.tm_sec) * 6)
            second.backward(30*SCALE)
            second.forward(190*SCALE)
            updateSecond = False

      time.sleep(0.3)
      b = time.gmtime(time.time())
      new_min = b.tm_min
      new_sec = b.tm_sec

      if new_min != m:
            update = True
            hour.clear() # Clear out the drawing (if any)
            hour.reset()
            minute.clear()
            minute.reset()
      if new_sec != s:
            updateSecond = True
            second.clear()
            second.reset()
