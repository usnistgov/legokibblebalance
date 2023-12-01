import PyDAQmx as daq
import numpy as np
        
class CoilSelector(object):
    def __init__(self, config):
        self.myConfig = config
        
    def getMWRef(self, w_main):
        self.myMainWindow = w_main
        
    def coilInit(self):
        self.selectCoil(self.myConfig['global']['activecoil'])
        if self.myConfig['global']['activecoil'] == 'coilA':
            self.myMainWindow.RB_coilA.setChecked(True)
        else:
            self.myMainWindow.RB_coilB.setChecked(True)
        

    def useCoilA(self):
        self.selectCoil('coilA')
        
    def useCoilB(self):
        self.selectCoil('coilB')
        
        
    def selectCoil(self, coil):
        self.myConfig['global']['activecoil'] = str(coil)
        with open('config.ini','w') as cfg:
            self.myConfig.write(cfg)
        if coil == 'coilA':
            self.updateText('coilA')
            digitalOutBits = np.array([0,0,0,0,0,0,0,0], dtype=np.uint8)
        elif coil == 'coilB':
            self.updateText('coilB')
            digitalOutBits = np.array([0,0,0,0,0,0,0,1], dtype=np.uint8)
        else:
            print('Invalid Coil!Select "coilA" or "coilB"')
            return

        dtask = daq.Task()
        dtask.CreateDOChan("/"+self.myConfig['global']['device']+"/port0/line0:7","",daq.DAQmx_Val_ChanForAllLines)
        dtask.StartTask()
        dtask.WriteDigitalLines(1,1,10.0,daq.DAQmx_Val_GroupByChannel,digitalOutBits,None,None)
        dtask.StopTask()
    
        
            
    def updateText(self, coil):
        self.myMainWindow.TXT_BLCoil.setText(self.getBLCoil())
        self.myMainWindow.TXT_weighingCoil.setText(self.getWeightCoil())
        if coil == 'coilA':
            self.myMainWindow.RB_coilB.setChecked(False)
        else:
            self.myMainWindow.RB_coilA.setChecked(False)
            
            
    def getWeightCoil(self):
        if self.myConfig['global']['activecoil'] == 'coilA':
            return 'A'
        else:
            return 'B'
            
    def getBLCoil(self):
        if self.myConfig['global']['activecoil'] == 'coilA':
            return 'B'
        else:
            return 'A'

        
    
    
    
        