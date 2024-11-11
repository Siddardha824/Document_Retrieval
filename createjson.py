import os
import json

# Define the paths for the folders
dataset_folder = 'dataset'
img_folder = os.path.join(dataset_folder, 'img')
gt_folder = os.path.join(dataset_folder, 'gt')
output_json_path = os.path.join(dataset_folder, 'dataset.json')

# Create a list to hold the data entries
data = []

# Iterate through each file in the img folder
for img_file in os.listdir(img_folder):
    # Check if the file is an image (you can add more extensions if needed)
    if img_file.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif')):
        # Get image name without the extension
        image_id = os.path.splitext(img_file)[0]
        
        # Paths for the image and corresponding ground truth file
        image_path = os.path.join(img_folder, img_file)
        gt_path = os.path.join(gt_folder, f"{image_id}.txt")
        
        # Check if the corresponding ground truth file exists
        if os.path.isfile(gt_path):
            # Append the data entry to the list
            data.append({
                "image_id": image_id,
                "image_path": image_path,
                "gt_path": gt_path
            })

# Write the collected data to a JSON file
with open(output_json_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)

print(f"JSON file created at: {output_json_path}")
