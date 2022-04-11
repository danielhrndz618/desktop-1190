import pyfirmata
from datetime import datetime

pause = 2

hot = 35
cold = 25

puerto = "\\.\COM3"
board = pyfirmata.Arduino(puerto)

pyfirmata.util.Iterator(board).start()

entrada = board.get_pin('a:1:i')
entrada.enable_reporting()
led1 = board.digital[5]
led2 = board.digital[4]
led3 = board.digital[3]

def volts_to_celsius(v):
    "Convierte un voltaje v obtenido de un sensor DHT11 a grados Celsius."
    return 100 * (v - 0.5)

try:
    while True:
        d = datetime.now()
        v = entrada.read()
        if v != None:
            v *= 5

            c = volts_to_celsius(v)
            print('{}, {:.3f} V, {:.2f} °C'
                .format(d,v,c))
            board.pass_time(pause)
            if c < cold:
                led1.write(1)
                led2.write(0)
                led3.write(0)
            elif c >= hot:
                led1.write(0)
                led2.write(0)
                led3.write(1)
            else: 
                led1.write(0)
                led2.write(1)
                led3.write(0)



except KeyboardInterrupt:
    pass                  

finally:
    board.exit()
