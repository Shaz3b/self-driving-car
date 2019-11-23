#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

#PLT Issue
image = mpimg.imread('images/test.jpg')
print('This image is: ',type(image),
        'with dimensions:', image.shape)

ysize = image.shape[0]
xsize = image.shape[1]

color_select = np.copy(image)
region_select = np.copy(image)

left_bottom = [130, 535]
right_bottom = [790, 540]
apex = [480, 335]

red_thershold = 210
green_thershold = 210
blue_thershold = 210
rgb_thershold = [red_thershold,green_thershold,blue_thershold]

thersholds = (image[:,:,0] < rgb_thershold[0]) \
            |(image[:,:,1] < rgb_thershold[1]) \
            | (image[:,:,2] < rgb_thershold[2]) 
color_select[thersholds] = [0,0,0]

plt.imshow(color_select)
plt.show()

