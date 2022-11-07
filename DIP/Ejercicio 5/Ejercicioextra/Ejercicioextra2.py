import numpy as np
from PIL import Image

img = np.array(Image.open('/Users/cvillegas/workspace/Py/DIP/Ejercicio 5/car.jpeg'))
print(type(img))

print(img.shape)

Image.fromarray(np.flip(img, (0, 1))).save('/Users/cvillegas/workspace/Py/DIP/Ejercicio 5/car_flip.jpeg')

#Recuperado de: note.nkmk.me/en/python-opencv-numpy-rotate-flip/