import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, 
                             QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import Qt
from pyqtgraph import PlotWidget # Requires pyqtgraph

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Plotwindow")
        # Set a default size, but allow resizing
        self.resize(600, 400) 
        self.initUI()

    def initUI(self):
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)

        # Main Layout: Vertical (Labels on Top, Graph on Bottom)
        self.main_layout = QVBoxLayout(self.centralwidget)

        # --- Top Section: Legend Labels ---
        self.header_layout = QHBoxLayout()

        # Label 2 (Red) - Originally on the left (col 1)
        self.TXT_plot2 = QLabel(" ")
        self.TXT_plot2.setAlignment(Qt.AlignCenter)
        # Replaced QPalette with Stylesheet
        self.TXT_plot2.setStyleSheet("color: red; font-weight: bold;")
        self.TXT_plot2.setObjectName("TXT_plot2")

        # Label 1 (Blue) - Originally on the right (col 2)
        self.TXT_plot1 = QLabel(" ")
        self.TXT_plot1.setAlignment(Qt.AlignCenter)
        self.TXT_plot1.setStyleSheet("color: blue; font-weight: bold;")
        self.TXT_plot1.setObjectName("TXT_plot1")

        # Add to horizontal layout
        self.header_layout.addWidget(self.TXT_plot2)
        self.header_layout.addWidget(self.TXT_plot1)

        # --- Bottom Section: Plot Widget ---
        self.PW = PlotWidget()
        self.PW.setObjectName("PW")

        # --- Assemble Main Layout ---
        self.main_layout.addLayout(self.header_layout)
        self.main_layout.addWidget(self.PW)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Enable High DPI scaling
    app.setAttribute(Qt.AA_EnableHighDpiScaling)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())