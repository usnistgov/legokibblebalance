import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, 
                             QSpinBox, QLCDNumber, QPushButton, 
                             QVBoxLayout, QGridLayout, QFrame)
from PyQt5.QtCore import Qt

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data acquisition settings")
        # Set a reasonable default size
        self.resize(550, 300)
        self.initUI()

    def initUI(self):
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)

        # Main Layout: Vertical
        self.main_layout = QVBoxLayout(self.centralwidget)

        # --- Top: Warning Label ---
        self.label_8 = QLabel("CHANGING THESE VALUES REQUIRES A PROGRAM RESTART!!!")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setStyleSheet("color: #aa0000; font-weight: bold; "
                                   "text-decoration: underline; font-size: 10pt;")
        self.label_8.setObjectName("label_8")
        
        self.main_layout.addWidget(self.label_8)

        # --- Middle: Data Grid ---
        # We use a grid with 4 columns: 
        # [Label] [Input] | [Label] [LCD]
        self.grid_layout = QGridLayout()
        self.grid_layout.setHorizontalSpacing(20) # Add space between left and right groups

        # --- Left Column (Inputs) ---
        
        # Row 0
        self.label = QLabel("Samplerate per channel")
        self.TB_samprate = self.create_spinbox()
        self.TB_samprate.setObjectName("TB_samprate")
        self.grid_layout.addWidget(self.label, 0, 0)
        self.grid_layout.addWidget(self.TB_samprate, 0, 1)

        # Row 1
        self.label_2 = QLabel("Samples per channel")
        self.TB_length = self.create_spinbox()
        self.TB_length.setObjectName("TB_length")
        self.grid_layout.addWidget(self.label_2, 1, 0)
        self.grid_layout.addWidget(self.TB_length, 1, 1)

        # Row 2
        self.label_9 = QLabel("Buffersize (Faktor)")
        self.TB_buffersize = self.create_spinbox()
        self.TB_buffersize.setObjectName("TB_buffersize")
        self.grid_layout.addWidget(self.label_9, 2, 0)
        self.grid_layout.addWidget(self.TB_buffersize, 2, 1)

        # Row 3
        self.label_6 = QLabel("Saved seconds per chnl.")
        self.TB_maxlen = self.create_spinbox()
        self.TB_maxlen.setObjectName("TB_maxlen")
        self.grid_layout.addWidget(self.label_6, 3, 0)
        self.grid_layout.addWidget(self.TB_maxlen, 3, 1)

        # --- Right Column (Outputs/LCDs) ---

        # Row 0
        self.label_3 = QLabel("Overall samplerate")
        self.LCD_totalSamprate = self.create_lcd()
        self.LCD_totalSamprate.setObjectName("LCD_totalSamprate")
        self.grid_layout.addWidget(self.label_3, 0, 2)
        self.grid_layout.addWidget(self.LCD_totalSamprate, 0, 3)

        # Row 1
        self.label_4 = QLabel("Time between samples")
        self.LCD_TrueSampleDt = self.create_lcd()
        self.LCD_TrueSampleDt.setObjectName("LCD_TrueSampleDt")
        self.grid_layout.addWidget(self.label_4, 1, 2)
        self.grid_layout.addWidget(self.LCD_TrueSampleDt, 1, 3)

        # Row 2
        self.label_5 = QLabel("Time between callbacks")
        self.LCD_dt = self.create_lcd()
        self.LCD_dt.setObjectName("LCD_dt")
        self.grid_layout.addWidget(self.label_5, 2, 2)
        self.grid_layout.addWidget(self.LCD_dt, 2, 3)

        # Row 3
        self.label_7 = QLabel("Callbacks per sine period")
        self.LCD_callbacksPerPeriod = self.create_lcd()
        self.LCD_callbacksPerPeriod.setObjectName("LCD_callbacksPerPeriod")
        self.grid_layout.addWidget(self.label_7, 3, 2)
        self.grid_layout.addWidget(self.LCD_callbacksPerPeriod, 3, 3)

        # Add grid to main layout
        self.main_layout.addLayout(self.grid_layout)

        # --- Bottom: Save Button ---
        self.BTN_saverestart = QPushButton("Save values and restart program")
        self.BTN_saverestart.setObjectName("BTN_saverestart")
        self.BTN_saverestart.setMinimumHeight(40) # Make it prominent
        
        self.main_layout.addWidget(self.BTN_saverestart)

    # --- Helper Methods ---
    def create_spinbox(self):
        sb = QSpinBox()
        sb.setMaximum(999999999) # Match original max
        return sb

    def create_lcd(self):
        lcd = QLCDNumber()
        lcd.setSegmentStyle(QLCDNumber.Flat)
        lcd.setSmallDecimalPoint(True)
        return lcd

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Enable High DPI scaling
    app.setAttribute(Qt.AA_EnableHighDpiScaling)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())