import json
import pandas as pd
from pymongo import MongoClient
import os

# Convert DataFrame to JSON
image_json = "./output_json"  # Change this to the actual JSON file path

json_data_list = []

# Read JSON files from the directory
for filename in os.listdir(image_json):
    if filename.lower().endswith('.json'):
        json_path = os.path.join(image_json, filename)
        with open(json_path, "r") as json_file:
            json_data = json.load(json_file)
            json_data_list.append(json_data)

# MongoDB URI
uri = "mongodb+srv://abhy:abhy@cluster0.wogjoet.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)
db = client["abhy"]  # Replace with your database name
collection = db["Cluster0"]

# Insert JSON data into the collection
collection.insert_many(json_data_list)

print("JSON data deployed to MongoDB successfully.")
