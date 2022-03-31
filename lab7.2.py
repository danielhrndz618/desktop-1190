import serial
import time
import matplotlib.pyplot as plt


ser = serial.Serial('COM3', 9600, timeout=1)
print('Conectado')
time.sleep(2)

data = []
for i in range(200):
    line = ser.readline()   
    if line:
        s = line.decode()  
        num = int(s) 
        print(num)
        data.append(num) 
ser.close()


plt.plot(data)
plt.xlabel('Tiempo')
plt.ylabel('Potenciometro Lecturas')
plt.title('Potenciometro Lectruas vs. Tiempo')
plt.show()
