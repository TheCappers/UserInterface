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
        item = QtWidgets.QTableWidgetItem()
        self.annotation_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.annotation_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.annotation_table.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.annotation_table.setItem(0, 3, item)
        self.annotation_table.horizontalHeader().setDefaultSectionSize(200)
        self.annotation_table.horizontalHeader().setStretchLastSection(True)
        
		return annotation_table

    def getTable(self):
        return self.annotation_table

    def display_annotation(self,selected):
        self.annotation_table.setRowCount(len(selected['annotation']))
        _translate = QtCore.QCoreApplication.translate
        i = 0
        #global selected
        #time
        #ip
        #mac
        #annotation
        item = QtWidgets.QTableWidgetItem()
        item.setText("TimeStamp")
        self.annotation_table.setItem(i, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.annotation_table.setItem(i, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.annotation_table.setItem(i, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.annotation_table.setItem(i, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item = self.annotation_table.item(i, 0)
        item.setText(_translate("MainWindow", selected['timestamp']))
        item = self.annotation_table.item(i, 1)
        item.setText(_translate("MainWindow", selected['ip_address']))
        item = self.annotation_table.item(i, 2)
        item.setText(_translate("MainWindow", selected['mac_address']))
        item = self.annotation_table.item(i, 3)
        item.setText(_translate("MainWindow", self.annotation_text.toPlainText()))
        item = self.annotation_table.item(i, 4)
        return
