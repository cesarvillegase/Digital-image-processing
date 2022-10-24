# Histograma mediante librería PIL
#Elaborado por César Alejandro Villegas Espíndola

# Se importo desde PIL imagen
from PIL import Image
img = Image.open('/Users/cvillegas/workspace/Py/DIP/Ejercicio 4/Cat4.jpg')
img_gris = img.convert('L')
hist=img_gris.histogram()