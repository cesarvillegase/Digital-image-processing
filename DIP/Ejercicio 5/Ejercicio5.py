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
imagen2 = Image.open('/Users/cvillegas/workspace/Py/DIP/Ejercicio 5/car.jpeg')
#Numpy trabaja con arreglos

#Convertir la imagen en una variable de tipo "array"
data = asarray(imagen2)
print(data.shape)

#Convertir un arreglo a una imagen
imagen3 = Image.fromarray(data)
print(imagen3.format)
#Imprime el espacio de cpñpr 
print(imagen3.mode)
#Obtener las dimensiones de la imagen
print(imagen3.size)

##########################################################################
#Manipular imágenes a traves de
#PIL

#from PIL import Image
#Imagen3 = Image.fromarray(data)
imagen3.thumbnail((100,50)) #El segundo número después de la coma es el porcentaje que se mantiene
#El ratio de una imagen es igual al alto/ancho.
print(imagen3.size)
imagen3.show()

#Rescalamiento de imagenes 2
imagen4 = Image.open('/Users/cvillegas/workspace/Py/DIP/Ejercicio 5/car.jpeg')
imagen_reescalada = imagen4.resize((100,100))
print(imagen_reescalada.size)
imagen_reescalada.show()

#Cambiar la orientación de imágenes
#from PIL import Image
#from matplotlib import pyplot
#imagen4 = Image.open('/Users/cvillegas/workspace/Py/DIP/Ejercicio 5/car.jpeg')

#Cambiar la orientación horizontal
horizontal = imagen4.transpose(Image.FLIP_LEFT_RIGHT)
#Cambiar la orientación vertical 
vertical = imagen4.transpose(Image.FLIP_TOP_BOTTOM)

#Subplot de tres posiciones, el primero en la posición 1,1, el siguiente 1,2
pyplot.subplot(311) 
pyplot.imshow(imagen4)

pyplot.subplot(312) 
pyplot.imshow(horizontal)

pyplot.subplot(313) 
pyplot.imshow(vertical)

pyplot.show()