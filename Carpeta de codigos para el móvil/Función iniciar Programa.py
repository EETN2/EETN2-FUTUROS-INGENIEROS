#Importación de las bibliotecas
import os
import subprocess
import RPi.GPIO as GPIO
import time

# Configura el pin del pulsador y el directorio del programa a ejecutar
pulsador_pin = 22  
programa_a_ejecutar = "/home/tecnica2/Desktop/funcionando/SLyU (4).py"  # Ruta del programa

# Configuración de los pines GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pulsador_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Variable de estado para controlar si el programa está en ejecución
programa_en_ejecucion = False
proceso_programa = None

try:
    while True:
        input_state = GPIO.input(pulsador_pin)
        if input_state == False:
            # Cuando el pulsador se presiona, ejecuta el programa
            if not programa_en_ejecucion:
                time.sleep(3)
                programa_en_ejecucion = True
                proceso_programa = subprocess.Popen(["python", programa_a_ejecutar])
                print("El programa ha empezado.")
            # Si el pulsador se vuelve a presionar, se detiene el programa
            else:
                proceso_programa.terminate()
                proceso_programa.wait()
                time.sleep(1)
                programa_en_ejecucion = False
                print("El programa ha sido detenido.")
        time.sleep(0.1)  # Pequeña pausa para evitar rebotes del pulsador
        
finally:
    GPIO.cleanup()