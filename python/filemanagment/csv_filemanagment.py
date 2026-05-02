import csv
import os



def write_csv(filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "City"])
        writer.writerow(["Alice", 30, "Pune"])
        writer.writerow(["Bob", 25, "Mumbai"])
    print("Data written successfully.")


def read_csv(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    else:
        print("File not found.")


def delete_csv(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print("File deleted successfully.")
    else:
        print("File not found.")


# write_csv("myfile.csv")
# read_csv("myfile.csv")
# delete_csv("myfile.csv")
