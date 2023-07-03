# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 18:57:21 2017

@author: Alex
"""

import gui_w_pathsAndVariables
import basicWindow

class PathsAndVariables(gui_w_pathsAndVariables.QtGui.QMainWindow,gui_w_pathsAndVariables.Ui_w_pathsAndVariables,basicWindow.BasicWindow):
    def __init__(self,w_main):
        super(PathsAndVariables,self).__init__()
        self.loadBasicObjects(w_main)
        self.setupUi(self)
#        
#        self.w_main_pos = w_main.pos()        
#        self.move(self.w_main_pos.x(),self.w_main_pos.y()-self.height()-26)
        
        #loading values
        self.TB_Armlength.setValue(float(self.myConfig['global']['armlength']))
        self.TB_little_g.setValue(float(self.myConfig['global']['g']))
        self.TB_Resistance.setValue(float(self.myConfig['global']['resistance']))
        self.TB_AcceptablePositionDeviation.setValue(float(self.myConfig['global']['accPosError']))
        
       #connecting Button
        self.BTN_saveRestart.clicked.connect(self.saveRestart)
        self.show()
        self.windowShown=True
        
    def saveRestart(self):
        result = gui_w_pathsAndVariables.QtGui.QMessageBox.question(self.myMainWindow,
                          "Save new Settings?",
                          "If you save the new Settings the Program will close and you have to restart manually.",
                          gui_w_pathsAndVariables.QtGui.QMessageBox.Yes| gui_w_pathsAndVariables.QtGui.QMessageBox.No)

        if result == gui_w_pathsAndVariables.QtGui.QMessageBox.Yes:
            self.myConfig['global']['armlength']=str(self.TB_Armlength.value())
            self.myConfig['global']['g']=str(self.TB_little_g.value())
            self.myConfig['global']['resistance']=str(self.TB_Resistance.value())
            self.myConfig['global']['accPosError']=str(self.TB_AcceptablePositionDeviation.value())
            with open('config.ini','w') as cfg:
                self.myConfig.write(cfg)
                
            self.myMainWindow.prepareDesiredClose()
            self.myMainWindow.close()
    
        
        
    def manualClose(self):
        self.windowShown = False    
        self.close()
        
    def closeEvent(self,event):
        self.manualClose()
        
