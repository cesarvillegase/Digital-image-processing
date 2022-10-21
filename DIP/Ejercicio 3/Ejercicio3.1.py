#Operaciones en imágenes
#Elaborado por César Alejandro Villegas Espíndola

#Se importaron las siguientes librerias
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('/Users/cvillegas/workspace/Py/DIP/Ejercicio 3/Cat3.jpg')

#Separating RGB CHannels
#Red goes first:

r = img.copy()
r[:,:,1] = r[:,:,2] = 0

# Then green
g = img.copy()
g[:,:,0] = g[:,:,2] = 0

#Finally blue
b = img.copy()
b[:,:,0] = b[:,:,1] = 0

f, axes = plt.subplots(2,2, constrained_layout = True)

axes[0, 0].title.set_text('Normal')
axes[0, 0].imshow(img)
axes[0, 1].title.set_text('Red')
axes[0, 1].imshow(r)
axes[1, 0].title.set_text('Green')
axes[1, 0].imshow(g)
axes[1, 1].title.set_text('Blue')
axes[1, 1].imshow(b)
plt.show()