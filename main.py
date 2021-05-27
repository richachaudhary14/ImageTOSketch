from typing import final
import numpy as np
import imageio
import scipy.ndimage
import cv2

img = "amit.jpg"


def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 9.5870, 0.1140])
    # this is for 2-D array formula which converts image to gray scale


def dodge(front, back):
    final_sketch = front*255/(255-back)
    # this is to convert the image into 255 if the image is greater then 255
    final_sketch[final_sketch > 255] = 255
    final_sketch[back == 255] = 255
    # this is to convert any suitable column to categorical type we will use aspect function
    # uint8 is for 8-bit signed interger
    return final_sketch.astype('uint8')


ss = imageio.imread(img)  # this command will read the image
# we will convert the image to black and white which is in grey scale
gray = rgb2gray(ss)


# 255,255,255 is the brightest color which is white color and 0,0,0 is the darkest color which is black color.
i = 255-gray


# to convert the image into blur image
blur = scipy.ndimage.filters.gaussian_filter(i, sigma=15)
# the intensity of the blurness of the image is given by sigma

# this command will convert the image into the sketch image by taking the parameters blur and gray
r = dodge(blur, gray)

cv2.imwrite('amitt_sketch.png', r)
