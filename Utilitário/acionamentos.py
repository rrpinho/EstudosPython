import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

valorAvanca = 21 # 26 e 19
valorRetrocede = 20 # 16 e 13
GPIO.setup(valorAvanca, GPIO.OUT)
GPIO.setup(valorRetrocede, GPIO.OUT)
sono = 1

mv = ''

def acionaCLP( mv ):
    if mv == 'avancar':
        GPIO.output(valorAvanca, GPIO.HIGH)
        time.sleep(sono)
        GPIO.output(valorAvanca, GPIO.LOW)
    elif mv == 'retroceder':
        GPIO.output(valorRetrocede, GPIO.HIGH)
        time.sleep(sono)
        GPIO.output(valorRetrocede, GPIO.LOW)