import pyfirmata
import time

puerto = "\\.\COM3"
board = pyfirmata.Arduino(puerto)


led1 = board.digital[4]
led2 = board.digital[6]
led3 = board.digital[8]
led4 = board.digital[10]
led5 = board.digital[12]

poten = board.get_pin('a:0:i')
it = pyfirmata.util.Iterator(board)
it.start()

def enc():
        po = poten.read()

        if po == 1:
                led1.write(1)
                led2.write(1)
                led3.write(1)
                led4.write(1)
                led5.write(1)
                print("Led1:HIGH; Led2:HIGH; Led3:HIGH; Led4:HIGH; Led5:HIGH")
                
        else:
                print("Led1:LOW; Led2:LOW; Led3:LOW; Led4:LOW; Led5:LOW")
                led1.write(0)
                led2.write(0)
                led3.write(0)
                led4.write(0)
                led5.write(0)
                

while True:
        enc()