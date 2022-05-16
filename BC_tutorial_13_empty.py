# inspiration (delete seam code copied) from https://github.com/margaret/seam-carver/blob/master/seam_carver.py
import cv2
import numpy as np

# load image
img = cv2.imread('images/halong-bay.jpg', cv2.IMREAD_GRAYSCALE)

# global parameters
delay = 100  # delay in ms before next seam is removed
shrink_factor = 2  # decrease image size by this factor
title = "Dynamic programming"  # window title
visualize_energy = True  # set true in order to visualize the energy images once

img = cv2.resize(img, (0, 0), fx=1/shrink_factor, fy=1/shrink_factor)
rows, cols = img.shape


def calculateEnergySobel(img):
    return np.abs(cv2.Sobel(img, cv2.CV_32FC1, 1, 1, borderType=cv2.BORDER_REPLICATE))


# TODO compute accumulated energy image
def calculateAccumulatedImage(_img):
    


# remove all seams until the last ten in a loop
for i in range(cols - 10):
    # compute energy image
    energy = calculateEnergySobel(img)

    if visualize_energy:
        # normalize and visualize summation image
        normalized_energy = np.zeros(energy.shape, np.uint8)
        normalized_energy = cv2.normalize(energy, normalized_energy, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)

        cv2.imshow(title, normalized_energy)
        cv2.waitKey(0)

    # get accumulated energy
    acc_energy = calculateAccumulatedImage(energy)

    if visualize_energy:
        normalized_acc_energy = np.zeros(acc_energy.shape, np.uint8)
        normalized_acc_energy = cv2.normalize(acc_energy, normalized_acc_energy, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)

        cv2.imshow(title, normalized_acc_energy)
        cv2.waitKey(0)
        visualize_energy = False

    # TODO find path with minimal energy from bottom to top
    # HINT init data structures (exemplary)
    min_path = np.zeros(img.shape, np.bool8)  # an image with the seam
    seam = [0] * rows  # an array with the seam column indices
    # HINT find pixel/column with minimal accumulated energy in last row
    
    # HINT find connected path with min accumulated energy
    # the path upwards has only up to three possible directions: up-left, up, up-right
    

    # TODO show path in img
    
    # remove path
    new_img = np.array([np.delete(img[row], seam[row], axis=0) for row in range(rows)])
    

    # allow the user to abort by pressing q
    

    # set the new image to be the next image
    img = new_img
