from PyQt5 import QtCore, QtGui, QtWidgets

class ProcessInterface:
    # def __init__(self):
    #     self.scrollAreaWidgetContents_590 = QtWidgets.QWidget()
    #     self.scrollAreaWidgetContents_590.setGeometry(
    #         QtCore.QRect(0, 0, 1128, 454))
    #     self.scrollAreaWidgetContents_590.setObjectName(
    #         "scrollAreaWidgetContents_590")
    #     self.gridLayout_220 = QtWidgets.QGridLayout(
    #         self.scrollAreaWidgetContents_590)
    #     self.gridLayout_220.setObjectName("gridLayout_220")
    #     self.tableWidget_380 = QtWidgets.QTableWidget(
    #         self.scrollAreaWidgetContents_590)
    #     self.tableWidget_380.setObjectName("tableWidget_380")
    #     self.tableWidget_380.setColumnCount(2)
    #     self.tableWidget_380.setRowCount(13)
    #     item = QtWidgets.QTableWidgetItem()
    #     self.tableWidget_380.setVerticalHeaderItem(0, item)
    #     # item = QtWidgets.QTableWidgetItem()
    #     # self.tableWidget_380.setHorizontalHeaderItem(0, item)
    #     # item = QtWidgets.QTableWidgetItem()
    #     # self.tableWidget_380.setHorizontalHeaderItem(1, item)
    #     for i in range(12):
    #         item = QtWidgets.QTableWidgetItem()
    #         self.tableWidget_380.setItem(i, 0, item)
    #         item = QtWidgets.QTableWidgetItem()
    #         self.tableWidget_380.setItem(i, i + 1, item)

    #     # item = QtWidgets.QTableWidgetItem()
    #     # self.tableWidget_380.setItem(0, 0, item)
    #     # item = QtWidgets.QTableWidgetItem()
    #     # self.tableWidget_380.setItem(0, 1, item)
    #     # item = QtWidgets.QTableWidgetItem()
    #     # self.tableWidget_380.setItem(1, 0, item)
    #     # item = QtWidgets.QTableWidgetItem()
    #     # self.tableWidget_380.setItem(1, 2, item)
    #     # item = QtWidgets.QTableWidgetItem()
    #     # self.tableWidget_380.setItem(2, 0, item)
    #     # item = QtWidgets.QTableWidgetItem()
    #     # self.tableWidget_380.setItem(3, 0, item)

    #     # item = QtWidgets.QTableWidgetItem()
    #     # self.tableWidget_380.setItem(4, 0, item)

    #     # item = QtWidgets.QTableWidgetItem()
    #     # self.tableWidget_380.setItem(5, 0, item)

    #     # item = QtWidgets.QTableWidgetItem()
    #     # self.tableWidget_380.setItem(6, 0, item)

    #     # item = QtWidgets.QTableWidgetItem()
    #     # self.tableWidget_380.setItem(7, 0, item)

    #     # item = QtWidgets.QTableWidgetItem()
    #     # self.tableWidget_380.setItem(8, 0, item)

    #     # self.tableWidget_380.horizontalHeader().setDefaultSectionSize(400)
    #     # self.tableWidget_380.horizontalHeader().setSortIndicatorShown(True)
    #     # self.tableWidget_380.horizontalHeader().setStretchLastSection(True)
    #     _translate = QtCore.QCoreApplication.translate
    #     # item = self.tableWidget_380.horizontalHeaderItem(0)
    #     # item.setText(_translate("MainWindow", "IP Address"))
    #     # item = self.tableWidget_380.horizontalHeaderItem(1)
    #     # item.setText(_translate("MainWindow", "MAC Address"))
    #     __sortingEnabled = self.tableWidget_380.isSortingEnabled()
    #     self.tableWidget_380.setSortingEnabled(False)
    #     item = self.tableWidget_380.item(0, 0)
    #     item.setText(_translate("MainWindow", "No. of Thread:"))
    #     item = self.tableWidget_380.item(0, 1)
    #     item.setText(_translate("MainWindow", "5"))

    #     item = self.tableWidget_380.item(1, 0)
    #     item.setText(_translate("MainWindow", "No. of Thread:"))
    #     item = self.tableWidget_380.item(0, 1)
    #     item.setText(_translate("MainWindow", "5"))
    #     self.tableWidget_380.setSortingEnabled(__sortingEnabled)
        
    def start_table(self, process_table):
        self.tableWidget_41 = QtWidgets.QTableWidget(process_table)
        self.tableWidget_41.setGeometry(QtCore.QRect(0, 0, 1118, 428))
        self.tableWidget_41.setShowGrid(False)
        self.tableWidget_41.setObjectName("tableWidget_41")
        self.tableWidget_41.setColumnCount(2)
        self.tableWidget_41.setRowCount(14)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_41.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_41.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_41.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_41.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_41.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_41.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_41.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_41.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_41.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_41.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_41.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_41.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_41.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_41.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_41.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_41.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_41.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_41.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_41.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_41.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_41.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_41.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_41.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_41.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_41.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_41.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_41.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_41.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_41.setItem(11, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_41.setItem(12, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_41.setItem(13, 0, item)
        self.tableWidget_41.horizontalHeader().setVisible(False)
        self.tableWidget_41.horizontalHeader().setDefaultSectionSize(400)
        self.tableWidget_41.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_41.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_41.verticalHeader().setVisible(False)
        self.populate_table(self.tableWidget_41)

    def populate_table(tableWidget_41):
        _translate = QtCore.QCoreApplication.translate
        __sortingEnabled = tableWidget_41.isSortingEnabled()
        tableWidget_41.setSortingEnabled(False)
        item = tableWidget_41.item(0, 0)
        item.setText(_translate("MainWindow", "No. of Thread:"))
        item = tableWidget_41.item(0, 1)
        item.setText(_translate("MainWindow", "5"))
        item = tableWidget_41.item(1, 0)
        item.setText(_translate("MainWindow", "CPU Percentage:"))
        item = tableWidget_41.item(2, 0)
        item.setText(_translate("MainWindow", "Process Privileges:"))
        item = tableWidget_41.item(3, 0)
        item.setText(_translate("MainWindow", "Process Priority:"))
        item = tableWidget_41.item(4, 0)
        item.setText(_translate("MainWindow", "Process Type:"))
        item = tableWidget_41.item(5, 0)
        item.setText(_translate("MainWindow", "Timestamp:"))
        item = tableWidget_41.item(6, 0)
        item.setText(_translate("MainWindow", "Command:"))
        item = tableWidget_41.item(7, 0)
        item.setText(_translate("MainWindow", "Terminal:"))
        item = tableWidget_41.item(8, 0)
        item.setText(_translate("MainWindow", "Status:"))
        item = tableWidget_41.item(9, 0)
        item.setText(_translate("MainWindow", "Memory Usage:"))
        item = tableWidget_41.item(10, 0)
        item.setText(_translate("MainWindow", "User Name:"))
        item = tableWidget_41.item(11, 0)
        item.setText(_translate("MainWindow", "Process Name:"))
        item = tableWidget_41.item(12, 0)
        item.setText(_translate("MainWindow", "Process ID:"))
        item = tableWidget_41.item(13, 0)
        item.setText(_translate("MainWindow", "Parent Process ID:"))
        tableWidget_41.setSortingEnabled(__sortingEnabled)
