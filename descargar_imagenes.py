
from selenium.webdriver.common.by import By
from selenium import webdriver
import requests
import time 
import os

URL = "https://www.characterdesigns.com/photoset-035-natalie-adams-foreshorten_poses/"
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)
def descargar_imagenes(URL):
    try:
        if not os.path.exists("imagenes_descargadas"):
            os.makedirs("imagenes_descargadas")

        driver.get(URL)
        time.sleep(2)
        lista = driver.find_elements(by=By.TAG_NAME, value="img")

        lista_imagenes = []
        for imagen in lista:
            lista_imagenes.append(imagen.get_attribute("src"))

        print("comenzando a descargar imagenes...")

        for imagen in lista_imagenes:
            nombre_archivo = imagen.split("/")[7].split("?")[0]
            link_descarga = imagen.split("?")[0] + "?format=500w"
            img_data = requests.get(link_descarga).content #descarga imagenes
            with open(f'./imagenes_descargadas/{nombre_archivo}', 'wb') as handler:
                handler.write(img_data) #las guarda con nombre caracteristico
        print("imagenes descargadas con exito")
    except:
        pass

#descargar_imagenes(URL)
