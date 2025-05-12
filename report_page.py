import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtCharts import QChart, QChartView, QBarSeries, QBarSet, QValueAxis, QBarCategoryAxis
from navigator import Navigator
from order_data import OrderData
from PyQt6.QtCore import Qt
from datetime import datetime, timedelta
class ReportPage(QWidget, Navigator, OrderData):
    def __init__(self):
        super().__init__()
        OrderData.__init__(self)
        self.setWindowTitle("Galala Bites Report")

        sales_list=self.get_selles_in_week()
        today = datetime.today().date()
        start_date = today - timedelta(days=6)
        expected_date = start_date

        filled = []
        row_index = 0

        while expected_date <= today:
            date_str = expected_date.strftime('%Y-%m-%d')

            if row_index < len(sales_list) and sales_list[row_index][0] == date_str:
                filled.append((date_str, sales_list[row_index][1]))
                row_index += 1
            else:
                filled.append((date_str, 0))

            expected_date += timedelta(days=1)

        x_axis = list(map(lambda x: x[0], filled))
        y_axis = list(map(lambda x: x[1], filled))
      

        layout = QVBoxLayout()
        button = QPushButton("previos")
        button.clicked.connect(self.previous)
        layout.addWidget(button)

        bar_set = QBarSet("Sales")
        bar_set.append(y_axis)

        series = QBarSeries()
        series.append(bar_set)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Monthly Sales")
        chart.setAnimationOptions(QChart.AnimationOption.AllAnimations)

        axisX = QBarCategoryAxis()
        axisX.append(x_axis)
        chart.addAxis(axisX, Qt.AlignmentFlag.AlignBottom)
        series.attachAxis(axisX)

        axisY = QValueAxis()

        chart.addAxis(axisY, Qt.AlignmentFlag.AlignLeft)
        series.attachAxis(axisY)

        chart.legend().setVisible(False)
        chartView = QChartView(chart)
        layout.addWidget(chartView)
        self.setLayout(layout)

    def previous(self):
        self.go_to("admin")

