# load an image and find vanishing points
# Sources: https://docs.opencv.org/3.4/d6/d10/tutorial_py_houghlines.html
import cv2
import numpy as np


# load image
width = 1024
height = 768
img = cv2.imread('images/IMG_3234.JPEG', cv2.IMREAD_COLOR)
img = cv2.resize(img, (width, height))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
title = 'Original image'
cv2.imshow(title, img)
cv2.waitKey(0)
cv2.destroyWindow(title)

# canny edge detection (not in use)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
title = 'Canny edge detection'
cv2.imshow(title, edges)
cv2.waitKey(0)
cv2.destroyWindow(title)


# hough transform (not used)
# lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=90)
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
lines_img = img.copy()

# # draw the lines
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(lines_img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# show the image
title = 'Original image with lines'
cv2.imshow(title, lines_img)
cv2.waitKey(0)
cv2.destroyWindow(title)


def getIntersectionPosition(line1, line2):
    intersection = np.cross(line1, line2)
    intersection = intersection/intersection[2]
    return (round(intersection[0]), round(intersection[1]))


def click_frame(event, x, y, flags, param):
    # grab references to the global variables
    global clicked_points
    # if the left mouse button was clicked, add the point to the source array
    if event == cv2.EVENT_LBUTTONDOWN:
        pos = len(clicked_points)
        if (pos == 0):
            clicked_points = [(x, y)]
        else:
            clicked_points.append((x, y))
        cv2.circle(img, (x, y), 4, (0, 255, 0), 2)
        cv2.imshow(title, img)

        if (len(clicked_points) >= 2):
            # enough points are clicked, draw lines and compute intersection
            p1 = clicked_points[0]
            p2 = clicked_points[1]
            cv2.line(img, p1, p2, (255, 0, 0), 2)
            cv2.imshow(title, img)

        if (len(clicked_points) == 4):
            # enough points are clicked, draw lines and compute intersection
            p3 = clicked_points[2]
            p4 = clicked_points[3]
            cv2.line(img, p3, p4, (255, 0, 0), 2)
            cv2.imshow(title, img)
            p1h = [p1[0], p1[1], 1]
            p2h = [p2[0], p2[1], 1]
            p3h = [p3[0], p3[1], 1]
            p4h = [p4[0], p4[1], 1]
            line1 = np.cross(p1h, p2h)
            line2 = np.cross(p3h, p4h)
            intersectionPoint = getIntersectionPosition(line1, line2)
            cv2.circle(img, intersectionPoint, 6, (0, 255, 255), 2)
            cv2.imshow(title, img)
            print(intersectionPoint)


# create a window for the image
title = 'Click two lines'
clicked_points = []
img_orig = img.copy()
# Note that window parameters have no effect on MacOS
cv2.namedWindow(title,  cv2.WINDOW_FREERATIO)
cv2.setMouseCallback(title, click_frame)
cv2.imshow(title, img)

while True:
    key = cv2.waitKey(100)
    # press r to reset the clicked points
    if (key == ord('r')):
        clicked_points.clear()
        img = img_orig.copy()
        cv2.imshow(title, img)
    # press q to close the window
    if (key == ord('q')):
        cv2.destroyAllWindows()
        break
