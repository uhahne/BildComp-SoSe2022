import exifread
import cv2
import numpy as np


# a function to compute a fraction given as string
def _derationalize(rational):
    all = rational.split('/')
    numerator = float(all[0])
    denominator = float(all[1])

    return numerator / denominator


# Open an jpg image file in order to read out the exif data
file_name = 'images/table_bottle_01.jpg'
f = open(file_name, 'rb')

# Get all Exif tags
tags = exifread.process_file(f, details=False)

# Read the EXIF FOcalLength tag and compute the value from it
for tag in tags.keys():
    if tag in ('EXIF FocalLength'):
        print("Key:", tag, "value:", tags[tag])
        focalLength_mm = _derationalize(tags[tag].__str__())

# print the computed focal length as float value
print(focalLength_mm)

# Close the file
f.close()

# Read the file as an OpenCV image
img = cv2.imread(file_name, cv2.IMREAD_COLOR)

# Extract image resolution
width, height, channels = img.shape

# Compute fx, fy using sensor size information as proposed here: http://phototour.cs.washington.edu/focal.html
# focal length in pixels = (image width in pixels) * (focal length in mm) / (CCD width in mm)
# Exemplary iPhone 8 image sensor size from https://www.dpreview.com/forums/thread/4206729 and
# https://en.wikipedia.org/wiki/Image_sensor_format#Table_of_sensor_formats_and_sizes
# Type  Diagonal (mm) 	Width (mm) 	Height (mm) 	Aspect Ratio
# 1/3"  6.00 	        4.80       	3.60        	4:3
sensor_width_mm = 4.8
sensor_height_mm = 3.6
fx = width * focalLength_mm / sensor_width_mm
fy = height * focalLength_mm / sensor_height_mm
cx = width / 2.0
cy = height / 2.0

# define camera intrinsic matrix K
K = np.zeros((3, 3), np.float32)
K[0, 0] = fx
K[1, 1] = fy
K[0, 2] = cx
K[1, 2] = cy
K[2, 2] = 0.0

print(K)
