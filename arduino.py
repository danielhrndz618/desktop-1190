import pyfirmata

 
puerto = "\\.\COM3" 
pin = (13) 
 
print("Conectando con Arduino por USB ...")
tarjeta = pyfirmata.Arduino(puerto)
print("Conectado a Arduino por USB...")
while True:
    print("Encendiendo LED")
    tarjeta.digital[pin].write(1)
    print("Encendido LED")
    tarjeta.pass_time(3)
    print("Apagando LED")
    tarjeta.digital[pin].write(0)
    print("Apagado LED")
    tarjeta.pass_time(3)
tarjeta.exit()