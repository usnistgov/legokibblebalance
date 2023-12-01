from PyQt5 import QtWidgets
import gui_w_main

import w_plot

import w_cfgPID
import w_cfgShadowSensor
import w_cfgPosition
import w_cfgVelomode

import w_controlBalance
import w_measureBL
import w_weighMass

import w_dataAcqSettings
import w_pathsAndVariables
import w_coilPolarity

import factoryReset



class MainWindow(QtWidgets.QMainWindow, gui_w_main.Ui_MainWindow):
    signalMainWindowClosed = gui_w_main.QtCore.pyqtSignal()    
    
    def __init__(self):
        super(MainWindow, self).__init__()      
        self.setupUi(self)
        self.TXT_activeMode.setText('Static')
        
        self.desiredClose = False #Variable used to determine if program 
        # should be closed without asking the User
        
    def trueInit(self, config, timer, task, data, sine, coilSelector, deviceFinder):
    #Basic objects-------------------------------------------------------------
        self.myTimer = timer
        self.myConfig = config
        self.myTask = task
        self.myData = data
        self.mySine = sine
        self.myCoilSelector = coilSelector
        self.myDeviceFinder = deviceFinder
            
        
    #Coil & Mode Info----------------------------------------------------------
        self.RB_coilA.clicked.connect(self.myCoilSelector.useCoilA)
        self.RB_coilB.clicked.connect(self.myCoilSelector.useCoilB)
        
        
        self.BTN_manualBalancecontrol.clicked.connect(self.controlBalanceManual_clicked)
    
    #Buttons-------------------------------------------------------------------
        #Graphs
        self.BTN_rawphoto.clicked.connect(self.rawphoto_clicked)
        self.BTN_coilposition.clicked.connect(self.coilPosition_clicked)
        self.BTN_coilvelocities.clicked.connect(self.coilVelocities_clicked)
        self.BTN_voltageacrosscoils.clicked.connect(self.coilVoltages_clicked)
        self.BTN_current.clicked.connect(self.current_clicked)
        
#        self.BTN_showallai.clicked.connect(self.showAllAI_clicked)
#        self.BTN_showallaiF.clicked.connect(self.showAllAIF_clicked)
        
        #Calibrations
        self.BTN_PID.clicked.connect(self.cfgPID_clicked)
        self.BTN_cfgPos.clicked.connect(self.cfgPos_clicked)
        self.BTN_cfgShadowSensor.clicked.connect(self.cfgShadowSensor_clicked)
        self.BTN_velocitymode.clicked.connect(self.cfgVelomode_clicked)
     
      
        #Measurements
        self.BTN_measureBL.clicked.connect(self.measureBL_clicked)
        self.BTN_weighMass.clicked.connect(self.weighMass_clicked)

        #Settings
#        self.BTN_coilSelection.clicked.connect(self.coilSelection_clicked)
        self.BTN_dataAcq.clicked.connect(self.dataAcq_clicked)
        self.BTN_FactoryReset.clicked.connect(self.factoryReset_clicked)
        self.BTN_ChooseDevice.clicked.connect(self.chooseDevice_clicked)
        self.BTN_PathAndVariables.clicked.connect(self.pathsAndVariables_clicked)
        self.BTN_CoilPolarities.clicked.connect(self.coilPolarity_clicked)
        self.RB_coilA.setChecked(True)
            

    # Basic Objects--------------------------------------------------------   
    def giveTimer(self):
        return self.myTimer
        
    def giveConfig(self):
        return self.myConfig
        
    def giveTask(self):
        return self.myTask
        
    def giveData(self):
        return self.myData
        
    def giveSine(self):
        return self.mySine
        
    def giveCoilSelector(self):
        return self.myCoilSelector
        
    #Button_click methods------------------------------------------------------
        
         
    def controlBalanceManual_clicked(self):
        try:
            if self.window_controlBalanceManual.windowShown==True:
                self.window_controlBalanceManual.manualClose()
            else:
                raise Exception('Show that window')         
        except:
            self.TXT_activeMode.setText('Manual')
            self.window_controlBalanceManual = w_controlBalance.ControlBalance(self)
        
    #Graphs
        
    def graphClosed(self, name):
        if name == 'Coil Positions':
            self.TXT_coilPosition.setEnabled(False)
        elif name == 'Coil Velocities':
            self.TXT_coilVelocities.setEnabled(False)
        elif name == 'Voltage across Coils':
            self.TXT_coilVoltage.setEnabled(False)
        elif name == 'Current':
            self.TXT_current.setEnabled(False)
            


    def rawphoto_clicked(self):
        try:
            if self.window_rawphoto.windowShown==True:
                self.window_rawphoto.manualClose()
            else:
                raise Exception('Show that window')
        except:
            xydata = [['t','photoraw','D']]
            name = ['Raw photo voltage','raw photo voltage']
            self.window_rawphoto = w_plot.PlotWindow(self, xydata, name)
            self.TXT_rawphoto.setEnabled(True)

           
        
    def coilPosition_clicked(self):
        try:
            if self.window_coilPos.windowShown==True:
                self.window_coilPos.manualClose()
            else:
                raise Exception('Show that window')
        except:
            xydata = [['t','posA','D'],['t','posB','D']]
            name = ['Coil Positions','Coil A Position in mm','Coil B Position in mm']
            self.window_coilPos = w_plot.PlotWindow(self, xydata, name)
            self.TXT_coilPosition.setEnabled(True)

