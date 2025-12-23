import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QCheckBox, 
                             QGroupBox, QDoubleSpinBox, QLCDNumber, 
                             QVBoxLayout, QHBoxLayout, QAbstractSpinBox)
from PyQt5.QtCore import Qt

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Control Balance Manual")
        # Flexible default size
        self.resize(350, 150)
        self.initUI()

    def initUI(self):
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)

        # Main Layout: Horizontal
        # Left Side: Checkboxes
        # Right Side: Output Voltage Group
        self.main_layout = QHBoxLayout(self.centralwidget)

        # --- Left Section: Checkboxes ---
        self.checkbox_layout = QVBoxLayout()
        
        self.CB_usePIDFeedback = QCheckBox("Use static PID Feedback")
        self.CB_usePIDFeedback.setChecked(True)
        self.CB_usePIDFeedback.setObjectName("CB_usePIDFeedback")
        
        self.CB_useInputBox = QCheckBox("Use Input Box")
        self.CB_useInputBox.setChecked(False)
        self.CB_useInputBox.setObjectName("CB_useInputBox")
        
        self.CB_useInputWheel = QCheckBox("Use Input Wheel")
        self.CB_useInputWheel.setEnabled(False)
        self.CB_useInputWheel.setObjectName("CB_useInputWheel")

        # Add checkboxes to vertical layout
        self.checkbox_layout.addWidget(self.CB_usePIDFeedback)
        self.checkbox_layout.addWidget(self.CB_useInputBox)
        self.checkbox_layout.addWidget(self.CB_useInputWheel)
        self.checkbox_layout.addStretch() # Push checkboxes to the top

        # --- Right Section: Output Group ---
        self.groupBox = QGroupBox("Output Voltage")
        self.group_layout = QHBoxLayout()

        # Input SpinBox
        self.TB_analogOutput = QDoubleSpinBox()
        self.TB_analogOutput.setFrame(True)
        self.TB_analogOutput.setAlignment(Qt.AlignCenter)
        self.TB_analogOutput.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.TB_analogOutput.setKeyboardTracking(False)
        self.TB_analogOutput.setDecimals(3)
        self.TB_analogOutput.setRange(-10.0, 10.0)
        self.TB_analogOutput.setSingleStep(0.5)
        self.TB_analogOutput.setObjectName("TB_analogOutput")

        # Output LCD
        self.LCD_analogOutput = QLCDNumber()
        self.LCD_analogOutput.setSegmentStyle(QLCDNumber.Flat) # Optional: cleaner look
        self.LCD_analogOutput.setObjectName("LCD_analogOutput")

        # Add widgets to group layout
        self.group_layout.addWidget(self.TB_analogOutput)
        self.group_layout.addWidget(self.LCD_analogOutput)
        self.groupBox.setLayout(self.group_layout)

        # --- Assemble Main Layout ---
        self.main_layout.addLayout(self.checkbox_layout)
        self.main_layout.addWidget(self.groupBox)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Enable High DPI scaling
    app.setAttribute(Qt.AA_EnableHighDpiScaling)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())