import cv2
import numpy as np

class Window:
    def __init__(self, width, height, r, mouse_color, circle_color, main=True):
        # get a frame
        self.frame = np.zeros((height, width, 3))

        # get the circles attributes
        self.r = r
        self.mouse_color = mouse_color
        self.circle_color = circle_color

        # create a variable to store the circles and the mouse position
        self.mouse_pos = (0, 0)
        self.circles = []

        # create a window interactive if asked
        if main:
            cv2.namedWindow('Main Window', cv2.WINDOW_NORMAL)
            cv2.setMouseCallback('Main Window', self.mouse_event)
        else:
            cv2.namedWindow('Client Window', cv2.WINDOW_NORMAL)

    def mouse_event(self, event, x, y, flags, param):
        # actualize the mouse position
        self.mouse_pos = (x, y)
        # add circle if left mouse button clicked (when released)
        if event == cv2.EVENT_LBUTTONUP:
            self.circles.append(self.mouse_pos)

    def update_frame(self):
        # reset the frame
        self.frame = self.frame * 0
        # draw the circles stored and the mouse position in the frame
        for circle in self.circles:
            cv2.circle(self.frame, circle, self.r, self.circle_color, -1)
        cv2.circle(self.frame, self.mouse_pos, self.r, self.mouse_color, -1)

    def to_dict(self):
        d = {}
        d['width'] = self.frame.shape[1]
        d['height'] = self.frame.shape[0]
        d['r'] = self.r
        b, g, r = self.mouse_color
        d['mouse_color'] = {'B':b, 'G':g, 'R':r}
        b, g, r = self.circle_color
        d['circle_color'] = {'B':b, 'G':g, 'R':r}
        d['mouse_pos'] = {'x': self.mouse_pos[0], 'y': self.mouse_pos[1]}
        d['circles'] = [{'x': x, 'y': y} for x, y in self.circles]
        return d

def from_dict(d):
    # get all the attributes from the dictionary
    width = d['width']
    height = d['height']
    r = d['r']
    d_col = d['mouse_color']
    mouse_color = (d_col['B'], d_col['G'], d_col['R'])
    d_col = d['circle_color']
    circle_color = (d_col['B'], d_col['G'], d_col['R'])
    mouse_pos = (d['mouse_pos']['x'], d['mouse_pos']['y'])
    # create the window and add the other missing attributes from __init__()
    circles = [(d_circle['x'], d_circle['y']) for d_circle in d['circles']]
    window = Window(width, height, r, mouse_color, circle_color, main=False)
    window.mouse_pos = mouse_pos
    window.circles = circles
    return window
