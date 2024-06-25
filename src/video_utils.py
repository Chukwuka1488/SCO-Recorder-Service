import cv2 as cv
import os
import zipfile
from datetime import datetime
import io


def open_video(video_path):
    cap = cv.VideoCapture(video_path)
    if not cap.isOpened():
        raise IOError(f"Error opening video file '{video_path}'")
    return cap


def get_frame_count(cap):
    return int(cap.get(cv.CAP_PROP_FRAME_COUNT))


def capture_last_frames(cap, num_frames):
    frame_count = get_frame_count(cap)
    frames = []
    for i in range(max(0, frame_count - num_frames), frame_count):
        cap.set(cv.CAP_PROP_POS_FRAMES, i)
        ret, frame = cap.read()
        if not ret:
            raise IOError(f"Error reading frame {i}")
        frames.append(frame)
    return frames


def encode_frames(frames):
    encoded_frames = []
    for i, frame in enumerate(frames):
        _, buffer = cv.imencode('.jpg', frame)
        byte_frame = buffer.tobytes()
        encoded_frames.append((f"frame_{i}.jpg", byte_frame))
    return encoded_frames


def create_zip(output_dir, zip_name, encoded_frames):
    zip_path = os.path.join(output_dir, zip_name)
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for filename, data in encoded_frames:
            zipf.writestr(filename, data)
    return zip_path


def timestamped_zip_name():
    timestamp = datetime.now().strftime("%d_%m_%y_%H_%M_%S")
    return f"{timestamp}_last_20_frames.zip"
