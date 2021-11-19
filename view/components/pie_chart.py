
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen
from PyQt5.Qt import Qt


def add_pie_chart():


    series = QPieSeries()
    series.append("Python", 80)
    series.append("C++", 70)
    series.append("Java", 50)
    series.append("C#", 40)
    series.append("PHP", 30)



    #adding slice
    slice = QPieSlice()
    slice = series.slices()[2]
    slice.setExploded(True)
    slice.setLabelVisible(True)
    slice.setPen(QPen(Qt.darkGreen, 2))
    slice.setBrush(Qt.green)


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

    '''
    set0 = QPieSlice('Screenshot')
    set1 = QPieSlice('Video')
    set2 = QPieSlice('Mouse Action')
    set3 = QPieSlice('Window History')

    set0.append(28)
    set1.append(47)
    set2.append(100)
    set3.append(25)

    series = QPieSeries()
    series.append(set0)
    series.append(set1)
    series.append(set2)
    series.append(set3)

    chart = QChart()
    chart.addSeries(series)
    chart.setTitle('Pie Chart')
    chart.setAnimationOptions(QChart.SeriesAnimations)

    axisX = QBarCategoryAxis()
    axisX.append('Components')

    axisY = QValueAxis()
    axisY.setRange(0, 100)
    chart.addAxis(axisX, Qt.AlignBottom)
    chart.addAxis(axisY, Qt.AlignLeft)

    chart.legend().setVisible(True)
    chart.legend().setAlignment(Qt.AlignBottom)

    '''

    return chart_view
