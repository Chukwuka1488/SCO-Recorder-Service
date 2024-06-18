import cv2

# Reads video streams from a specified local source.
cap_file = cv2.VideoCapture('earth_video.mp4')
print(type(cap_file))
# <class 'cv2.VideoCapture'>

# check if it is successfully read with the isOpened() method. 
# If there is no problem, True is returned.
print(cap_file.isOpened())

# frame width
print(cap_file.get(cv2.CAP_PROP_FRAME_WIDTH))

# frame height
print(cap_file.get(cv2.CAP_PROP_FRAME_HEIGHT))

# frames per second
print(cap_file.get(cv2.CAP_PROP_FPS))

# no of frames
print(cap_file.get(cv2.CAP_PROP_FRAME_COUNT))


cap_file.release()