import json
import requests
import os

# Define the full path to the data.json file
file_path = os.path.join(os.getcwd(), 'data.json')  # Specify full path if needed
print("File path:", file_path)

# Check if the file exists at the specified path
if not os.path.isfile(file_path):
    print("File does not exist. Please check the path.")
else:
    # Load JSON data
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Prepare directory to save images
    save_dir = os.path.join(os.getcwd(), 'dataset', 'images')
    os.makedirs(save_dir, exist_ok=True)

    # Update the JSON data with local paths
    updated_images = []
    for i, image in enumerate(data['images'][:50]):  # Only download the first 50 images
        # Extract image URL and file name
        url = image['url']
        file_name = image['file_name']
        local_path = os.path.join(save_dir, file_name)

        # Download the image
        try:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open(local_path, 'wb') as img_file:
                    img_file.write(response.content)
                # Update the image entry with the new local path
                image['local_path'] = local_path
                updated_images.append(image)
                print(f"Downloaded {file_name}")
            else:
                print(f"Failed to download {file_name}: {response.status_code}")
        except Exception as e:
            print(f"Error downloading {file_name}: {e}")

    # Save the updated JSON data with new paths
    new_data = data.copy()
    new_data['images'] = updated_images
    json_output_path = os.path.join(save_dir, 'final_dataset.json')
    with open(json_output_path, 'w') as f:
        json.dump(new_data, f, indent=4)

    print("Download complete and JSON file updated.")
