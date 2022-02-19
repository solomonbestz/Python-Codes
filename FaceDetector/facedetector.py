import cv2
from random import randrange

# load some pre-trained data on face frontals from opencv 
trained_face_data = cv2.CascadeClassifier('FaceDetector/haarcascade_frontalface_default.xml')

# Choose an image to detect faces in
# img = cv2.imread('FaceDetector/sol.jpg')

# Instatiate an object of the cv2 video cam
my_webcam = cv2.VideoCapture(0)


while True:
    # First variable reads true if the cam is visible while the second variable saves the frame in the frame variable
    successful_read_frame, frame = my_webcam.read()

    # Must convert to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    # Detect the coordinates of frontal Faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    # loops through the coordinates if more than on list is avaliable
    for n in range(len(face_coordinates)):
        # saves the four coordinate value in a tuple
        (top_x, top_y, bottom_x, bottom_y) = face_coordinates[0]
        # print(face_coordinates[n])

        # Creates a coloured rectangle shape round the face coordinates
        cv2.rectangle(frame, (top_x, top_y), (top_x+bottom_x, top_y+bottom_y), (randrange(1, 255), randrange(1, 255), randrange(1, 255)), 3)

    #show image
    cv2.imshow('Bestz Face detector', frame)
    # The wait key waits until a key is pressed
    key = cv2.waitKey(1)

    """ Using the ascii code number of Q which is 81 and q which is 113
        we can quit the program out of the loop when done.
    """
    if key==81 or key==113:
        break

#Release the videoCapture object
my_webcam.release()


print("Code Completed")