#       CALLBACK DT
#        try:
#            if self.window_cbdt.windowShown==True:
#                self.window_cbdt.manualClose()
#            else:
#                raise Exception('Show that window')
#        except:
#            xydata = [['t','cbdt','D']]
#            name = ['Coil Positions','Callback dt in s']
#            self.window_cbdt = w_plot.PlotWindow(self, xydata, name)
      
    def coilVelocities_clicked(self):
        try:
            if self.window_coilVelocities.windowShown==True:
                self.window_coilVelocities.manualClose()
            else:
                raise Exception('Show that window')
        except:
            xydata = [['t','veloA','D'],['t','veloB','D']]
            name = ['Coil Velocities','Coil A Velocity in mm/s','Coil B Velocity in mm/s']
            self.window_coilVelocities = w_plot.PlotWindow(self, xydata, name)
            self.TXT_coilVelocities.setEnabled(True)

    def coilVoltages_clicked(self):
        try:
            if self.window_coilVoltages.windowShown==True:
                self.window_coilVoltages.manualClose()
            else:
                raise Exception('Show that window')
        except:
            xydata = [['t','ai6','F'],['t','ai2','F']]
            name = ['Voltage across Coils','Coil B Voltage','Coil A Voltage']
            self.window_coilVoltages = w_plot.PlotWindow(self, xydata, name)
            self.TXT_coilVoltage.setEnabled(True)

    def current_clicked(self):
        try:
            if self.window_current.windowShown==True:
                self.window_current.manualClose()
            else:
                raise Exception('Show that window')
        except:
            xydata = [['t','current','D']]
            name = ['Current','Current in mA']
            self.window_current = w_plot.PlotWindow(self, xydata, name)
            self.TXT_current.setEnabled(True)

    def showAllAI_clicked(self):      
        try:
            if self.window_ai0.windowShown==True:
                self.window_ai0.manualClose()
            else:
                raise Exception('Show that window')
        except:
            xydata = [['t','ai0','D']]
            name = ['Raw Analog Input 0','Analog Input 0 in V']
            self.window_ai0 = w_plot.PlotWindow(self, xydata, name)
            
        try:
            if self.window_ai1.windowShown==True:
                self.window_ai1.manualClose()
            else:
                raise Exception('Show that window')
        except:
            xydata = [['t','ai1','D']]
            name = ['Raw Analog Input 1','Analog Input 1 in V']
            self.window_ai1 = w_plot.PlotWindow(self, xydata, name)
            
        try:
            if self.window_ai2.windowShown==True:
                self.window_ai2.manualClose()
            else:
                raise Exception('Show that window')
        except:
            xydata = [['t','ai2','D']]
            name = ['Raw Analog Input 2','Analog Input 2 in V']
            self.window_ai2 = w_plot.PlotWindow(self, xydata, name)
            
        try:
            if self.window_ai6.windowShown==True:
                self.window_ai6.manualClose()
            else:
                raise Exception('Show that window')
        except:
            xydata = [['t','ai6','D']]
            name = ['Raw Analog Input 6','Analog Input 6 in V']
            self.window_ai6 = w_plot.PlotWindow(self, xydata, name)
            
            
