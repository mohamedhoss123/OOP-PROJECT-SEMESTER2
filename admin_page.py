from PyQt6.QtWidgets import QWidget, QVBoxLayout,QPushButton

from navigator import Navigator
class AdminPage(QWidget,Navigator):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        button_category = QPushButton(text="category")
        button_category.clicked.connect(self.go_to_category)
        layout.addWidget(button_category)
        
        button_report = QPushButton(text="report")
        button_report.clicked.connect(self.go_to_report)
        layout.addWidget(button_report)
        
        button_products = QPushButton(text="products")
        button_products.clicked.connect(self.go_to_products)
        layout.addWidget(button_products)
        self.setLayout(layout)
        
    def go_to_category(self):
        self.go_to("category")
        
    def go_to_report(self):
        self.go_to("report")
        
    def go_to_products(self):
        self.go_to("products")

