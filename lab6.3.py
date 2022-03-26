import pyfirmata
import time

puerto = "\\.\COM3"
board = pyfirmata.Arduino(puerto)
print("Conectado")

led1 = board.digital[12]
led2 = board.digital[8]


it = pyfirmata.util.Iterator(board)
it.start()

def luz():
    enc = input("Ingrese AY para encender intermitentemente: ").upper()
    if enc == 'AY':
        while True:
            led1.write(1)
            led2.write(1)
            time.sleep(.25)
            led1.write(0)
            led2.write(0)
            time.sleep(.25)
    else:
        print("No son las Teclas correctas\n")

while True:
    luz()

                    