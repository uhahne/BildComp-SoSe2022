# Code adapted from https://docs.opencv2.org/4.5.5/da/de9/tutorial_py_epipolar_geometry.html
# and https://www.andreasjakl.com/understand-and-apply-stereo-rectification-for-depth-maps-part-2/
import cv2
import numpy as np


# TODO load left and right images

# TODO find the keypoints and descriptors using SIFT_create

# TODO Visualize the SIFT keypoints

# TODO match the keypoints using a FlannBasedMatcher

# TODO ratio test as per Lowe's paper - only use matches with a reasonable small distance

# Now we have the list of best matches from both the images.
# TODO Compute the Fundamental Matrix.

# TODO Visualize the epilines
