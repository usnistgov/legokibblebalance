import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, 
                             QLineEdit, QCheckBox, QDoubleSpinBox, 
                             QPushButton, QVBoxLayout, QGridLayout, 
                             QGroupBox, QFrame)
from PyQt5.QtCore import Qt

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings: Paths & Variables")
        # Responsive default size
        self.resize(400, 500)
        self.initUI()

    def initUI(self):
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)

        # Main Layout: Vertical
        self.main_layout = QVBoxLayout(self.centralwidget)

        # --- Top Group: Paths ---
        self.setup_paths_group()
        self.main_layout.addWidget(self.groupBox)

        # --- Middle Group: Variables ---
        self.setup_variables_group()
        self.main_layout.addWidget(self.groupBox_2)

        # --- Bottom: Save Button ---
        self.BTN_saveRestart = QPushButton("save values and close program")
        self.BTN_saveRestart.setObjectName("BTN_saveRestart")
        self.BTN_saveRestart.setMinimumHeight(40) # Make it easier to click
        
        self.main_layout.addWidget(self.BTN_saveRestart)

    def setup_paths_group(self):
        self.groupBox = QGroupBox("Paths")
        self.groupBox.setEnabled(False) # Kept from original, though logic likely enables it
        self.groupBox.setObjectName("groupBox")
        
        layout = QGridLayout()

        # Checkboxes
        self.CB_defaultFolder = QCheckBox("Use default Folder")
        self.CB_defaultFolder.setChecked(True)
        self.CB_defaultFolder.setEnabled(False)
        self.CB_defaultFolder.setObjectName("CB_defaultFolder")

        self.CB_diffrentFolder = QCheckBox("Use different Folder")
        self.CB_diffrentFolder.setEnabled(False)
        self.CB_diffrentFolder.setObjectName("CB_diffrentFolder")

        layout.addWidget(self.CB_defaultFolder, 0, 0)
        layout.addWidget(self.CB_diffrentFolder, 0, 1)

        # Path Input
        self.label_Path = QLabel("Path for Config-Files:")
        self.label_Path.setEnabled(False)
        self.label_Path.setObjectName("label_Path")

        self.TEXT_Path = QLineEdit()
        self.TEXT_Path.setEnabled(False)
        self.TEXT_Path.setObjectName("TEXT_Path")

        layout.addWidget(self.label_Path, 1, 0)
        layout.addWidget(self.TEXT_Path, 1, 1)

        self.groupBox.setLayout(layout)

    def setup_variables_group(self):
        self.groupBox_2 = QGroupBox("Variables")
        self.groupBox_2.setObjectName("groupBox_2")
        
        layout = QGridLayout()
        # Columns: [Label] [Input] [Unit]

        # Row 0: Arm Length
        l1 = QLabel("Watt Balance Armlength")
        self.TB_Armlength = QDoubleSpinBox()
        self.TB_Armlength.setDecimals(2)
        self.TB_Armlength.setMaximum(1000.0)
        self.TB_Armlength.setObjectName("TB_Armlength")
        u1 = QLabel("cm")

        layout.addWidget(l1, 0, 0)
        layout.addWidget(self.TB_Armlength, 0, 1)
        layout.addWidget(u1, 0, 2)

        # Row 1: Resistance
        l2 = QLabel("Resistance")
        self.TB_Resistance = QDoubleSpinBox()
        self.TB_Resistance.setMaximum(999999999.0)
        self.TB_Resistance.setObjectName("TB_Resistance")
        u2 = QLabel("ohm")

        layout.addWidget(l2, 1, 0)
        layout.addWidget(self.TB_Resistance, 1, 1)
        layout.addWidget(u2, 1, 2)

        # Row 2: Little g
        l3 = QLabel("g")
        self.TB_little_g = QDoubleSpinBox()
        self.TB_little_g.setDecimals(4)
        self.TB_little_g.setRange(8.0, 11.0)
        self.TB_little_g.setSingleStep(0.01)
        self.TB_little_g.setValue(8.0)
        self.TB_little_g.setObjectName("TB_little_g")
        u3 = QLabel("m/s²")

        layout.addWidget(l3, 2, 0)
        layout.addWidget(self.TB_little_g, 2, 1)
        layout.addWidget(u3, 2, 2)

        # Row 3: Deviation
        l4 = QLabel("Acceptable Position Deviation:")
        self.TB_AcceptablePositionDeviation = QDoubleSpinBox()
        self.TB_AcceptablePositionDeviation.setDecimals(4)
        self.TB_AcceptablePositionDeviation.setRange(0.0, 1.0)
        self.TB_AcceptablePositionDeviation.setSingleStep(0.001)
        self.TB_AcceptablePositionDeviation.setValue(0.007)
        self.TB_AcceptablePositionDeviation.setObjectName("TB_AcceptablePositionDeviation")
        u4 = QLabel("?mm?") # Kept exact text from original

        layout.addWidget(l4, 3, 0)
        layout.addWidget(self.TB_AcceptablePositionDeviation, 3, 1)
        layout.addWidget(u4, 3, 2)

        self.groupBox_2.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Enable High DPI scaling
    app.setAttribute(Qt.AA_EnableHighDpiScaling)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())