import imgaug as ia
from imgaug import augmenters as iaa
import numpy as np
import imageio

ia.seed(1)

img = imageio.imread("test.jpg") #read you image
images = np.array(
    [img for _ in range(32)], dtype=np.uint8)  # 32 means creat 32 enhanced images using following methods.

seq = iaa.Sequential(
    [
        iaa.FastSnowyLandscape(64,1.5),
        iaa.Snowflakes(0.075,0.9,0.7,0.8,30,0.03)
        
    ],
    random_order=True)  # apply augmenters in random order

images_aug = seq.augment_images(images)

for i in range(32):
    imageio.imwrite(str(i)+'new.jpg', images_aug[i])  #write all changed images