#    def showAllAIF_clicked(self):      
#            
#        try:
#            if self.window_ai0f.windowShown==True:
#                self.window_ai0f.manualClose()
#            else:
#                raise Exception('Show that window')
#        except:
#            xydata = [['t','ai0','F']]
#            name = ['Raw Analog Input 0F','Analog Input 0 in V']
#            self.window_ai0f = w_plot.PlotWindow(self, xydata, name)
#            
#        try:
#            if self.window_ai1f.windowShown==True:
#                self.window_ai1f.manualClose()
#            else:
#                raise Exception('Show that window')
#        except:
#            xydata = [['t','ai1','F']]
#            name = ['Raw Analog Input 1F','Analog Input 1 in V']
#            self.window_ai1f = w_plot.PlotWindow(self, xydata, name)
#            
#        try:
#            if self.window_ai2f.windowShown==True:
#                self.window_ai2f.manualClose()
#            else:
#                raise Exception('Show that window')
#        except:
#            xydata = [['t','ai2','F']]
#            name = ['Raw Analog Input 2F','Analog Input 2 in V']
#            self.window_ai2f = w_plot.PlotWindow(self, name)
#            
#        try:
#            if self.window_ai6f.windowShown==True:
#                self.window_ai6f.manualClose()
#            else:
#                raise Exception('Show that window')
#        except:
#            xydata = [['t','ai6','F']]
#            name = ['Raw Analog Input 6F','Analog Input 6 in V']
#            self.window_ai6f = w_plot.PlotWindow(self, xydata, name)

    
    #Calibrations    
    
    def cfgPID_clicked(self):      
        try:
            if self.Window_cfgPID.windowShown==True:
                self.Window_cfgPID.manualClose()
            else:
                raise Exception('Show that window')
        except:
            self.Window_cfgPID = w_cfgPID.CalibratePID(self)
            
    def cfgPos_clicked(self):
        try:
            if self.window_cfgPos.windowShown==True:
                self.window_cfgPos.manualClose()
            else:
                raise Exception('Show that window')         
        except:
            self.window_cfgPos = w_cfgPosition.ConfigurePosition(self)

    def cfgShadowSensor_clicked(self):
        try:
            if self.window_cfgShadowSensor.windowShown==True:
                self.window_cfgShadowSensor.manualClose()
            else:
                raise Exception('Show that window')         
        except:
            self.window_cfgShadowSensor = w_cfgShadowSensor.ConfigureShadowSensor(self)          
                 
    def cfgVelomode_clicked(self):
        try:
            if self.window_cfgVelomode.windowShown==True:
                self.window_cfgVelomode.manualClose()
            else:
                raise Exception('Show that window')         
        except:
            self.myTask.switchToVelo()
            self.TXT_activeMode.setText('Velo')
            self.mySine.setActive(True)
            self.window_cfgVelomode = w_cfgVelomode.VeloMode(self)
            
    #Measurements
                        
    def measureBL_clicked(self):
        try:
            if self.Window_measureBL.windowShown==True:
                self.Window_measureBL.manualClose()
            else:
                raise Exception('Show that window')
        except:
            self.myTask.switchToVelo()
            self.Window_measureBL = w_measureBL.MeasureBL(self)   
            self.TXT_activeMode.setText('Velo')                     

    def weighMass_clicked(self):
        try:
            if self.window_weighMass.windowShown==True:
                self.window_weighMass.manualClose()
            else:
                raise Exception('Show that window')         
        except:
            self.window_weighMass = w_weighMass.WeighMass(self)

    #Settings:
    
    def dataAcq_clicked(self):
        try:
            if self.window_dataAcqSettings.windowShown==True:
                self.window_dataAcqSettings.manualClose()
            else:
                raise Exception('Show that window')
        except:
            self.window_dataAcqSettings = w_dataAcqSettings.DataAcqSettings(self)
            
    def pathsAndVariables_clicked(self):
        try:
            if self.window_pathsAndVariables.windowShown==True:
                self.window_pathsAndVariables.manualClose()
            else:
                raise Exception('Show that window')
        except:
            self.window_pathsAndVariables = w_pathsAndVariables.PathsAndVariables(self)
            
            
    def factoryReset_clicked(self):
        factoryReset.doFactoryReset(self,self.myConfig)
        
    def chooseDevice_clicked(self):
        self.myDeviceFinder.forcedSearch(self)
        
        
    
    def coilPolarity_clicked(self):
        try:
            if self.window_coilPolarity.windowShown==True:
                self.window_coilPolarity.manualClose()
            else:
                raise Exception('Show that window')
        except:
            self.window_coilPolarity = w_coilPolarity.CoilPolarity(self)
        


    #Close Method--------------------------------------------------------------

    def prepareDesiredClose(self):
        self.desiredClose = True
        print("desired close ahead")
            
    def closeEvent(self,event):
        print("main window close event")
        if self.desiredClose == True:
            self.desiredClose = False
            self.signalMainWindowClosed.emit()
            event.accept()
        else:
            result = gui_w_main.QtWidgets.QMessageBox.question(self,
                          "Confirm Exit...",
                          "Are you sure you want to exit ?",
                          gui_w_main.QtWidgets.QMessageBox.Yes| gui_w_main.QtWidgets.QMessageBox.No)
            event.ignore()
    
            if result == gui_w_main.QtWidgets.QMessageBox.Yes:
                
                self.signalMainWindowClosed.emit()
                self.myTimer.stop()
                self.myTask.StopTask()
                self.myTask.ClearTask()
                event.accept()
