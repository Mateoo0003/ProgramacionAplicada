from machine_sym import Pin
import time

led1 = Pin(17, Pin.OUT)
led2 = Pin(18, Pin.OUT)
led3 = Pin(19, Pin.OUT)
led4 = Pin(20, Pin.OUT)
led5 = Pin(21, Pin.OUT)

button1 = Pin(6, Pin.IN, Pin.PULL_UP)
button2 = Pin(7, Pin.IN, Pin.PULL_UP)
button3 = Pin(8, Pin.IN, Pin.PULL_UP)
button4 = Pin(9, Pin.IN, Pin.PULL_UP)
button5 = Pin(10, Pin.IN, Pin.PULL_UP)

estado = 'S1'


def est_sig_sal(estado_actual, entrada):
    estado_siguiente = estado_actual
    if estado_actual == 'S1':
        salida = [1, 0, 0, 0, 0]
        if entrada[0:2] == [0,1]:
            estado_siguiente = 'S2'
    elif estado_actual == 'S2':
        salida = [0, 0, 0, 1, 1]
        if entrada[4,5] == [1,1]:
            estado_siguiente = 'S3'
        elif entrada[4] == [1]:
            estado_siguiente = 'S4'
    elif estado_actual == 'S3':
        salida = [0, 0, 1, 0, 0]
        if entrada[0, 1] == [1, 0]:
            estado_siguiente = 'S1'
    elif estado_actual == 'S4':
        salida = [0, 1, 0, 0, 0]
        if entrada[2] == 1:
            estado_siguiente = 'S3'
    else:
        output = [0, 0, 0, 0, 0]
    return estado_siguiente, salida


while True:
    
    entrada = [button1.value(), button2.value(), button3.value(),
               button4.value(), button5.value()]
    print('Current state:'+estado, "Input:" + str(entrada), end=', ')

    estado, salida = est_sig_sal(estado, entrada)
    led1.value(salida[0])
    led2.value(salida[1])
    led3.value(salida[2])
    led4.value(salida[3])
    led5.value(salida[4])
    print("Output:" + str(salida), 'Next state:'+estado)
    time.sleep(0.2)