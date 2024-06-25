import os
from video_utils import open_video, capture_last_frames, encode_frames, create_zip, timestamped_zip_name
from display_video import display_video


def main():
    # Ask the user to upload a video file
    # video_path = input("Please enter the path to your video file: ")
    video_path = '../Videos/earth_video.mp4'
    # Directory to save the ZIP file containing the captured frames
    output_dir = './output_frames'
    # Number of frames to capture
    num_frames = 20

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        # Open the video
        cap = open_video(video_path)

        # Capture the frames
        frames = capture_last_frames(cap, num_frames)
        cap.release()

        # Encode the frames
        encoded_frames = encode_frames(frames)

        # Create a timestamped ZIP file name
        zip_name = timestamped_zip_name()

        # Create the ZIP file
        zip_path = create_zip(output_dir, zip_name, encoded_frames)

        print(f"ZIP file created: {zip_path}")

    except Exception as e:
        # Log the error
        print(f"Error: {str(e)}")

    # Optional: Display the video (not necessary for frame capturing)
    display_video(video_path)


if __name__ == "__main__":
    main()
