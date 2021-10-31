from PyQt5 import QtWidgets, QtCore, QtGui
from view.components import result_table, annotation_table, bar_graph

class Script_Accordion:
	def __init__(self):
		self.script_accordion = ""


	def startAccordion(self):
		_translate = QtCore.QCoreApplication.translate
		self.script_accordion = QtWidgets.QWidget()
		self.script_accordion.setGeometry(QtCore.QRect(0, 0, 548, 197))
		self.script_accordion.setObjectName("script_accordion")
		self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.script_accordion)
		self.verticalLayout_8.setObjectName("verticalLayout_8")
		
		#Script Table Content Area BEGIN
		self.table_tag_2 = QtWidgets.QTableWidget(self.script_accordion)
		self.table_tag_2.setAcceptDrops(False)
		self.table_tag_2.setEditTriggers(
				QtWidgets.QAbstractItemView.AnyKeyPressed | QtWidgets.QAbstractItemView.DoubleClicked)
		self.table_tag_2.setAlternatingRowColors(True)
		self.table_tag_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
		self.table_tag_2.setCornerButtonEnabled(True)
		self.table_tag_2.setRowCount(0)
		self.table_tag_2.setObjectName("table_tag_2")
		self.table_tag_2.setColumnCount(7)
		item = QtWidgets.QTableWidgetItem()
		item.setText(_translate("MainWindow", "Select"))
		self.table_tag_2.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		item.setText(_translate("MainWindow", "Added Artifact"))
		self.table_tag_2.setHorizontalHeaderItem(1, item)
		item = QtWidgets.QTableWidgetItem()
		item.setText(_translate("MainWindow", "Time Stamp"))
		self.table_tag_2.setHorizontalHeaderItem(2, item)
		item = QtWidgets.QTableWidgetItem()
		item.setText(_translate("MainWindow", "Artifact Type"))
		self.table_tag_2.setHorizontalHeaderItem(3, item)
		item = QtWidgets.QTableWidgetItem()
		item.setText(_translate("MainWindow", "Tag"))
		self.table_tag_2.setHorizontalHeaderItem(4, item)
		item = QtWidgets.QTableWidgetItem()
		item.setText(_translate("MainWindow", "MAC Address"))
		self.table_tag_2.setHorizontalHeaderItem(5, item)
		item = QtWidgets.QTableWidgetItem()
		item.setText(_translate("MainWindow", "Description"))
		self.table_tag_2.setHorizontalHeaderItem(6, item)

		self.table_tag_2.horizontalHeader().setCascadingSectionResizes(True)
		self.table_tag_2.horizontalHeader().setDefaultSectionSize(150)
		self.table_tag_2.horizontalHeader().setMinimumSectionSize(20)
		self.table_tag_2.horizontalHeader().setSortIndicatorShown(True)
		self.table_tag_2.horizontalHeader().setStretchLastSection(True)
		self.table_tag_2.verticalHeader().setVisible(False)
		self.table_tag_2.verticalHeader().setCascadingSectionResizes(True)
		self.table_tag_2.verticalHeader().setSortIndicatorShown(True)
		#Script Table Content Area END

		#Script Button Content Area START
		self.verticalLayout_8.addWidget(self.table_tag_2)
		self.frame_13 = QtWidgets.QFrame(self.script_accordion)
		self.frame_13.setMaximumSize(QtCore.QSize(16777215, 111))
		self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_13.setObjectName("frame_13")
		self.gridLayout_35 = QtWidgets.QGridLayout(self.frame_13)
		self.gridLayout_35.setObjectName("gridLayout_35")
		self.pushButton_7 = QtWidgets.QPushButton(self.frame_13)
		self.pushButton_7.setObjectName("pushButton_7")
		self.pushButton_7.setText(_translate("MainWindow", "Up"))
		self.gridLayout_35.addWidget(self.pushButton_7, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
		self.pushButton_8 = QtWidgets.QPushButton(self.frame_13)
		self.pushButton_8.setObjectName("pushButton_8")
		self.pushButton_8.setText(_translate("MainWindow", "Down"))

		self.gridLayout_35.addWidget(self.pushButton_8, 0, 1, 1, 1, QtCore.Qt.AlignLeft)
		self.pushButton_9 = QtWidgets.QPushButton(self.frame_13)
		self.pushButton_9.setObjectName("pushButton_9")
		self.pushButton_9.setText(_translate("MainWindow", "Remove"))

		self.gridLayout_35.addWidget(self.pushButton_9, 0, 2, 1, 1, QtCore.Qt.AlignLeft)
		self.pushButton_11 = QtWidgets.QPushButton(self.frame_13)
		self.pushButton_11.setObjectName("pushButton_11")
		self.pushButton_11.setText(_translate("MainWindow", "Generate"))
		self.gridLayout_35.addWidget(self.pushButton_11, 0, 3, 1, 1, QtCore.Qt.AlignLeft)
		self.pushButton_10 = QtWidgets.QPushButton(self.frame_13)
		self.pushButton_10.setObjectName("pushButton_10")
		self.pushButton_10.setText(_translate("MainWindow", "Export"))
		self.gridLayout_35.addWidget(self.pushButton_10, 0, 4, 1, 1, QtCore.Qt.AlignLeft)
		self.pushButton_12 = QtWidgets.QPushButton(self.frame_13)
		self.pushButton_12.setObjectName("pushButton_12")
		self.pushButton_12.setText(_translate("MainWindow", "Preview"))
		self.gridLayout_35.addWidget(self.pushButton_12, 0, 5, 1, 1, QtCore.Qt.AlignLeft)
		self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.frame_13)
		self.plainTextEdit_2.setReadOnly(True)
		self.plainTextEdit_2.setBackgroundVisible(False)
		self.plainTextEdit_2.setObjectName("plainTextEdit_2")
		self.plainTextEdit_2.setPlainText(_translate("MainWindow", "Move Artifact Up"))
		self.gridLayout_35.addWidget(self.plainTextEdit_2, 1, 0, 1, 1)
		self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.frame_13)
		self.plainTextEdit_3.setReadOnly(True)
		self.plainTextEdit_3.setObjectName("plainTextEdit_3")
		self.plainTextEdit_3.setPlainText(_translate("MainWindow", "Move Artifact Down"))
		self.gridLayout_35.addWidget(self.plainTextEdit_3, 1, 1, 1, 1)
		self.plainTextEdit_5 = QtWidgets.QPlainTextEdit(self.frame_13)
		self.plainTextEdit_5.setReadOnly(True)
		self.plainTextEdit_5.setObjectName("plainTextEdit_5")
		self.plainTextEdit_5.setPlainText(_translate("MainWindow", "Remove Artifact from Script Creation Table"))
		self.gridLayout_35.addWidget(self.plainTextEdit_5, 1, 2, 1, 1)
		self.plainTextEdit_6 = QtWidgets.QPlainTextEdit(self.frame_13)
		self.plainTextEdit_6.setReadOnly(True)
		self.plainTextEdit_6.setObjectName("plainTextEdit_6")
		self.plainTextEdit_6.setPlainText(_translate("MainWindow", "Generate Script"))
		self.gridLayout_35.addWidget(self.plainTextEdit_6, 1, 3, 1, 1)
		self.plainTextEdit_7 = QtWidgets.QPlainTextEdit(self.frame_13)
		self.plainTextEdit_7.setReadOnly(True)
		self.plainTextEdit_7.setObjectName("plainTextEdit_7")
		self.plainTextEdit_7.setPlainText(_translate("MainWindow", "Export Script"))
		self.gridLayout_35.addWidget(self.plainTextEdit_7, 1, 4, 1, 1)
		self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.frame_13)
		self.plainTextEdit_4.setReadOnly(True)
		self.plainTextEdit_4.setObjectName("plainTextEdit_4")
		self.plainTextEdit_4.setPlainText(_translate("MainWindow", "Generate Script Preview Window"))
		self.gridLayout_35.addWidget(self.plainTextEdit_4, 1, 5, 1, 1)
		self.verticalLayout_8.addWidget(self.frame_13)
		#Script Button content Area END

		__sortingEnabled = self.table_tag_2.isSortingEnabled()
		self.table_tag_2.setSortingEnabled(False)
		self.table_tag_2.setSortingEnabled(__sortingEnabled)

	
	def inittemp(self):
		_translate = QtCore.QCoreApplication.translate
		self.script_accordion = QtWidgets.QWidget()
		self.script_accordion.setGeometry(QtCore.QRect(0, 0, 548, 197))
		self.script_accordion.setObjectName("script_accordion")
		self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.script_accordion)
		self.verticalLayout_8.setObjectName("verticalLayout_8")
		
		#Script Table Content Area BEGIN
		self.table_tag_2 = QtWidgets.QTableWidget(self.script_accordion)
		self.table_tag_2.setAcceptDrops(False)
		self.table_tag_2.setEditTriggers(
				QtWidgets.QAbstractItemView.AnyKeyPressed | QtWidgets.QAbstractItemView.DoubleClicked)
		self.table_tag_2.setAlternatingRowColors(True)
		self.table_tag_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
		self.table_tag_2.setCornerButtonEnabled(True)
		self.table_tag_2.setRowCount(0)
		self.table_tag_2.setObjectName("table_tag_2")
		self.table_tag_2.setColumnCount(7)
		item = QtWidgets.QTableWidgetItem()
		item.setText(_translate("MainWindow", "Select"))
		self.table_tag_2.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		item.setText(_translate("MainWindow", "Added Artifact"))
		self.table_tag_2.setHorizontalHeaderItem(1, item)
		item = QtWidgets.QTableWidgetItem()
		item.setText(_translate("MainWindow", "Time Stamp"))
		self.table_tag_2.setHorizontalHeaderItem(2, item)
		item = QtWidgets.QTableWidgetItem()
		item.setText(_translate("MainWindow", "Artifact Type"))
		self.table_tag_2.setHorizontalHeaderItem(3, item)
		item = QtWidgets.QTableWidgetItem()
		item.setText(_translate("MainWindow", "Tag"))
		self.table_tag_2.setHorizontalHeaderItem(4, item)
		item = QtWidgets.QTableWidgetItem()
		item.setText(_translate("MainWindow", "MAC Address"))
		self.table_tag_2.setHorizontalHeaderItem(5, item)
		item = QtWidgets.QTableWidgetItem()
		item.setText(_translate("MainWindow", "Description"))
		self.table_tag_2.setHorizontalHeaderItem(6, item)
		"""item = QtWidgets.QTableWidgetItem()
		item.setCheckState(QtCore.Qt.Unchecked)
		self.table_tag_2.setItem(0, 0, item)
		item = QtWidgets.QTableWidgetItem()
		item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
		self.table_tag_2.setItem(0, 1, item)
		item = QtWidgets.QTableWidgetItem()
		item.setFlags(QtCore.Qt.ItemIsSelectable)
		self.table_tag_2.setItem(0, 3, item)
		item = QtWidgets.QTableWidgetItem()
		item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled)
		self.table_tag_2.setItem(0, 4, item)"""
		"""item = QtWidgets.QTableWidgetItem()
		item.setCheckState(QtCore.Qt.Unchecked)
		self.table_tag_2.setItem(1, 0, item)
		item = QtWidgets.QTableWidgetItem()
		item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
		self.table_tag_2.setItem(1, 1, item)
		item = QtWidgets.QTableWidgetItem()
		item.setFlags(QtCore.Qt.ItemIsSelectable)
		self.table_tag_2.setItem(1, 3, item)
		item = QtWidgets.QTableWidgetItem()
		item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled)
		self.table_tag_2.setItem(1, 4, item)"""
		"""item = QtWidgets.QTableWidgetItem()
		item.setCheckState(QtCore.Qt.Unchecked)
		self.table_tag_2.setItem(2, 0, item)
		item = QtWidgets.QTableWidgetItem()
		item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
		self.table_tag_2.setItem(2, 1, item)
		item = QtWidgets.QTableWidgetItem()
		item.setFlags(QtCore.Qt.ItemIsSelectable)
		self.table_tag_2.setItem(2, 3, item)
		item = QtWidgets.QTableWidgetItem()
		item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled)
		self.table_tag_2.setItem(2, 4, item)"""
		self.table_tag_2.horizontalHeader().setCascadingSectionResizes(True)
		self.table_tag_2.horizontalHeader().setDefaultSectionSize(150)
		self.table_tag_2.horizontalHeader().setMinimumSectionSize(20)
		self.table_tag_2.horizontalHeader().setSortIndicatorShown(True)
		self.table_tag_2.horizontalHeader().setStretchLastSection(True)
		self.table_tag_2.verticalHeader().setVisible(False)
		self.table_tag_2.verticalHeader().setCascadingSectionResizes(True)
		self.table_tag_2.verticalHeader().setSortIndicatorShown(True)
		#Script Table Content Area END

		#Script Button Content Area START
		self.verticalLayout_8.addWidget(self.table_tag_2)
		self.frame_13 = QtWidgets.QFrame(self.script_accordion)
		self.frame_13.setMaximumSize(QtCore.QSize(16777215, 111))
		self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_13.setObjectName("frame_13")
		self.gridLayout_35 = QtWidgets.QGridLayout(self.frame_13)
		self.gridLayout_35.setObjectName("gridLayout_35")
		self.pushButton_7 = QtWidgets.QPushButton(self.frame_13)
		self.pushButton_7.setObjectName("pushButton_7")
		self.pushButton_7.setText(_translate("MainWindow", "Up"))
		self.gridLayout_35.addWidget(self.pushButton_7, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
		self.pushButton_8 = QtWidgets.QPushButton(self.frame_13)
		self.pushButton_8.setObjectName("pushButton_8")
		self.pushButton_8.setText(_translate("MainWindow", "Down"))

		self.gridLayout_35.addWidget(self.pushButton_8, 0, 1, 1, 1, QtCore.Qt.AlignLeft)
		self.pushButton_9 = QtWidgets.QPushButton(self.frame_13)
		self.pushButton_9.setObjectName("pushButton_9")
		self.pushButton_9.setText(_translate("MainWindow", "Remove"))

		self.gridLayout_35.addWidget(self.pushButton_9, 0, 2, 1, 1, QtCore.Qt.AlignLeft)
		self.pushButton_11 = QtWidgets.QPushButton(self.frame_13)
		self.pushButton_11.setObjectName("pushButton_11")
		self.pushButton_11.setText(_translate("MainWindow", "Generate"))
		self.gridLayout_35.addWidget(self.pushButton_11, 0, 3, 1, 1, QtCore.Qt.AlignLeft)
		self.pushButton_10 = QtWidgets.QPushButton(self.frame_13)
		self.pushButton_10.setObjectName("pushButton_10")
		self.pushButton_10.setText(_translate("MainWindow", "Export"))
		self.gridLayout_35.addWidget(self.pushButton_10, 0, 4, 1, 1, QtCore.Qt.AlignLeft)
		self.pushButton_12 = QtWidgets.QPushButton(self.frame_13)
		self.pushButton_12.setObjectName("pushButton_12")
		self.pushButton_12.setText(_translate("MainWindow", "Preview"))
		self.gridLayout_35.addWidget(self.pushButton_12, 0, 5, 1, 1, QtCore.Qt.AlignLeft)
		self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.frame_13)
		self.plainTextEdit_2.setReadOnly(True)
		self.plainTextEdit_2.setBackgroundVisible(False)
		self.plainTextEdit_2.setObjectName("plainTextEdit_2")
		self.plainTextEdit_2.setPlainText(_translate("MainWindow", "Move Artifact Up"))
		self.gridLayout_35.addWidget(self.plainTextEdit_2, 1, 0, 1, 1)
		self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.frame_13)
		self.plainTextEdit_3.setReadOnly(True)
		self.plainTextEdit_3.setObjectName("plainTextEdit_3")
		self.plainTextEdit_3.setPlainText(_translate("MainWindow", "Move Artifact Down"))
		self.gridLayout_35.addWidget(self.plainTextEdit_3, 1, 1, 1, 1)
		self.plainTextEdit_5 = QtWidgets.QPlainTextEdit(self.frame_13)
		self.plainTextEdit_5.setReadOnly(True)
		self.plainTextEdit_5.setObjectName("plainTextEdit_5")
		self.plainTextEdit_5.setPlainText(_translate("MainWindow", "Remove Artifact from Script Creation Table"))
		self.gridLayout_35.addWidget(self.plainTextEdit_5, 1, 2, 1, 1)
		self.plainTextEdit_6 = QtWidgets.QPlainTextEdit(self.frame_13)
		self.plainTextEdit_6.setReadOnly(True)
		self.plainTextEdit_6.setObjectName("plainTextEdit_6")
		self.plainTextEdit_6.setPlainText(_translate("MainWindow", "Generate Script"))
		self.gridLayout_35.addWidget(self.plainTextEdit_6, 1, 3, 1, 1)
		self.plainTextEdit_7 = QtWidgets.QPlainTextEdit(self.frame_13)
		self.plainTextEdit_7.setReadOnly(True)
		self.plainTextEdit_7.setObjectName("plainTextEdit_7")
		self.plainTextEdit_7.setPlainText(_translate("MainWindow", "Export Script"))
		self.gridLayout_35.addWidget(self.plainTextEdit_7, 1, 4, 1, 1)
		self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.frame_13)
		self.plainTextEdit_4.setReadOnly(True)
		self.plainTextEdit_4.setObjectName("plainTextEdit_4")
		self.plainTextEdit_4.setPlainText(_translate("MainWindow", "Generate Script Preview Window"))
		self.gridLayout_35.addWidget(self.plainTextEdit_4, 1, 5, 1, 1)
		self.verticalLayout_8.addWidget(self.frame_13)
		#Script Button content Area END

		__sortingEnabled = self.table_tag_2.isSortingEnabled()
		self.table_tag_2.setSortingEnabled(False)
		self.table_tag_2.setSortingEnabled(__sortingEnabled)
		

	def get_accordion(self):
		return self.script_accordion

	def populateTable(self, selected_items):
		print("populate table script !!!")
		print(selected_items)