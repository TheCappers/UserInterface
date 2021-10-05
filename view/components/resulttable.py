from PyQt5 import QtCore, QtGui, QtWidgets

class ResultTable:

	def __init__(self, avert_result_table):
		#global table_result
		# avert_result_table = QtWidgets.QTableWidget(table_result)
		self.avert_result_table = avert_result_table
		self.avert_result_table.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.avert_result_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		self.avert_result_table.setAlternatingRowColors(True)
		self.avert_result_table.setRowCount(1)
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
		item = QtWidgets.QTableWidgetItem()
		item.setCheckState(QtCore.Qt.Unchecked)
		self.avert_result_table.setItem(0, 0, item)
		item = QtWidgets.QTableWidgetItem()
		self.avert_result_table.setItem(0, 1, item)
		item = QtWidgets.QTableWidgetItem()
		self.avert_result_table.setItem(0, 2, item)
		item = QtWidgets.QTableWidgetItem()
		self.avert_result_table.setItem(0, 3, item)
		item = QtWidgets.QTableWidgetItem()
		self.avert_result_table.setItem(0, 4, item)
		item = QtWidgets.QTableWidgetItem()
		self.avert_result_table.setItem(0, 5, item)


		self.avert_result_table.horizontalHeader().setCascadingSectionResizes(True)
		self.avert_result_table.horizontalHeader().setDefaultSectionSize(150)
		self.avert_result_table.horizontalHeader().setHighlightSections(False)
		self.avert_result_table.horizontalHeader().setSortIndicatorShown(True)
		self.avert_result_table.horizontalHeader().setStretchLastSection(True)
		self.avert_result_table.verticalHeader().setVisible(True)
		self.avert_result_table.verticalHeader().setHighlightSections(True)

		self.avert_result_table.setSortingEnabled(True)
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
		__sortingEnabled = self.avert_result_table.isSortingEnabled()
		self.avert_result_table.setSortingEnabled(False)
		item = self.avert_result_table.item(0, 1)
		item.setText(_translate("MainWindow", "10-06-26 02:31:29"))
		item = self.avert_result_table.item(0, 2)
		item.setText(_translate("MainWindow", "Video"))
		item = self.avert_result_table.item(0, 3)
		item.setText(_translate("MainWindow", "125.42.0.1"))
		item = self.avert_result_table.item(0, 4)
		item.setText(_translate("MainWindow", "89:28:B2:C6:55:19"))
		item = self.avert_result_table.item(0, 5)
		item.setText(_translate("MainWindow", "A sample artifact"))
		self.avert_result_table.setSortingEnabled(__sortingEnabled)

		# return avert_result_table

	def getTable(self):
			return self.avert_result_table