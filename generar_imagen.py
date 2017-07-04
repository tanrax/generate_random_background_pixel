import numpy as np
import time
from math import ceil
import scipy.misc as smp
from random import randint

WIDTH = 1600
HEIGHT = 2560
BORDER = 50
# Create a 1024x1024x3 array of 8 bit unsigned integers
data = np.zeros((WIDTH, HEIGHT, 3), dtype=np.uint8)

#data[512,512] = [254,0,0]       # Makes the middle pixel red
#data[512,513] = [0,0,255]       # Makes the next pixel blue
# First random pixel
data[0, 0] = [randint(0, 255), randint(0, 255), randint(0, 255)]

for x in range(0, WIDTH):
    for y in range(0, HEIGHT, BORDER):
        if y > 0:
            new_color = data[0, y - BORDER]
        else:
            new_color = data[0, 0]
        # Get one color
        pos = randint(0, 2)
        mod = new_color[pos] 
        # Mod comor
        if mod > 0 and mod < 255:
            mod = randint(-1, 1) + mod
        # Set color
        new_color[pos] = mod
        for num_border in range(BORDER):
            if y + num_border < HEIGHT:
                try:
                    data[x, y + num_border] = [new_color[0], new_color[1], new_color[2]]
                except:
                    print(y + num_border)
        
img = smp.toimage( data )       # Create a PIL image
#img.show()    
#name = str(ceil(time.time())) + '.png'
name = '/Users/androsfenollosa/Pictures/background-color.png'
img.save(name, "PNG")
