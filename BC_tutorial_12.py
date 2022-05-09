# Code adapted from https://docs.opencv2.org/4.5.5/da/de9/tutorial_py_epipolar_geometry.html
# and https://www.andreasjakl.com/understand-and-apply-stereo-rectification-for-depth-maps-part-2/
import cv2
import numpy as np


# load left and right images
img1 = cv2.imread('images/table_left.jpg', 0)  # queryimage # left image
img2 = cv2.imread('images/table_right.jpg', 0)  # trainimage # right image
title = 'Bildverarbeitung und Computergrafik'
cv2.namedWindow(title, cv2.WINDOW_GUI_NORMAL)

# find the keypoints and descriptors using SIFT_create
sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)
print('We found %d keypoints in the left image.' % len(kp1))
print('We found %d keypoints in the right image.' % len(kp2))
print('Each SIFT keypoint is described with a %s-dimensional array' % des1.shape[1])
# Visualize the SIFT keypoints
imgSift = cv2.drawKeypoints(
    img1, kp1, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow(title, imgSift)
cv2.waitKey(0)

# match the keypoints using a FlannBasedMatcher
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1, des2, k=2)
matchesMask = [[0, 0] for i in range(len(matches))]
pts1 = []
pts2 = []

# ratio test as per Lowe's paper - only use matches with a reasonable small distance
for i, (m, n) in enumerate(matches):
    if m.distance < 0.8*n.distance:
        matchesMask[i] = [1, 0]
        pts2.append(kp2[m.trainIdx].pt)
        pts1.append(kp1[m.queryIdx].pt)

# Now we have the list of best matches from both the images. Let's find the Fundamental Matrix.
pts1 = np.int32(pts1)
pts2 = np.int32(pts2)
assert(len(pts1) == len(pts2))
print('We found %d matching keypoints in both images.' % len(pts1))

# Now we compute the fundamental matrix
F, mask = cv2.findFundamentalMat(pts1, pts2, cv2.FM_RANSAC)
print('\nFundamental matrix\n', '\n'.join(['\t'.join(
    ['%03.4f' % cell for cell in row]) for row in F]))

# Visualize the epilines
# We select only inlier points
pts1 = pts1[mask.ravel() == 1]
pts2 = pts2[mask.ravel() == 1]


# Next we find the epilines. Epilines corresponding to the points
# in first image is drawn on second image. So mentioning of correct
# images are important here. We get an array of lines. So we define
# a new function to draw these lines on the images.
def drawlines(img1, img2, lines, pts1, pts2):
    ''' img1 - image on which we draw the epilines for the points in img2
        lines - corresponding epilines '''
    r, c = img1.shape
    img1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
    img2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)
    for r, pt1, pt2 in zip(lines, pts1, pts2):
        color = tuple(np.random.randint(0, 255, 3).tolist())
        x0, y0 = map(int, [0, -r[2]/r[1]])
        x1, y1 = map(int, [c, -(r[2]+r[0]*c)/r[1]])
        img1 = cv2.line(img1, (x0, y0), (x1, y1), color, 1)
        img1 = cv2.circle(img1, tuple(pt1), 5, color, -1)
        img2 = cv2.circle(img2, tuple(pt2), 5, color, -1)
    return img1, img2


# Now we find the epilines in both the images and draw them.
# Find epilines corresponding to points in right image (second image) and
# drawing its lines on left image
lines1 = cv2.computeCorrespondEpilines(pts2.reshape(-1, 1, 2), 2, F)
lines1 = lines1.reshape(-1, 3)
img5, img6 = drawlines(img1, img2, lines1, pts1, pts2)

# Find epilines corresponding to points in left image (first image) and
# drawing its lines on right image
lines2 = cv2.computeCorrespondEpilines(pts1.reshape(-1, 1, 2), 1, F)
lines2 = lines2.reshape(-1, 3)
img3, img4 = drawlines(img2, img1, lines2, pts2, pts1)
cv2.imshow(title, np.concatenate((img3, img5), axis=1))
cv2.waitKey(0)
