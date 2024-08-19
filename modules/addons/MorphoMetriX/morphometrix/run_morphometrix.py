import sys
import os
import urllib.parse
import requests
import subprocess

# Add the directory containing morphometrix to the Python path
morphometrix_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(morphometrix_dir)

from morphometrix.__main__ import main

def label_studio_helper():
    """
    Helper function to retrieve the image path from Label Studio's URL and import it into MorphoMetriX.
    """
    api_key = "3ba72f8c09ddfe2c6f41975fe39b63e45e0ebd32"
    url = "http://localhost:8080/projects/1/data?tab=1&task=1"

    # 1. Parse the string to get the project id and task id:
    parsed_url = urllib.parse.urlparse(url)
    query_params = urllib.parse.parse_qs(parsed_url.query)

    task_id = query_params.get('task', [None])[0]
    
    api_url = "http://localhost:8080/api/tasks/" + str(task_id) + "/"
    print(api_url)
    headers = {
        "Authorization": f"Token {api_key}"
    }   

    response = requests.get(api_url, headers=headers)
    # Check the response status
    if response.status_code == 200:
        try:
            data = response.json()
            image_path = data.get('data', {}).get('image')  # Retrieve the image path
            if image_path:
                print("Image path found:", image_path)

                # Convert the Docker container path to host path
                host_path = convert_path(image_path)
                print("Converted host path:", host_path)
            else:
                print("Image path not found.")
                host_path = None
        except requests.exceptions.JSONDecodeError:
            print("Failed to decode JSON response.")
            host_path = None
    else:
        print("Failed with status code:", response.status_code)
        print("Response:", response.text)
        host_path = None
    
    return host_path, task_id

def convert_path(container_path):
    """
    Convert a Docker container path to the corresponding host path.
    """
    # Assuming container path starts with /data/upload/
    if container_path.startswith('/data/upload/'):
        # Extract the project ID and the rest of the path
        relative_path = container_path[len('/data/upload/'):]  # Remove the '/data/upload/' prefix
        project_id = relative_path.split('/')[0]
        
        # Construct the host path by correctly mapping to the actual directory structure
        host_base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'core', 'label-studio', 'mydata', 'media', 'upload'))
        host_path = os.path.join(host_base_path, project_id, '/'.join(relative_path.split('/')[1:]))
        return host_path
    else:
        print("Unrecognized container path format.")
        return None


if __name__ == "__main__":
    # Call the helper function
    image_path, task_id = label_studio_helper()

    if image_path:
        # Set your custom arguments here
        id = task_id
        focal_length = None
        altitude = None
        pixel_dim = None

        # Run the MorphoMetriX program with custom arguments
        main(image_path=image_path, id=id, focal_length=focal_length, altitude=altitude, pixel_dim=pixel_dim)
