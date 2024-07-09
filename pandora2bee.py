import json
import numpy as np
import os

# Specify the file path
file_path = "pandora-sp.txt"

# Load the data from the text file into numpy arrays
x, y, z, q, cluster_id = np.loadtxt(file_path, unpack=True)

# Create a dictionary with the arrays
data = {
    "eventNo": 0,
    "subRunNo": 0,
    "type": "cluster",
    "geom": "sbnd",
    "x": x.tolist(),
    "y": y.tolist(),
    "z": z.tolist(),
    "q": q.tolist(),
    "cluster_id": cluster_id.tolist()
}

# Specify the file path to save the JSON data
output_file_path = "data/0/0-pandora.json"


# Create the directory structure if it does not exist
output_dir = os.path.dirname(output_file_path)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save the JSON data to the file
with open(output_file_path, "w") as output_file:
    json.dump(data, output_file)
