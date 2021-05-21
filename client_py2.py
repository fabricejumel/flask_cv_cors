import json
import urllib

import cv2

from window import from_dict

HOST, PORT = '127.0.0.1', 5000
# get the url as a string
#url = f'http://{HOST}:{PORT}/'
url = "http://{}:{}/".format(HOST, PORT)

def get_data_to_dict(url):
    # open url
    oper_url = urllib.urlopen(url)
    if(oper_url.getcode()==200):
        # get data and convert it to dictionary
        data = oper_url.read()
        return json.loads(data)
    else:
       print("Error receiving data", oper_url.getcode())
       return None


if __name__ == '__main__':
    while True:
        # get the data from the API as a dictionary
        d = get_data_to_dict(url)
        # if exists, recreate the window
        if d is not None:
            window_from_api = from_dict(d)
            window_from_api.update_frame()
            cv2.imshow('Client Window', window_from_api.frame)
        # exit the program by pressing 'q' key
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
