from PyQt6.QtWidgets import QStackedWidget

class Navigator:
    stack = None
    _widget_map = {}

    @staticmethod
    def register_widget(name, widget):
        Navigator._widget_map[name] = widget

    @staticmethod
    def go_to(name):
        widget = Navigator._widget_map[name]
        data = Navigator.stack.currentWidget()
        if data != None:
            Navigator.stack.removeWidget(data)
        Navigator.stack.addWidget(widget())



