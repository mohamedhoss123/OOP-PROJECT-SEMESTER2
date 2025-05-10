from PyQt6.QtWidgets import QStackedWidget, QWidget,QVBoxLayout,QPushButton,QApplication,QLabel,QHBoxLayout,QLineEdit
from navigator import Navigator
class HomeWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        label = QLabel(text="Welcome To Our Resturant")

        button_admin = QPushButton(text="admin")
        button_admin.clicked.connect(self.go_to_admin)
        button_order = QPushButton(text="order")
        button_order.clicked.connect(self.go_to_order)



        layout.addWidget(label)
        layout.addWidget(button_admin)
        layout.addWidget(button_order)

        self.setLayout(layout)

    def go_to_admin(self):
        Navigator.go_to("admin")
    def go_to_order(self):
        Navigator.go_to("category")