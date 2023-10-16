# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 14:46:57 2017

@author: Alex
"""

import gui_w_coilPolarity
import basicWindow
from PyQt5 import QtWidgets

class CoilPolarity(QtWidgets.QMainWindow,gui_w_coilPolarity.Ui_MainWindow,basicWindow.BasicWindow):
    def __init__(self,w_main):
        super(CoilPolarity,self).__init__()
        self.loadBasicObjects(w_main)
        self.setupUi(self)
        
        self.polarity_coilA = self.myConfig['coilA']['polarity']
        self.polarity_coilB = self.myConfig['coilB']['polarity']
        
        self.loadPolarities()
        print("A: ", self.polarity_coilA," B: ",self.polarity_coilB)
        
        self.RDB_A_pos.toggled.connect(self.polaritiesAChanged)
        self.RDB_B_pos.toggled.connect(self.polaritiesBChanged)
        
        
        
        
        self.show()
        self.windowShown=True
    
    def loadPolarities(self):
        if self.polarity_coilA == "+1":
            self.RDB_A_pos.setChecked(True)
        else:
            self.RDB_A_neg.setChecked(True)
            
        if self.polarity_coilB == "+1":
            self.RDB_B_pos.setChecked(True)
        else:
            self.RDB_B_neg.setChecked(True)
    
    def polaritiesAChanged(self):
        if self.RDB_A_pos.isChecked():
            self.polarity_coilA = "+1"
            self.myConfig['coilA']['polarity']="+1"
        else:
            self.polarity_coilA = "-1"
            self.myConfig['coilA']['polarity']="-1"
            
        print(self.polarity_coilA)
            
    def polaritiesBChanged(self):
        if self.RDB_B_pos.isChecked():
            self.polarity_coilB = "+1"
            self.myConfig['coilB']['polarity']="+1"
        else:
            self.polarity_coilB = "-1"
            self.myConfig['coilB']['polarity']="-1"
        
        print(self.polarity_coilB)
        
    def manualClose(self):
        self.windowShown = False    
        self.close()
        
    def closeEvent(self,event):
        self.manualClose()
        