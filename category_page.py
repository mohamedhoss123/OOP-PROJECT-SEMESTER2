from PyQt6.QtWidgets import QWidget,QVBoxLayout,QPushButton,QApplication,QLabel,QHBoxLayout,QLineEdit
from category_data import CategoryData
class CategoryPage(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.categories = CategoryData().get_all_categories()

        self.input = QLineEdit()
        self.button = QPushButton(text="Add Category")
        self.button.clicked.connect(self.submite)
        self.button_previos = QPushButton(text="previos")
        self.button_previos.clicked.connect(self.previos)
        self.layout.addWidget(self.button_previos)
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.button)


        for i in self.categories:
            self.add_category(i)
        self.setLayout( self.layout)

    def add_category(self,name):
        self.layout.addWidget(CategoryWidget(name))
    def submite(self):
        category = CategoryData()
        data = category.save(self.input.text())
        self.add_category(data)
    def previos(self):
        print("previos")


class CategoryWidget(QWidget):
    def __init__(self,category):
        super().__init__()
        print(category)
        self.id = category[0]
        self.name = category[1]
        layout = QHBoxLayout()
        label = QLabel(text=self.name)
        button = QPushButton(text="delete")
        button.clicked.connect(self.delete)
        layout.addWidget(label)
        layout.addWidget(button)
        self.setLayout(layout)
    def delete(self):
        category =CategoryData()
        category.delete(self.id)
        self.hide()


