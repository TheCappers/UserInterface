# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'floating_accordion.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import QChart, QChartView, QPieSeries
from PyQt5.QtGui import QPen
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets, QtChart


class Ui_Form():
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1005, 479)
        self.toolBox = QtWidgets.QToolBox(Form)
        self.toolBox.setGeometry(QtCore.QRect(0, 0, 1141, 641))
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget(Form)
        self.page.setGeometry(QtCore.QRect(0, 0, 1141, 608))
        self.page.setObjectName("page")
        self.tableWidget = QtWidgets.QTableWidget(self.page)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 691, 281))
        self.tableWidget.setMaximumSize(QtCore.QSize(1080, 16777215))
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 3, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(170)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(26)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)

        self.checkBox_Screenshot = QtWidgets.QCheckBox(self.page)
        self.checkBox_Screenshot.setGeometry(QtCore.QRect(410, 30, 92, 20))
        self.checkBox_Screenshot.setAutoFillBackground(False)
        self.checkBox_Screenshot.setText("")
        self.checkBox_Screenshot.setChecked(True)
        self.checkBox_Screenshot.setTristate(False)
        self.checkBox_Screenshot.setObjectName("checkBox_Screenshot")

        self.checkBox_Video = QtWidgets.QCheckBox(self.page)
        self.checkBox_Video.setGeometry(QtCore.QRect(410, 60, 92, 20))
        self.checkBox_Video.setAutoFillBackground(False)
        self.checkBox_Video.setText("")
        self.checkBox_Video.setChecked(True)
        self.checkBox_Video.setTristate(False)
        self.checkBox_Video.setObjectName("checkBox_Video")

        self.checkBox_Process = QtWidgets.QCheckBox(self.page)
        self.checkBox_Process.setGeometry(QtCore.QRect(410, 120, 92, 20))
        self.checkBox_Process.setAutoFillBackground(False)
        self.checkBox_Process.setText("")
        self.checkBox_Process.setChecked(True)
        self.checkBox_Process.setTristate(False)
        self.checkBox_Process.setObjectName("checkBox_Process")

        self.checkBox_Keystroke = QtWidgets.QCheckBox(self.page)
        self.checkBox_Keystroke.setGeometry(QtCore.QRect(410, 150, 92, 20))
        self.checkBox_Keystroke.setAutoFillBackground(False)
        self.checkBox_Keystroke.setText("")
        self.checkBox_Keystroke.setChecked(True)
        self.checkBox_Keystroke.setTristate(False)
        self.checkBox_Keystroke.setObjectName("checkBox_Keystroke")

        self.checkBox_Mouse_Action = QtWidgets.QCheckBox(self.page)
        self.checkBox_Mouse_Action.setGeometry(QtCore.QRect(410, 180, 92, 20))
        self.checkBox_Mouse_Action.setAutoFillBackground(False)
        self.checkBox_Mouse_Action.setText("")
        self.checkBox_Mouse_Action.setChecked(True)
        self.checkBox_Mouse_Action.setTristate(False)
        self.checkBox_Mouse_Action.setObjectName("checkBox_Mouse_Action")

        self.checkBox_Window_History = QtWidgets.QCheckBox(self.page)
        self.checkBox_Window_History.setGeometry(QtCore.QRect(410, 210, 92, 20))
        self.checkBox_Window_History.setAutoFillBackground(False)
        self.checkBox_Window_History.setText("")
        self.checkBox_Window_History.setChecked(True)
        self.checkBox_Window_History.setTristate(False)
        self.checkBox_Window_History.setObjectName("checkBox_Window_History")

        self.checkBox_System_Call = QtWidgets.QCheckBox(self.page)
        self.checkBox_System_Call.setGeometry(QtCore.QRect(410, 240, 92, 20))
        self.checkBox_System_Call.setAutoFillBackground(False)
        self.checkBox_System_Call.setText("")
        self.checkBox_System_Call.setChecked(True)
        self.checkBox_System_Call.setTristate(False)
        self.checkBox_System_Call.setObjectName("checkBox_System_Call")

        self.checkBox_Network = QtWidgets.QCheckBox(self.page)
        self.checkBox_Network.setGeometry(QtCore.QRect(410, 90, 92, 25))
        self.checkBox_Network.setAutoFillBackground(False)
        self.checkBox_Network.setText("")
        self.checkBox_Network.setChecked(True)
        self.checkBox_Network.setTristate(False)
        self.checkBox_Network.setObjectName("checkBox_Network")

        self.video_camera = QtWidgets.QLabel(self.page)
        self.video_camera.setGeometry(QtCore.QRect(560, 60, 67, 19))
        self.video_camera.setText("")
        self.video_camera.setPixmap(QtGui.QPixmap("view/assets/video_camera.png"))
        self.video_camera.setObjectName("video_camera")
        self.screenshot_button = QtWidgets.QPushButton(self.page)
        self.screenshot_button.setGeometry(QtCore.QRect(560, 30, 67, 19))

        self.screenshot_button.setText("Screenshot")
        self.screenshot_button.setObjectName("screenshot_button")
        self.toolBox.addItem(self.page, "")

        ### PIE CHART START ###

        series = QPieSeries()
        series.append("Available", 80)
        series.append("Used Space", 30)

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
        chart.setGeometry(QtCore.QRectF(1310, 510, 571, 0))

        charview = QChartView(chart)
        charview.setGeometry(QtCore.QRect(1310, 510, 771, 0))

        vox = QtWidgets.QVBoxLayout(self.page)
        vox.setContentsMargins(682, 7, 130, 170)  # ltrb
        vox.addWidget(charview)

        ### PIE CHART END ###

        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Floating Accordion"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Artifact Type"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Recording Status"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Auto Recording On/Off"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "On Demand Recording"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Form", "Still Screenshot"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Form", "Recording"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("Form", "Video"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("Form", "Recording"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("Form", "Network Activity Data"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("Form", "Recording"))
        item = self.tableWidget.item(2, 3)
        item.setText(_translate("Form", "Not Available"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("Form", "Process"))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("Form", "Recording"))
        item = self.tableWidget.item(3, 3)
        item.setText(_translate("Form", "Not Available"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("Form", "Keystroke"))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("Form", "Recording"))
        item = self.tableWidget.item(4, 3)
        item.setText(_translate("Form", "Not Available"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("Form", "Mouse Action"))
        item = self.tableWidget.item(5, 1)
        item.setText(_translate("Form", "Recording"))
        item = self.tableWidget.item(5, 3)
        item.setText(_translate("Form", "Not Available"))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("Form", "Window History"))
        item = self.tableWidget.item(6, 1)
        item.setText(_translate("Form", "Recording"))
        item = self.tableWidget.item(6, 3)
        item.setText(_translate("Form", "Not Available"))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("Form", "System Call"))
        item = self.tableWidget.item(7, 1)
        item.setText(_translate("Form", "Recording"))
        item = self.tableWidget.item(7, 3)
        item.setText(_translate("Form", "Not Available"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Form", "Recording Floating Control Bar"))
