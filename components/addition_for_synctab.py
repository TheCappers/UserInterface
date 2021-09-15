
import time
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtChart import QChart, QChartView, QPieSeries
from PyQt5.QtGui import QPen
from PyQt5.QtCore import Qt


def toggleButtons(val, b_ex, b_in):
    if val == "allexcludingvideo_btn":
        b_ex.setChecked(1)
        b_in.setChecked(0)
    if val == "allincludingvideo_btn":
        b_ex.setChecked(0)
        b_in.setChecked(1)


def syncbuttonpressed(b_ex, b_in, err):
    if not (b_ex.isChecked() or b_in.isChecked()):
        err.setHidden(False)
    else:
        err.setHidden(True)


def btns_connector_in_synctab(b_ex, b_in, b_sync, err):
    b_ex.setCheckable(True)
    b_in.setCheckable(True)
    b_ex.clicked.connect(lambda: toggleButtons(
        'allexcludingvideo_btn', b_ex, b_in))
    b_in.clicked.connect(lambda: toggleButtons(
        'allincludingvideo_btn', b_ex, b_in))
    b_sync.clicked.connect(lambda: syncbuttonpressed(b_ex, b_in, err))


def piechart_for_synctab():
    series = QPieSeries()
    series.append("Available (45%)", 45)
    series.append("Used Space (65%)", 65)

    my_slice = series.slices()[0]
    my_slice.setExploded(True)
    my_slice.setLabelVisible(True)
    my_slice.setPen(QPen(Qt.green, 4))
    my_slice.setBrush(Qt.green)

    my_slice = series.slices()[1]
    my_slice.setExploded(True)
    my_slice.setLabelVisible(True)
    my_slice.setPen(QPen(Qt.green, 4))
    my_slice.setBrush(Qt.green)

    chart = QChart()
    chart.addSeries(series)
    chart.setAnimationOptions(QChart.SeriesAnimations)
    chart.setTitle("Hard Drive Space")
    chart.setTheme(QChart.ChartThemeDark)
    chart.setGeometry(QtCore.QRectF(1310, 110, 171, 60))

    charview = QChartView(chart)
    charview.setGeometry(QtCore.QRect(1310, 110, 171, 60))

    return charview
