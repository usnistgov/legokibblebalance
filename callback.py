from __future__ import division
import PyDAQmx as daq
from PyQt5 import QtCore
import numpy as np
import PID

import datetime 

class CallbackTask(daq.Task, QtCore.QObject):
    signalNewCallback = QtCore.pyqtSignal()
    signalFitBL = QtCore.pyqtSignal()
    signalRawdata = QtCore.pyqtSignal(object, object, object, object, object)
    def __init__(self,data, config,sine,coilSelector):
        daq.Task.__init__(self)
        QtCore.QObject.__init__(self)
        self.myData = data                  #Save given data object
        self.myConfig = config              #Save given config object
        self.myCoilSelector = coilSelector
        self.mySine = sine        
        print('callback here: Dev- ', self.myConfig['global']['device'])
        self.myDevice = self.myConfig['global']['device']
        #INITIALISE VARIABLES
        self.samprate = float(self.myConfig['dataacq']['samprate'])                 #Samples per sec and channel
        self.L =int(self.myConfig['dataacq']['length'])                           #Samples to read per channel
        self.NrOfCh=4                      #Channels used for reading
        self.totalL=self.L*self.NrOfCh      #Samples read per Callback
        self.dt = 1.0/self.samprate              #Time between Samples
        self.rawdata = np.zeros(self.totalL)#Array to read rawdata into
        self.s = float(self.myConfig['dataacq']['s'])
        self.maxlen = self.samprate * self.L * self.s           #Maximal amount of data to be stored
        self.myData.setAllMaxlen(self.maxlen)
        self.buffer_factor = int(self.myConfig['dataacq']['buffer_factor'])  
        self.photooffset = float(self.myConfig['global']['balance0photooffset'])
        

        self.oldt =datetime.datetime.now()
        
#        self.offset = 0.0
        self.periodCo = 0
        self.doPID = True                   #Determines if Feedback is on
        self.mode = 'static'                #Determines the PID mode
        self.oldmode = 'static'                #Determines the PID mode        
#        self.controlViaTarget = True
        self.PID_fine = []                  #List for fine PID values
        self.PID_coarse = []                #List for coarse PID values
        self.PID_velo = []
        self.PID_fine.append(float(self.myConfig['coilA']['P_fine']))           #Loading PID From config
        self.PID_fine.append(float(self.myConfig['coilA']['I_fine']))
        self.PID_fine.append(float(self.myConfig['coilA']['D_fine']))
        self.PID_coarse.append(float(self.myConfig['coilA']['P_coarse']))
        self.PID_coarse.append(float(self.myConfig['coilA']['I_coarse']))
        self.PID_coarse.append(float(self.myConfig['coilA']['D_coarse']))
        self.PID_velo.append(float(self.myConfig['coilA']['p_velo']))
        self.PID_velo.append(float(self.myConfig['coilA']['i_velo']))
        self.PID_velo.append(float(self.myConfig['coilA']['d_velo']))
        self.Ilimit = 10.0                  #Limits the Derivator prev. in cfg
        self.target = 0.0                   #Target of Balancing  prev. in cfg
        self.PIDSwitchvalue = float(self.myConfig['coilA']['pidswitchvalue'])   #Value that determines when to use fine/coarse
        self.maxoutput = 10                 #Maximum Voltage to give to the Balance
        self.co = 0
        self.sign = 1.0

        
        
        self.velo_f = float(self.myConfig['global']['velo_freq'])
        self.samplesperperiod = (self.samprate/self.velo_f)
        self.callbacksPerPeriod = self.samplesperperiod/self.L
#        n = 2
#        self.veloPIDwidth = n*self.samplesperperiod
        
        #Creating PID Object for static mode which is later used to 'bring balance to the Force[s]'
        self.staticPID = PID.PID(True, self.PID_coarse,self.PID_fine,self.PIDSwitchvalue,self.dt, self.L, self.Ilimit,self.target,self.maxoutput)
        #Creating PID Object for velo mode, because sometimes [the] Balance requires changes
        self.veloPID = PID.PID(False, self.PID_velo,self.PID_velo,0,self.dt, self.L, self.Ilimit,self.target,self.maxoutput)
        
        #OPEN LOOP VERSION
