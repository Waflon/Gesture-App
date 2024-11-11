import cv2
import time
from timer import timer

def centrar_imagen(img):
    h, w, _ = img.shape

    # load background image as grayscale
    back = cv2.imread('fondo.png', cv2.IMREAD_COLOR)
    #cv2.putText(back, str(timer), (70,70), cv2.FONT_HERSHEY_SIMPLEX , 1, (255, 0, 0), 2, cv2.LINE_AA)# adding timer text

    hh, ww, __ = back.shape

    # compute xoff and yoff for placement of upper left corner of resized image   
    yoff = round((hh-h)/2)
    xoff = round((ww-w)/2)

    # indexing to place the resized image in the center of background image
    result = back.copy()
    result[yoff:yoff+h, xoff:xoff+w] = img
    return result

def mostrar_modelo(lista_imagenes, delay):
    for img in lista_imagenes:
        starting_time = time.time()
        img = cv2.imread(img, cv2.IMREAD_COLOR)
        centrada = centrar_imagen(img)

        cv2.imshow('Modelo', centrada)
        timer_flag = timer(starting_time, delay) #banner alerta 15 segundos antes
        if timer_flag == "cerrar": #cerrar en caso de apretar escape en el timer
            cv2.destroyWindow('Modelo')
            return False
        if timer_flag == "siguiente":
            continue
            
    cv2.destroyWindow('Modelo')
    print("Finalizado con exito")
    return True

def timer(starting_time, tiempo_maximo, aviso_alerta_segundos = 5):
    flag=True
    while flag:
        frame = cv2.imread('fondo_timer.png', cv2.IMREAD_COLOR)

        height, width, channels = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Draw rectangle
        cv2.rectangle(frame, (0, 0), (width, 70), (10, 10, 10), -1)

        elapsed_time = int(time.time() - starting_time)

        if elapsed_time > tiempo_maximo-aviso_alerta_segundos:
            # Reached maximum time, show alert
            cv2.rectangle(frame, (0, 0), (width, height), (0, 0, 225), 10)
            cv2.setWindowProperty("Frame", cv2.WND_PROP_TOPMOST, 1)

        # Draw elapsed time on screen
        cv2.putText(frame, "{} segundos".format(elapsed_time), (10, 50), cv2.FONT_HERSHEY_PLAIN,
                    3, (15, 225, 215), 2)

        # Display frame
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)

        if elapsed_time > tiempo_maximo:
            cv2.destroyWindow("Frame")
            return "finalizado"
        
        if key == 27:
            cv2.destroyWindow("Frame")
            return "cerrar"
        
        if key == 32:
            cv2.destroyWindow("Frame")
            return "siguiente"
