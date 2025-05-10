from PyQt6.QtWidgets import QStackedWidget

from routes import routes
class Navigator:
    stack = QStackedWidget()
    _widget_map = {}

    @staticmethod
    def register_widget(name, widget):
        index = Navigator.stack.addWidget(widget)
        Navigator._widget_map[name] = index

    @staticmethod
    def go_to(name):
        index = Navigator._widget_map.get(name)
        if index is not None:
            Navigator.stack.setCurrentIndex(index)

