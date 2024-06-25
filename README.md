# SCO-Recorder-Service
This project implements a recorder service designed to capture and store video frames from a Self-Checkout (SCO) camera along with metadata received from a cashier system. 

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
2. Have python 3.10 or higher installed
3. Set up the virtual environment and install dependencies.
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Create the recorder service flask application
5. Create simple templating using Jinja for view dynamic web pages (to see outputs)
6. Create the python dependencies (reqirements.txt)
```bash
pip freeze > requirements.txt
```
7. Build and run the Docker image.
- FROM python:3.12-alpine3.20
   ```bash
   docker build -t recorder-service .
   docker run -d -p 80:5050 --name sco-recorder-service recorder-service:1.0
   ```
8. Create a Docker Compose file for ???
```bash
docker-compose build
docker tag recorder-service:3.0 chukwuka1488/recorder-service:3.0
docker login
docker push chukwuka1488/recorder-service:3.0
```
9. Write kubernetes manifest files for the application
10. Create Helm charts for ???
#### Interview Preparation:
Be prepared to:
- Present and explain your solution.
- Discuss your design choices and reasoning.
- Suggest improvements for making the solution production-ready.

---

This description provides an overview of the project, its features, setup instructions, and usage, making it easy for others to understand and use your project.