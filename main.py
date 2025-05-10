from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QPushButton, QVBoxLayout, QWidget

from report_page import ReportPage
from category_page import CategoryPage
from home_page import HomeWidget
import sys


app = QApplication(sys.argv)
from navigator import Navigator  # Your Navigator class

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Navigator Demo")

        # Create and assign the stacked widget
        self.stack = QStackedWidget()
        Navigator.stack = self.stack
   
        # Layout with buttons and stack
        layout = QVBoxLayout()

        layout.addWidget(self.stack)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Initially navigate to home
        Navigator.register_widget("home", HomeWidget())
        Navigator.register_widget("report", ReportPage())
        Navigator.register_widget("category", CategoryPage())
        Navigator.go_to("home")

window = MainWindow()
window.show()
sys.exit(app.exec())