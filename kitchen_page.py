from PyQt6.QtWidgets import QApplication,QWidget, QVBoxLayout, QLabel,QGroupBox
import sys


class KitchenPage(QWidget):
    def __init__(self):

        super().__init__()
        data = [[1,"bending"],[2,"done"]]
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        for i in data:
            self.layout.addWidget(OrderStatusComponent(i))
        
# order [id,order_status]
class OrderStatusComponent(QWidget):
    def __init__(self,order):
        super().__init__()
        print(order)
        self.id = order[0]
        self.order_status = order[1]
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.label = QLabel(text=f"order id is: {self.id}")
        layout.addWidget(self.label)
        self.label = QLabel(text=f"status is: {self.order_status}")
        layout.addWidget(self.label)
        

app=QApplication(sys.argv)
window = KitchenPage()
window.show()
sys.exit(app.exec())