#This file will generate a random image and a balck image
import numpy as np
import scipy.misc as smp


width = int(raw_input('Width: '))
height = int(raw_input('Height: '))

#random image
data = np.random.randint(255, size=(height, width, 3))

img = smp.toimage( data )       # Create a PIL image
img.save('noise.png')

#black image
data = np.zeros( (height,width,3), dtype=np.uint8 )
img = smp.toimage( data )       # Create a PIL image
img.save('black.png')

