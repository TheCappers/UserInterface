
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