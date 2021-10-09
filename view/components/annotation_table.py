from PyQt5 import QtCore, QtGui, QtWidgets


class AnnotationTable:

    def __init__(self):
        self.annotation_table = ""
        #global table_result

    def startTable(self, annotation_table):
        self.annotation_table = annotation_table
        self.annotation_table.setRowCount(1)
        self.annotation_table.setObjectName("annotation_table")
        self.annotation_table.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.annotation_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.annotation_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.annotation_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.annotation_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.annotation_table.setHorizontalHeaderItem(3, item)

        self.annotation_table.horizontalHeader().setCascadingSectionResizes(True)
        self.annotation_table.horizontalHeader().setDefaultSectionSize(200)
        self.annotation_table.horizontalHeader().setHighlightSections(False)
        self.annotation_table.horizontalHeader().setSortIndicatorShown(True)
        self.annotation_table.horizontalHeader().setStretchLastSection(True)
        self.annotation_table.verticalHeader().setVisible(True)
        self.annotation_table.verticalHeader().setHighlightSections(True)
        self.annotation_table.setSortingEnabled(True)


        item = self.annotation_table.horizontalHeaderItem(0)
        _translate = QtCore.QCoreApplication.translate
        item.setText(_translate("MainWindow", "Timestamp"))
        item = self.annotation_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "IP Address"))
        item = self.annotation_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "MAC Address"))
        item = self.annotation_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Annotation"))

        return annotation_table

    def getTable(self):
        return self.annotation_table

    def display_annotation(self, selected):
        print(selected)
        print("SELECTED")

        if selected:
            self.annotation_table.setRowCount(len(selected['annotation']))

            #/self.annotation_table.setRowCount(2)
            _translate = QtCore.QCoreApplication.translate
            i = 0
            #global selected
            # time
            # ip
            # mac
            # annotation
            time = selected['timestamp']
            ip = selected ['ip_address']
            mac = selected ['mac_address']


            for annotation in selected['annotation']:
                item = QtWidgets.QTableWidgetItem()
                self.annotation_table.setItem(i, 0, item)
                item = self.annotation_table.item(i, 0)
                item.setText(_translate("MainWindow", time))
                # self.annotation_table.setText("hello")
                item = QtWidgets.QTableWidgetItem()
                self.annotation_table.setItem(i, 1, item)
                item = self.annotation_table.item(i, 1)
                item.setText(_translate("MainWindow", ip))

                item = QtWidgets.QTableWidgetItem()
                self.annotation_table.setItem(i, 2, item)
                item = self.annotation_table.item(i, 2)
                item.setText(_translate("MainWindow", mac))

                item = QtWidgets.QTableWidgetItem()
                self.annotation_table.setItem(i, 3, item)
                item = self.annotation_table.item(i, 3)
                item.setText(_translate("MainWindow", annotation))
