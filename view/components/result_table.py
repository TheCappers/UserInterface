from PyQt5 import QtCore, QtGui, QtWidgets


class ResultTable:
    def __init__(self):
        self.avert_result_table = ""
        self.indexSelected = 0

    def setIndexSelected(self, index):
        self.indexSelected = index

    def getIndexSelected(self):
        return self.indexSelected

    def startTable(self, avert_result_table):
        self.avert_result_table = avert_result_table
        self.avert_result_table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.avert_result_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.avert_result_table.setAlternatingRowColors(True)
        self.avert_result_table.setObjectName("avert_result_table")
        self.avert_result_table.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.avert_result_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.avert_result_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.avert_result_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.avert_result_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.avert_result_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.avert_result_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.avert_result_table.setHorizontalHeaderItem(5, item)

        self.avert_result_table.horizontalHeader().setCascadingSectionResizes(True)
        self.avert_result_table.horizontalHeader().setDefaultSectionSize(150)
        self.avert_result_table.horizontalHeader().setHighlightSections(False)
        self.avert_result_table.horizontalHeader().setSortIndicatorShown(True)
        self.avert_result_table.horizontalHeader().setStretchLastSection(True)
        self.avert_result_table.verticalHeader().setVisible(True)
        self.avert_result_table.verticalHeader().setHighlightSections(False)

        self.avert_result_table.setSortingEnabled(False)
        item = self.avert_result_table.horizontalHeaderItem(0)
        _translate = QtCore.QCoreApplication.translate
        item.setText(_translate("MainWindow", "Select"))
        item = self.avert_result_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Timestamp"))
        item = self.avert_result_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Artifact Type"))
        item = self.avert_result_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "IP Address"))
        item = self.avert_result_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "MAC Address"))
        item = self.avert_result_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Description"))

    def getTable(self):
        return self.avert_result_table

    def populateTable(self, attain):
        # global attain
        self.avert_result_table.setRowCount(len(attain))
        _translate = QtCore.QCoreApplication.translate
        i = 0
        for val in attain:
            # print(val)
            item = QtWidgets.QTableWidgetItem()
            item.setCheckState(QtCore.Qt.Unchecked)
            self.avert_result_table.setItem(i, 0, item)
            item = QtWidgets.QTableWidgetItem()
            self.avert_result_table.setItem(i, 1, item)
            item = QtWidgets.QTableWidgetItem()
            self.avert_result_table.setItem(i, 2, item)
            item = QtWidgets.QTableWidgetItem()
            self.avert_result_table.setItem(i, 3, item)
            item = QtWidgets.QTableWidgetItem()
            self.avert_result_table.setItem(i, 4, item)
            item = QtWidgets.QTableWidgetItem()
            self.avert_result_table.setItem(i, 5, item)
            item = self.avert_result_table.item(i, 1)
            item.setText(_translate("MainWindow", val['timestamp']))
            item = self.avert_result_table.item(i, 2)
            item.setText(_translate("MainWindow", val['name']))
            item = self.avert_result_table.item(i, 3)
            item.setText(_translate("MainWindow", val['ip_address']))
            item = self.avert_result_table.item(i, 4)
            item.setText(_translate("MainWindow", val["mac_address"]))
            item = self.avert_result_table.item(i, 5)
            if val['name'] == "Mouse_Action":
                mouse = val['data']
                if mouse['clicked']:
                    item.setText(_translate("MainWindow", "Mouse Click"))
                else:
                    item.setText(_translate("MainWindow", "Mouse Movement"))
            elif val['name'] == "Keystroke":
                item.setText(_translate("MainWindow", "Key Pressed"))
            else:
                item.setText(_translate("MainWindow", val['name']))
            i = i + 1
        return
