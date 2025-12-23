import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QTabWidget, 
                             QPushButton, QLabel, QGroupBox, QVBoxLayout, 
                             QHBoxLayout, QGridLayout, QPlainTextEdit, 
                             QRadioButton, QSizePolicy, QSpacerItem)
from PyQt5.QtCore import Qt, QRect

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LEGO Watt-Balance")
        self.resize(800, 600) # Initial size, but fully resizable
        self.initUI()

    def initUI(self):
        # --- Central Widget & Main Layout ---
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        
        # The main layout is vertical: Tabs on top, GroupBoxes on bottom
        self.main_layout = QVBoxLayout(self.centralwidget)

        # --- Top Section: Tab Widget ---
        self.tabWidget = QTabWidget()
        self.setup_measurement_tab()
        self.setup_calibration_tab()
        self.setup_settings_tab()
        self.setup_about_tab()
        
        # Add tabs to main layout
        self.main_layout.addWidget(self.tabWidget)

        # --- Bottom Section: Group Boxes ---
        # We use a Horizontal Layout to place the 3 groups side-by-side
        self.bottom_layout = QHBoxLayout()
        
        self.setup_graphs_group()
        self.setup_mode_group()
        self.setup_coil_group()

        # Add the bottom layout to the main layout
        self.main_layout.addLayout(self.bottom_layout)

    def setup_measurement_tab(self):
        self.TAB_measurement = QWidget()
        layout = QGridLayout()
        
        # Buttons & Labels
        self.BTN_measureBL = QPushButton("Measure BL")
        self.label_6 = QLabel("Start velocity mode to measure BL at zero position")
        
        self.BTN_weighMass = QPushButton("Weigh Mass")
        self.label_5 = QLabel("Weigh a Mass")

        # Add to Grid (Widget, Row, Column)
        layout.addWidget(self.BTN_measureBL, 0, 0)
        layout.addWidget(self.label_6, 0, 1)
        layout.addWidget(self.BTN_weighMass, 1, 0)
        layout.addWidget(self.label_5, 1, 1)
        
        # Spacer to push content to the top
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), 2, 0)
        
        self.TAB_measurement.setLayout(layout)
        self.tabWidget.addTab(self.TAB_measurement, "Measurement")

    def setup_calibration_tab(self):
        self.TAB_calibration = QWidget()
        layout = QGridLayout()

        # Define items (Button Text, Label Text, Object Name)
        items = [
            ("Configure static PID", "Modify the control loop which is used to stabilize the balance", "BTN_PID"),
            ("Configure Shadow S.", "Set the balance's zero position and determine where correlation is linear", "BTN_cfgShadowSensor"),
            ("Configure Position", "Calibrate the shadow-sensor voltage to millimeter conversion", "BTN_cfgPos"),
            ("Configure Velomode", "Modify the control loop used in velo mode and customize sine wave", "BTN_velocitymode"),
        ]

        # Loop to create and add widgets
        for i, (btn_text, lbl_text, obj_name) in enumerate(items):
            btn = QPushButton(btn_text)
            btn.setObjectName(obj_name)
            setattr(self, obj_name, btn) # Bind to self for external access
            
            lbl = QLabel(lbl_text)
            lbl.setWordWrap(True) # Allow text to wrap if window is small
            
            layout.addWidget(btn, i, 0)
            layout.addWidget(lbl, i, 1)

        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), len(items), 0)
        self.TAB_calibration.setLayout(layout)
        self.tabWidget.addTab(self.TAB_calibration, "Calibration")

    def setup_settings_tab(self):
        self.TAB_settings = QWidget()
        layout = QGridLayout()

        items = [
            ("Choose Device", "Choose another Device in your System", "BTN_ChooseDevice"),
            ("Data Acquisition", "Customize the Data Acquisition Parameters", "BTN_dataAcq"),
            ("Paths and Variables", "Adjust File Path, and Variables depending on your Setup", "BTN_PathAndVariables"),
            ("Coil Polarities", "Set the polarities for your Wattbalance coils", "BTN_CoilPolarities"),
            ("Debugging", "Get some more information to debug your system", "BTN_Debugging"),
            ("Factory reset", "Reset everything to default", "BTN_FactoryReset"),
        ]

        for i, (btn_text, lbl_text, obj_name) in enumerate(items):
            btn = QPushButton(btn_text)
            btn.setObjectName(obj_name)
            setattr(self, obj_name, btn)
            
            lbl = QLabel(lbl_text)
            lbl.setWordWrap(True)
            
            layout.addWidget(btn, i, 0)
            layout.addWidget(lbl, i, 1)

        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), len(items), 0)
        self.TAB_settings.setLayout(layout)
        self.tabWidget.addTab(self.TAB_settings, "Settings")

    def setup_about_tab(self):
        self.TAB_about = QWidget()
        layout = QVBoxLayout()
        
        self.Messages = QPlainTextEdit()
        layout.addWidget(self.Messages)
        
        self.TAB_about.setLayout(layout)
        self.tabWidget.addTab(self.TAB_about, "Messages")

    def setup_graphs_group(self):
        self.groupBox = QGroupBox("Graphs:")
        # Bold and Underline font for GroupBox title
        self.groupBox.setStyleSheet("QGroupBox { font-weight: bold; text-decoration: underline; }")
        
        layout = QGridLayout()
        
        # Helper to create status row
        def create_row(row, btn_text, btn_name, lbl_name):
            btn = QPushButton(btn_text)
            btn.setStyleSheet("font-weight: normal; text-decoration: none;") # Reset style from groupbox
            btn.setObjectName(btn_name)
            setattr(self, btn_name, btn)
            
            lbl = QLabel("Open")
            lbl.setAlignment(Qt.AlignCenter)
            lbl.setStyleSheet("color: #2ec205; font-weight: normal;") # Green text
            lbl.setEnabled(False)
            lbl.setObjectName(lbl_name)
            setattr(self, lbl_name, lbl)
            
            layout.addWidget(btn, row, 0)
            layout.addWidget(lbl, row, 1)

        create_row(0, "Raw photo", "BTN_rawphoto", "TXT_rawphoto")
        create_row(1, "Photo (Offset removed)", "BTN_photowoff", "TXT_photowoff")
        create_row(2, "Coil position", "BTN_coilposition", "TXT_coilPosition")
        create_row(3, "Coil velocities", "BTN_coilvelocities", "TXT_coilVelocities")
        create_row(4, "Voltage in coils", "BTN_voltageacrosscoils", "TXT_coilVoltage")
        create_row(5, "Current", "BTN_current", "TXT_current")

        self.groupBox.setLayout(layout)
        self.bottom_layout.addWidget(self.groupBox)

    def setup_mode_group(self):
        self.groupBox_3 = QGroupBox("Mode Info:")
        self.groupBox_3.setStyleSheet("QGroupBox { font-weight: bold; text-decoration: underline; }")
        
        layout = QVBoxLayout()
        
        lbl_mode = QLabel("Mode:")
        lbl_mode.setAlignment(Qt.AlignCenter)
        lbl_mode.setStyleSheet("font-weight: bold;")
        
        self.TXT_activeMode = QLabel("S/V/M")
        self.TXT_activeMode.setAlignment(Qt.AlignCenter)
        self.TXT_activeMode.setStyleSheet("font-weight: bold;")
        
        self.BTN_manualBalancecontrol = QPushButton("Manual Control")
        self.BTN_manualBalancecontrol.setStyleSheet("font-weight: normal; text-decoration: none;")
        
        layout.addWidget(lbl_mode)
        layout.addWidget(self.TXT_activeMode)
        layout.addWidget(self.BTN_manualBalancecontrol)
        layout.addStretch() # Push items to center/top
        
        self.groupBox_3.setLayout(layout)
        self.bottom_layout.addWidget(self.groupBox_3)

    def setup_coil_group(self):
        self.groupBox_2 = QGroupBox("Coil Info:")
        self.groupBox_2.setStyleSheet("QGroupBox { font-weight: bold; text-decoration: underline; }")
        
        layout = QGridLayout()
        
        # Label: Coil with current
        l1 = QLabel("Coil with current:")
        l1.setStyleSheet("font-weight: bold; text-decoration: none;")
        layout.addWidget(l1, 0, 0, 1, 2) # Span 2 columns

        # Radio Buttons
        self.RB_coilA = QRadioButton("Coil A")
        self.RB_coilA.setStyleSheet("font-weight: normal; text-decoration: none;")
        self.RB_coilB = QRadioButton("Coil B")
        self.RB_coilB.setStyleSheet("font-weight: normal; text-decoration: none;")
        
        layout.addWidget(self.RB_coilA, 1, 0, 1, 2)
        layout.addWidget(self.RB_coilB, 2, 0, 1, 2)

        # BL Measurement info
        l2 = QLabel("BL meas. on:")
        l2.setStyleSheet("font-weight: bold; text-decoration: none;")
        self.TXT_BLCoil = QLabel("A/B")
        self.TXT_BLCoil.setStyleSheet("font-weight: bold; text-decoration: none;")
        self.TXT_BLCoil.setAlignment(Qt.AlignCenter)
        
        layout.addWidget(l2, 3, 0)
        layout.addWidget(self.TXT_BLCoil, 3, 1)

        # Weighing info
        l3 = QLabel("Weighing on:")
        l3.setStyleSheet("font-weight: bold; text-decoration: none;")
        self.TXT_weighingCoil = QLabel("A/B")
        self.TXT_weighingCoil.setStyleSheet("font-weight: bold; text-decoration: none;")
        self.TXT_weighingCoil.setAlignment(Qt.AlignCenter)

        layout.addWidget(l3, 4, 0)
        layout.addWidget(self.TXT_weighingCoil, 4, 1)
        
        self.groupBox_2.setLayout(layout)
        self.bottom_layout.addWidget(self.groupBox_2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Enable High DPI scaling for modern screens
    app.setAttribute(Qt.AA_EnableHighDpiScaling)
    app.setAttribute(Qt.AA_UseHighDpiPixmaps)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())