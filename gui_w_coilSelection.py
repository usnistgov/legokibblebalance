import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, 
                             QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import Qt

class ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Coil Selection")
        # Small default size, but resizable
        self.resize(300, 120) 
        self.initUI()

    def initUI(self):
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)

        # Main Layout: Vertical
        # Top: Status Text
        # Bottom: Buttons
        self.main_layout = QVBoxLayout(self.centralwidget)

        # --- Top: Active Coil Label ---
        self.TXT_activecoil = QLabel("Active: Coil X")
        self.TXT_activecoil.setAlignment(Qt.AlignCenter)
        # Using stylesheet instead of HTML for cleaner code
        self.TXT_activecoil.setStyleSheet("font-size: 10pt; font-weight: bold;")
        self.TXT_activecoil.setObjectName("TXT_activecoil")
        
        # Add to main layout
        self.main_layout.addWidget(self.TXT_activecoil)

        # --- Bottom: Buttons Row ---
        self.button_layout = QHBoxLayout()

        self.BTN_useCoilA = QPushButton("Use coil A")
        self.BTN_useCoilA.setObjectName("BTN_useCoilA")
        
        self.BTN_useCoilB = QPushButton("Use coil B")
        self.BTN_useCoilB.setObjectName("BTN_useCoilB")

        # Add buttons to horizontal layout
        self.button_layout.addWidget(self.BTN_useCoilA)
        self.button_layout.addWidget(self.BTN_useCoilB)

        # Add horizontal layout to main layout
        self.main_layout.addLayout(self.button_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Enable High DPI scaling for sharp text
    app.setAttribute(Qt.AA_EnableHighDpiScaling)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())