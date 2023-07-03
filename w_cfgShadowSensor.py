from __future__ import division
import numpy as np

import gui_w_cfgShadowSensor
import basicWindow
from PyQt5 import QtCore
      
      
class ConfigureShadowSensor(gui_w_cfgShadowSensor.QtGui.QMainWindow,\
                            gui_w_cfgShadowSensor.Ui_MainWindow,\
                            basicWindow.BasicWindow):
    def __init__(self, w_main):
        super(ConfigureShadowSensor,self).__init__()
        self.loadBasicObjects(w_main)
        self.setupUi(self)
        
        self.w_main_pos = w_main.pos()
        #Inherited from Basic Window
        self.checkMoveWindow(self.w_main_pos.x()+w_main.width()+8,self.w_main_pos.y())

        self.myStaticPID = self.myTask.giveStaticPID()
        

        self.LCD_oldZeropos.display(float(self.myConfig['global']['balance0photooffset']))    
        
        
        self.oldphotoOffset = float(self.myConfig['global']['balance0photooffset'])
        self.TB_photooffsetChange.setValue(self.oldphotoOffset)
        
        self.TB_photooffsetChange.valueChanged.connect(self.photooffsetChanged)
        self.updateInputVoltage()
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateInputVoltage)
        self.timer.start(100)  # every 10,000 milliseconds
        self.show()
        self.windowShown=True
        
            
        
####ZEROPOSITION###############################################################

        
    def photooffsetChanged(self):
        newvalue = self.TB_photooffsetChange.value()

        self.myConfig['global']['balance0photooffset'] = str(newvalue)
        self.oldphotoOffset = newvalue
        
        
        self.LCD_oldZeropos.display(float(self.myConfig['global']['balance0photooffset']))    
        with open('config.ini','w') as cfg:
            self.myConfig.write(cfg)
        
            
    def updateInputVoltage(self):
        self.LCD_InputVoltage.display(self.myData.ai0raw)


    def manualClose(self):
        self.myStaticPID.setTarget(0)
        self.windowShown = False
        self.close()

        
    def closeEvent(self,event):
        self.timer.stop()
        self.manualClose()