import os
import random
import zipfile
from PIL import Image
import cv2
from PIL import Image

def random_crop(image, crop_width=512, crop_height=512):
    # Get the width and height of the input image
    width, height = image.size
    
    # Calculate the maximum x-coordinate for the top-left corner of the crop
    max_x = width - crop_width
    
    # Calculate the maximum y-coordinate for the top-left corner of the crop
    max_y = height - crop_height
    
    # Generate random coordinates for the top-left corner of the crop
    x = random.randint(0, max_x)
    y = random.randint(0, max_y)
    
    # Crop the image
    cropped_image = image.crop((x, y, x + crop_width, y + crop_height))
    
    return cropped_image, x, y

def process_video_frames(video_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video
    cap = cv2.VideoCapture(video_path)

    # Check if the video opened successfully
    if not cap.isOpened():
        print("Error: Unable to open video.")
        return

    frame_count = 0

    while True:
        # Read a frame
        ret, frame = cap.read()

        # Check if frame was read successfully
        if not ret:
            break

        frame_count += 1

        # Only process every 24th frame
        if frame_count % 24 != 0:
            continue

        # Convert frame to PIL Image
        frame_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        # Perform random crop 24 times and save to folder
        for i in range(24):
            cropped_image, x, y = random_crop(frame_pil)
            folder_name = os.path.join(output_folder, f"frame_{frame_count}")
            os.makedirs(folder_name, exist_ok=True)
            cropped_image.save(os.path.join(folder_name, f"crop_{i}_{x}_{y}.jpg"))

    # Release the video capture object
    cap.release()

    # Zip each folder
    for folder_name in os.listdir(output_folder):
        print("zipping>", folder_name)
        folder_path = os.path.join(output_folder, folder_name)
        if os.path.isdir(folder_path):
            zip_path = os.path.join(output_folder, f"{folder_name}.zip")
            with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zipf.write(file_path, os.path.relpath(file_path, folder_path))
    print("finished")


def process_single_image(image_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for i in range(24):
        cropped_image, x, y = random_crop(frame_pil)
        folder_name = os.path.join(output_folder, f"frame_{frame_count}")
        os.makedirs(folder_name, exist_ok=True)
        cropped_image.save(os.path.join(folder_name, f"crop_{i}_{x}_{y}.jpg"))

# Example usage
process_video_frames(video_path, output_folder)

process_single_image(image_path,output_folder)
