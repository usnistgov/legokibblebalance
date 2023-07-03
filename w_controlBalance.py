import gui_w_controlBalance
import basicWindow

      
class ControlBalance(gui_w_controlBalance.QtGui.QMainWindow,gui_w_controlBalance.Ui_MainWindow,basicWindow.BasicWindow):
    def __init__(self, w_main):
        super(ControlBalance,self).__init__()
        self.loadBasicObjects(w_main)
        self.setupUi(self)

        self.w_main_pos = w_main.pos()
        #Inherited from Basic Window
        self.checkMoveWindow(self.w_main_pos.x(),self.w_main_pos.y()-self.height()-26)

        self.weighingPID = self.myTask.giveStaticPID()

        
        #connecting UI Elements
        self.CB_usePIDFeedback.clicked.connect(self.usePIDFeedback)
        self.CB_useInputBox.clicked.connect(self.useInputBox)
        self.CB_useInputWheel.clicked.connect(self.useInputWheel)
        
        self.TB_analogOutput.valueChanged.connect(self.setVoltageManual)
        self.myTimer.timeout.connect(self.updateLCD)

        self.show()
        self.windowShown=True
    
    def updateLCD(self):
        if self.CB_usePIDFeedback.isChecked():
            analogOutput=self.weighingPID.getOutput()
            self.LCD_analogOutput.display(analogOutput)
        elif self.CB_useInputBox.isChecked():
            analogOutput = self.TB_analogOutput.value()
            self.LCD_analogOutput.display(analogOutput)
        
    def usePIDFeedback(self):
        print('fb')
        self.CB_useInputBox.setChecked(False)
        self.CB_useInputWheel.setChecked(False)
        self.myTask.setDoPID(True)
        
    def useInputBox(self):
        print('box')
        self.CB_usePIDFeedback.setChecked(False)
        self.CB_useInputWheel.setChecked(False)
        self.myTask.setDoPID(False)

    def useInputWheel(self):
        print('wheel')
        self.CB_usePIDFeedback.setChecked(False)
        self.CB_useInputBox.setChecked(False)
        self.myTask.setDoPID(False)
        
    def setVoltageManual(self):   #Outputs Voltage if use Input Box is checked
        if self.CB_useInputBox.isChecked():
            self.myTask.setVoltage(self.TB_analogOutput.value())
            
    def manualClose(self):
        self.windowShown = False
        self.myTask.setDoPID(True)
        self.myMainWindow.TXT_activeMode.setText('Static')        
        self.close()
        
    def closeEvent(self,event):
        self.manualClose()
        

        
        
            
            
