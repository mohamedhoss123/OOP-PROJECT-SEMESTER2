from PyQt6.QtWidgets import QStackedWidget

class Navigator:
    stack = QStackedWidget()

    def add_page(self,page):
        self.stack.addWidget(page)
    def show_page(self,page):
        self.stack.setCurrentWidget(page)