# Manipulación de imágenes e información
#Elaborado por César Alejandro Villegas Espíndola

# Obtener datos de las imágenes

from PIL import Image
from numpy import imag

image = Image.open('/Users/cvillegas/workspace/Py/DIP/Ejercicio 5/car.jpeg')

#Extensión de la imagen
print(image.format)

#Imprime el espacio de color en el que se trabaja
print(image.mode)

#Obtener las dimensiones de la imagen
print(image.size)

# Obtención de dimensiones por separado
ancho = image.size[0]
alto = image.size[1]
print(alto)
print(ancho)

#Información a través de matplotlib
from matplotlib import image
from matplotlib import pyplot

imagen = image.imread('/Users/cvillegas/workspace/Py/DIP/Ejercicio 5/car.jpeg')

print(imagen.dtype)
print(imagen.shape)

#uint8 - es de 8bits, variables enteros y la u nos dice 

# Se separa el arreglo para tener de manera separada alto, ancho y canales.
print(imagen.shape[0])
print(imagen.shape[1])
print(imagen.shape[2])

# Información a través de numpy, apertura es con PIL
from numpy import asarray   #De ser necesario volver a importar PIL
#from PIL import Image