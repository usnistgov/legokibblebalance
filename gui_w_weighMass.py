import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, 
                             QPushButton, QLCDNumber, QPlainTextEdit, 
                             QVBoxLayout, QGridLayout, QSizePolicy)
from PyQt5.QtCore import Qt

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weigh Mass")
        # Set a responsive default size
        self.resize(450, 400)
        self.initUI()

    def initUI(self):
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)

        # Main Layout: Vertical
        self.main_layout = QVBoxLayout(self.centralwidget)

        # --- Top Section: Control Grid ---
        # Columns: [Status/Start] [Action Button] [Result/LCD]
        self.grid_layout = QGridLayout()
        self.grid_layout.setVerticalSpacing(10)
        self.grid_layout.setHorizontalSpacing(10)

        # Row 0: Headers / Start Controls
        self.BTN_start = QPushButton("Start")
        self.BTN_start.setObjectName("BTN_start")
        
        self.BTN_restart = QPushButton("Restart")
        self.BTN_restart.setEnabled(False)
        self.BTN_restart.setObjectName("BTN_restart")

        self.TXT_oncoil = QLabel("Measured Current:")
        self.TXT_oncoil.setAlignment(Qt.AlignCenter)
        self.TXT_oncoil.setObjectName("TXT_oncoil")

        self.grid_layout.addWidget(self.BTN_start, 0, 0)
        self.grid_layout.addWidget(self.BTN_restart, 0, 1)
        self.grid_layout.addWidget(self.TXT_oncoil, 0, 2)

        # Row 1: Zero Reading 1
        self.TXT_readyZR1 = self.create_ready_label()
        self.TXT_readyZR1.setObjectName("TXT_readyZR1")
        
        self.BTN_ZR1 = QPushButton("Zero Reading")
        self.BTN_ZR1.setEnabled(False)
        self.BTN_ZR1.setObjectName("BTN_ZR1")
        
        self.LCD_ZR1 = self.create_lcd()
        self.LCD_ZR1.setObjectName("LCD_ZR1")

        self.grid_layout.addWidget(self.TXT_readyZR1, 1, 0)
        self.grid_layout.addWidget(self.BTN_ZR1, 1, 1)
        self.grid_layout.addWidget(self.LCD_ZR1, 1, 2)

        # Row 2: Weigh Mass
        self.TXT_readyWM = self.create_ready_label()
        self.TXT_readyWM.setObjectName("TXT_readyWM")
        
        self.BTN_WM = QPushButton("Weigh Mass")
        self.BTN_WM.setEnabled(False)
        self.BTN_WM.setObjectName("BTN_WM")
        
        self.LCD_WM = self.create_lcd()
        self.LCD_WM.setObjectName("LCD_WM")

        self.grid_layout.addWidget(self.TXT_readyWM, 2, 0)
        self.grid_layout.addWidget(self.BTN_WM, 2, 1)
        self.grid_layout.addWidget(self.LCD_WM, 2, 2)

        # Row 3: Zero Reading 2
        self.TXT_readyZR2 = self.create_ready_label()
        self.TXT_readyZR2.setObjectName("TXT_readyZR2")
        
        self.BTN_ZR2 = QPushButton("Zero Reading")
        self.BTN_ZR2.setEnabled(False)
        self.BTN_ZR2.setObjectName("BTN_ZR2")
        
        self.LCD_ZR2 = self.create_lcd()
        self.LCD_ZR2.setObjectName("LCD_ZR2")

        self.grid_layout.addWidget(self.TXT_readyZR2, 3, 0)
        self.grid_layout.addWidget(self.BTN_ZR2, 3, 1)
        self.grid_layout.addWidget(self.LCD_ZR2, 3, 2)

        # Add grid to main layout
        self.main_layout.addLayout(self.grid_layout)

        # --- Bottom Section: Result Text ---
        self.T_result = QPlainTextEdit()
        self.T_result.setPlainText("Press Start Measurement!")
        self.T_result.setObjectName("T_result")
        # Ensure text area expands to fill remaining space
        self.T_result.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        self.main_layout.addWidget(self.T_result)

    # --- Helper Methods ---
    def create_lcd(self):
        lcd = QLCDNumber()
        lcd.setSegmentStyle(QLCDNumber.Flat)
        lcd.setMinimumHeight(30)
        return lcd

    def create_ready_label(self):
        lbl = QLabel("READY")
        lbl.setAlignment(Qt.AlignCenter)
        lbl.setEnabled(False)
        # Replaced complex QPalette with simple Stylesheet
        lbl.setStyleSheet("color: #2ec205; font-weight: bold; font-size: 10pt;")
        return lbl

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Enable High DPI scaling
    app.setAttribute(Qt.AA_EnableHighDpiScaling)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())