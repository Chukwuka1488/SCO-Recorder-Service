from flask import Flask, jsonify, render_template
import socket
import sys

app = Flask(__name__)



# function to get hostname and ip
def fetchDetails():

    # IP lookup from hostname
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
    except socket.gaierror as e:
        print(f'Invalid hostname, error raised is {e}')

    return str(hostname), str(ip)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# as a check to know if our app is up and running
@app.route("/health")
def health():
	return jsonify(status="WE ARE UP AND RUNNING! 😆 🤌 🙈")

@app.route("/details")
def details():
    # tuple unpacking
    hostname, ip = fetchDetails()
    return render_template('index.html', HOSTNAME=hostname, IP=ip)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7000)









# import cv2
# import json
# import os
# from flask import Flask, request

# app = Flask(__name__)

# VIDEO_PATH = 'earth_video.mp4'
# OUTPUT_DIR = 'output/'
# NUM_FRAMES = 10

# def capture_frames(video_path, num_frames):
#     """
#     Captures the last `num_frames` frames from the video located at `video_path`.

#     Parameters:
#     - video_path (str): Path to the video file.
#     - num_frames (int): Number of frames to capture.

#     Returns:
#     - frames (list): List of captured frames (numpy arrays).
#     """
#     frames = []
#     try:
#         cap = cv2.VideoCapture(video_path)
#         if not cap.isOpened():
#             raise IOError(f"Error opening video file '{video_path}'")
        
#         # Get the total number of frames in the video
#         frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
#         # Capture the last `num_frames` frames
#         for i in range(max(0, frame_count - num_frames), frame_count):
#             cap.set(cv2.CAP_PROP_POS_FRAMES, i)
#             ret, frame = cap.read()
#             if not ret:
#                 raise IOError(f"Error reading frame {i} from video '{video_path}'")
#             frames.append(frame)
        
#         cap.release()
#     except Exception as e:
#         # Log the error
#         app.logger.error(f"Error capturing frames: {str(e)}")
#         frames = []
    
#     return frames

# @app.route('/store', methods=['POST'])
# def store_frames():
#     """
#     Endpoint to receive metadata via POST request and store frames with metadata.
#     """
#     try:
#         metadata = request.json
#         if not metadata:
#             raise ValueError("No JSON data received")
        
#         # Capture frames only if specific metadata key is present and has desired value
#         if 'trigger_capture' in metadata and metadata['trigger_capture'] == True:
#             frames = capture_frames(VIDEO_PATH, NUM_FRAMES)
#             if not frames:
#                 raise IOError("Failed to capture frames")
            
#             if not os.path.exists(OUTPUT_DIR):
#                 os.makedirs(OUTPUT_DIR)
            
#             for i, frame in enumerate(frames):
#                 cv2.imwrite(os.path.join(OUTPUT_DIR, f'frame_{i}.png'), frame)
            
#             with open(os.path.join(OUTPUT_DIR, 'metadata.json'), 'w') as f:
#                 json.dump(metadata, f)
            
#             return 'Frames and metadata stored successfully', 200
#         else:
#             return 'No action triggered', 200
    
#     except ValueError as ve:
#         app.logger.error(f"ValueError: {str(ve)}")
#         return 'Error: Invalid JSON data', 400
    
#     except IOError as ioe:
#         app.logger.error(f"IOError: {str(ioe)}")
#         return 'Error: Failed to capture frames', 500
    
#     except Exception as e:
#         app.logger.error(f"Unexpected error: {str(e)}")
#         return 'Error: Internal server error', 500

# @app.route('/metadata', methods=['POST'])
# def receive_metadata():
#     """
#     Endpoint to receive metadata from the SCO system via POST request.
#     """
#     try:
#         metadata = request.json
#         if not metadata:
#             raise ValueError("No JSON data received")
        
#         # Process the received metadata (e.g., validate, store in database, etc.)
#         app.logger.info(f"Received metadata: {json.dumps(metadata)}")
        
#         # Trigger frame capture process by sending metadata to /store endpoint
#         response = requests.post('http://localhost:8000/store', json=metadata)
#         if response.status_code == 200:
#             return 'Metadata received and frames triggered for capture', 200
#         else:
#             return 'Error triggering frame capture', 500
    
#     except ValueError as ve:
#         app.logger.error(f"ValueError: {str(ve)}")
#         return 'Error: Invalid JSON data', 400
    
#     except Exception as e:
#         app.logger.error(f"Unexpected error: {str(e)}")
#         return 'Error: Internal server error', 500

# if __name__ == '__main__':
#     # Set up logging
#     import logging
#     logging.basicConfig(filename='app.log', level=logging.INFO)
#     app.logger.addHandler(logging.StreamHandler())
    
#     # Run the Flask app on host '0.0.0.0' (accessible from outside) and port 8000
#     app.run(host='0.0.0.0', port=8000)
