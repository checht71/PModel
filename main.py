import dataloader, dataset
from visualization import load_image_batch_to_plot

IMAGE_LOCATION = "/media/christian/USB STICK/Images/Images"
LABEL_CSV_LOCATION = "/media/christian/USB STICK/labels/base_labels_2.csv"
BATCH_SIZE = 16
VAL_SPLIT_RATIO = 0.2

train_dataloader, validation_dataloader = dataloader.create_dataloaders(IMAGE_LOCATION, LABEL_CSV_LOCATION, BATCH_SIZE, VAL_SPLIT_RATIO)

load_image_batch_to_plot(IMAGE_LOCATION, LABEL_CSV_LOCATION, BATCH_SIZE, shuffle=True)

"""
# Begin Training loop here
for i, data in enumerate(train_dataloader):
    pass
"""