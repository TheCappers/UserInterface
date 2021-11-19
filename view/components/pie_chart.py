from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen
from PyQt5.Qt import Qt

class PieChart:
    def __init__(self):
        self.chart_view = None
        self.series = QPieSeries()

    def setExploded(self,slice,state):
        slice.setExploded(state)
        slice.setLabelVisible(state)

    def removeItem(self,slice):
        self.series.remove(slice)


    def add_pie_chart(self, artifact_data):
        for i in artifact_data:
            self.series.append(i)

        self.series.clicked.connect(self.removeItem)
        self.series.hovered.connect(self.setExploded)

        chart = QChart()
        chart.legend().hide()
        chart.addSeries(self.series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Pie Chart")

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        self.chart_view = chart_view

    def get_chart_view(self):
        return self.chart_view

    def get_series(self):
        return self.series
