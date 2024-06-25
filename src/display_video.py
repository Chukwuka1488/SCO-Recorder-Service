import cv2 as cv
from rescale import rescale_frame

class VideoDisplayer:
    def __init__(self, video_path):
        self.video_path = video_path

    def display_video(self):
        capture = cv.VideoCapture(self.video_path)
        while True:
            isTrue, frame = capture.read()
            if not isTrue:
                break

            frame_resized = rescale_frame(frame)

            cv.imshow('Video', frame)
            cv.imshow('Video Resized', frame_resized)

            if cv.waitKey(20) & 0xFF == ord('d'):
                break

        capture.release()
        cv.destroyAllWindows()
