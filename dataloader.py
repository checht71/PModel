from dataset import csvImageDataset
from torch.utils.data import DataLoader, random_split


def split_dataset(unsplit_set, split_ratio):
    set_size = len(unsplit_set)
    val_size = int(split_ratio * set_size) #0.2 for 20%, etc
    train_size = set_size - val_size
    train_dataset, val_dataset = random_split(unsplit_set, [train_size, val_size])
    return train_dataset, val_dataset


def create_dataloader(IMAGE_LOCATION, LABEL_CSV_LOACTION, BATCH_SIZE, VAL_SPLIT_RATIO):
    dataset = csvImageDataset(IMAGE_LOCATION, LABEL_CSV_LOACTION)
    train_dataset, val_dataset = split_dataset(dataset, VAL_SPLIT_RATIO)

    train_dataloader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
    validation_dataloader = DataLoader(val_dataset, batch_size=BATCH_SIZE, shuffle=False)
    return train_dataloader, validation_dataloader


if __name__ == "__main__":
    IMAGE_LOCATION = ""
    LABEL_CSV_LOACTION = ""
    BATCH_SIZE = 16
    VAL_SPLIT_RATIO = 0.2
    if IMAGE_LOCATION or LABEL_CSV_LOACTION == "":
        print("Error: Empty Image or CSV file location")
    try:
        train_dataloader, validation_dataloader = create_dataloader(IMAGE_LOCATION, LABEL_CSV_LOACTION, BATCH_SIZE, VAL_SPLIT_RATIO)
    except:
        print("Error creating dataloaders")