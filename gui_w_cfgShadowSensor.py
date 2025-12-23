import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, 
                             QPlainTextEdit, QLCDNumber, QDoubleSpinBox, 
                             QVBoxLayout, QGridLayout, QAbstractSpinBox)
from PyQt5.QtCore import Qt

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calibrate Zero-Position")
        # Set a reasonable default size, but allow resizing
        self.resize(400, 200)
        self.initUI()

    def initUI(self):
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)

        # Main Layout (Vertical)
        self.main_layout = QVBoxLayout(self.centralwidget)

        # --- Top: Instructions ---
        self.T_instructions = QPlainTextEdit()
        self.T_instructions.setPlainText("Bring the balance to the center\n(with your hands).\nEnter the measured value as new Photoffset")
        self.T_instructions.setReadOnly(False) # Original code didn't set ReadOnly, keeping it editable?
        # Usually instructions are read-only, but adhering to original behavior (default is editable)
        self.T_instructions.setObjectName("T_instructions")
        
        # Add to layout with a stretch factor so it takes up extra space
        self.main_layout.addWidget(self.T_instructions, 1)

        # --- Bottom: Data Grid ---
        self.grid_layout = QGridLayout()

        # Column 1: Input Voltage
        self.label_12 = QLabel("Input Voltage:")
        self.label_12.setObjectName("label_12")
        
        self.LCD_InputVoltage = QLCDNumber()
        self.LCD_InputVoltage.setDigitCount(7)
        self.LCD_InputVoltage.setSegmentStyle(QLCDNumber.Filled)
        self.LCD_InputVoltage.setSmallDecimalPoint(False)
        self.LCD_InputVoltage.setObjectName("LCD_InputVoltage")
        self.LCD_InputVoltage.setMinimumHeight(30) # Ensure it's legible

        # Column 2: Photooffset (Old Zero Pos)
        self.label_13 = QLabel("Photooffset:")
        self.label_13.setObjectName("label_13")
        
        self.LCD_oldZeropos = QLCDNumber()
        self.LCD_oldZeropos.setDigitCount(8)
        self.LCD_oldZeropos.setObjectName("LCD_oldZeropos")
        self.LCD_oldZeropos.setMinimumHeight(30)

        # Column 3: New Photooffset (Input)
        self.label_10 = QLabel("New Photooffset:")
        self.label_10.setObjectName("label_10")
        
        self.TB_photooffsetChange = QDoubleSpinBox()
        self.TB_photooffsetChange.setAlignment(Qt.AlignCenter)
        self.TB_photooffsetChange.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.TB_photooffsetChange.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.TB_photooffsetChange.setKeyboardTracking(False)
        self.TB_photooffsetChange.setDecimals(5)
        self.TB_photooffsetChange.setRange(-10.0, 10.0)
        self.TB_photooffsetChange.setSingleStep(0.001)
        self.TB_photooffsetChange.setValue(0.0)
        self.TB_photooffsetChange.setObjectName("TB_photooffsetChange")
        self.TB_photooffsetChange.setMinimumHeight(30)

        # Add widgets to grid (Row 0 for labels, Row 1 for values)
        self.grid_layout.addWidget(self.label_12, 0, 0)
        self.grid_layout.addWidget(self.LCD_InputVoltage, 1, 0)

        self.grid_layout.addWidget(self.label_13, 0, 1)
        self.grid_layout.addWidget(self.LCD_oldZeropos, 1, 1)

        self.grid_layout.addWidget(self.label_10, 0, 2)
        self.grid_layout.addWidget(self.TB_photooffsetChange, 1, 2)

        # Add grid to main layout
        self.main_layout.addLayout(self.grid_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Enable High DPI scaling
    app.setAttribute(Qt.AA_EnableHighDpiScaling)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())