import numpy as np
import cv2


# capture webcam image
cap = cv2.VideoCapture(0)

# TODO get camera image parameters (width, height, format, autofocus, ...) from get()



# TODO implement a callback function for the mouse clicks that store the clicked positions



# TODO create a window for the video with a mouse callback definition


# start a loop
while True:
    # read a camera frame
    ret, frame = cap.read()
    # check if capture was successful
    if (ret):
        # display the image
        img = frame
        # TODO draw a circle around the clicked points
       
        # TODO display the image

        # press q to close the window
        if cv2.waitKey(10) == ord('q'):
            break
    else:
        print('Could not start video camera')
        break

# release the video capture object and window
cap.release()
cv2.destroyAllWindows()
