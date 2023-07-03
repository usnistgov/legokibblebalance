from __future__ import division
import gui_w_dataAcqSettings
import basicWindow

class DataAcqSettings(gui_w_dataAcqSettings.QtGui.QMainWindow, gui_w_dataAcqSettings.Ui_MainWindow, basicWindow.BasicWindow):
    def __init__(self, w_main):
        super(DataAcqSettings,self).__init__()
        self.loadBasicObjects(w_main)
        self.setupUi(self)
        
        self.w_main_pos = w_main.pos()
        #Inherited from Basic Window
        self.checkMoveWindow(self.w_main_pos.x(),self.w_main_pos.y()+w_main.height()+26)
        
        self.TB_samprate.setValue(int(self.myConfig['dataacq']['samprate']))
        self.TB_length.setValue(int(self.myConfig['dataacq']['length']))
        self.TB_maxlen.setValue(int(self.myConfig['dataacq']['s']))
        self.TB_buffersize.setValue(int(self.myConfig['dataacq']['buffer_factor']))
        
        self.TB_samprate.valueChanged.connect(self.updateLCD)
        self.TB_length.valueChanged.connect(self.updateLCD)
        self.TB_maxlen.valueChanged.connect(self.updateLCD)

        self.updateLCD()        
        
        self.BTN_saverestart.clicked.connect(self.saveRestart)
        
        self.show()
        self.windowShown = True
        
    def updateLCD(self):
        self.LCD_totalSamprate.display(4*int(self.myConfig['dataacq']['samprate']))
        self.LCD_TrueSampleDt.display(1.0/int(self.myConfig['dataacq']['samprate']))
        self.LCD_dt.display(int(self.myConfig['dataacq']['length'])*1.0/int(self.myConfig['dataacq']['samprate']))
        self.LCD_callbacksPerPeriod.display((1/self.myMainWindow.mySine.getF())/(1/int(self.myConfig['dataacq']['samprate'])))
        
    def saveRestart(self):
        result = gui_w_dataAcqSettings.QtGui.QMessageBox.question(self.myMainWindow,
                          "Save new Settings?",
                          "If you save the new Settings the Program will close and you have to restart manually.",
                          gui_w_dataAcqSettings.QtGui.QMessageBox.Yes| gui_w_dataAcqSettings.QtGui.QMessageBox.No)

        if result == gui_w_dataAcqSettings.QtGui.QMessageBox.Yes:
            self.myConfig['dataacq']['samprate'] = str(self.TB_samprate.value())
            self.myConfig['dataacq']['length'] = str(self.TB_length.value())
            self.myConfig['dataacq']['s'] = str(self.TB_maxlen.value())
            self.myConfig['dataacq']['buffer_factor'] = str(self.TB_buffersize.value())
            with open('config.ini','w') as cfg:
                self.myConfig.write(cfg)
                
            self.myMainWindow.prepareDesiredClose()
            self.myMainWindow.close()
    
    def manualClose(self):
        self.windowShown = False 
        self.close()
            
    def closeEvent(self,event):
        self.manualClose()
        
        
        
        
        
        
        
        

    