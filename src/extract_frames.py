import cv2
import os

def extract_frames(video_path, output_folder):
    """
    Extract frames from video and save to output folder
    """

    # Create folder if not exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)

    frame_count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.png")

        cv2.imwrite(frame_filename, frame)

        print(f"Saved: {frame_filename}")

        frame_count += 1

    cap.release()

    print(f"\nTotal frames extracted: {frame_count}")


# Example usage
if __name__ == "__main__":
    video_path = "data/input_video.mp4"
    output_folder = "data/frames"

    extract_frames(video_path, output_folder)