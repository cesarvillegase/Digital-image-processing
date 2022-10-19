#Apertura de imágenes y conversión RGB a escala de grises
#Elaborado por César Alejandro Villegas Espíndola

#Importación de librerias 
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('/Users/cvillegas/workspace/Py/DIP/Ejercicio 2/Cat.jpg')

#Conversión a escala de grises
#Separar cada canal 
R = img[:,:,0]
G = img[:,:,1]
B = img[:,:,2]

img_gris = 0.2989*R + 0.5870*G + 0.1140*B

#Desplegamos las imagen a color
plt.imshow(img) #Este comando forma la imagen
plt.title("Imagen a color")
plt.show() #Este comando despliega la imagen

#Imagen a escala de grises
plt.imshow(img_gris, cmap='gray') #Este comando forma la imagen
plt.title("Imagen a escala de grises")
plt.show() #Este comando despliega la imagen

#Uso de libreria skimage - Compacta pero completa
from skimage import color
from skimage import io

img2 = io.imread('/Users/cvillegas/workspace/Py/DIP/Ejercicio 2/Cat.jpg')
img2_gris = color.rgb2gray(img2)

#Imagen a color
imgplot = plt.imshow(img2)
plt.show()

#Imagen a escala de grises
imgplot = plt.imshow(img2_gris, cmap='gray')
plt.show()
 
 #Uso de la libreria PIL - Sirve para el tratamiento de imágenes
from PIL import Image

img3 = Image.open('/Users/cvillegas/workspace/Py/DIP/Ejercicio 2/Cat.jpg')
img3_gris = img3.convert('L')
img3_gris.save('Cat_gray.jpg')

#Uso de la libreria OPEN CV
#import CV2
#img4 = cv2.imread('/Users/cvillegas/workspace/Py/DIP/Ejercicio 2/Cat.jpg')
#plt.imshow(img4)