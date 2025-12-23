import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, 
                             QPushButton, QLCDNumber, QVBoxLayout, 
                             QHBoxLayout, QGridLayout, QSizePolicy)
from PyQt5.QtCore import Qt
from pyqtgraph import PlotWidget # Requires pyqtgraph

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Measure BL")
        # Taller default size to accommodate 3 stacked graphs
        self.resize(700, 800)
        self.initUI()

    def initUI(self):
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)

        # Main Layout: Vertical
        # 1. Top Controls & Status (Grid)
        # 2. Graph 1 (Voltage/Velocity)
        # 3. Graph 2 (BL vs Position)
        # 4. Graph 3 (BL vs Time)
        self.main_layout = QVBoxLayout(self.centralwidget)

        # --- Top Section: Controls and LCDs ---
        self.top_grid = QGridLayout()
        self.top_grid.setVerticalSpacing(10)

        # Row 0: Reset | Title | Save
        self.BTN_resetBL0 = QPushButton("Reset: BL at zero position (time)")
        self.BTN_resetBL0.setObjectName("BTN_resetBL0")
        
        self.TXT_BLcoil = QLabel("BL of coil X")
        self.TXT_BLcoil.setAlignment(Qt.AlignCenter)
        self.TXT_BLcoil.setStyleSheet("font-size: 12pt; font-weight: bold; text-decoration: underline;")
        self.TXT_BLcoil.setObjectName("TXT_BLcoil")

        self.BTN_saveBL0 = QPushButton("Save Mean Bl0")
        self.BTN_saveBL0.setObjectName("BTN_saveBL0")

        self.top_grid.addWidget(self.BTN_resetBL0, 0, 0)
        self.top_grid.addWidget(self.TXT_BLcoil, 0, 1)
        self.top_grid.addWidget(self.BTN_saveBL0, 0, 2)

        # Row 1: Headers for LCDs
        self.label_2 = QLabel("Current BL@0:")
        self.label_2.setObjectName("label_2")
        
        self.label = QLabel("Mean BL@0:")
        self.label.setObjectName("label")
        
        self.label_3 = QLabel("Error in %:")
        self.label_3.setObjectName("label_3")

        self.top_grid.addWidget(self.label_2, 1, 0)
        self.top_grid.addWidget(self.label, 1, 1)
        self.top_grid.addWidget(self.label_3, 1, 2)

        # Row 2: LCD Values
        self.LCD_BLcurrent = self.create_lcd()
        self.LCD_BLcurrent.setObjectName("LCD_BLcurrent")
        
        self.LCD_BLmean = self.create_lcd()
        self.LCD_BLmean.setObjectName("LCD_BLmean")
        
        self.LCD_BLerror = self.create_lcd()
        self.LCD_BLerror.setObjectName("LCD_BLerror")

        self.top_grid.addWidget(self.LCD_BLcurrent, 2, 0)
        self.top_grid.addWidget(self.LCD_BLmean, 2, 1)
        self.top_grid.addWidget(self.LCD_BLerror, 2, 2)

        self.main_layout.addLayout(self.top_grid)

        # --- Graph 1 Section: Voltage vs Velocity ---
        self.g1_label_layout = QHBoxLayout()
        
        self.label_5 = QLabel("Voltage depending on coil velocity (white)")
        self.label_5.setObjectName("label_5")
        
        self.label_8 = QLabel("Fit (red)")
        self.label_8.setStyleSheet("color: red;")
        self.label_8.setObjectName("label_8")
        
        self.g1_label_layout.addWidget(self.label_5)
        self.g1_label_layout.addWidget(self.label_8)
        self.g1_label_layout.addStretch()

        self.PW_2periods = PlotWidget()
        self.PW_2periods.setObjectName("PW_2periods")
        self.PW_2periods.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.main_layout.addLayout(self.g1_label_layout)
        self.main_layout.addWidget(self.PW_2periods)

        # --- Graph 2 Section: BL vs Position ---
        self.label_6 = QLabel("BL depending on balance position")
        self.label_6.setObjectName("label_6")
        
        self.PW_BLofPos = PlotWidget()
        self.PW_BLofPos.setObjectName("PW_BLofPos")
        self.PW_BLofPos.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.main_layout.addWidget(self.label_6)
        self.main_layout.addWidget(self.PW_BLofPos)

        # --- Graph 3 Section: BL vs Time ---
        self.label_7 = QLabel("BL at zero position measurements:")
        self.label_7.setObjectName("label_7")
        
        self.PW_BL0ofTime = PlotWidget()
        self.PW_BL0ofTime.setObjectName("PW_BL0ofTime")
        self.PW_BL0ofTime.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.main_layout.addWidget(self.label_7)
        self.main_layout.addWidget(self.PW_BL0ofTime)

    # --- Helper to create standard LCDs ---
    def create_lcd(self):
        lcd = QLCDNumber()
        lcd.setSegmentStyle(QLCDNumber.Flat)
        lcd.setMinimumHeight(30)
        return lcd

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Enable High DPI scaling
    app.setAttribute(Qt.AA_EnableHighDpiScaling)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())