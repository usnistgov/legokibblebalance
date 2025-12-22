from __future__ import division
import numpy as np
import scipy.signal
import time

class DataArray(object):                                          #class creating a data object
    def __init__(self):                             #containing arrays for data and filtered data
        self.data = np.zeros(1)
            
        self.mymaxlen = 123
        
    def setMaxlen(self, maxlen):
        self.mymaxlen = int(maxlen)
        
    def addData(self, newdata):                             #add data to the object and create dataF for it
        self.data = np.hstack((self.data,newdata))

        if len(self.data)>self.mymaxlen:                       #ensuring data arrays dont get longer than specified maxlength
            self.data = self.data[-self.mymaxlen:]
        
    
    def removeAllData(self):
        self.data = np.zeros(0)
        
    def giveAllData(self):
        return self.data
        
    def giveLastData(self):
        return self.data[-1]
        
    def giveLastXDataElements(self, x):
        return self.data[-x:]
        
    def giveNDataPeriods(self, N, dt, f):
        samplesperperiod = int((1/f) / dt)
        if len(self.data) < N*samplesperperiod:
            return self.data
        else:
            return self.giveLastXDataElements(N*samplesperperiod)

###############################################################################            
      
class DataArrayWithFilt(DataArray):
    def __init__(self):
        super(DataArrayWithFilt,self).__init__()
        self.dataF = np.zeros(1)
                
        try:
            b,a = scipy.signal.butter(2,[0.005])                 #creating filter koefficients for butterworth filter
        except:
            b,a = scipy.signal.butter(2,0.005)                 #creating filter koefficients for butterworth filter

        self.filter = myfilter(b,a)                         #creating IIR filter 
        
    def addData(self, newdata):
        super(DataArrayWithFilt, self).addData(newdata)
        newdataf = self.filter.filt(newdata)
        self.dataF = np.hstack((self.dataF, newdataf))
        
        if len(self.dataF)>self.mymaxlen: 
            self.dataF = self.dataF[-self.mymaxlen:]
            
    def removeAllDataF(self):
        self.dataF = np.zeros(0)
        
    def giveAllDataF(self):
        return self.dataF     
    
    def giveLastDataF(self):
        return self.dataF[-1]
    
    def giveLastXDataFElements(self, x):
        return self.dataF[-x:]
        
    def giveNDataFPeriods(self, N, dt, f):
        samplesperperiod = int((1/f) / dt)
        if len(self.dataF) < N*samplesperperiod:
            return self.dataF
        else:
            return self.giveLastXDataFElements(N*samplesperperiod)  
      

        
###############################################################################        
        
class myfilter():                                           #creating an IIR filter 
    def __init__(self,b,a):
        self.b =b
        self.a = a
        self.zi =scipy.signal.lfilter_zi(b,a)
    def filt(self,inp):
        outp,self.zi= scipy.signal.lfilter(self.b,self.a,inp,axis=0,zi=self.zi)
        return outp
###############################################################################        
        
