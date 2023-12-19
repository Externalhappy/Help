import os

d = {"21": "fire lily", "3": "canterbury bells", "45": "bolero deep blue"}

# Get the list of all items in the directory
path = "./data/flowers/train"
items = os.listdir(path)

# Iterate through each item
for item in items:
    item_path = os.path.join(path, item)
    # Check if it's a directory
    if os.path.isdir(item_path):
        # Check if the folder name matches the old_name
        if item in d.keys():
            # Construct the new path with the new folder name
            new_path = os.path.join(path, d[item])
            # Rename the folder
            os.rename(item_path, new_path)
