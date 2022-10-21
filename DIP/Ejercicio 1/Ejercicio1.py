#Creacion en escala de grises
#Elaborado por César Alejandro Villegas Espíndola

#Importar Librerias

import matplotlib as mpl
import matplotlib.pyplot as plt #Se encarga de hacer gráficos
import matplotlib.image as mpimg    
import numpy as np                   #Se encarga de matrices

M1 = [[1, 30, 45, 60, 100, 150, 190, 245],
      [1, 30, 45, 60, 100, 150, 190, 245],
      [1, 30, 45, 60, 100, 150, 190, 245],
      [1, 30, 45, 60, 100, 150, 190, 245],
      [1, 30, 45, 60, 100, 150, 190, 245],
      [1, 30, 45, 60, 100, 150, 190, 245],
      [1, 30, 45, 60, 100, 150, 190, 245],
      [1, 30, 45, 60, 100, 150, 190, 245]]

imgplot = plt.imshow(M1, cmap='gray')

#Mostrar la imagen
plt.show()
plt.title("Imagen 1")
print(M1)

#Imagen en escala de grises pero con ciclo For
#Crea una matriz de 255x255 con valores en cero en cada entrada
M2 = np.zeros([255,255])
#Control con for anidado de las filas y columnas
for i in range(0,255):
    for j in range(0,255):
        M2[i,j] = j
        
imgplot = plt.imshow(M2, cmap='gray')
plt.show()
plt.title("Imagen 2")
print(M2)

#Crea una matriz de 255x255 con valores en cero en cada entrada
M3 = np.zeros([256,256])
#control con for anidado de las filas y columnas
for i in range(0,256):
    for j in range(0,256):
        M3[i,j] = 256-j

imgplot = plt.imshow(M3, cmap='gray')
plt.show()
plt.title("Imagen 3")
print(M3)

#Crea una matriz de 2000x1500 con valores en cero en cada entrada
M4 = np.zeros([2000,1500])
#control con for anidado de las filas y columnas
for i in range(0,2000):
    for j in range(0,1500):
        M4[i,j] = 2000-j

imgplot = plt.imshow(M4, cmap='gray')
plt.title("Imagen 4")
plt.show()

#Crea una imagen vertical
M5 = np.zeros([1500,1500])
#control con for anidado de las filas y columnas
for i in range(0,1500):
    for j in range(0,1500):
        if i==j:
            M5[i,j]=0
        elif abs(i-j) < 31:
            M5[i,j]=0
        
        else:
            M5[i,j]=255

imgplot = plt.imshow(M5, cmap='gray')
plt.title("Imagen 5")
plt.show()
print(M5)

#Tarea hacer un asterísco

#Se crea una imagen vertical
M6 = np.zeros([1500,1500])
#Control con for anidado de las filas y columnas
for i in range(0,1500):
    for j in range(0,1500):
        if i==j:
            M6[i,j]=0
        elif abs(i-j) < 31:
            M6[i,j]=0
            
        elif abs(i-750) < 31:
            M6[i,j]=0
            
        elif abs(j-750) < 31:
            M6[i,j]=0
            
        elif abs(1500-i-j) < 31:
            M6[i,j]=0
            
        else:
            M6[i,j]=255
            
imgplot = plt.imshow(M6, cmap='gray')
plt.title("Tarea")
plt.show()
print(M6)