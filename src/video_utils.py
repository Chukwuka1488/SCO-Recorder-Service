import cv2 as cv
import os
import zipfile
import json
from datetime import datetime


class VideoProcessor:
    def __init__(self, video_path):
        self.video_path = video_path
        self.cap = self.open_video()
        self.frame_count = self.get_frame_count()

    def open_video(self):
        cap = cv.VideoCapture(self.video_path)
        if not cap.isOpened():
            raise IOError(f"Error opening video file '{self.video_path}'")
        return cap

    def get_frame_count(self):
        return int(self.cap.get(cv.CAP_PROP_FRAME_COUNT))

    def capture_last_frames(self, num_frames):
        frames = []
        for i in range(max(0, self.frame_count - num_frames), self.frame_count):
            self.cap.set(cv.CAP_PROP_POS_FRAMES, i)
            ret, frame = self.cap.read()
            if not ret:
                raise IOError(f"Error reading frame {i}")
            frames.append(frame)
        return frames

    @staticmethod
    def encode_frames(frames):
        encoded_frames = []
        for i, frame in enumerate(frames):
            _, buffer = cv.imencode('.png', frame)
            byte_frame = buffer.tobytes()
            encoded_frames.append((f"frame_{i}.png", byte_frame))
        return encoded_frames

    @staticmethod
    def create_zip(output_dir, zip_name, encoded_frames, metadata):
        zip_path = os.path.join(output_dir, zip_name)
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            # Add frames to the ZIP file
            for filename, data in encoded_frames:
                zipf.writestr(filename, data)
            # Add metadata to the ZIP file
            metadata_filename = 'metadata.json'
            zipf.writestr(metadata_filename, json.dumps(metadata))
        return zip_path

    @staticmethod
    def timestamped_zip_name():
        timestamp = datetime.now().strftime("%d_%m_%y_%H_%M_%S")
        return f"{timestamp}_last_20_frames.zip"
