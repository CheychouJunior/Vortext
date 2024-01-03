import cv2
from matplotlib import pyplot as plot
import numpy as np
import pytesseract
from PIL import Image
# ici j'affiche l'image avec tous les encombrements d'ou les trois parametres en prendre en compte
def display(im_path):
    dpi=80
    im_data=plot.imread(im_path)
    height,width,depth  =im_data.shape
    figsize=width/ float(dpi),height/ float(dpi)
    fig=plot.figure(figsize=figsize)
    ax=fig.add_axes([0,0,1,1])
    ax.axis('off')
    ax.imshow(im_data,cmap='gray')
    plot.show()
# l'image est mis en noir et blanc
def grayscale(image):
    return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# on affiche et recupere l'mage sans les multiples couleurs
def display2(im_path):
    dpi=80
    im_data=plot.imread(im_path)
    height,width =im_data.shape
    figsize=width/ float(dpi),height/ float(dpi)
    fig=plot.figure(figsize=figsize)
    ax=fig.add_axes([0,0,1,1])
    ax.axis('off')
    ax.imshow(im_data,cmap='gray')
    plot.show()

image_file="capture.png"
img=cv2.imread(image_file)

gray_image=grayscale(img)
cv2.imwrite("gray.jpg",gray_image)

display2("gray.jpg")

thresh,im_bw=cv2.threshold(gray_image,65,255,cv2.THRESH_BINARY_INV)
cv2.imwrite("./bw_image.jpg",im_bw)

####affichage des données sur le terminal

no_noise="./bw_image.jpg"
img=Image.open(no_noise)
ocr_result=pytesseract.image_to_string(img)
print(ocr_result)
display2("./bw_image.jpg")

# #### affichage des données dans le fichier .txt
# no_noise = "dilated_image.jpg"
# img = Image.open(no_noise)
# ocr_result = pytesseract.image_to_string(img)

# # Création du fichier et écriture des données
# with open("paste.txt", "w",encoding="utf-8") as file:
#     file.write(ocr_result)

# print("Données extraites enregistrées dans le fichier 'paste.txt'.")