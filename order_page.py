import sys
import random
from PyQt6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QListWidget, QMessageBox, QSpinBox, QListWidgetItem, QFrame, QScrollArea
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

from product_data import ProductData
from navigator import Navigator
from order_data import OrderData
from category_data import CategoryData
class OrderPage(QWidget, Navigator, ProductData,OrderData,CategoryData):
    def __init__(self):
        super().__init__()
        ProductData.__init__(self)
        CategoryData.__init__(self)
        OrderData.__init__(self)
        
        self.setWindowTitle("Galala Bites")
        self.setGeometry(100, 100, 900, 600)

        self.menu = self.get_all_products()
        self.order_items = []
        self.catigores = self.get_all_categories()
        self.init_ui()

    def init_ui(self):
        main_layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        prev_button = QPushButton("Previous")
        prev_button.clicked.connect(self.previos)

        title = QLabel("Galala Bites Menu")
        title.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        top_layout.addWidget(prev_button)
        top_layout.addWidget(title)
        left_layout.addLayout(top_layout)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        menu_widget = QWidget()
        menu_layout = QVBoxLayout()

        for i in self.menu:
            frame = QFrame()
            frame_layout = QVBoxLayout()

            name_label = QLabel(f"{i[1]} - {i[2]} EGP")
            name_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
            name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

            qty_label = QLabel("Quantity:")
            qty_box = QSpinBox()
            qty_box.setRange(1, 20)

            qty_layout = QHBoxLayout()
            qty_layout.addWidget(qty_label)
            qty_layout.addWidget(qty_box)

            add_button = QPushButton("Add to Cart")
            add_button.clicked.connect(lambda _, id=i[0],name=i[1],price=i[2],qty=qty_box: self.add_to_order(id,name,price,qty))

            frame_layout.addWidget(name_label)
            frame_layout.addLayout(qty_layout)
            frame_layout.addWidget(add_button)
            frame.setLayout(frame_layout)
            menu_layout.addWidget(frame)

        menu_widget.setLayout(menu_layout)
        scroll_area.setWidget(menu_widget)
        left_layout.addWidget(scroll_area)

        right_layout = QVBoxLayout()

        order_title = QLabel("Your Order")
        order_title.setFont(QFont("Arial", 22, QFont.Weight.Bold))
        right_layout.addWidget(order_title)

        self.order_list = QListWidget()
        right_layout.addWidget(self.order_list)

        self.total_label = QLabel("Total: 0 EGP")
        self.total_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        right_layout.addWidget(self.total_label)

        self.tax_label = QLabel("Tax (14%): 0 EGP")
        self.tax_label.setFont(QFont("Arial", 14))
        right_layout.addWidget(self.tax_label)

        btn_layout = QHBoxLayout()
        self.clear_btn = QPushButton("Clear")
        self.clear_btn.clicked.connect(self.clear_order)

        self.confirm_btn = QPushButton("Confirm")
        self.confirm_btn.clicked.connect(self.confirm_order)

        btn_layout.addWidget(self.clear_btn)
        btn_layout.addWidget(self.confirm_btn)

        right_layout.addLayout(btn_layout)

        main_layout.addLayout(left_layout, 2)
        main_layout.addLayout(right_layout, 1)
        self.setLayout(main_layout)

    def add_to_order(self, id,name,price,qty):
        qty = qty.value()
        print(id,name,price,qty)
     
        total = price * qty
        self.order_items.append((id,name, qty, total))
        self.order_list.addItem(QListWidgetItem(f"{name} x{qty} = {total} EGP"))
        self.update_total()

    def update_total(self):
        subtotal = sum(i[3] for i in self.order_items)
        tax = round(subtotal * 0.14)
        self.total_label.setText(f"Total: {subtotal + tax} EGP")
        self.tax_label.setText(f"Tax (14%): {tax} EGP")

    def clear_order(self):
        self.order_items.clear()
        self.order_list.clear()
        self.update_total()

    def confirm_order(self):
        if not self.order_items:
            QMessageBox.warning(self, "Empty Order", "Please add some items.")
            return

        order_number = self.create_order()
        total = sum(i[3] for i in self.order_items)
        tax = round(total * 0.14)
        grand_total = total + tax

        QMessageBox.information(self, "Order Confirmed",
            f"Order #{order_number} confirmed!\nTotal: {grand_total} EGP\nPreparing now!")
        self.save_order_items(order_number,self.order_items)
        self.clear_order()

    def previos(self):
        self.go_to("home")