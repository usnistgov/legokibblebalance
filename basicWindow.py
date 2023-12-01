from PyQt5 import QtCore, QtGui, QtWidgets

class BasicWindow:
    def loadBasicObjects(self, w_main):
        self.myTask = w_main.giveTask()
        self.myData = w_main.giveData()
        self.myTimer = w_main.giveTimer()
        self.myConfig = w_main.giveConfig()
        self.mySine = w_main.giveSine()
        self.myCoilSelector = w_main.giveCoilSelector()
        self.myMainWindow = w_main
        
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        w_main.signalMainWindowClosed.connect(self.manualClose)
        w_main.RB_coilA.clicked.connect(self.useCoilA)
        w_main.RB_coilB.clicked.connect(self.useCoilB)
        
    #To make sure windows dont show "offscreen"        
    def checkMoveWindow(self, xpos, ypos):
        
        #Can be moved To main
        desktop = QtWidgets.QApplication.desktop()
        nr_mainScreen = desktop.primaryScreen()
        mainScreen = desktop.screenGeometry(nr_mainScreen)
        
        
        if not(mainScreen.x() <= xpos <= mainScreen.x()+mainScreen.width()-self.width()):
            self.move(0,0)
            print("x failure")
            return
            
        if not(mainScreen.y() <= ypos <= mainScreen.y()+mainScreen.height()-self.height()):
            self.move(0,0)
            print("y failure")
            return
            
        self.move(xpos,ypos)
        return
    def useCoilA(self):
        print('coil A')
        return
        
    def useCoilB(self):
        print('coil B')
        return



