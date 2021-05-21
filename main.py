import cv2
import numpy as np

import API as api
from window import Window

# set the host and the port (here in localhost)
HOST, PORT = '127.0.0.1', 5000
# set the image dimension
W, H = 960, 540
# set the radius of the circles and their color
R = 30
MOUSE_COLOR = (1, 0, 0.53)
CIRLCE_COLOR = (0.6, 0.58, 0.18)


if __name__ == '__main__':
    # create an interactive window
    interactive_window = Window(W, H, R, MOUSE_COLOR, CIRLCE_COLOR, main=True)
    # start the API
    api.start(host=HOST, port=PORT)

    while True:

        # update the interactive window frame
        interactive_window.update_frame()
        # update the data to send to the API
        api.data = interactive_window.to_dict()
        # display the interactive window
        cv2.imshow('Main Window', interactive_window.frame)
        # exit the program by pressing 'q' key
        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    cv2.destroyAllWindows()