class ProcessedData():
    def __init__(self, config):                                     #initialising data object for each input channel and t
        self.myConfig = config
        self.lastcalltime = time.time()
    
        self.photoraw = DataArrayWithFilt()
        self.ai0D = DataArrayWithFilt()
        self.ai1D = DataArrayWithFilt()
        self.ai2D = DataArrayWithFilt()
        self.ai6D = DataArrayWithFilt()
        
        self.cbdt = DataArray()        
        
        self.t = DataArray()
        
        self.current = DataArray()
        

        self.posA = DataArray()
        self.posB = DataArray()        
        
        self.veloA = DataArray()
        self.veloB = DataArray()
        
        self.bl0 = DataArray()
        self.bl0_t = DataArray()

        self.Dlength = 0
        self.co = 0
        self.tco = 0
        self.ai0raw = 0
        self.ai0rawlp = 0.01
        
    def setAllMaxlen(self, maxlen):
        self.photoraw.setMaxlen(maxlen)
        self.ai0D.setMaxlen(maxlen)
        self.ai1D.setMaxlen(maxlen)
        self.ai2D.setMaxlen(maxlen)
        self.ai6D.setMaxlen(maxlen)
        
        self.cbdt.setMaxlen(maxlen)
        
        self.t.setMaxlen(maxlen)
        
        self.current.setMaxlen(maxlen)
        
        self.posA.setMaxlen(maxlen)
        self.posB.setMaxlen(maxlen)
        
        self.veloA.setMaxlen(maxlen)
        self.veloB.setMaxlen(maxlen)
        
    def connectTask(self, task):
        task.signalRawdata.connect(self.storeRawData)
        
        
        
    def storeRawData(self, rawdata, NrOfCh, dt, L, cbdt):         #storing rawdata in data objects
        self.thiscalltime = time.time()  
        self.lastcalltime = self.thiscalltime
        self.Dlength = L
        
        self.ai0 = rawdata[0::NrOfCh]
        self.ai1 = rawdata[1::NrOfCh]
        self.ai2 = rawdata[2::NrOfCh]
        self.ai6 = rawdata[3::NrOfCh] 

        self.ai0raw = self.ai0raw*(1.0-self.ai0rawlp)+self.ai0rawlp*np.mean(self.ai0)
        self.ai0D.addData(self.ai0-float(self.myConfig['global']['balance0photooffset']))
        self.photoraw.addData(self.ai0)
        self.ai1D.addData(self.ai1)
        self.ai2D.addData(self.ai2)
        self.ai6D.addData(self.ai6)
        self.tco = (self.tco+1)%100
        #if self.tco ==0:
         #   print self.ai0raw,float(self.myConfig['global']['balance0photooffset'])
        
        self.cbdt.addData(cbdt)
        
        nt = dt*np.arange(self.co,self.co+self.Dlength)         #creating timeline for the added data
        self.t.addData(nt)
        self.co += self.Dlength
        
        self.current.addData((self.ai1D.giveLastXDataFElements(self.Dlength)/float(self.myConfig['global']['resistance'])*1000))              # I = U / R  & Converted in mA
        
        lastAi0F = self.ai0D.giveLastXDataFElements(self.Dlength)
        lastLPos = self.convertVoltToMM(lastAi0F)
        self.posB.addData(lastLPos)                            #CAREFUL WHEN IMPLEMENTING COIL SWITCH
        self.posA.addData(lastLPos*(-1))                       #--> IF STATEMENT
        
        aLast = self.posA.giveLastXDataElements(self.Dlength+1)
        posANews= np.array(aLast[1:])
        posAOlds= np.array(aLast[:-1])
        velA = (posANews-posAOlds)/(self.Dlength*dt)          #in mm/s
        self.veloA.addData(velA)
        #print('posANews={0:9.6f} denom={1:8.6f} '.format(posANews))
        
        bLast = self.posB.giveLastXDataElements(self.Dlength+1)
        posBNews= np.array(bLast[1:])
        posBOlds= np.array(bLast[:-1])
        velB = (posBNews-posBOlds)/(self.Dlength*dt)           #in mm/s
        self.veloB.addData(velB)        
        
    def convertVoltToMM(self, data):                    #TODO RENAME POS & SSV
        posfit = [ float(i) for i in (self.myConfig['global']['posfit']).split(',')]
        pos = np.polyval(posfit,data)
        return pos
        
    def convertMMToVolt(self, data):
        ssvfit = [ float(i) for i in (self.myConfig['global']['ssvfit']).split(',')]
        ssv = np.polyval(ssvfit,data)
        return ssv
    
    def simpleMMtoVolt(self,data):
        return float(self.myConfig['global']['balance0photooffset'])+data
  
    def giveDataArray(self, name):                         #give a specific data object
        if name == 't':
            returnarray = self.t
        elif name == 'ai0':
            returnarray = self.ai0D
        elif name == 'ai1':
            returnarray = self.ai1D
        elif name == 'ai2':
            returnarray = self.ai2D
        elif name == 'ai6':
            returnarray = self.ai6D
        elif name == 'current':
            returnarray = self.current
        elif name == 'posA':
            returnarray = self.posA
        elif name == 'posB':
            returnarray = self.posB
        elif name == 'veloA':
            returnarray = self.veloA
        elif name == 'veloB':
            returnarray = self.veloB
        elif name == 'bl0':
            returnarray = self.bl0
        elif name == 'bl0_t':
            returnarray = self.bl0_t
        elif name == 'cbdt':
            returnarray = self.cbdt
        elif name == 'photoraw':
            returnarray = self.photoraw
        elif name=='photowoff':
            returnarray = self.ai0D
        else:
            print('ERROR: Choose From t,ai0,ai1,ai2,ai6,posA,PosB,veloA,veloB,sine,bl0,bl0_t,cbdt and NOT:', name)     
        return returnarray        

    def correctSize(self, x, y):                                 #making sure that two data arrays are the same length
        l1 =len(x)
        l2 =len(y)
        ll =min(l1,l2)
        return x[0:ll],y[0:ll]