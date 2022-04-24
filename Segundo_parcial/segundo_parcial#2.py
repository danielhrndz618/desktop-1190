import pyfirmata
import time

puerto = "\\.\COM3"
board = pyfirmata.Arduino(puerto)



led1 = board.digital[4]
led2 = board.digital[6]
led3 = board.digital[8]
led4 = board.digital[10]
led5 = board.digital[12]


while True:
        led1.write(1)
        led2.write(1)
        led3.write(1)
        time.sleep(1)
        led1.write(0)
        led2.write(0)
        led3.write(0)
        led4.write(1)
        led5.write(1)
        time.sleep(2)
        led4.write(0)
        led5.write(0)
        
      
