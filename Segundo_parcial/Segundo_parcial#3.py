import pyfirmata
import time
puerto = "\\.\COM3"
board = pyfirmata.Arduino(puerto)


led1 = board.digital[4]
led2 = board.digital[6]
led3 = board.digital[8]
led4 = board.digital[10]
led5 = board.digital[12]

it = pyfirmata.util.Iterator(board)
it.start()

poten = board.get_pin('a:0:i')

def descpot():
    po = poten.read()
    if po is not None:
        delay = po + 0.01
        time.sleep(delay)
        led5.write(1)
        time.sleep(delay)
        led4.write(1)
        time.sleep(delay)
        led3.write(1)
        time.sleep(delay)
        led2.write(1)
        time.sleep(delay)
        led1.write(1)
        time.sleep(delay)
        led5.write(0)
        led4.write(0)
        led3.write(0)
        led2.write(0)
        led1.write(0)
    else:
        time.sleep(0.1)


while True:
    descpot()
    