import torchvision.transforms as transforms
from torch.utils.data import Dataset
from PIL import Image
from torchvision.transforms import v2
import pandas as pd
import torch

class csvImageDataset(Dataset):
    def __init__(self, IMAGE_DIR, CSV_DIR):
        self.df = pd.read_csv(CSV_DIR)
        self.imgs=self.df[['Img_name']].reset_index(drop=True)
        self.labels=self.df[['label']].reset_index(drop=True)
        self.transforms = v2.Compose([
        v2.Resize(size=(256, 256)),
        v2.RandomHorizontalFlip(p=0.5),
        v2.ToDtype(torch.float32),
        v2.Grayscale(),
        v2.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),  
        ])

    def __len__(self):
        return len(self.imgs)

    def __getitem__(self, idx):
        try:
            rawimg = Image.open(f'{IMAGE_DIR}/{self.imgs.iat[idx, 0]}')
        except:
            print(f"PIL could not open {self.imgs.iat[idx, 0]}")

        try:
            transformed_image= np.array(self.transforms(rawimg))
            label = self.labels.iat[idx, 0]
            return transformed_image, label
        except:
            print(f"Could not transform {self.imgs.iat[idx, 0]}")



