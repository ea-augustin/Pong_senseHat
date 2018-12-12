#!/usr/bin/python
# coding: utf-8
try:
    from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
    sense = SenseHat()
except:
    from sense_emu import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
    sense = SenseHat()

import time

# create variables

x = 4
y = 4 #position of the ball


# Draw the raquette

raqy1 = 0
raqy2 = 1
raqy3 = 2

raqFactor = 1


#Move the  raquette

tSleep = lambda x: time.sleep(x / 1000.0)

def drawRaq():
    sense.set_pixel(0, raqy1,(0,255,0))
    sense.set_pixel(0, raqy2,(0,255,0))
    sense.set_pixel(0, raqy3,(0,255,0))

# draw the ball
def drawBall():
    sense.set_pixel(x,y,(255,0,0))
    
#move the Raquette up

def moveRaqDown(e):
    global raqy1
    global raqy2
    global raqy3
    if (raqy3 <= 7 and raqy1 >= 0) and e.action == ACTION_PRESSED:
        if raqy3 == 7:
            raqy3 = 7
            raqy2 = 6
            raqy1 = 5
        else:
            raqy1 += 1
            raqy2 += 1
            raqy3 += 1
            
#Move the Raquette down
        
def moveRaqUp(e):
    global raqy1
    global raqy2
    global raqy3
    if (raqy3 <= 7 and raqy1 >= 0) and e.action == ACTION_PRESSED:
        if raqy1 == 0:
            raqy1 = 0
            raqy2 = 1
            raqy3 = 2
        else:
            raqy1 -= 1
            raqy2 -= 1
            raqy3 -= 1
            
#Move the bal

i = 1
j = 1
def moveBall():
    global x
    global y
    global i
    global j
    global raqy1
    global raqy2
    global raqy3
    x += i
    y += j
    #rebondire si on touche un mur en X ou la raquette
    if x >=7 or (x <= 1 and (y <= raqy3+1 and y >= raqy1-1)):
        i *= -1
        #si on touche la raquette sur l'angle
        if (y == raqy3+1 or y == raqy1-1) and x == 1:
            j *= -1
    #si on touche un mur en Y        
    if y <= 0 or y >= 7:
        j *= -1


while True:
    tSleep(100)
    sense.clear()
    drawBall()
    moveBall()
    drawRaq()
    sense.stick.direction_down = moveRaqDown
    sense.stick.direction_up = moveRaqUp
    #stopper quand X sort du côté de la raquette sans la toucher
    if x <=0 and not (y <= raqy3 and y >= raqy1):
        tSleep(100)
        sense.clear()
        drawBall()
        tSleep(500)
        sense.clear()
        break
