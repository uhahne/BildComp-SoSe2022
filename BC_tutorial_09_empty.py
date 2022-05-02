# load an image and find vanishing points
import operator
import cv2
import numpy as np


# load image
img = cv2.imread('images/table_bottle_01.jpg', cv2.IMREAD_COLOR)
height, width, _ = img.shape


# Compute intersection position using the cross product of two lines
def getIntersectionPosition(line1, line2):
    intersection = np.cross(line1, line2)
    intersection = intersection/intersection[2]
    return (round(intersection[0]), round(intersection[1]))


# TODO Implement callback function that contains the whole process

# TODO Create a large image that contains the vanishing points

# TODO Draw the original image region and vanishing points in the large image

# TODO Draw the vanishing line between

# TODO create a window for the image
