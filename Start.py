import sys

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

import configparser as cp
import data as Data
import callback
import sine
import devSelect as dev
import signal

import w_main
from w_coilSelection import CoilSelector

launch = True

def go(window_main):
        
    deviceFinder.myChanger.deviceFound.disconnect(go)
    data = Data.ProcessedData(config)
    
    sine_a = float(config['global']['velo_amp']) 
    sine_f = float(config['global']['velo_freq']) 
    velo_sine = sine.Sine(sine_a,sine_f, data)
    
    coilSelector = CoilSelector(config)
    task=callback.CallbackTask(data,config,velo_sine,coilSelector)
    
    data.connectTask(task)    
    velo_sine.saveTask(task)
        
           
    timer = QtCore.QTimer()
    
    
        
    window_main.trueInit(config, timer, task, data, velo_sine, coilSelector,deviceFinder)
    
    coilSelector.getMWRef(window_main)
    coilSelector.coilInit()    
    
    window_main.show() 
    
    timer.start(100)
    task.StartTask()
#    timer.timeout.connect(bla)
    
    return    
    
    
#    
#def bla():
#    print "blabla"
#    

if __name__ == "__main__":
    
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    #Read configfile
    config = cp.ConfigParser()
    config.read('config.ini')
    
    app = QtWidgets.QApplication(sys.argv)    
    
    window_main=w_main.MainWindow()    
    
    deviceFinder = dev.DeviceFinder(config, window_main)
    deviceFinder.myChanger.deviceFound.connect(go)
    deviceFinder.search()
    
#    go()
    
    sys.exit(app.exec_())
    
    


