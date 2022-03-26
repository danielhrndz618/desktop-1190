import pyfirmata
import time

puerto = "\\.\COM3"
board = pyfirmata.Arduino(puerto)
print("Conectado")

button = board.digital[4]
led1 = board.digital[12]
led2 = board.digital[8]

led_encendido = 0
button_enc = 0

it = pyfirmata.util.Iterator(board)
it.start()
button.mode = pyfirmata.INPUT

while True:
    button_state = button.read()
    if button_state != button_enc:
        if button_state is False:

            led1.write(0)
            led2.write(0)
            led_encendido +=1
            time.sleep(.05)
            print("Pulsado")
            if led_encendido == 2:
                led1.write(1)
                time.sleep(2)
                led1.write(0)
            elif led_encendido == 4:
                led2.write(1)
                time.sleep(2)
                led2.write(0)
                led_encendido = 0
    button_enc = button_state







