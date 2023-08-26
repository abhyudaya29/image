import os
import json
import base64

def image_to_json(image_path):
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        base64_image = base64.b64encode(image_data).decode("utf-8")

    image_info = {
        "image_path": image_path,
        "image_format": image_path.split(".")[-1],
        "image_data": base64_image
    }

    return json.dumps(image_info, indent=4)

image_directory = "./test_data"
output_directory = "./output_json"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for filename in os.listdir(image_directory):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
        image_path = os.path.join(image_directory, filename)
        json_data = image_to_json(image_path)
        
        json_filename = os.path.splitext(filename)[0] + ".json"
        json_path = os.path.join(output_directory, json_filename)
        
        with open(json_path, "w") as json_file:
            json_file.write(json_data)

print("Image data converted to JSON and saved in the 'output_json' directory")
