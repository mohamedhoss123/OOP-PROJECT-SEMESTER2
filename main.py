from PyQt6.QtWidgets import QApplication, QStackedWidget, QVBoxLayout, QWidget
import sys
from PyQt6.QtGui import QIcon
from report_page import ReportPage
from category_page import CategoryPage
from home_page import HomeWidget
from admin_page import AdminPage
from products_page import ProductPage
from order_page import OrderPage

app = QApplication(sys.argv)

from navigator import Navigator  

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Galala bites")
        self.setWindowIcon(QIcon("galala.png"))
        self.stack = QStackedWidget()
        Navigator.stack = self.stack
   
        layout = QVBoxLayout()

        layout.addWidget(self.stack)

        self.setLayout(layout)
        self.setMinimumWidth(900)
        self.setMinimumHeight(500)
        
        # Initially navigate to home
        Navigator.register_widget("home", HomeWidget)
        Navigator.register_widget("admin", AdminPage)

        Navigator.register_widget("report", ReportPage)
        Navigator.register_widget("category", CategoryPage)
        Navigator.register_widget("order", OrderPage)
        Navigator.register_widget("products", ProductPage)
        Navigator.go_to("home")

window = MainWindow()
window.show()
sys.exit(app.exec())