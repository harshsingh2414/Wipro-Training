import os
import json

def write_json(filename):
    data = [
        {"Name": "Alice", "Age": 30, "City": "Pune"},
        {"Name": "Bob", "Age": 25, "City": "Mumbai"}
    ]
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print("Data written successfully.")

def read_json(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            data = json.load(f)
            for record in data:
                print(record)
    else:
        print("File not found.")

def delete_json(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print("File deleted successfully.")
    else:
        print("File not found.")


# write_json("myfile.json")
# read_json("myfile.json")
delete_json("myfile.json")
