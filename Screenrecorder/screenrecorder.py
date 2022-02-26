import pyautogui
import numpy as np
import cv2


#Specifying the screen resolution with pyautogui
resolution = (1366, 768)

#instantiating an object of the video codec with cv2
codec = cv2.VideoWriter_fourcc(*"XVID")


#Specifying the name of the output file
filename = "Recording.avi"


'''
Specifying the frame rate per second
'''
fps = 60.0

#instantiating the videowriter object
out = cv2.VideoWriter(filename, codec, fps, resolution)

cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Live", 480, 270)

while True:
    # Take the screenshot using Pyautogui
    image = pyautogui.screenshot()

    # Convert the screenshot to numpy array
    frame = np.array(image)


    '''
    convert the frame color(BGR) to RGB
    '''
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #Write it to the output file
    out.write(frame)

    cv2.imshow("Live", frame)

    #Stop recording when 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video writer
out.release()

#Destroy all windows
cv2.destroyAllWindows()