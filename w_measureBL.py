import numpy as np

import gui_w_measureBL
import basicWindow
from PyQt5 import QtWidgets

class MeasureBL(QtWidgets.QMainWindow, gui_w_measureBL.Ui_MainWindow,basicWindow.BasicWindow):
    def __init__(self, w_main):
        super(MeasureBL,self).__init__()
        self.loadBasicObjects(w_main)
        self.setupUi(self)       
        self.windowShown = True
        
        self.w_main_pos = w_main.pos()
        #Inherited from Basic Window
        self.checkMoveWindow(self.w_main_pos.x()+(w_main.width()/2),self.w_main_pos.y()-self.height()-26+(self.height()/2))

        self.myTask.switchToVelo()

        self.TXT_BLcoil.setText('BL of coil: ' + self.myCoilSelector.getBLCoil())
        self.BTN_resetBL0.clicked.connect(self.resetBL0)
        self.BTN_saveBL0.clicked.connect(self.saveBL0)
        self.myTask.signalFitBL.connect(self.fitBL)

        self.dt = self.myTask.getDt()
        self.f = self.mySine.getF()        
        self.startplotOn=False
        self.show()
        
        self.startPlot()
        
    def startPlot(self):
        self.mySine.setActive(True)
        self.dt = self.myTask.getDt()
        self.f = self.mySine.getF()
        self.bl0 = self.myData.giveDataArray('bl0')
        self.bl0.removeAllData()          #to get rid of the initial 0 as first value
        self.bl0_t = self.myData.giveDataArray('bl0_t')
        self.bl0_t.removeAllData()          #to get rid of the initial 0 as first value
        self.bl0.setMaxlen(600)
        self.bl0_t.setMaxlen(600)
                
        
        self.velodata = self.myData.giveDataArray('veloB')
        self.induceddata = self.myData.giveDataArray('ai6')
        
        #self.velodata,self.induceddata = self.myData.correctSize(self.velodata,self.induceddata)
    
        self.twoPeriodsVel = self.velodata.giveNDataPeriods(2,self.dt, self.f)
        self.twoPeriodsInd = self.induceddata.giveNDataFPeriods(2,self.dt,self.f)
        
        try:
            self.PWperiods.clear()
            #self.PWperiods = self.PW_2periods.plotItem.plot(self.twoPeriodsVel,self.twoPeriodsInd)    
            self.PWperiods = self.PW_2periods.plotItem.plot([0],[0],pen='b')
            self.PWperiodsFit = self.PW_2periods.plotItem.plot([0],[0],pen='r') 
            #self.PWperiods.setBackground('w') 
            #self.PWperiodsFit.setBackground('w') 
        except:
            self.PWperiods = self.PW_2periods.plotItem.plot([0],[0],pen='b')
            self.PWperiodsfit = self.PW_2periods.plotItem.plot([0],[0],pen='r')  
            
        self.PW_2periods.setBackground('w')    
        self.PWblofpos = self.PW_BLofPos.plotItem.plot([0],[0])
        self.PW_BLofPos.setBackground('w') 
        #self.PWblofpos2 = self.PW_BLofPos.plotItem.plot([0],[0],pen='r')
        
        self.Plot_BL0ofTime = self.PW_BL0ofTime.plotItem.plot([0],[0])
        self.PW_BL0ofTime.setBackground('w') 
                 
        self.myTimer.timeout.connect(self.updatePlot)
        self.startplotOn=True
        
    def updatePlot(self):
        self.f = self.mySine.getF()
        self.velodat = self.myData.giveDataArray('veloB')
        self.induceddat = self.myData.giveDataArray('ai6')
               
        self.twoPeriodsVe = self.velodat.giveNDataPeriods(2,self.dt, self.f)
        self.twoPeriodsIn = self.induceddat.giveNDataFPeriods(2,self.dt,self.f)

        self.PWperiods.setData(self.twoPeriodsVe,self.twoPeriodsIn)        
    def fitBL(self):
        
        if self.startplotOn==False:
            return
        
        
        self.f = self.mySine.getF()
#        self.velodata = self.myData.giveDataArray('veloB')
#        self.induceddata = self.myData.giveDataArray('ai6')
        self.veC = self.myData.giveDataArray('veloB')
        self.VoC = self.myData.giveDataArray('ai6')
               
