import sys
from PyQt6.QtWidgets import QApplication, QWidget,QVBoxLayout,QPushButton
from PyQt6.QtCharts import QChart, QChartView, QLineSeries
from navigator import Navigator

class ReportPage(QWidget, Navigator):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Galala Bites Report")
        
        layout = QVBoxLayout()
        button = QPushButton("previos")
        button.clicked.connect(self.previous)
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

     
    def previous(self):
        self.go_to("admin")

