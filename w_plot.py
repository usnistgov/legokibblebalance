import gui_w_plot
import basicWindow
from PyQt5 import QtWidgets 

class PlotWindow(QtWidgets.QMainWindow,gui_w_plot.Ui_MainWindow,basicWindow.BasicWindow):
    def __init__(self, w_main, xydata, name,):
        super(PlotWindow,self).__init__()
        self.loadBasicObjects(w_main)    
        self.setupUi(self)                     #Is used to determine if window is open or closed
        
        self.mymainwindow = w_main
        self.w_main_pos = w_main.pos()
        #Inherited from Basic Window
        self.checkMoveWindow(self.w_main_pos.x()-self.width()-8,self.w_main_pos.y())

        self.myTimer.timeout.connect(self.updateGraphs)
        self.name = name
        self.xydata = xydata        
        self.nrofgraphs = len(self.xydata)
                                     #setting up ui
        self.setWindowTitle(self.name[0])
        self.TXT_plot1.setText(name[1])
        if self.nrofgraphs == 2:
            self.TXT_plot2.setText(name[2])
        
        self.x1 = self.getDataFromArray(self.xydata[0][0],'D')        #setting up graph1
        self.y1 = self.getDataFromArray(self.xydata[0][1],self.xydata[0][2])
        self.curve1 = self.myData.correctSize(self.x1,self.y1)
        self.plot1 = self.PW.plotItem.plot(*self.curve1,pen = 'b')

        if self.nrofgraphs == 2:                                                    #setting up graph2 if needed
            self.x2 = self.getDataFromArray(self.xydata[1][0],'D')
            self.y2 = self.getDataFromArray(self.xydata[1][1],self.xydata[1][2])
            self.curve2 = self.myData.correctSize(self.x2,self.y2)
            self.plot2 = self.PW.plotItem.plot(*self.curve2,pen = 'r')
        
        self.show()
        self.windowShown=True   

    def updateGraphs(self):                                                         #updating graphs 
        self.x1 = self.getDataFromArray(self.xydata[0][0],'D')
        self.y1 = self.getDataFromArray(self.xydata[0][1],self.xydata[0][2])
        self.curve1 = self.myData.correctSize(self.x1,self.y1)
        self.plot1.setData(*self.curve1)
        
        if self.nrofgraphs == 2:
            self.x2 = self.getDataFromArray(self.xydata[1][0],'D')
            self.y2 = self.getDataFromArray(self.xydata[1][1],self.xydata[1][2])
            self.curve2 = self.myData.correctSize(self.x2,self.y2)
            self.plot2.setData(*self.curve2)
            
    def getDataFromArray(self, arrayname, mode):
        array = self.myData.giveDataArray(arrayname)
        if mode == 'F':
            return array.giveAllDataF()
        elif mode == 'D':
            return array.giveAllData()
        
    def manualClose(self):
        self.mymainwindow.graphClosed(self.name[0])
        self.windowShown = False
        self.close()
            
    def closeEvent(self,event):
        self.manualClose()    