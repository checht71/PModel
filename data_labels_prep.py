import os
import shutil
from tqdm import tqdm

'''
This script is used to move the images to their corresponding folders based on the labels.
To run this script, you need to have the images and the labels in the same working directory to be able to access them.
or you can specify the path to the images and the labels in the variables path_to_images and labels_path respectively.
'''

path_to_images = "Images_Data/Images" # Path to the folder containing the images
target_folder = "Dataset V6" # Path to the folder where the images will be moved
labels_path = "labels/base_labels.txt" # Path to the file containing the labels

# 0: road
# 1: crack
# 2: pothole
# 3: crack & pothole

labels_folder = { # Dictionary to map the labels to the folder names
    "0": "Road",
    "1": "Crack",
    "2": "Pothole",
    "3": "Crack & Pothole"
}

for folder in labels_folder.values(): # Loop to get the folder names
    folder_path = os.path.join(target_folder, folder) # Join the target folder with the folder name to get the full path
    if not os.path.exists(folder_path): # Check if the folder exists if not create it
        os.makedirs(folder_path)

with open(labels_path, "r") as file: # Open the file containing the labels
    labels = file.readlines() # Read the lines of the file
    
labels_dict = {} # Dictionary to store the labels
for line in labels: # Loop to get the label of each image
    image_name, label = line.strip().split(",") # Split the line to get the image name and the label and assign them to the variables
    labels_dict[image_name] = label.strip() # Adding the image name and the label to the dictionary

labels_count = {} # Dictionary to store the count of each label
for key in labels_folder.values(): # Loop to get the folder names
    labels_count[key] = 0 # Initialize the count of each label to 0
    

for image_name in tqdm(os.listdir(path_to_images), desc="Copying Images", unit="file"): # Loop to get the image names
    if image_name in labels_dict: # Checks if the image name is in the dictionary
        label = labels_dict[image_name] # Get the label of the image
        shutil.copy2(os.path.join(path_to_images, image_name), os.path.join(target_folder, labels_folder[label], image_name)) # Copy the image to the corresponding folder
        labels_count[labels_folder[label]] += 1 # Increment the count of the label
    else:
        print(f"Label not found for {image_name}") # Print the image name if the label is not found
        
for label_name, count in labels_count.items(): # Loop to print the count of each label
    print(f"Total number of images of {label_name}: {count}") # Print the count of the label
        
print("Images have been successfully copied to their corresponding folders.")