#        self.twoPeriodsVel = self.velodata.giveNDataPeriods(2,self.dt, self.f)
#        self.twoPeriodsInd = self.induceddata.giveNDataFPeriods(2,self.dt,self.f)
        self.ve = self.veC.giveNDataPeriods(2,self.dt,self.f)        
        self.Vo = self.VoC.giveNDataFPeriods(2,self.dt,self.f)

        zC = self.myData.giveDataArray('posB')

        z = zC.giveNDataPeriods(2,self.dt,self.f)

        
#        self.PWblofpos.setData(self.twoPeriodsVel,self.twoPeriodsInd)
#        self.PWblofpos.setData(self.ve,self.Vo)
        
        


        #
        # fit V(t,z,v) = b0*v + b1*z*v + b2*z^2*v + b3*z^3*v ... +bm*z^m*v + V0
        # fit parameter b0,..bm,V0
        #
        # BL(z) = b0 *+ b1*z +b2*z^2 ....
        #
        m=4
        f = np.zeros((m+1,len(self.ve)))

        for i in range(m):
            f[i,:] = self.ve*z**i
        
        f[m,:] = np.ones(len(self.ve))
        
        A = np.zeros((m+1,m+1))
        b = np.zeros((m+1,1))
        
        for i in range(m+1):
            for j in range(m+1):
                A[i,j] = np.dot(f[i,:],f[j,:])
            b[i] = np.dot(f[i,:],self.Vo)
        pars = np.dot(np.linalg.inv(A),b)
        
        fitV = np.dot(pars.T,f)
#        res= fitV-V
#        res2 = np.dot(res,res.T)[0,0]
#        res2_per_dgf = res2/(len(v)-m)
        #print res2,res2_per_dgf
        
#        now =datetime.datetime.now()
#        fn = 'data{0}.dat'.format(now.strftime("%H%M%S"))
#        fi = file(fn,'w')
#        for zz,vv,VV in zip(z,v,V):
#            s = "{0:9.8f}\t{1:9.8f}\t{2:9.8f}\n".format(zz,vv,VV)
#            fi.write(s)
#        fi.close()
        

        self.PWperiodsfit.setData(self.ve,fitV[0,:])
        self.PWblofpos.setData(z,np.polyval(pars[-2::-1],z))
        #self.PWblofpos.setData(z,fitV[0,:])
        
        currentBL0 = np.polyval(pars[-2::-1],[0])[-1]
        
        self.bl0_t.addData(len(self.bl0.giveAllData())-1)
        self.bl0.addData(currentBL0)
        self.Plot_BL0ofTime.setData(self.bl0_t.giveAllData(),self.bl0.giveAllData())
        
        self.bl0mean = np.mean(self.bl0.giveAllData())
        bl0eps = abs(self.bl0mean-currentBL0)
        bl0error = abs(bl0eps/currentBL0)*100
        
        self.LCD_BLcurrent.display(currentBL0)
        self.LCD_BLmean.display(self.bl0mean)
        self.LCD_BLerror.display(bl0error)
        
        
        
#       OLD BL FIT
        '''[]
        self.velodata = self.myData.giveDataArray('veloB')
        self.induceddata = self.myData.giveDataArray('ai6')
           
        self.twoPeriodsVel = self.velodata.giveNDataPeriods(2,self.dt,self.f)
        self.twoPeriodsInd = self.induceddata.giveNDataFPeriods(2,self.dt,self.f)
        print np.polyfit(self.twoPeriodsVel,self.twoPeriodsInd,1), self.myTask.getPIDmode(), self.myTask.veloSineCreated
        '''
        
    def resetBL0(self):
        self.bl0.removeAllData()
        self.bl0_t.removeAllData()
        
    def saveBL0(self):
        activeCoil = self.myConfig['global']['activecoil']
        self.myConfig[activeCoil]['bl0'] = str(self.bl0mean)
        with open('config.ini','w') as configfile:
            self.myConfig.write(configfile)
        
    def manualClose(self):
        self.windowShown = False 
        self.myTask.switchToStatic()
        self.mySine.setActive(False)
        self.myMainWindow.TXT_activeMode.setText('Static')
        self.close()  
            
    def closeEvent(self,event):
        self.manualClose()
        
    def useCoilA(self):
        print('coil A')
        print(self.myCoilSelector.getBLCoil())
        self.updateCoil()
        
    def useCoilB(self):
        print('coil B')
        print(self.myCoilSelector.getBLCoil())
        self.updateCoil()
        
    def updateCoil(self):
        self.TXT_BLcoil.setText('BL of coil: ' + self.myCoilSelector.getBLCoil())