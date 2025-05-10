import sys
from PyQt6.QtWidgets import QApplication, QWidget,QVBoxLayout,QPushButton
from PyQt6.QtCharts import QChart, QChartView, QLineSeries


class BarChartApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Bar Chart")

        layout = QVBoxLayout()
        button = QPushButton("Generate Chart")
        layout.addWidget(button)
        series = QLineSeries()
        series.append(10, 20)
        series.append(20, 10)
        series.append(30, 40)
        

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Monthly Sales")
        chart.createDefaultAxes()
        chart.legend().hide()
        chartView = QChartView(chart)
        layout.addWidget(chartView)
        self.setLayout(layout)

     


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BarChartApp()
    window.resize(600, 400)
    window.show()
    sys.exit(app.exec())
