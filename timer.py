#https://pysource.com/2023/03/13/build-a-computer-vision-timer-tracker-opencv-with-python-tutorial/
import cv2
import time

def timer(starting_time, tiempo_maximo, aviso_alerta_segundos = 5):
    #starting_time = time.time()
    flag=True
    while flag:
        # Take frame from camera
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
