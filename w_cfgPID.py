import gui_w_cfgPID
import basicWindow
from PyQt5 import QtWidgets

class CalibratePID(gui_w_cfgPID.Ui_MainWindow,basicWindow.BasicWindow):
    def __init__(self, w_main):
        super(CalibratePID, self).__init__()
        self.loadBasicObjects(w_main)  
        #self.setupUi(self)
        
        self.w_main_pos = w_main.pos()
        #Inherited from Basic Window
        self.checkMoveWindow(self.w_main_pos.x()+w_main.width()+8,self.w_main_pos.y())
        
        
        self.myStaticPID = self.myTask.giveStaticPID()
        
        #setting up the ui
        #self.minPos = float(self.myConfig['global']['mymin'])
        #self.maxPos = float(self.myConfig['global']['mymax'])
        #mivopos = self.myData.convertVoltToMM(self.minPos)
        #mavopos = self.myData.convertVoltToMM(self.maxPos)
  #      if mavopos > mivopos :
  #          self.TB_target.setMinimum(mivopos)
  #          self.TB_target.setMaximum(mavopos)
    #    else:
  #          self.TB_target.setMinimum(mavopos)
   #         self.TB_target.setMaximum(mivopos)
        
        
        self.TB_target.setMinimum(-10)
        self.TB_target.setMaximum(10)

        
        self.loadPID()
        self.TB_target.setValue(0.0)
        
        print('target: ',self.TB_target.value())

        #connecting timers and buttons and Textboxes        
        self.TB_P_fine.valueChanged.connect(self.setPIDs)
        self.TB_I_fine.valueChanged.connect(self.setPIDs)
        self.TB_D_fine.valueChanged.connect(self.setPIDs)
        self.TB_P_coarse.valueChanged.connect(self.setPIDs)
        self.TB_I_coarse.valueChanged.connect(self.setPIDs)
        self.TB_D_coarse.valueChanged.connect(self.setPIDs)
        #self.TB_target.valueChanged.connect(lambda: self.myStaticPID.setTarget(self.myData.convertMMToVolt(self.TB_target.value())))
        self.TB_target.valueChanged.connect(lambda: self.myStaticPID.setTarget(self.TB_target.value()))

        self.TB_eps_switch.valueChanged.connect(self.setPIDs)    
        
        
        self.BTN_savePID.clicked.connect(self.savePID)
        self.BTN_loadPID.clicked.connect(self.loadPID)
        self.BTN_resetIntegrator.clicked.connect(self.myStaticPID.resetIntegrator)

        self.myTimer.timeout.connect(self.updateDisplay) 
        
        self.show()
        self.windowShown = True             #Is used to determine if window is open or closed

        
    def updateDisplay(self):                    #updating labels and lcds
        self.TXT_PID_mode.setText(self.myStaticPID.getPIDmode())
        self.LCD_pos.display(-self.myStaticPID.y)
        self.LCD_su.display(self.myStaticPID.getSu())
        self.LCD_eps.display(self.myData.convertVoltToMM(self.myStaticPID.getEps()))
        self.LCD_AO1.display(self.myStaticPID.getOutput())
    
    def loadPID(self):                      #loading PID values from config
        activeCoil = self.myConfig['global']['activecoil']
        self.TB_P_fine.setValue(float(self.myConfig[activeCoil]['P_fine']))
        self.TB_I_fine.setValue(float(self.myConfig[activeCoil]['I_fine']))
        self.TB_D_fine.setValue(float(self.myConfig[activeCoil]['D_fine']))
        self.TB_P_coarse.setValue(float(self.myConfig[activeCoil]['P_coarse']))
        self.TB_I_coarse.setValue(float(self.myConfig[activeCoil]['I_coarse']))
        self.TB_D_coarse.setValue(float(self.myConfig[activeCoil]['D_coarse']))
        self.TB_eps_switch.setValue(float(self.myConfig[activeCoil]['pidswitchvalue']))
        
    def savePID(self):                      #saving pid values to config  
        activeCoil = self.myConfig['global']['activecoil']
        self.myConfig[activeCoil]['P_fine']= str(self.TB_P_fine.value())
        self.myConfig[activeCoil]['I_fine']=str(self.TB_I_fine.value())
        self.myConfig[activeCoil]['D_fine']=str(self.TB_D_fine.value())
        self.myConfig[activeCoil]['P_coarse']=str(self.TB_P_coarse.value())
        self.myConfig[activeCoil]['I_coarse']=str(self.TB_I_coarse.value())
        self.myConfig[activeCoil]['D_coarse']=str(self.TB_D_coarse.value())
        self.myConfig[activeCoil]['pidswitchvalue']=str(self.TB_eps_switch.value())
        with open('config.ini', 'w') as configfile:
            self.myConfig.write(configfile)
            
    def setPIDs(self):
        print('target: ',self.TB_target.value())
        self.myStaticPID.setPID(self.TB_P_fine.value(), 'p', 'fine')
        self.myStaticPID.setPID(self.TB_I_fine.value(), 'i', 'fine')
        self.myStaticPID.setPID(self.TB_D_fine.value(), 'd', 'fine')
        self.myStaticPID.setPID(self.TB_P_coarse.value(), 'p', 'coarse')
        self.myStaticPID.setPID(self.TB_I_coarse.value(), 'i', 'coarse')
        self.myStaticPID.setPID(self.TB_D_coarse.value(), 'd', 'coarse')
        self.myStaticPID.setPIDSwitch(self.myData.convertMMToVolt(self.TB_eps_switch.value()))

    def manualClose(self):
        self.windowShown = False
        self.myStaticPID.setTarget(0)
        self.close()
            
    def closeEvent(self,event):
        self.manualClose()