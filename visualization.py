from torchvision.utils import make_grid
from matplotlib import pyplot as plt
from dataset import csvImageDataset
from random import randint

def plot_image_grid(images, texts, figsize=(10, 10)):
    print(len(images))
    if len(images) <= 3:
        num_cols = len(images)
        num_rows = 1
    else:
        num_cols = 3
        num_rows = round(len(images)/num_cols)
    fig, axes = plt.subplots(num_rows, num_cols, figsize=figsize)
    for i, ax in enumerate(axes.flat):
        if i < len(images):
            ax.imshow(images[i])
            ax.axis('off')
            ax.set_title(texts[i], fontsize=10, pad=5)
    plt.tight_layout()
    plt.show()
    

def load_image_batch_to_plot(IMAGE_LOCATION, LABEL_CSV_LOCATION, BATCH_SIZE, shuffle):
    dataset = csvImageDataset(IMAGE_LOCATION, LABEL_CSV_LOCATION)
    sample_img_array = []
    sample_label_array = []
    for img_idx in range(BATCH_SIZE):
        if shuffle == True:
            img_idx = randint(0, dataset.__len__())
            print(img_idx)
        sample_img, sample_label = dataset.get_raw_image(img_idx)
        sample_img_array.append(sample_img)
        sample_label_array.append(sample_label)

    plot_image_grid(sample_img_array, sample_label_array)



if __name__ == "__main__":
    from PIL import Image
    load_image_batch_to_plot("/media/christian/USB STICK/Images/Images",
     "/media/christian/USB STICK/labels/base_labels_2.csv", 9, True)

