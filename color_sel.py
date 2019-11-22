#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


image = mpimg.imread('test.jpg')
print('This image is: ',type(image),
        'with dimensions:', image.shape)

ysize = image.shape[0]
xsize = image.shape[1]

color_select = np.copy(image)

red_thershold = 0
green_thershold = 0
blue_thershold = 0
rgb_thershold = [red_thershold,green_thershold,blue_thershold]

thersholds = (image[:,:,0] < rgb_thershold[0]) \
            |(image[:,:,1] < rgb_thershold[1]) \
            | (image[:,:,2] < rgb_thershold[2]) 
color_select[thersholds] = [0,0,0]

plt.imshow(color_select)
plt.show()

               



