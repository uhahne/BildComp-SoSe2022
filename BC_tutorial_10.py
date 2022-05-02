# Code inspired from
# OpenCV tutorial on stereo depthmaps https://docs.opencv.org/4.5.5/dd/d53/tutorial_py_depthmap.html
# and https://learnopencv.com/introduction-to-epipolar-geometry-and-stereo-vision/
import cv2
import numpy as np

# Reading the left and right images.
imgL = cv2.imread("images/tsukuba01.jpg", cv2.IMREAD_GRAYSCALE)
imgR = cv2.imread("images/tsukuba02.jpg", cv2.IMREAD_GRAYSCALE)

# Set parameters for block matching stereo
numDisparities = 64
blockSize = 9

# Create a simple block matching stereo computation object StereoBM_create
stereo = cv2.StereoBM_create(numDisparities=numDisparities, blockSize=blockSize)

# Setting parameters for StereoSGBM algorithm
minDisparity = 0
numDisparities = 64
blockSize = 8
disp12MaxDiff = 1
uniquenessRatio = 10
speckleWindowSize = 10
speckleRange = 8

# Creating an object of StereoSGBM algorithm
stereo = cv2.StereoSGBM_create(minDisparity=minDisparity,
                               numDisparities=numDisparities,
                               blockSize=blockSize,
                               disp12MaxDiff=disp12MaxDiff,
                               uniquenessRatio=uniquenessRatio,
                               speckleWindowSize=speckleWindowSize,
                               speckleRange=speckleRange)

# Calculate disparity using the chosen stereo algorithm
disp = stereo.compute(imgL, imgR).astype(np.float32)

# Normalie the disparity map in order to display it
disp = cv2.normalize(disp, 0, 255, cv2.NORM_MINMAX)

# Display the disparity map
cv2.imshow("disparity", disp)
cv2.waitKey(0)
