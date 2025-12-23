import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, 
                             QDoubleSpinBox, QPushButton, QLCDNumber, 
                             QVBoxLayout, QHBoxLayout, QGridLayout, 
                             QGroupBox, QAbstractSpinBox, QSizePolicy)
from PyQt5.QtCore import Qt
from pyqtgraph import PlotWidget # Requires pyqtgraph

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Configure velocity mode")
        # Set a responsive default size
        self.resize(650, 500)
        self.initUI()

    def initUI(self):
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)

        # Main Layout: Vertical (Graph Top, Configs Bottom)
        self.main_layout = QVBoxLayout(self.centralwidget)

        # --- Top: Plot Widget ---
        self.PW_sine = PlotWidget()
        self.PW_sine.setObjectName("PW_sine")
        # Set size policy to expand vertically
        self.PW_sine.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        self.main_layout.addWidget(self.PW_sine, 1) # Stretch factor 1

        # --- Bottom: Configuration Groups ---
        self.bottom_layout = QHBoxLayout()
        
        self.setup_pid_group()
        self.setup_sine_group()

        self.bottom_layout.addWidget(self.groupBox)
        self.bottom_layout.addWidget(self.groupBox_3)
        
        # Add bottom layout to main, with stretch 0 (fixed height based on content)
        self.main_layout.addLayout(self.bottom_layout, 0)

    def setup_pid_group(self):
        self.groupBox = QGroupBox("Configure velocity PID")
        layout = QGridLayout()

        # --- Row 0: Headers (P, I, D) ---
        l_p = QLabel("P")
        l_p.setAlignment(Qt.AlignCenter)
        l_p.setObjectName("label_10")
        
        l_i = QLabel("I")
        l_i.setAlignment(Qt.AlignCenter)
        l_i.setObjectName("label_6")
        
        l_d = QLabel("D")
        l_d.setAlignment(Qt.AlignCenter)
        l_d.setObjectName("label_11")

        layout.addWidget(l_p, 0, 0)
        layout.addWidget(l_i, 0, 1)
        layout.addWidget(l_d, 0, 2)

        # --- Row 1: SpinBoxes ---
        self.TB_P_velo = self.create_spinbox(-1000, 1000, 2)
        self.TB_I_velo = self.create_spinbox(-1000, 1000, 2)
        self.TB_D_velo = self.create_spinbox(-1000, 1000, 2)

        layout.addWidget(self.TB_P_velo, 1, 0)
        layout.addWidget(self.TB_I_velo, 1, 1)
        layout.addWidget(self.TB_D_velo, 1, 2)

        # --- Row 2: Buttons ---
        self.BTN_save = QPushButton("Save")
        self.BTN_save.setObjectName("BTN_save")
        
        self.BTN_load = QPushButton("Load")
        self.BTN_load.setObjectName("BTN_load")
        
        self.BTN_resetI = QPushButton("Reset I")
        self.BTN_resetI.setObjectName("BTN_resetI")

        layout.addWidget(self.BTN_save, 2, 0)
        layout.addWidget(self.BTN_load, 2, 1)
        layout.addWidget(self.BTN_resetI, 2, 2)

        # --- Rows 3-5: Monitoring ---
        
        # Integrator Sum
        self.label_7 = QLabel("Integrator sum:")
        self.label_7.setObjectName("label_7")
        self.LCD_su = self.create_lcd(10)
        
        layout.addWidget(self.label_7, 3, 0)
        layout.addWidget(self.LCD_su, 3, 1, 1, 2) # Span 2 columns

        # Epsilon
        self.label_9 = QLabel("Epsilon:")
        self.label_9.setObjectName("label_9")
        self.LCD_eps = self.create_lcd(10)

        layout.addWidget(self.label_9, 4, 0)
        layout.addWidget(self.LCD_eps, 4, 1, 1, 2)

        # Output
        self.label_13 = QLabel("Output:")
        self.label_13.setObjectName("label_13")
        self.LCD_output = self.create_lcd(10)

        layout.addWidget(self.label_13, 5, 0)
        layout.addWidget(self.LCD_output, 5, 1, 1, 2)

        self.groupBox.setLayout(layout)

    def setup_sine_group(self):
        self.groupBox_3 = QGroupBox("Sine Curve")
        layout = QGridLayout()

        # --- Row 0: Frequency Labels ---
        self.label = QLabel("Frequency in Hz:")
        self.label.setObjectName("label")
        
        self.label_5 = QLabel("Period in s:")
        self.label_5.setObjectName("label_5")
        
        layout.addWidget(self.label, 0, 0)
        layout.addWidget(self.label_5, 0, 1)

        # --- Row 1: Frequency Controls ---
        self.TB_freq = self.create_spinbox(0.01, 99.99, 2)
        self.TB_freq.setValue(1.0)
        self.TB_freq.setObjectName("TB_freq")
        
        self.LCD_period = self.create_lcd(3)
        self.LCD_period.setObjectName("LCD_period")

        layout.addWidget(self.TB_freq, 1, 0)
        layout.addWidget(self.LCD_period, 1, 1)

        # --- Row 2: Amplitude Labels ---
        self.label_2 = QLabel("Amplitude in mm:")
        self.label_2.setObjectName("label_2")
        
        self.label_12 = QLabel("Maximal Amplitude:") # Shortened text slightly for layout fit
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")

        layout.addWidget(self.label_2, 2, 0)
        layout.addWidget(self.label_12, 2, 1)

        # --- Row 3: Amplitude Controls ---
        self.TB_amp = self.create_spinbox(-10.0, 10.0, 3)
        self.TB_amp.setSingleStep(0.1)
        self.TB_amp.setValue(0.2)
        self.TB_amp.setObjectName("TB_amp")

        self.LCD_validRange = self.create_lcd(5)
        self.LCD_validRange.setObjectName("LCD_validRange")

        layout.addWidget(self.TB_amp, 3, 0)
        layout.addWidget(self.LCD_validRange, 3, 1)
        
        # Add spacer to push content up if needed
        layout.setRowStretch(4, 1) 

        self.groupBox_3.setLayout(layout)

    # --- Helpers ---
    def create_spinbox(self, min_val, max_val, decimals):
        sb = QDoubleSpinBox()
        sb.setAlignment(Qt.AlignCenter)
        sb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        sb.setKeyboardTracking(False)
        sb.setDecimals(decimals)
        sb.setRange(min_val, max_val)
        return sb

    def create_lcd(self, digits):
        lcd = QLCDNumber()
        lcd.setDigitCount(digits)
        lcd.setSegmentStyle(QLCDNumber.Flat)
        return lcd

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_EnableHighDpiScaling)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())