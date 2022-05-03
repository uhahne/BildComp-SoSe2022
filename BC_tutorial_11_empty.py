import exifread
import cv2
import numpy as np


# TODO Define  a function to compute a fraction given as string

# TODO Open an jpg image file in order to read out the exif data

# TODO Get all Exif tags

# TODO Read the EXIF FocalLength tag and compute the value from it

# TODO print the computed focal length as float value

# TODO Close the file

# TODO Read the file as an OpenCV image

# TODO Extract image resolution

# TODO Compute fx, fy, cx, cy using sensor size information as proposed here:
# http://phototour.cs.washington.edu/focal.html
# focal length in pixels = (image width in pixels) * (focal length in mm) / (CCD width in mm)
# Exemplary iPhone 8 image sensor size from https://www.dpreview.com/forums/thread/4206729 and
# https://en.wikipedia.org/wiki/Image_sensor_format#Table_of_sensor_formats_and_sizes
# Type  Diagonal (mm) 	Width (mm) 	Height (mm) 	Aspect Ratio
# 1/3"  6.00 	        4.80       	3.60        	4:3

# TODO define camera intrinsic matrix K

# TODO print(K)
