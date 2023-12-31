import gui_w_cfgVelomode
import basicWindow
from PyQt5 import QtWidgets 

      
class VeloMode(QtWidgets.QMainWindow,gui_w_cfgVelomode.Ui_MainWindow,basicWindow.BasicWindow):
    def __init__(self, w_main):
        super(VeloMode,self).__init__()
        self.loadBasicObjects(w_main)
        self.setupUi(self) 
        
        self.w_main_pos = w_main.pos()
        #Inherited from Basic Window
        self.checkMoveWindow(self.w_main_pos.x()+w_main.width()+8,self.w_main_pos.y())        
                
#        #INITIALISING:
        self.myVeloPID = self.myTask.giveVeloPID()
     
        self.load()
        self.LCD_validRange.display(self.myData.convertVoltToMM(float(self.myConfig['global']['valRange'])))
        self.LCD_period.display(1/self.TB_freq.value())
         
        self.sinePlot = self.PW_sine.plotItem.plot([],[],pen = 'g')
        
        #CONNECTING BUTTONS AND SIGNALS:
        self.TB_amp.valueChanged.connect(self.setAF)
        self.TB_freq.valueChanged.connect(self.setAF)

        self.TB_P_velo.valueChanged.connect(self.setPIDs)
        self.TB_I_velo.valueChanged.connect(self.setPIDs)
        self.TB_D_velo.valueChanged.connect(self.setPIDs)
        
        self.BTN_save.clicked.connect(self.save)   
        self.BTN_load.clicked.connect(self.load)
        self.BTN_resetI.clicked.connect(self.myVeloPID.resetIntegrator)
        
        self.myTimer.timeout.connect(self.updateWindow)
                
        self.show()
        self.windowShown=True                      

    def updateWindow(self): 
        sineData = self.mySine.giveSineData()
        x =sineData[0]
        y =self.myData.simpleMMtoVolt(sineData[1])
        self.sinePlot.setData(x,y)
        
        self.LCD_su.display(self.myVeloPID.getSu())
        self.LCD_eps.display(self.myVeloPID.getEps())
        self.LCD_output.display(self.myVeloPID.getOutput())

    def setAF(self):
        a = float(self.TB_amp.value())
        f = float(self.TB_freq.value())
        self.mySine.setAF(a,f)
        self.LCD_period.display(1/f)
        
       
    def setPIDs(self):
        self.myVeloPID.setPID(self.TB_P_velo.value(),'p','velo')
        self.myVeloPID.setPID(self.TB_I_velo.value(),'i','velo')
        self.myVeloPID.setPID(self.TB_D_velo.value(),'d','velo')
       
    def save(self):
        activeCoil = self.myConfig['global']['activecoil']
        a = str(self.TB_amp.value())
        f = str(self.TB_freq.value())
        self.myConfig['global']['velo_freq'] = f
        self.myConfig['global']['velo_amp'] = a
        self.myConfig[activeCoil]['P_velo']=str(self.TB_P_velo.value())
        self.myConfig[activeCoil]['I_velo']=str(self.TB_I_velo.value())
        self.myConfig[activeCoil]['D_velo']=str(self.TB_D_velo.value())
        with open('config.ini', 'w') as configfile:
            self.myConfig.write(configfile)

        
    def load(self):  
        activeCoil = self.myConfig['global']['activecoil']
        self.TB_P_velo.setValue(float(self.myConfig[activeCoil]['P_velo']))
        self.TB_I_velo.setValue(float(self.myConfig[activeCoil]['I_velo']))
        self.TB_D_velo.setValue(float(self.myConfig[activeCoil]['D_velo']))
        self.TB_freq.setValue(float(self.myConfig['global']['velo_freq']))
        self.TB_amp.setValue(float(self.myConfig['global']['velo_amp']))
        self.setAF()


            
    def manualClose(self):
        self.windowShown = False
        self.myTask.switchToStatic()
        self.sineActive = False
        self.myMainWindow.TXT_activeMode.setText('Static')  
        self.close() 
        
    def closeEvent(self,event):
        self.manualClose()
        

        
        
            
            
