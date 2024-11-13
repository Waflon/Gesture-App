from Modelo import mostrar_modelo
import pathlib
import random
import glob
import sys

segundos = sys.argv[0]

print("Argument List:", str(sys.argv))
ruta = f'{pathlib.Path().resolve()}\\imagenes_descargadas\\'

try:
    minutos = int(sys.argv[1])
except:
    minutos = 2
    
try:
    segundos = int(sys.argv[2])
except:
    segundos = 0

def main():
    lista_imagenes = glob.glob(ruta + "*.jpg")
    random.shuffle(lista_imagenes)
    delay = segundos + minutos*60
    flag = True

    while flag:
        flag = mostrar_modelo(lista_imagenes, delay) 

if __name__ == "__main__":
    main()