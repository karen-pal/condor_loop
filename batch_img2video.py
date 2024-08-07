import requests
import os
import json
from tqdm import tqdm
import requests

# Define the API endpoint
api_url = 'http://127.0.0.1:7864/prompt'  # Replace with the actual endpoint

# Paths to the directories and the workflow file
input_dir = 'input_images'
output_dir = 'processed/images'
workflow_file_path = 'workflow_api.json'

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Load the workflow from the JSON file
with open(workflow_file_path, 'r') as workflow_file:
    workflow = json.load(workflow_file)

def queue_prompt(prompt):
    p = {"prompt": prompt}
    print(type(p))
    print(type(prompt))
    data = json.dumps(p).encode('utf-8')
    response = requests.post(api_url, data=data)

    #a = request.urlopen(req)
    print(response)
    print(response.text)
    return response


prompt = workflow


# Get a list of image files in the input directory
image_files = [f for f in os.listdir(input_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Iterate through each image in the input directory with a progress bar
for image_name in tqdm(image_files, desc="Processing images"):
    image_path = os.path.join(input_dir, image_name)

    # Read the image
    with open(image_path, 'rb') as image_file:
        files = {'file': image_file}
        data = {'workflow': json.dumps(workflow)}  # Convert workflow to JSON string
        prompt["23"]["inputs"]["image"] = image_file.name

        response = queue_prompt(prompt)
        
        if response.status_code == 200:
            print(image_name, "success")
        else:
            print(f'Failed to process: {image_name}, Status Code: {response.status_code}')

print('Batch processing complete.')

