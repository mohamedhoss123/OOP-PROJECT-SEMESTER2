from PyQt6.QtWidgets import QWidget,QVBoxLayout,QListWidget,QComboBox,QPushButton,QApplication,QLabel,QHBoxLayout,QLineEdit
from product_data import ProductData
from category_data import CategoryData
from navigator import Navigator


class ProductPage(QWidget,CategoryData,ProductData,Navigator):
    def __init__(self):
        super().__init__()
        products = self.get_all_products()
        print(products)
        self.custome_layout = QVBoxLayout()
        self.setLayout(self.custome_layout)

        button = QPushButton(text="previos")
        button.clicked.connect(self.previos)
        self.custome_layout.addWidget(button)
        

        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText("Enter product name")
        self.custome_layout.addWidget(self.input_name)

        self.input_price = QLineEdit()
        self.input_price.setPlaceholderText("Enter product price")
        self.custome_layout.addWidget(self.input_price)


        self.categoryDropdown = QComboBox()
        self.categoryDropdown.addItem("Select category")
        categories = self.get_all_categories()
        for i in categories:
            self.categoryDropdown.addItem(i[1], i[0])
        self.custome_layout.addWidget(self.categoryDropdown)
        
        self.button = QPushButton(text="Add Product")
        self.button.clicked.connect(self.add_product)
        self.custome_layout.addWidget(self.button)

        for i in products:
            self.custome_layout.addWidget(ProductComponent(i))

       


    def add_product(self):
        name = self.input_name.text()
        price = float(self.input_price.text())
        category_id = self.categoryDropdown.currentData()
        ProductData().save(name, price, category_id)
        self.custome_layout.addWidget()
    def previos(self):
        self.go_to("admin")

class ProductComponent(QWidget):
    def __init__(self,product):
        super().__init__()
        print(product)
        self.id = product[0]
        self.name = product[1]
        self.price = product[2]
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.label = QLabel(text=f"product id is: {self.id}")
        layout.addWidget(self.label)
        self.label = QLabel(text=f"product name is: {self.name}")
        layout.addWidget(self.label)
        self.label = QLabel(text=f"product price is: {self.price}")
        layout.addWidget(self.label)
        button = QPushButton(text="delete")
        button.clicked.connect(self.delete)
    def delete(self):
        ProductData().delete(self.id)
        self.hide()
    



if __name__ == "__main__":
    app = QApplication([])
    window = ProductPage()
    window.show()
    app.exec()
