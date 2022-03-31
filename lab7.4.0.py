from pyqtgraph.Qt import QtGui, QtCore 
 
import pyqtgraph as pg 
 
from pyfirmata import Arduino, util 
import time 
 
puerto ="\\.\COM3" 
board=Arduino(puerto) 
                                         
it=util.Iterator(board) 
it.start() 
 
app=QtGui.QApplication([]) 
win=pg.GraphicsWindow(title='Tiempo Real De La Gráfica') 
p=win.addPlot(title='GRÁFICA EN TIEMPO REAL') 
curva=p.plot(pen='y') 
 
p.setRange(yRange=[-10,240]) 
dataX=[] 
dataY=[] 
lastY=0 
 
analog0=board.get_pin('a:0:i') 
 
def Update(): 
    global curva, dataX, dataY, lastY, nuevoDato 
     
    dato=analog0.read() 
    if dato is not None: 
       nuevoDato=dato*100 
       print (nuevoDato) 
       time.sleep(1) 
    else: 
        nuevoDato=0 
         
    dataX.append (nuevoDato) 
    dataY.append (lastY) 
    lastY+=1 
     
    if len(dataX)>200: 
        dataX=dataX[:-1] 
        dataY=dataY[:-1] 
     
    curva.setData(dataY, dataX) 
    QtGui.QApplication.processEvents() 
     
     
try: 
    while True: Update() 
     
except KeyboardInterrupt: 
    pg. QtGui. Application.exec_() 
    board.exit() 
     