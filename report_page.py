import sys
from PyQt6.QtWidgets import QApplication, QWidget,QVBoxLayout,QPushButton
from PyQt6.QtCharts import QChart, QChartView, QLineSeries


class ReportPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Bar Chart")

        layout = QVBoxLayout()
        button = QPushButton("previos")
        button.clicked.connect(self.previos)
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

     
    def previos(self):
        print("previos")

