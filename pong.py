from sense_emu import SenseHat
sense = SenseHat()


import time


white = (255,255,255)
sense = SenseHat()
sense.clear()
msleep = lambda x: time.sleep(x /1000.0)

x = 4 # set variables
y = 5

sense.set_pixel(x,y,255,0,0) # display pixels

i = 1
j = 1

while x >= 0 and y >= 0 and x <= 7 and y <= 7:
  x += i
  y += j
  msleep(400) 
  sense.clear()
  sense.set_pixel(x,y,255,0,0)
  if x == 0 or x ==7:
    i = -i
  if y == 0 or y == 7:
    j = -j
