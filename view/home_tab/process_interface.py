from PyQt5 import QtCore, QtGui, QtWidgets

class ProcessInterface:
    def __init__(self):
        self.scrollAreaWidgetContents_590 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_590.setGeometry(
            QtCore.QRect(0, 0, 1128, 454))
        self.scrollAreaWidgetContents_590.setObjectName(
            "scrollAreaWidgetContents_590")
        self.gridLayout_220 = QtWidgets.QGridLayout(
            self.scrollAreaWidgetContents_590)
        self.gridLayout_220.setObjectName("gridLayout_220")
        self.tableWidget_380 = QtWidgets.QTableWidget(
            self.scrollAreaWidgetContents_590)
        self.tableWidget_380.setObjectName("tableWidget_380")
        self.tableWidget_380.setColumnCount(2)
        self.tableWidget_380.setRowCount(13)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_380.setVerticalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget_380.setHorizontalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget_380.setHorizontalHeaderItem(1, item)
        for i in range(12):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_380.setItem(i, 0, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_380.setItem(i, i + 1, item)

        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget_380.setItem(0, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget_380.setItem(0, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget_380.setItem(1, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget_380.setItem(1, 2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget_380.setItem(2, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget_380.setItem(3, 0, item)

        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget_380.setItem(4, 0, item)

        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget_380.setItem(5, 0, item)

        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget_380.setItem(6, 0, item)

        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget_380.setItem(7, 0, item)

        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget_380.setItem(8, 0, item)

        # self.tableWidget_380.horizontalHeader().setDefaultSectionSize(400)
        # self.tableWidget_380.horizontalHeader().setSortIndicatorShown(True)
        # self.tableWidget_380.horizontalHeader().setStretchLastSection(True)
        _translate = QtCore.QCoreApplication.translate
        # item = self.tableWidget_380.horizontalHeaderItem(0)
        # item.setText(_translate("MainWindow", "IP Address"))
        # item = self.tableWidget_380.horizontalHeaderItem(1)
        # item.setText(_translate("MainWindow", "MAC Address"))
        __sortingEnabled = self.tableWidget_380.isSortingEnabled()
        self.tableWidget_380.setSortingEnabled(False)
        item = self.tableWidget_380.item(0, 0)
        item.setText(_translate("MainWindow", "No. of Thread:"))
        item = self.tableWidget_380.item(0, 1)
        item.setText(_translate("MainWindow", "5"))

        item = self.tableWidget_380.item(1, 0)
        item.setText(_translate("MainWindow", "No. of Thread:"))
        item = self.tableWidget_380.item(0, 1)
        item.setText(_translate("MainWindow", "5"))
        self.tableWidget_380.setSortingEnabled(__sortingEnabled)
