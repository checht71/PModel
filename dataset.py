import torchvision.transforms as transforms
from torch.utils.data import Dataset
from PIL import Image
from torchvision.transforms import v2
import pandas as pd
import torch
import numpy as np

transforms = v2.Compose([
    v2.Resize(size=(128, 128)),
    v2.RandomResizedCrop(size=(224, 224), antialias=True),
    v2.RandomHorizontalFlip(p=0.5),
    v2.ToDtype(torch.float32),
    #v2.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),  
])

class csvImageDataset(Dataset):
    def __init__(self, IMAGE_DIR, CSV_DIR):
        self.df = pd.read_csv(CSV_DIR)
        self.imgs=self.df[['Img_name']]
        self.labels=self.df[['label']]
        self.imgs.reset_index(drop=True)
        self.labels.reset_index(drop=True)
        self.image_dir = IMAGE_DIR

    def __len__(self):
        return len(self.imgs)

    def __getitem__(self, idx): 
        rawimg = Image.open(f'{self.image_dir}/{self.imgs.iat[idx, 0]}')
        try:
            trans_image= transforms(rawimg)
            numpyimage = np.array(trans_image)
            return numpyimage, self.labels.iat[idx, 0]
        except:
            print(f"{self.imgs.iat[idx, 0]} is corrupted")