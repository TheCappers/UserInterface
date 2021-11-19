
from PyQt5.QtChart import QBarSet, QBarSeries, QChart, QBarCategoryAxis, QValueAxis, QChartView
from PyQt5.Qt import Qt


def add_bar_graph():
    set0 = QBarSet('Screenshot')
    set1 = QBarSet('Video')
    set2 = QBarSet('Mouse Action')
    set3 = QBarSet('Window History')

    set0.append(28)
    set1.append(47)
    set2.append(100)
    set3.append(25)

    series = QBarSeries()
    series.append(set0)
    series.append(set1)
    series.append(set2)
    series.append(set3)

    chart = QChart()
    chart.addSeries(series)
    chart.setTitle('Bar Chart')
    chart.setAnimationOptions(QChart.SeriesAnimations)

    axisX = QBarCategoryAxis()
    axisX.append('Components')

    axisY = QValueAxis()
    axisY.setRange(0, 100)
    chart.addAxis(axisX, Qt.AlignBottom)
    chart.addAxis(axisY, Qt.AlignLeft)

    chart.legend().setVisible(True)
    chart.legend().setAlignment(Qt.AlignBottom)

    chart_view = QChartView(chart)

    return chart_view

class BarGraph:
    def __init__(self):
        self.chart_view = None
        self.series = QBarSeries()


    def setExploded(self,status,index):slice
        self.series.setLabelsVisible(status)

        '''
        spl = self.series[index].label().split(" ")
        if (state):
            self.series[index].setLabel(spl[0] + ' ' + str(self.series[index].sum()))
        else:
            self.series[index].setLabel(spl[0])

        '''

    def add_bar_graph(self, artifact_data):

        for i in artifact_data:
            self.series.append(i)

        #self.series.clicked.connect(self.removeItem)
        self.series.hovered.connect(self.setExploded)

        chart = QChart()
        chart.legend().hide()
        chart.addSeries(self.series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Bar Graph")

        axisX = QBarCategoryAxis()
        axisX.append('Components')

        axisY = QValueAxis()
        #axisY.setRange(0, 100)

        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY, Qt.AlignLeft)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chart_view = QChartView(chart)
        #chart_view.setRenderHint(QPainter.Antialiasing)

        self.chart_view = chart_view

    def get_chart_view(self):
        return self.chart_view

    def get_series(self):
        return self.series
