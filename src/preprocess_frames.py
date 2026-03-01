import cv2
import os

input_folder = "data/frames"
output_folder = "data/processed_frames"

os.makedirs(output_folder, exist_ok=True)

width = 128
height = 128

files = os.listdir(input_folder)

count = 0

for filename in files:

    if filename.endswith(".png"):

        img_path = os.path.join(input_folder, filename)

        img = cv2.imread(img_path)

        if img is None:
            continue

        resized = cv2.resize(img, (width, height))

        output_path = os.path.join(output_folder, filename)

        cv2.imwrite(output_path, resized)

        count += 1

        if count % 100 == 0:
            print(f"Processed {count} frames")

print("Done")
print("Total processed frames:", count)