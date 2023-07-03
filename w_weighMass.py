from __future__ import division

import gui_w_weighMass
import basicWindow
      
      
class WeighMass(gui_w_weighMass.QtGui.QMainWindow,gui_w_weighMass.Ui_MainWindow,basicWindow.BasicWindow):
    def __init__(self, w_main):
        super(WeighMass,self).__init__()
        self.loadBasicObjects(w_main)
        self.setupUi(self)
        
        self.w_main_pos = w_main.pos()
        #Inherited from Basic Window
        self.checkMoveWindow(self.w_main_pos.x(),self.w_main_pos.y()-self.height()-26)
        
        self.myStaticPID = self.myTask.giveStaticPID()
        
        self.step = 0  
        activeCoil = self.myConfig['global']['activecoil']
        self.stabilityBarrier = float(self.myConfig['global']['accPosError'])  #0.007 
        self.isHorizontalCo = 0
        self.stabilityTime = 2 #Time ,in Seconds, to wait before allowing to take measurement
        self.stabilityLength = 10 * self.stabilityTime
        
        self.iArray = self.myData.giveDataArray('current')
        self.bl = float(self.myConfig[activeCoil]['bl0'])
        self.g = float(self.myConfig['global']['g'])
        

        self.BTN_start.clicked.connect(self.start)
        self.BTN_restart.clicked.connect(self.restart)        
        
        self.BTN_ZR1.clicked.connect(self.doZR1)
        self.BTN_WM.clicked.connect(self.doWM)
        self.BTN_ZR2.clicked.connect(self.doZR2)
      
        self.myTimer.timeout.connect(self.checkBalanceStatus)
        
        self.show()
        self.windowShown=True
        
    def restart(self):
        self.start()
        
        
        
    def start(self):
        self.T_result.setPlainText('Take your first zeroreading when the balance is ready!')
        
        self.setUIReady(False)
        self.LCD_ZR1.display(0)
        self.LCD_WM.display(0)
        self.LCD_ZR2.display(0)
        
        self.BTN_start.setEnabled(False)
        self.BTN_restart.setEnabled(True)
        
        #START OF WEIGHING PROCESS
        self.step = 1
        
    def doZR1(self):
        activeCoil = self.myConfig['global']['activecoil']
        self.T_result.setPlainText('Now put your mass on coil'+ self.myCoilSelector.getWeightCoil(activeCoil)+' and weigh it!')
        
        #ZEROREADING 1
        self.iZR1 = self.iArray.giveLastData()
        self.LCD_ZR1.display(self.iZR1)
        
        self.step = 2
        self.BTN_ZR1.setEnabled(False)
        self.TXT_readyZR1.setEnabled(False)
    
    def doWM(self):
        self.T_result.setPlainText('Now take your mass mass off and take another zeroreading!')

        #WEIGHMASS
        self.iWM = self.iArray.giveLastData()
        self.LCD_WM.display(self.iWM)
        
        i = self.iWM - self.iZR1
        mass = self.polarity()*((self.bl * i)/self.g)
        
        self.T_result.appendPlainText('The first guess for your mass : '+ str(mass) +' g')
        
        self.step = 3 
        self.BTN_WM.setEnabled(False)
        self.TXT_readyWM.setEnabled(False)
        
    def doZR2(self):
        self.T_result.setPlainText('Your Mass has been succesfully measured!')
        
        #ZEROREADING 2
        self.iZR2 = self.iArray.giveLastData()
        self.LCD_ZR2.display(self.iZR2)
        
        i = self.iWM - ((self.iZR1+self.iZR2)/2)
        mass = self.polarity()*((self.bl * i)/self.g)
        
        self.T_result.appendPlainText('It is: '+ str(mass) +' g')
        self.step = 0
        self.BTN_ZR2.setEnabled(False)
        self.TXT_readyZR2.setEnabled(False)
        self.BTN_start.setEnabled(True)
        self.BTN_restart.setEnabled(False)
        
    def checkBalanceStatus(self):
        if self.isBalanceHorizontal():
            self.setUIReady(True)
#            print 'TRUE'
        else:
            self.setUIReady(False)
#            print 'FALSE'
            
        
    def isBalanceHorizontal(self):
        if abs(self.myStaticPID.getEps()) < self.stabilityBarrier:
            if self.isHorizontalCo == self.stabilityLength:
#                print 'ready', self.isHorizontalCo
                return True               
            else:                
                self.isHorizontalCo += 1
#                print 'almost ready', self.isHorizontalCo
                return False                
        else:
            self.isHorizontalCo = 0
#            print 'not ready', self.isHorizontalCo
            return False
            
    def setUIReady(self, boolean):
        if self.step == 0:
            pass
        elif self.step == 1:
            self.BTN_ZR1.setEnabled(boolean)
            self.TXT_readyZR1.setEnabled(boolean)
        elif self.step == 2:
            self.BTN_WM.setEnabled(boolean)
            self.TXT_readyWM.setEnabled(boolean)
        elif self.step == 3:
            self.BTN_ZR2.setEnabled(boolean)
            self.TXT_readyZR2.setEnabled(boolean)
            
    def polarity(self):
        BLcoil = "coil"+self.myCoilSelector.getBLCoil()
        return int(self.myConfig[BLcoil]['polarity'])
    
    def manualClose(self):
        self.windowShown = False
        self.close()
        
    def closeEvent(self,event):
        self.manualClose()
        

        
        
            
            
