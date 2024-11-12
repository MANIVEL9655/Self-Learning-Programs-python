import PIL
import numpy as np
print(PIL.__version__)
from PIL import Image
from numpy import asarray
img1=Image.open("default.jpg")
img2=Image.open("Photo.jpg")

print(img1.format)
print(img1.size)
print(img1.mode)

npdata = asarray(img1)
print(npdata)
print(np.ndim(img1))
print(np.shape(img1))

