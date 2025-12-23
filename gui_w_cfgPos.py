import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, 
                             QPushButton, QPlainTextEdit, QGroupBox, 
                             QDoubleSpinBox, QSpinBox, QVBoxLayout, 
                             QHBoxLayout, QGridLayout, QSizePolicy, 
                             QAbstractSpinBox, QSpacerItem)
from PyQt5.QtCore import Qt
from pyqtgraph import PlotWidget # Make sure pyqtgraph is installed

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calibrate Position")
        self.resize(800, 600) # Resizable, better default size
        self.initUI()

    def initUI(self):
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)

        # Main Layout (Vertical)
        # Top: Control Boxes
        # Bottom: Graph Box
        self.main_layout = QVBoxLayout(self.centralwidget)

        # --- Top Section Layout (Horizontal) ---
        self.top_layout = QHBoxLayout()
        
        self.setup_sample_points_group()
        self.setup_fitting_group()
        
        self.top_layout.addWidget(self.groupBox_2, 1) # Stretch factor 1
        self.top_layout.addWidget(self.groupBox_3, 1) # Stretch factor 1
        
        # --- Bottom Section Layout ---
        self.setup_graph_group()

        # Add to Main Layout
        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addWidget(self.groupBox_4, 1) # Give graph more stretch space

    def setup_sample_points_group(self):
        self.groupBox_2 = QGroupBox("Take Sample Points:")
        layout = QVBoxLayout()

        # 1. Start Button
        self.BTN_start = QPushButton("Start Calibration")
        self.BTN_start.setObjectName("BTN_start")
        
        # 2. Instructions Text
        self.T_Instructions = QPlainTextEdit()
        self.T_Instructions.setReadOnly(True)
        self.T_Instructions.setPlainText("Start the Calibration, \nthen follow the Instructions here!")
        self.T_Instructions.setObjectName("T_Instructions")

        # 3. Bottom Controls (Value, Status Labels, Confirm)
        bottom_grid = QGridLayout()

        # Spinbox
        self.TB_value = QDoubleSpinBox()
        self.TB_value.setEnabled(False)
        self.TB_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.TB_value.setAlignment(Qt.AlignCenter)
        self.TB_value.setDecimals(0)
        self.TB_value.setRange(0, 9999)
        self.TB_value.setObjectName("TB_value")

        # Status Labels (Wait / Ready)
        # We put them in the same grid cell or adjacent. 
        # Here I put them adjacent for clarity.
        
        self.TXT_wait = QLabel("WAIT")
        self.TXT_wait.setAlignment(Qt.AlignCenter)
        self.TXT_wait.setStyleSheet("color: red; font-weight: bold;")
        self.TXT_wait.setObjectName("TXT_wait")
        
        self.TXT_ready = QLabel("READY")
        self.TXT_ready.setEnabled(False)
        self.TXT_ready.setAlignment(Qt.AlignCenter)
        self.TXT_ready.setStyleSheet("color: #2ec205; font-weight: bold;") # Green
        self.TXT_ready.setObjectName("TXT_ready")

        # Confirm Button
        self.BTN_confirm = QPushButton("Confirm")
        self.BTN_confirm.setEnabled(False)
        self.BTN_confirm.setObjectName("BTN_confirm")
        self.BTN_confirm.setMinimumHeight(30) # Make it slightly taller as in original

        # Add to sub-grid (Widget, Row, Col, RowSpan, ColSpan)
        bottom_grid.addWidget(self.TB_value, 0, 0)
        bottom_grid.addWidget(self.TXT_wait, 0, 1)
        bottom_grid.addWidget(self.TXT_ready, 0, 2)
        bottom_grid.addWidget(self.BTN_confirm, 0, 3)

        # Assemble Group Layout
        layout.addWidget(self.BTN_start)
        layout.addWidget(self.T_Instructions)
        layout.addLayout(bottom_grid)
        
        self.groupBox_2.setLayout(layout)

    def setup_fitting_group(self):
        self.groupBox_3 = QGroupBox("Fitting Points:")
        layout = QGridLayout()

        # Left: Points Text Area
        self.T_points = QPlainTextEdit()
        self.T_points.setReadOnly(True)
        self.T_points.setPlainText("Once you took samplepoints, they will be displayed here:\n\n")
        self.T_points.setObjectName("T_points")
        
        # Right: Controls
        self.label_2 = QLabel("Degree of PolyFit:")
        
        self.TB_degree = QSpinBox()
        self.TB_degree.setEnabled(False)
        self.TB_degree.setAlignment(Qt.AlignCenter)
        self.TB_degree.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.TB_degree.setRange(-1, 999999999)
        self.TB_degree.setValue(-1)
        self.TB_degree.setObjectName("TB_degree")

        self.BTN_fit = QPushButton("Fit")
        self.BTN_fit.setEnabled(False)
        self.BTN_fit.setObjectName("BTN_fit")
        self.BTN_fit.setMinimumHeight(30)

        self.BTN_savefit = QPushButton("Save fit ")
        self.BTN_savefit.setEnabled(False)
        self.BTN_savefit.setObjectName("BTN_savefit")
        self.BTN_savefit.setMinimumHeight(30)

        # Bottom: Fit Result Text
        self.T_fitresult = QPlainTextEdit()
        self.T_fitresult.setReadOnly(True)
        self.T_fitresult.setMaximumHeight(60) # Keep it short like original
        self.T_fitresult.setPlainText("Once you fitted your points, the Fit will be shown here:\n(highest Polynomial first)\n\n")
        self.T_fitresult.setObjectName("T_fitresult")

        # Positioning in Grid
        # (Row 0-3, Col 0) -> T_points takes up left side
        layout.addWidget(self.T_points, 0, 0, 4, 1) 
        
        # Right side controls
        layout.addWidget(self.label_2, 0, 1)
        layout.addWidget(self.TB_degree, 1, 1)
        layout.addWidget(self.BTN_fit, 2, 1)
        layout.addWidget(self.BTN_savefit, 3, 1)
        
        # Bottom result text spans both columns
        layout.addWidget(self.T_fitresult, 4, 0, 1, 2)

        self.groupBox_3.setLayout(layout)

    def setup_graph_group(self):
        self.groupBox_4 = QGroupBox("Fit:")
        layout = QVBoxLayout()

        # Labels Row
        label_layout = QHBoxLayout()
        
        self.TXT_calculatedfit = QLabel("Calculated Fit")
        self.TXT_calculatedfit.setStyleSheet("color: #00aa00; font-weight: bold;")
        self.TXT_calculatedfit.setObjectName("TXT_calculatedfit")

        self.label_5 = QLabel("Current Fit:")
        self.label_5.setStyleSheet("color: #aa0000; font-weight: bold;")
        self.label_5.setObjectName("label_5")

        self.TXT_currentfit = QLabel("I AM JUST CLEANING HERE")
        self.TXT_currentfit.setStyleSheet("color: #aa0000; font-weight: bold;")
        self.TXT_currentfit.setObjectName("TXT_currentfit")

        self.TXT_currentfit_2 = QLabel("(highest polynomial first)")
        self.TXT_currentfit_2.setStyleSheet("color: #aa0000; font-weight: bold;")
        self.TXT_currentfit_2.setObjectName("TXT_currentfit_2")

        # Spacer to separate green label from red labels
        label_layout.addWidget(self.TXT_calculatedfit)
        label_layout.addSpacing(20) 
        label_layout.addWidget(self.label_5)
        label_layout.addWidget(self.TXT_currentfit)
        label_layout.addWidget(self.TXT_currentfit_2)
        label_layout.addStretch() # Push everything to the left

        # Plot Widget
        self.PW_fits = PlotWidget()
        self.PW_fits.setObjectName("PW_fits")

        layout.addLayout(label_layout)
        layout.addWidget(self.PW_fits)
        
        self.groupBox_4.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_EnableHighDpiScaling)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())