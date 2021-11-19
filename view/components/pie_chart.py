
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen
from PyQt5.Qt import Qt


series = QPieSeries()
def setExploded(slice,state):
    slice.setExploded(state)
    slice.setLabelVisible(state)


def removeItem(slice):
    series.remove(slice)




def add_pie_chart():

    screenshot_data = QPieSlice('Screenshot',69)
    #screenshot_data.onPressed()
    video_data = QPieSlice('Video',40)
    network_data = QPieSlice('Network',42)
    process_data = QPieSlice('Processes',69)
    keystroke_data = QPieSlice('Keystroke',14)
    mouse_action_data = QPieSlice('Mouse Actions',200)
    window_history_data = QPieSlice('Window_History',13)
    system_call_data = QPieSlice('System Calls',69)

    artifact_data = [screenshot_data, video_data, network_data, process_data, keystroke_data,mouse_action_data, window_history_data, system_call_data]



    for i in artifact_data:
        series.append(i)


    #self.tab_1.table_result.avert_result_table.cellClicked.connect(self.exportRow)
    series.clicked.connect(removeItem)
    series.hovered.connect(setExploded)

    #series.released.connect(removeExploded)
    #series.released.connect(removeExploded)


    #adding slice
    '''slice = QPieSlice()
    slice = series.slices()[2]
    slice.setExploded(True)
    slice.setLabelVisible(True)
    slice.setPen(QPen(Qt.darkGreen, 2))
    slice.setBrush(Qt.green)
    '''


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
