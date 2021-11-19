from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen
from PyQt5.Qt import Qt
#from view.home_tab.visualization import Visualization

'''
series = QPieSeries()

def setExploded(slice,state):
    slice.setExploded(state)
    slice.setLabelVisible(state)
    self.update_pie_chart()

    #if(slice.label() == 'Screenshot'):
    #slice.setLabel(slice.label() + ' ' +  str(slice.percentage()*100)[0:4] + '%')

def removeItem(slice):
    series.remove(slice)


def add_pie_chart(artifact_data):
    for i in artifact_data:
        series.append(i)

    #self.tab_1.table_result.avert_result_table.cellClicked.connect(self.exportRow)
    series.clicked.connect(removeItem)
    series.hovered.connect(setExploded)

    chart = QChart()
    chart.legend().hide()
    chart.addSeries(series)
    chart.createDefaultAxes()
    chart.setAnimationOptions(QChart.SeriesAnimations)
    chart.setTitle("Pie Chart")

    chart.legend().setVisible(True)
    chart.legend().setAlignment(Qt.AlignBottom)

    chart_view = QChartView(chart)
    chart_view.setRenderHint(QPainter.Antialiasing)

    return chart_view
'''

class PieChart:
    def __init__(self):
        self.chart_view = None
        self.series = QPieSeries()

    def setExploded(self,slice,state):
        slice.setExploded(state)
        slice.setLabelVisible(state)
        #self.update_pie_chart()

        #if(slice.label() == 'Screenshot'):
        #slice.setLabel(slice.label() + ' ' +  str(slice.percentage()*100)[0:4] + '%')

    def removeItem(self,slice):
        self.series.remove(slice)


    def add_pie_chart(self, artifact_data):
        for i in artifact_data:
            self.series.append(i)

        #self.tab_1.table_result.avert_result_table.cellClicked.connect(self.exportRow)
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
