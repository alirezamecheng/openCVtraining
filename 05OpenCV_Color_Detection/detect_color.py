# tutorial from: https://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/

# OpenCV and Python Color Detection
# USAGE:
# $ python detect_color_py --image pokemon_games.png

import numpy as np 
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", help="path to the image")
args = vars(ap.parse_args())

# loading image
image = cv2.imread(args["image"])

# """
# All we are doing here is defining a list of boundaries in the RGB color space 
# (or rather, BGR, since OpenCV represents images as NumPy arrays in reverse order), 
# where each entry in the list is a tuple with two values: a list of lower limits and 
# a list of upper limits.

# For example, let’s take a look at the tuple ([17, 15, 100], [50, 56, 200]) .

# Here, we are saying that all pixels in our image that have a R >= 100, B >= 15, 
# and G >= 17 along with R <= 200, B <= 56, and G <= 50 will be considered red.
# """

# define the list of boundaries
boundaries = [
	([17, 15, 100], [50, 56, 200]),
	([86, 31, 4], [220, 88, 50]),
	([25, 146, 190], [62, 174, 250]),
	([103, 86, 65], [145, 133, 128])
]

# loop over the boundaries
for (lower, upper) in boundaries:
    # create Numpy arrays from the boundaries
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper,dtype="uint8")

    # """
    # The cv2.inRange  function expects three arguments: the first is the image  
    # were we are going to perform color detection, the second is the lower  limit 
    # of the color you want to detect, and the third argument is the upper  limit of 
    # the color you want to detect.

    # After calling cv2.inRange, a binary mask is returned, where white pixels (255) 
    # represent pixels that fall into the upper and lower limit range and black pixels
    # (0) do not.

    # To create the output image, we apply our mask on Line 61. This line simply makes 
    # a call to cv2.bitwise_and, showing only pixels in the image that have a corresponding 
    # white (255) value in the mask.
    # """
    # finding the color within the specified boundaries and apply the mask
    mask = cv2.inRange(image, lower,upper)
    output = cv2.bitwise_and(image,image,mask=mask)

    # show the image 
    cv2.imshow("images",np.hstack([image,output]))
    cv2.waitKey(0)