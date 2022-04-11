# load an image and find vanishing points
import operator
import cv2
import numpy as np


# load image
img = cv2.imread('images/IMG_3250.JPEG', cv2.IMREAD_COLOR)
height, width, _ = img.shape


# Compute intersection position using the cross product of two lines
def getIntersectionPosition(line1, line2):
    intersection = np.cross(line1, line2)
    intersection = intersection/intersection[2]
    return (round(intersection[0]), round(intersection[1]))


# callback function that contains the whole process
def click_frame(event, x, y, flags, param):
    # grab references to the global variables
    global clicked_points, vanishing_points
    # if the left mouse button was clicked, do the whole proces
    if event == cv2.EVENT_LBUTTONDOWN:
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
            # store the vanishing points after four clicks
            print(intersectionPoint)
            pos = len(vanishing_points)
            if (pos == 0):
                vanishing_points = [intersectionPoint]
            else:
                vanishing_points.append(intersectionPoint)

        if (len(vanishing_points) == 2):
            # DEBUG: vanishing_points = [(2260, -180), (-2076, -362)]

            # create an image that contains the vanishing points
            min_world_x = min(min(vanishing_points)[0], 0)
            max_world_x = max(max(vanishing_points)[0], width)
            min_world_y = min(min(vanishing_points, key=lambda x: x[1])[1], 0)
            max_world_y = max(max(vanishing_points, key=lambda x: x[1])[1], height)
            print('World min/max:', min_world_x, max_world_x, min_world_y, max_world_y)
            border = 50  # pixel border so that vanishing points are fully visible
            world_width = max_world_x - min_world_x + (border*2)
            world_height = max_world_y - min_world_y + (border*2)
            print('World size:', world_width, world_height)
            world_img = np.zeros((world_height, world_width, 3), np.uint8)

            # get original image region and vanishing points in world_img coordinates
            # world image is translated about min_world + border
            origin = (abs(min_world_x) + border, abs(min_world_y) + border)
            vanishing_point1 = tuple(map(operator.add, vanishing_points[0], origin))
            vanishing_point2 = tuple(map(operator.add, vanishing_points[1], origin))
            print('Origin:', origin)
            print('Width/Height:', width, height)
            print(img.shape)
            print('Vanishing points:', vanishing_point1, vanishing_point2)
            world_img[origin[1]:origin[1]+height, origin[0]:origin[0]+width, :] = img
            cv2.circle(world_img, vanishing_point1, 20, (255, 0, 255), -1)
            cv2.circle(world_img, vanishing_point2, 10, (0, 0, 255), -1)
            cv2.line(world_img, vanishing_point1, vanishing_point2, (0, 0, 255), 3, cv2.LINE_AA)
            cv2.imshow(title, world_img)


# create a window for the image
title = 'Computing the vanishing line'
clicked_points = []
real_clicked_points = []
vanishing_points = []
img_orig = img.copy()
# Note that window parameters have no effect on MacOS
cv2.namedWindow(title, cv2.WINDOW_GUI_NORMAL)
cv2.setMouseCallback(title, click_frame)
cv2.imshow(title, img)

while True:
    img = img_orig.copy()
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