#        self.veloPID = PID.PID(False,self.PID_velo,self.PID_velo,1,self.dt,self.veloPIDwidth,self.Ilimit,self.target,self.maxoutputvelo) 

        #Creates 4 Input Channels to read ai0, ai1, ai2, ai6
        #self.CreateAIVoltageChan(self.myDevice +"/ai3","",daq.DAQmx_Val_Diff,-1.0,1.0,daq.DAQmx_Val_Volts,None)
        self.CreateAIVoltageChan(self.myDevice +"/ai0","",daq.DAQmx_Val_Diff,-1.0,1.0,daq.DAQmx_Val_Volts,None)
        self.CreateAIVoltageChan(self.myDevice +"/ai1","",daq.DAQmx_Val_Diff,-1.0,1.0,daq.DAQmx_Val_Volts,None)
        self.CreateAIVoltageChan(self.myDevice +"/ai2","",daq.DAQmx_Val_RSE,-1.0,1.0,daq.DAQmx_Val_Volts,None)
        self.CreateAIVoltageChan(self.myDevice +"/ai6","",daq.DAQmx_Val_RSE,-1.0,1.0,daq.DAQmx_Val_Volts,None)
        #Configures Buffer, timing and Callback
        self.CfgInputBuffer(self.buffer_factor*self.L)
        self.CfgSampClkTiming("",self.samprate,daq.DAQmx_Val_Rising,daq.DAQmx_Val_ContSamps,self.L*self.buffer_factor)  
        self.AutoRegisterEveryNSamplesEvent(daq.DAQmx_Val_Acquired_Into_Buffer,self.L,0)
        self.AutoRegisterDoneEvent(0)
        
        
    def EveryNCallback(self):
        self.takeTime()
        self.co = (self.co+1)%100
        self.photooffset = float(self.myConfig['global']['balance0photooffset'])
        #Configures data reading
        read = daq.int32()
        self.ReadAnalogF64(self.L,10.0,daq.DAQmx_Val_GroupByScanNumber,self.rawdata,self.totalL,daq.byref(read),None)
        
        #Sorts rawdata to their respective channel        
        self.signalRawdata.emit(self.rawdata, self.NrOfCh, self.dt, self.L, self.delta)
        self.fbSSV = ((self.rawdata[0::self.NrOfCh])[-1])-self.photooffset
        #self.myData.calcVelocities(self.dt)


        #Target Feedback using one of the created PIDs
        if (self.doPID):
            #getting current Balance position to work with
#            shadowVoltage = self.myData.giveDataArray('ai0')
#            currentShadowVoltage = shadowVoltage.giveLastData()
            currentShadowVoltage = self.fbSSV
            #Checking if the balance is in static mode
            if self.mode == 'static':
                self.periodCo = 0
                self.mySine.setActive(False)
                
                self.output = self.staticPID.doPIDCalc(currentShadowVoltage)
                #sign = int(self.myConfig[self.myCoilSelector.getWeightCoil]['polarity'])
                if self.co==0:
                    self.sign = int(self.myConfig['coil'+self.myCoilSelector.getWeightCoil()]['polarity'])
#                if self.co==0:
 #                   print(currentShadowVoltage,
  #                        self.photooffset,
   #                       self.staticPID.target,
    #                      self.sign,self.myCoilSelector.getWeightCoil())
                self.setVoltage(self.output*self.sign)    
                
            elif self.mode == 'velo':
                if self.oldmode!=self.mode:
                    self.veloPID.resetIntegrator()
                self.velo_f = self.mySine.getF()
                n = 2
                self.veloPIDwidth = n*(self.samprate/self.velo_f) #samplesperperiod
                self.periodCo +=1 
                #if periodCo%100=0 :
                    
                
#                if self.controlViaTarget == True:
                #CLOSED LOOP VERSION
                #self.sinepos = self.myData.convertMMToVolt(self.mySine.giveCurrentY())
                self.sinepos = self.myData.simpleMMtoVolt(self.mySine.giveCurrentY())
                #self.staticPID.setTarget(self.sinepos)
                self.veloPID.setTarget(0)
                #self.output = self.staticPID.doPIDCalc(currentShadowVoltage)
                self.output = self.veloPID.doPIDCalc(currentShadowVoltage,mode='velo')+\
                    self.mySine.giveCurrentY()
                                                     #target_der = self.mySine.giveDerivative(),\
                                                         #filtfac = 0.0)
                #sign = int(self.myConfig[self.myCoilSelector.getWeightCoil]['polarity'])
                #if self.co==0:
                self.sign = int(self.myConfig['coil'+self.myCoilSelector.getWeightCoil()]['polarity'])
                self.setVoltage(self.output*self.sign)
                
                if self.periodCo == self.veloPIDwidth:
                    self.periodCo = 0
                    self.signalFitBL.emit()
            else:
                print('ERROR: selected PID mode is Invalid')
            self.oldmode = self.mode
                
        self.signalNewCallback.emit()
           
        return 0 # The function should return an integer
            
    def takeTime(self):
        newt = datetime.datetime.now()
        self.delta = (newt - self.oldt).total_seconds()
        self.oldt = newt
            
    def setVoltage(self, newVolt):          #Outputs the given Voltage to Ao1 Channel
        vtask = daq.Task()            
        vtask.CreateAOVoltageChan(self.myDevice +"/ao1","",-10.0,10.0,daq.DAQmx_Val_Volts,None)
        vtask.StartTask()
        vtask.WriteAnalogScalarF64(1,10.0,newVolt,None)
        vtask.StopTask()
        
    def getDoPID(self):                     #Returns the value, which determinse if feedback is enabled
        return self.doPID
        
    def setDoPID(self, value):              #Sets the value, which determinse if feedback is enabled
        self.doPID = value
        
    def getPIDmode(self):                   #Return the current PID mode
        return self.mode
        
    def switchToVelo(self):
        self.mode = 'velo'
        
    def switchToStatic(self):
        self.mode = 'static'
        
    def giveStaticPID(self):                      #Returns the generated static PID object
        return self.staticPID
        
    def giveVeloPID(self):                        #Returns the generated velo PID object
        return self.veloPID
        
    def getL(self):                         #Returns L
        return self.L
        
    def getDt(self):                        #Returns Dt
        return self.dt
        
#    def getOffset(self):                    #Returns Offset
#        print 'goffs'
#        return self.offset
        
    def getSamprate(self):
        return self.samprate
#        
#    def getControlViaTarget(self):
#        return self.controlViaTarget