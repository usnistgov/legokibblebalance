from __future__ import division
import numpy as np
import pyqtgraph as pg

import gui_w_cfgPos
import basicWindow


      
class ConfigurePosition(gui_w_cfgPos.QtGui.QMainWindow,gui_w_cfgPos.Ui_MainWindow,basicWindow.BasicWindow):
    def __init__(self, w_main):
        super(ConfigurePosition,self).__init__()
        self.loadBasicObjects(w_main)
        self.setupUi(self)
        
        self.w_main_pos = w_main.pos()
        #Inherited from Basic Window
        self.checkMoveWindow(self.w_main_pos.x()+w_main.width()+8,self.w_main_pos.y())    
        
        self.myStaticPID = self.myTask.giveStaticPID()
        
        self.notConfirmed = True
        self.myZeroposition = 0.0 #previously in config
        self.armLength = float(self.myConfig['global']['armlength'])
        self.started = False
        self.readyToRead = False
        self.epsBarrierCo = 30
        self.readToReadCo = 0
        self.doEpsCheck = False
        self.samplescalculated = False
        
        self.myMax = float(self.myConfig['global']['valRange'])
        self.myMin = -1*self.myMax

        self.BTN_start.clicked.connect(self.start)
        self.BTN_confirm.clicked.connect(self.multiconnect)
        self.BTN_fit.clicked.connect(self.fit)
        self.BTN_savefit.clicked.connect(self.savefits)
        self.pt = 1
        self.pco = 0
        self.pointHeights = []
        self.points = [[],[]]
        self.epsco  = 30
        self.epsBarrier = 0.1*(self.myMax-self.myMin)
        
        self.currentFit = [ float(i) for i in (self.myConfig['global']['posfit']).split(',')]
        self.TXT_currentfit.setText(self.myConfig['global']['posfit'])
        self.fitDisplayRange = np.arange(self.myMin,self.myMax,0.0001)
        self.plotCurrentfit = self.PW_fits.plotItem.plot(self.fitDisplayRange,np.polyval(self.currentFit,self.fitDisplayRange), pen= 'r')
        self.newFit = self.PW_fits.plotItem.plot([0],[0],pen='g')
        self.fitPoints = pg.ScatterPlotItem(brush=None, symbol='x')     
        self.PW_fits.addItem(self.fitPoints)
        
        
        
        self.myTimer.timeout.connect(self.checkEpsBarrier)

        
        self.show() 
        self.windowShown=True             
            
    def start(self):
        if self.started == True:
            self.pco = 0
            self.pt = 0
            self.pointHeights = []
            self.points = [[],[]]
        self.started = True            
        self.status = 'getWallDistance()'
        self.T_Instructions.setPlainText('Please Input below:')
        self.T_Instructions.appendPlainText('Distance from the "KnifeEdge" to the Wall.')
        self.T_Instructions.appendPlainText('! Use the Distance in mm !')
        self.BTN_confirm.setEnabled(True)
        self.TB_value.setEnabled(True)
        self.BTN_start.setEnabled(False)
        self.TB_degree.setEnabled(False)
        self.BTN_fit.setEnabled(False)
        self.setBalanceUiReady(True)

        
    def multiconnect(self):
        if self.status == 'getWallDistance()':
            self.getWallDistance()
        elif self.status == 'getSampleNr()':
            self.getSampleNr()
        elif self.status == 'calibPt()':
            self.calibPt()
        elif self.status == 'restart()':
            self.restart()
        
    def getWallDistance(self):
        distance = self.TB_value.value()
        if distance > 0 :
            self.wallDistance = distance
            self.T_Instructions.setPlainText('Please Input below:')
            self.T_Instructions.appendPlainText('Number of Samplepoints to take.')
            self.T_Instructions.appendPlainText('! Number must be bigger than 3 and odd !')
            self.status = 'getSampleNr()'
        else: 
            self.T_Instructions.setPlainText('ERROR: Walldistance must be bigger than 0!')

    def getSampleNr(self):
        samplesize = int(self.TB_value.value())
        if samplesize >= 3:
                if self.isOdd(samplesize):
                    self.pco = samplesize
                    self.points[0] = self.calcMeasurementPos(samplesize)
                    
                    self.instructions()
                    self.setBalanceUiReady(False)
                else: 
                    self.T_Instructions.setPlainText('ERROR: Samplesize must be ODD!')
        else: 
            self.T_Instructions.setPlainText('ERROR: Samplesize must be bigger than 3!')        

    def instructions(self):
        if self.pco > 0:
            self.T_Instructions.setPlainText('Please wait until the Balance is ready.')
            self.T_Instructions.appendPlainText('Then read the Laserposition from the Wall')
            self.T_Instructions.appendPlainText('Please Input the heigt in mm below.')
            self.T_Instructions.appendPlainText(('Currently setting Point Nr: '+str(self.pt)+' at '+str(self.points[0][self.pt-1])+' V (Shadow Sensor)'))
            self.setNextPoint(self.points[0][self.pt-1])
            self.setBalanceUiReady(False)
            self.setCheckEps(True)
            self.status = 'calibPt()'
        else:
            self.points[1]= self.calcPos()
            self.T_Instructions.setPlainText('All samplepoints have been calculated!')
            self.T_Instructions.appendPlainText('Proceed by fitting them.')
            self.T_Instructions.appendPlainText('Press "Start Calibration" again to start over.')
            self.showPoints()
            self.started = False
            self.TB_degree.setEnabled(True)
            self.BTN_start.setEnabled(True)
            self.BTN_confirm.setEnabled(False)
            self.TB_value.setEnabled(False)
            self.BTN_fit.setEnabled(True)
        
    def calibPt(self):
        value = self.TB_value.value()
        self.TB_value.setValue(-1)
        if value >= 0:
            self.pointHeights.append(value)
            self.pt +=1
            self.pco -=1
            prinT(self.pco)
            self.instructions()
        else:
            self.T_Instructions.appendPlainText('ERROR')
            self.T_Instructions.appendPlainText('')
            self.T_Instructions.appendPlainText('Invalid input')
            self.T_Instructions.appendPlainText('')
            self.T_Instructions.appendPlainText('Please Input heigt in mm!')
            
    def showPoints(self):
        self.fitPoints.setData(self.points[0],self.points[1])
        self.T_points.setPlainText('Points SSV Coil-Position')
        co = 1
        for p in range(0,len(self.points[0])):
            self.T_points.appendPlainText(str(co)+': '+str(self.points[0][p])+' V: '+str(self.points[1][p])+' mm')
            co += 1
        
        try:
            (self.T_points.verticalScrollBar()).setValue(0)
        except:
            pass
        
        
    def fit(self):
        order = self.TB_degree.value()
        if order >= 2:
            self.posfit = np.polyfit(self.points[0],self.points[1],order)
            self.posfit[-1] = 0
            self.ssvfit = np.polyfit(self.points[1],self.points[0],order)
            self.ssvfit[-1] = 0
            self.newFit.setData(self.fitDisplayRange,np.polyval(self.posfit,self.fitDisplayRange), pen= 'g')
            self.T_fitresult.setPlainText(('Your Fit is: (highest polynomial first)'))
            self.T_fitresult.appendPlainText(str(self.posfit))
            self.BTN_savefit.setEnabled(True)
        else:
            self.T_fitresult.appendPlainText('ERROR')
            self.T_fitresult.appendPlainText('Invalid input')
            self.T_fitresult.appendPlainText('Please Input Integer >= 2!')
                
        try:
            (self.T_fitresult.verticalScrollBar()).setValue(0)
        except:
            pass            
            
    def savefits(self):
        self.savefit(self.posfit, 'posfit')
        self.savefit(self.ssvfit, 'ssvfit') #TODO CHECK below
        self.currentFit = [ float(i) for i in (self.myConfig['global']['posfit']).split(',')]
        self.fitDisplayRange = np.arange(self.myMin,self.myMax,0.0001)
        self.plotCurrentfit = self.PW_fits.plotItem.plot(self.fitDisplayRange,np.polyval(self.currentFit,self.fitDisplayRange), pen= 'r')
        self.TXT_currentfit.setText(self.myConfig['global']['posfit'])
            
    def savefit(self, fit, name):
        fitstr = ''
        for part in fit:
            if fitstr != '':
                fitstr = fitstr + ','
            fitstr = fitstr + str(part)
        self.myConfig['global'][name] = fitstr
        self.BTN_savefit.setEnabled(False)
        with open('config.ini', 'w') as configfile:
            self.myConfig.write(configfile)
            
        

        
    def calcMeasurementPos(self, number):
        toCalc = (number-1)/2
        fromMinToZero = np.linspace(self.myMin,self.myZeroposition,toCalc,False)
        fromZeroToMax = np.linspace(self.myZeroposition,self.myMax,toCalc+1,True)
        measurementPos = np.hstack((fromMinToZero,fromZeroToMax))
        returnlist = measurementPos.tolist()
        print(returnlist)
        return returnlist      
        
    def calcPos(self):
        zeroheight = self.pointHeights[int(((len(self.pointHeights)-1)/2))]
        relPos = []
        pos = []
        for heightpoint in self.pointHeights:
            print(heightpoint, zeroheight, heightpoint-zeroheight)
            relPos.append(heightpoint - zeroheight)
        print(relPos)
        for rp in relPos:
            h = (rp/self.wallDistance)*self.armLength
            pos.append(h)
        print(pos)
        return pos
        

        
    def isOdd(self, x):
        if x % 2 == 1:
            return True
        else: 
            return False
        
    def setCheckEps(self, checkEps):
        self.doEpsCheck = checkEps
    
    def checkEpsBarrier(self):
        if self.doEpsCheck == False:
            return
        if abs(self.myStaticPID.getEps()) < self.epsBarrier:
            if self.readToReadCo >= self.epsBarrierCo:
                self.setBalanceUiReady(True)
            else:                
                self.readToReadCo += 1
        else:
            self.readToReadCo = 0
            self.setBalanceUiReady(False)
            
    def setBalanceUiReady(self, isReady):
        if self.started == True:
            self.BTN_confirm.setEnabled(isReady)
            self.TXT_wait.setEnabled(not(isReady))
            self.TXT_ready.setEnabled(isReady)
            if not(isReady):
                self.readToReadCo = 0
        
    def setNextPoint(self, voltage):
        self.myStaticPID.setTarget(voltage)
        self.setBalanceUiReady(False)
            
    def manualClose(self):
        self.windowShown = False
        self.close()
        self.sineActive = False
        
    def closeEvent(self,event):
        self.manualClose()
        

        
        
            
            
