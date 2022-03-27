import numpy as np
import cv2


# capture webcam image
cap = cv2.VideoCapture(0)

# get camera image parameters from get()
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
format = int(cap.get(cv2.CAP_PROP_FORMAT))
autofocus = int(cap.get(cv2.CAP_PROP_AUTOFOCUS))
zoom = int(cap.get(cv2.CAP_PROP_ZOOM))
focus = int(cap.get(cv2.CAP_PROP_FOCUS))

print('Video properties:')
print('  Width = ' + str(width))
print('  Height = ' + str(height))
print('  Format = ' + str(format))
print('  Autofocus = ' + str(autofocus))
print('  Zoom = ' + str(zoom))
print('  Focus = ' + str(focus))


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


# create a window for the video
title = 'Video image'
clicked_points = []
img = np.zeros((height, width, 3), np.uint8)
# Note that window parameters have no effect on MacOS
cv2.namedWindow(title,  cv2.WINDOW_FREERATIO)
cv2.setMouseCallback(title, click_frame)
print('Press q to close the window.')

# start a loop
while True:
    # read a camera frame
    ret, frame = cap.read()
    # check if capture was successful
    if (ret):
        # display the image
        img = frame
        # draw a circle around the clicked points
        for c in clicked_points:
            cv2.circle(img, c, 4, (0, 255, 0), 2)
        cv2.imshow(title, img)

        # press q to close the window
        if cv2.waitKey(10) == ord('q'):
            break
    else:
        print('Could not start video camera')
        break

# release the video capture object and window
cap.release()
cv2.destroyAllWindows()
