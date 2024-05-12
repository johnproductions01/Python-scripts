import rotatescreen
import time
import random
screen = rotatescreen.get_primary_display()
for i in range(5):
    screen.rotate_top(i*90 % 360)