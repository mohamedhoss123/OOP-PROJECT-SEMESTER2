from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QPushButton, QVBoxLayout, QWidget
from navigator import Navigator  # Your Navigator class
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Navigator Demo")

        # Create and assign the stacked widget
        self.stack = QStackedWidget()
        Navigator.set_stack(self.stack)

   
        # Layout with buttons and stack
        layout = QVBoxLayout()

        layout.addWidget(self.stack)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Initially navigate to home
        Navigator.navigate("home")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())