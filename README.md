# SCO-Recorder-Service
This project implements a recorder service designed to capture and store video frames from a Self-Checkout (SCO) camera along with metadata received from a cashier system. 

Sure, here's a concise and clear description for your GitHub repository:

---

### SCO-Recorder-Service

This project implements a recorder service designed to capture and store video frames from a Self-Checkout (SCO) camera along with metadata received from a cashier system. The service reads a camera stream, stores a parameterizable number of images (in PNG format), and saves the associated metadata (in JSON format) to a predefined storage location.

#### Features:
- **Video Stream Capture**: Reads video streams from a specified local source.
- **Metadata Handling**: Receives metadata from the SCO system via a chosen communication protocol (e.g., HTTP, MQTT).
- **Frame Storage**: Stores the last N frames of the video stream along with the received metadata.
- **Configurable**: Allows parameterization of the number of frames to store and storage locations.
- **Dockerized**: Can be run within a Docker container for easy deployment and testing.

#### Requirements:
- Python 3.10 or higher
- Docker

#### Usage:
1. Specify an arbitrary video file as input.
2. Define the output location for stored images and metadata.
3. Configure the communication method for receiving metadata from the SCO system.
4. Run the service to start capturing and storing frames upon receiving metadata.

#### Setup and Installation:
1. Clone the empty repository.
2. Set up the virtual environment and install dependencies.
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Build and run the Docker image.
   ```bash
   docker build -t sco-recorder-service .
   docker run -p 8000:8000 sco-recorder-service
   ```

#### Interview Preparation:
Be prepared to:
- Present and explain your solution.
- Discuss your design choices and reasoning.
- Suggest improvements for making the solution production-ready.

---

This description provides an overview of the project, its features, setup instructions, and usage, making it easy for others to understand and use your project.