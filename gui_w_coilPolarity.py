import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QGroupBox, 
                             QLabel, QRadioButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import Qt

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings: Coil Polarity")
        # Set a reasonable default size; layouts will prevent it from being too small
        self.resize(300, 150)
        self.initUI()

    def initUI(self):
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)

        # Main Layout: Horizontal (Left Group | Right Group)
        self.main_layout = QHBoxLayout(self.centralwidget)

        # --- Setup Coil A Group ---
        self.setup_coil_a()
        
        # --- Setup Coil B Group ---
        self.setup_coil_b()

        # Add groups to the main layout
        self.main_layout.addWidget(self.groupBox)
        self.main_layout.addWidget(self.groupBox_2)

    def setup_coil_a(self):
        self.groupBox = QGroupBox("Coil A")
        layout = QVBoxLayout()

        # Label
        self.label = QLabel("Polarity")
        
        # Radio Buttons
        self.RDB_A_pos = QRadioButton("Positive")
        self.RDB_A_pos.setObjectName("RDB_A_pos")
        
        self.RDB_A_neg = QRadioButton("Negative")
        self.RDB_A_neg.setObjectName("RDB_A_neg")

        # Add to vertical layout
        layout.addWidget(self.label)
        layout.addWidget(self.RDB_A_pos)
        layout.addWidget(self.RDB_A_neg)
        layout.addStretch() # Push items to the top nicely

        self.groupBox.setLayout(layout)

    def setup_coil_b(self):
        self.groupBox_2 = QGroupBox("Coil B")
        layout = QVBoxLayout()

        # Label
        self.label_2 = QLabel("Polarity")
        
        # Radio Buttons
        self.RDB_B_pos = QRadioButton("Positive")
        self.RDB_B_pos.setObjectName("RDB_B_pos")
        
        self.RDB_B_neg = QRadioButton("Negative")
        self.RDB_B_neg.setObjectName("RDB_B_neg")

        # Add to vertical layout
        layout.addWidget(self.label_2)
        layout.addWidget(self.RDB_B_pos)
        layout.addWidget(self.RDB_B_neg)
        layout.addStretch() 

        self.groupBox_2.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Enable High DPI scaling for sharp text on modern screens
    app.setAttribute(Qt.AA_EnableHighDpiScaling)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())