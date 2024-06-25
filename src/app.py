from flask import Flask, request, jsonify, render_template, redirect, url_for
import socket
import os
from video_utils import VideoProcessor
from display_video import VideoDisplayer
import logging
from datetime import datetime
from werkzeug.utils import secure_filename
import json

app = Flask(__name__)
# Define the path to the new directory
new_dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Videos')

# Create the new directory
os.makedirs(new_dir_path, exist_ok=True)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Now parameterizable via environment variable
output_dir = os.getenv('OUTPUT_DIR', 'src/output_frames')

# Now parameterizable via environment variable
num_frames = int(os.getenv('NUM_FRAMES', 20))

last_uploaded_video = None

# Function to get hostname and IP
def fetch_details():
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
    except socket.gaierror as e:
        app.logger.error(f'Invalid hostname, error raised is {e}')
        hostname, ip = "Unknown", "Unknown"
    return str(hostname), str(ip)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/health")
def health():
    return jsonify(status="WE ARE UP AND RUNNING! 😆 🤌 🙈")


@app.route("/details")
def details():
    hostname, ip = fetch_details()
    return render_template('index.html', HOSTNAME=hostname, IP=ip)


@app.route('/upload_metadata', methods=['POST'])
def upload_metadata():
    global last_uploaded_video
    # Check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    # If user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file:
        filename = secure_filename(file.filename)
        video_path = os.path.join(new_dir_path, filename)  # Use the new directory path
        file.save(video_path)
        last_uploaded_video = video_path

    metadata = {
        "cashier_id": request.form.get('cashier_id'),
        "transaction_id": request.form.get('transaction_id'),
        "timestamp": datetime.now().isoformat()  # Auto-generate timestamp
    }

    if not metadata:
        return jsonify({"error": "metadata is required"}), 400

    app.logger.debug(f"Received request with video_path: {video_path} and metadata: {metadata}")

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        # Create an instance of VideoProcessor
        video_processor = VideoProcessor(video_path)

        # Capture the frames
        frames = video_processor.capture_last_frames(num_frames)

        # Encode the frames
        encoded_frames = video_processor.encode_frames(frames)

        # Create a timestamped ZIP file name
        zip_name = video_processor.timestamped_zip_name()

        # Add the ZIP file name to the metadata
        metadata['zip_name'] = zip_name

        # Create the ZIP file with frames and metadata
        zip_path = video_processor.create_zip(output_dir, zip_name, encoded_frames, metadata)

        # Read existing data from the JSON file
        json_file_path = os.path.join(output_dir, 'metadata.json')
        if os.path.exists(json_file_path):
            with open(json_file_path, 'r') as f:
                existing_data = json.load(f)
                if not isinstance(existing_data, list):  # Check if existing_data is not a list
                    existing_data = []  # Initialize existing_data to an empty list
        else:
            existing_data = []

        # Append the new metadata to the existing data
        existing_data.append(metadata)

        # Write the updated data back to the JSON file
        with open(json_file_path, 'w') as f:
            json.dump(existing_data, f)

        app.logger.debug(f"ZIP file created: {zip_path}")

        return redirect(url_for('show_result', zip_path=zip_path))

    except Exception as e:
        app.logger.error(f"Error processing video: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route('/result')
def show_result():
    zip_path = request.args.get('zip_path')
    if zip_path:
        app.logger.debug(f"Displaying result for ZIP path: {zip_path}")
    else:
        app.logger.error("ZIP path is missing in the request")
    return render_template('result.html', ZIP_PATH=zip_path)


@app.route('/display_video', methods=['GET', 'POST'])
def display_video():
    global last_uploaded_video  # Use the global variable
    if not last_uploaded_video:
        return jsonify({"error": "No video has been uploaded yet"}), 400

    app.logger.debug(f"Received request to display video: {last_uploaded_video}")

    # Display the video (not necessary for frame capturing)
    video_displayer = VideoDisplayer(last_uploaded_video)
    video_displayer.display_video()

    return jsonify({"message": "Video displayed"}), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7100)
