import cv2 as cv
from rescale import rescale_frame


def display_video(video_path):
    """
    Displays the video specified by the `video_path` and a resized version of it.

    Parameters:
    - video_path (str): Path to the video file.
    """
    capture = cv.VideoCapture(video_path)

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
