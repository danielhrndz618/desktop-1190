from tkinter import *
root = Tk()
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

def botton():
    boton1 = True
    button_state = boton1
    texto = Label(root, text="Led Apagado").grid()
    if button_state != button_enc:

        if button_state is True:
            led1.write(1)
            time.sleep(10)
            led1.write(0)

boton1 = Button(root,text="Enciende Led", bg="blue", padx=200, pady=50,command=botton).grid(row=0,column=0)

root.mainloop()




