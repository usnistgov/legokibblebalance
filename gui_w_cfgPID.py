import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, 
                             QDoubleSpinBox, QPushButton, QLCDNumber, 
                             QVBoxLayout, QHBoxLayout, QGridLayout, 
                             QGroupBox, QAbstractSpinBox, QSizePolicy)
from PyQt5.QtCore import Qt

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Configure static PID")
        # Resize logic: Minimum size to fit content, but allow expansion
        self.resize(650, 300) 
        self.initUI()

    def initUI(self):
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)

        # Main Layout: Horizontal split (Left: Monitoring, Right: PID Config)
        self.main_layout = QHBoxLayout(self.centralwidget)

        # --- Setup Left Side (Monitoring/Target) ---
        self.setup_monitoring_section()
        
        # --- Setup Right Side (PID Parameters) ---
        self.setup_pid_section()

        # Add the two groups to the main layout
        self.main_layout.addWidget(self.group_monitoring)
        self.main_layout.addWidget(self.group_pid)

    def setup_monitoring_section(self):
        self.group_monitoring = QGroupBox("Monitoring & Target")
        layout = QGridLayout()

        # --- Row 0: Target Setting ---
        self.label_5 = QLabel("Target:")
        self.TB_target = self.create_spinbox(-1000, 1000, 3) # Name: TB_target
        self.label_13 = QLabel("V")
        
        self.BTN_resetIntegrator = QPushButton("Reset Integrator")
        self.BTN_resetIntegrator.setObjectName("BTN_resetIntegrator")

        # Add Target widgets to grid
        layout.addWidget(self.label_5, 0, 0)
        layout.addWidget(self.TB_target, 0, 1)
        layout.addWidget(self.label_13, 0, 2)
        layout.addWidget(self.BTN_resetIntegrator, 0, 3)

        # --- Row 1: Position ---
        self.label_12 = QLabel("Pos:")
        self.LCD_pos = self.create_lcd() # Name: LCD_pos
        layout.addWidget(self.label_12, 1, 0)
        layout.addWidget(self.LCD_pos, 1, 1, 1, 3) # Span across columns

        # --- Row 2: Analog Output ---
        self.label_11 = QLabel("Analog Output:")
        self.LCD_AO1 = self.create_lcd() # Name: LCD_AO1
        layout.addWidget(self.label_11, 2, 0)
        layout.addWidget(self.LCD_AO1, 2, 1, 1, 3)

        # --- Row 3: Integrator Sum ---
        self.label_7 = QLabel("Integrator sum:")
        self.LCD_su = self.create_lcd() # Name: LCD_su
        layout.addWidget(self.label_7, 3, 0)
        layout.addWidget(self.LCD_su, 3, 1, 1, 3)

        # --- Row 4: Epsilon ---
        self.label_9 = QLabel("Epsilon:")
        self.LCD_eps = self.create_lcd() # Name: LCD_eps
        layout.addWidget(self.label_9, 4, 0)
        layout.addWidget(self.LCD_eps, 4, 1, 1, 3)

        self.group_monitoring.setLayout(layout)

    def setup_pid_section(self):
        self.group_pid = QGroupBox("PID Parameters")
        layout = QGridLayout()

        # --- Top: Save/Load Buttons ---
        self.BTN_savePID = QPushButton("Save P, I, D")
        self.BTN_savePID.setObjectName("BTN_savePID")
        
        self.BTN_loadPID = QPushButton("Load P, I, D")
        self.BTN_loadPID.setObjectName("BTN_loadPID")

        layout.addWidget(self.BTN_savePID, 0, 0, 1, 2) # Span
        layout.addWidget(self.BTN_loadPID, 0, 2, 1, 2) # Span

        # --- Middle: PID Matrix ---
        
        # Headers
        l_p = QLabel("P")
        l_p.setAlignment(Qt.AlignCenter)
        l_p.setStyleSheet("font-weight: bold;")
        
        l_i = QLabel("I")
        l_i.setAlignment(Qt.AlignCenter)
        l_i.setStyleSheet("font-weight: bold;")
        
        l_d = QLabel("D")
        l_d.setAlignment(Qt.AlignCenter)
        l_d.setStyleSheet("font-weight: bold;")

        layout.addWidget(l_p, 1, 1)
        layout.addWidget(l_i, 1, 2)
        layout.addWidget(l_d, 1, 3)

        # Row: Fine
        self.label = QLabel("Fine:")
        self.TB_P_fine = self.create_spinbox(-1000, 1000, 2)
        self.TB_I_fine = self.create_spinbox(-1000, 1000, 2)
        self.TB_D_fine = self.create_spinbox(-1000, 1000, 2)

        layout.addWidget(self.label, 2, 0)
        layout.addWidget(self.TB_P_fine, 2, 1)
        layout.addWidget(self.TB_I_fine, 2, 2)
        layout.addWidget(self.TB_D_fine, 2, 3)

        # Row: Coarse
        self.label_8 = QLabel("Coarse:")
        self.TB_P_coarse = self.create_spinbox(-1000, 1000, 2)
        self.TB_I_coarse = self.create_spinbox(-1000, 1000, 2)
        self.TB_D_coarse = self.create_spinbox(-1000, 1000, 2)

        layout.addWidget(self.label_8, 3, 0)
        layout.addWidget(self.TB_P_coarse, 3, 1)
        layout.addWidget(self.TB_I_coarse, 3, 2)
        layout.addWidget(self.TB_D_coarse, 3, 3)

        # --- Bottom: Switch Logic ---
        self.label_6 = QLabel("Switch at eps:")
        self.TB_eps_switch = self.create_spinbox(-100, 100, 3)
        self.TB_eps_switch.setSingleStep(1.0)
        
        self.label_10 = QLabel("using:")
        self.TXT_PID_mode = QLabel("FILL")
        self.TXT_PID_mode.setStyleSheet("font-weight: bold;")

        # Add switch widgets to grid (Row 4)
        layout.addWidget(self.label_6, 4, 0)
        layout.addWidget(self.TB_eps_switch, 4, 1)
        layout.addWidget(self.label_10, 4, 2)
        layout.addWidget(self.TXT_PID_mode, 4, 3)

        self.group_pid.setLayout(layout)

    # --- Helper Methods to reduce code repetition ---

    def create_spinbox(self, min_val, max_val, decimals):
        sb = QDoubleSpinBox()
        sb.setAlignment(Qt.AlignCenter)
        sb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        sb.setKeyboardTracking(False)
        sb.setRange(min_val, max_val)
        sb.setDecimals(decimals)
        # Required to keep variable names accessible via self.TB_name if assigned
        return sb

    def create_lcd(self):
        lcd = QLCDNumber()
        lcd.setDigitCount(10)
        lcd.setSegmentStyle(QLCDNumber.Flat) # Optional: Looks cleaner
        return lcd

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_EnableHighDpiScaling)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())