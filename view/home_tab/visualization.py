from PyQt5 import QtWidgets, QtCore, QtGui
from view.components import result_table, annotation_table, bar_graph

class Visualization:
	def __init__(self):
		self.visualization_accordion = QtWidgets.QWidget()
		self.visualization_accordion.setGeometry(QtCore.QRect(0, 0, 429, 443))
		self.visualization_accordion.setObjectName("visualization_accordion")
		self.gridLayout_9 = QtWidgets.QGridLayout(self.visualization_accordion)
		self.gridLayout_9.setObjectName("gridLayout_9")
		self.visualization_tabs = QtWidgets.QTabWidget(self.visualization_accordion)
		self.visualization_tabs.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.visualization_tabs.setObjectName("visualization_tabs")
		self.type = QtWidgets.QWidget()
		self.type.setObjectName("type")
		self.gridLayout = QtWidgets.QGridLayout(self.type)
		self.gridLayout.setObjectName("gridLayout")
		self.visualization_selection = QtWidgets.QFrame(self.type)
		self.visualization_selection.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.visualization_selection.setFrameShadow(QtWidgets.QFrame.Plain)
		self.visualization_selection.setObjectName("visualization_selection")
		self.gridLayout_13 = QtWidgets.QGridLayout(self.visualization_selection)
		self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
		self.gridLayout_13.setObjectName("gridLayout_13")
		self.radioButton_2 = QtWidgets.QRadioButton(self.visualization_selection)
		self.radioButton_2.setObjectName("radioButton_2")
		self.gridLayout_13.addWidget(self.radioButton_2, 1, 0, 1, 1, QtCore.Qt.AlignLeft)
		self.radioButton_4 = QtWidgets.QRadioButton(self.visualization_selection)
		self.radioButton_4.setObjectName("radioButton_4")
		self.gridLayout_13.addWidget(self.radioButton_4, 2, 0, 1, 1, QtCore.Qt.AlignLeft)
		self.radioButton = QtWidgets.QRadioButton(self.visualization_selection)
		self.radioButton.setChecked(True)
		self.radioButton.setObjectName("radioButton")
		self.gridLayout_13.addWidget(self.radioButton, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
		self.gridLayout.addWidget(self.visualization_selection, 0, 0, 1, 1)
		self.visualization_generators = QtWidgets.QFrame(self.type)
		self.visualization_generators.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.visualization_generators.setFrameShadow(QtWidgets.QFrame.Plain)
		self.visualization_generators.setObjectName("visualization_generators")
		self.gridLayout_12 = QtWidgets.QGridLayout(self.visualization_generators)
		self.gridLayout_12.setObjectName("gridLayout_12")
		spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.gridLayout_12.addItem(spacerItem1, 0, 0, 1, 1)
		spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.gridLayout_12.addItem(spacerItem2, 0, 1, 1, 1)
		self.pushButton_5 = QtWidgets.QPushButton(self.visualization_generators)
		self.pushButton_5.setObjectName("pushButton_5")
		self.gridLayout_12.addWidget(self.pushButton_5, 1, 0, 1, 1)
		self.pushButton_6 = QtWidgets.QPushButton(self.visualization_generators)
		self.pushButton_6.setObjectName("pushButton_6")
		self.gridLayout_12.addWidget(self.pushButton_6, 1, 1, 1, 1)
		self.gridLayout.addWidget(self.visualization_generators, 1, 3, 1, 1)
		spacerItem3 = QtWidgets.QSpacerItem(399, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
		spacerItem4 = QtWidgets.QSpacerItem(466, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout.addItem(spacerItem4, 0, 2, 1, 1)
		self.visualization_tabs.addTab(self.type, "")
		self.pie_chart = QtWidgets.QWidget()
		self.pie_chart.setObjectName("pie_chart")
		self.gridLayout_10 = QtWidgets.QGridLayout(self.pie_chart)
		self.gridLayout_10.setObjectName("gridLayout_10")
		self.widget = QtWidgets.QWidget(self.pie_chart)
		self.widget.setObjectName("widget")
		self.gridLayout_34 = QtWidgets.QGridLayout(self.widget)
		self.gridLayout_34.setObjectName("gridLayout_34")
		self.timeline_metadata_2 = QtWidgets.QFrame(self.widget)
		self.timeline_metadata_2.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.timeline_metadata_2.setFrameShadow(QtWidgets.QFrame.Plain)
		self.timeline_metadata_2.setObjectName("timeline_metadata_2")
		self.gridLayout_16 = QtWidgets.QGridLayout(self.timeline_metadata_2)
		self.gridLayout_16.setObjectName("gridLayout_16")
		self.label_91 = QtWidgets.QLabel(self.timeline_metadata_2)
		self.label_91.setObjectName("label_91")
		self.gridLayout_16.addWidget(self.label_91, 1, 0, 1, 1)
		self.lineEdit_4 = QtWidgets.QLineEdit(self.timeline_metadata_2)
		self.lineEdit_4.setText("")
		self.lineEdit_4.setObjectName("lineEdit_4")
		self.gridLayout_16.addWidget(self.lineEdit_4, 1, 1, 1, 1)
		self.label_90 = QtWidgets.QLabel(self.timeline_metadata_2)
		self.label_90.setObjectName("label_90")
		self.gridLayout_16.addWidget(self.label_90, 0, 0, 1, 1)
		self.gridLayout_34.addWidget(self.timeline_metadata_2, 0, 0, 1, 1, QtCore.Qt.AlignTop)
		self.timeline_title_2 = QtWidgets.QFrame(self.widget)
		self.timeline_title_2.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.timeline_title_2.setFrameShadow(QtWidgets.QFrame.Raised)
		self.timeline_title_2.setObjectName("timeline_title_2")
		self.gridLayout_17 = QtWidgets.QGridLayout(self.timeline_title_2)
		self.gridLayout_17.setObjectName("gridLayout_17")
		self.label_92 = QtWidgets.QLabel(self.timeline_title_2)
		self.label_92.setObjectName("label_92")
		self.gridLayout_17.addWidget(self.label_92, 0, 0, 1, 1)
		self.label_93 = QtWidgets.QLabel(self.timeline_title_2)
		self.label_93.setObjectName("label_93")
		self.gridLayout_17.addWidget(self.label_93, 1, 0, 1, 1)
		self.lineEdit_5 = QtWidgets.QLineEdit(self.timeline_title_2)
		self.lineEdit_5.setObjectName("lineEdit_5")
		self.gridLayout_17.addWidget(self.lineEdit_5, 1, 1, 1, 1)
		self.frame_4 = QtWidgets.QFrame(self.timeline_title_2)
		self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_4.setObjectName("frame_4")
		self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
		self.horizontalLayout_4.setObjectName("horizontalLayout_4")
		self.gridLayout_17.addWidget(self.frame_4, 2, 1, 1, 1)
		self.gridLayout_34.addWidget(self.timeline_title_2, 0, 1, 1, 1, QtCore.Qt.AlignTop)
		self.frame_12 = QtWidgets.QFrame(self.widget)
		self.frame_12.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.frame_12.setFrameShadow(QtWidgets.QFrame.Plain)
		self.frame_12.setObjectName("frame_12")
		self.gridLayout_15 = QtWidgets.QGridLayout(self.frame_12)
		self.gridLayout_15.setObjectName("gridLayout_15")
		self.label_94 = QtWidgets.QLabel(self.frame_12)
		self.label_94.setMaximumSize(QtCore.QSize(301, 241))
		self.label_94.setText("")
		self.label_94.setPixmap(QtGui.QPixmap("view/assets/pie-chart-too-few-slices.png"))
		self.label_94.setObjectName("label_94")
		self.gridLayout_15.addWidget(self.label_94, 0, 0, 1, 1)
		self.gridLayout_34.addWidget(self.frame_12, 1, 0, 1, 2)
		self.gridLayout_10.addWidget(self.widget, 0, 0, 1, 1)
		self.visualization_tabs.addTab(self.pie_chart, "")
		self.bar_graph = QtWidgets.QWidget()
		self.bar_graph.setObjectName("bar_graph")
		self.gridLayout_37 = QtWidgets.QGridLayout(self.bar_graph)
		self.gridLayout_37.setObjectName("gridLayout_37")
		self.Bar_Graph_Area_123 = QtWidgets.QScrollArea(self.bar_graph)
		self.Bar_Graph_Area_123.setWidgetResizable(True)
		self.Bar_Graph_Area_123.setObjectName("Bar_Graph_Area_123")
		self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
		self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 72, 16))
		self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
		self.Bar_Graph_Area_123.setWidget(self.scrollAreaWidgetContents_2)
		# bar graph addition
		self.Bar_Graph_Area_123.setWidget(bar_graph.add_bar_graph())
		self.gridLayout_37.addWidget(self.Bar_Graph_Area_123, 0, 0, 1, 1)
		self.visualization_tabs.addTab(self.bar_graph, "")
		self.timeline = QtWidgets.QWidget()
		self.timeline.setObjectName("timeline")
		self.gridLayout_11 = QtWidgets.QGridLayout(self.timeline)
		self.gridLayout_11.setObjectName("gridLayout_11")
		self.scrollArea_2 = QtWidgets.QScrollArea(self.timeline)
		self.scrollArea_2.setFocusPolicy(QtCore.Qt.StrongFocus)
		self.scrollArea_2.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.scrollArea_2.setFrameShadow(QtWidgets.QFrame.Plain)
		self.scrollArea_2.setLineWidth(1)
		self.scrollArea_2.setWidgetResizable(True)
		self.scrollArea_2.setObjectName("scrollArea_2")
		self.scrollAreaWidgetContents = QtWidgets.QWidget()
		self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 572, 265))
		self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
		self.gridLayout_6 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
		self.gridLayout_6.setObjectName("gridLayout_6")
		self.timeline_footer = QtWidgets.QFrame(self.scrollAreaWidgetContents)
		self.timeline_footer.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.timeline_footer.setFrameShadow(QtWidgets.QFrame.Plain)
		self.timeline_footer.setObjectName("timeline_footer")
		self.gridLayout_8 = QtWidgets.QGridLayout(self.timeline_footer)
		self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
		self.gridLayout_8.setObjectName("gridLayout_8")
		self.timeline_legend = QtWidgets.QFrame(self.timeline_footer)
		self.timeline_legend.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.timeline_legend.setFrameShadow(QtWidgets.QFrame.Raised)
		self.timeline_legend.setObjectName("timeline_legend")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.timeline_legend)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.label_35 = QtWidgets.QLabel(self.timeline_legend)
		self.label_35.setObjectName("label_35")
		self.verticalLayout_2.addWidget(self.label_35)
		self.listWidget = QtWidgets.QListWidget(self.timeline_legend)
		self.listWidget.setObjectName("listWidget")
		item = QtWidgets.QListWidgetItem()
		self.listWidget.addItem(item)
		item = QtWidgets.QListWidgetItem()
		self.listWidget.addItem(item)
		item = QtWidgets.QListWidgetItem()
		self.listWidget.addItem(item)
		item = QtWidgets.QListWidgetItem()
		self.listWidget.addItem(item)
		item = QtWidgets.QListWidgetItem()
		self.listWidget.addItem(item)
		item = QtWidgets.QListWidgetItem()
		self.listWidget.addItem(item)
		item = QtWidgets.QListWidgetItem()
		self.listWidget.addItem(item)
		item = QtWidgets.QListWidgetItem()
		self.listWidget.addItem(item)
		self.verticalLayout_2.addWidget(self.listWidget)
		self.gridLayout_8.addWidget(self.timeline_legend, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
		self.frame_3 = QtWidgets.QFrame(self.timeline_footer)
		self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
		self.frame_3.setObjectName("frame_3")
		self.line = QtWidgets.QFrame(self.frame_3)
		self.line.setGeometry(QtCore.QRect(10, 50, 341, 20))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.line_2 = QtWidgets.QFrame(self.frame_3)
		self.line_2.setGeometry(QtCore.QRect(20, 60, 3, 61))
		self.line_2.setStyleSheet("background-color: rgb(170, 0, 0);\n"
															"border-color: rgb(170, 0, 0);")
		self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.line_3 = QtWidgets.QFrame(self.frame_3)
		self.line_3.setGeometry(QtCore.QRect(70, 0, 3, 61))
		self.line_3.setStyleSheet("background-color: rgb(170, 0, 0);\n"
															"border-color: rgb(170, 0, 0);")
		self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_3.setObjectName("line_3")
		self.line_5 = QtWidgets.QFrame(self.frame_3)
		self.line_5.setGeometry(QtCore.QRect(230, 0, 3, 61))
		self.line_5.setStyleSheet("background-color: rgb(170, 0, 0);\n"
															"border-color: rgb(170, 0, 0);")
		self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_5.setObjectName("line_5")
		self.line_6 = QtWidgets.QFrame(self.frame_3)
		self.line_6.setGeometry(QtCore.QRect(280, 60, 3, 61))
		self.line_6.setStyleSheet("background-color: rgb(170, 0, 0);\n"
															"border-color: rgb(170, 0, 0);")
		self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_6.setObjectName("line_6")
		self.line_7 = QtWidgets.QFrame(self.frame_3)
		self.line_7.setGeometry(QtCore.QRect(340, 0, 3, 61))
		self.line_7.setStyleSheet("background-color: rgb(170, 0, 0);\n"
															"border-color: rgb(170, 0, 0);")
		self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_7.setObjectName("line_7")
		self.line_8 = QtWidgets.QFrame(self.frame_3)
		self.line_8.setGeometry(QtCore.QRect(10, 200, 391, 16))
		self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_8.setObjectName("line_8")
		self.line_4 = QtWidgets.QFrame(self.frame_3)
		self.line_4.setGeometry(QtCore.QRect(130, 60, 3, 61))
		self.line_4.setStyleSheet("background-color: rgb(170, 0, 0);")
		self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_4.setObjectName("line_4")
		self.label_36 = QtWidgets.QLabel(self.frame_3)
		self.label_36.setGeometry(QtCore.QRect(10, 230, 61, 16))
		self.label_36.setObjectName("label_36")
		self.label_37 = QtWidgets.QLabel(self.frame_3)
		self.label_37.setGeometry(QtCore.QRect(110, 230, 61, 16))
		self.label_37.setObjectName("label_37")
		self.label_38 = QtWidgets.QLabel(self.frame_3)
		self.label_38.setGeometry(QtCore.QRect(210, 230, 61, 16))
		self.label_38.setObjectName("label_38")
		self.label_39 = QtWidgets.QLabel(self.frame_3)
		self.label_39.setGeometry(QtCore.QRect(320, 230, 61, 16))
		self.label_39.setObjectName("label_39")
		self.line_9 = QtWidgets.QFrame(self.frame_3)
		self.line_9.setGeometry(QtCore.QRect(20, 200, 16, 21))
		self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_9.setObjectName("line_9")
		self.line_10 = QtWidgets.QFrame(self.frame_3)
		self.line_10.setGeometry(QtCore.QRect(120, 200, 16, 21))
		self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_10.setObjectName("line_10")
		self.line_11 = QtWidgets.QFrame(self.frame_3)
		self.line_11.setGeometry(QtCore.QRect(220, 200, 16, 21))
		self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_11.setObjectName("line_11")
		self.line_12 = QtWidgets.QFrame(self.frame_3)
		self.line_12.setGeometry(QtCore.QRect(330, 200, 16, 21))
		self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_12.setObjectName("line_12")
		self.gridLayout_8.addWidget(self.frame_3, 0, 1, 1, 1)
		self.gridLayout_6.addWidget(self.timeline_footer, 1, 0, 1, 1, QtCore.Qt.AlignTop)
		self.timeline_header = QtWidgets.QFrame(self.scrollAreaWidgetContents)
		self.timeline_header.setAutoFillBackground(False)
		self.timeline_header.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.timeline_header.setFrameShadow(QtWidgets.QFrame.Plain)
		self.timeline_header.setObjectName("timeline_header")
		self.gridLayout_4 = QtWidgets.QGridLayout(self.timeline_header)
		self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
		self.gridLayout_4.setHorizontalSpacing(6)
		self.gridLayout_4.setObjectName("gridLayout_4")
		self.timeline_metadata = QtWidgets.QFrame(self.timeline_header)
		self.timeline_metadata.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.timeline_metadata.setFrameShadow(QtWidgets.QFrame.Plain)
		self.timeline_metadata.setObjectName("timeline_metadata")
		self.gridLayout_7 = QtWidgets.QGridLayout(self.timeline_metadata)
		self.gridLayout_7.setObjectName("gridLayout_7")
		self.label_31 = QtWidgets.QLabel(self.timeline_metadata)
		self.label_31.setObjectName("label_31")
		self.gridLayout_7.addWidget(self.label_31, 0, 0, 1, 1)
		self.label_32 = QtWidgets.QLabel(self.timeline_metadata)
		self.label_32.setObjectName("label_32")
		self.gridLayout_7.addWidget(self.label_32, 1, 0, 1, 1)
		self.lineEdit = QtWidgets.QLineEdit(self.timeline_metadata)
		self.lineEdit.setText("")
		self.lineEdit.setObjectName("lineEdit")
		self.gridLayout_7.addWidget(self.lineEdit, 1, 1, 1, 1)
		self.label_33 = QtWidgets.QLabel(self.timeline_metadata)
		self.label_33.setObjectName("label_33")
		self.gridLayout_7.addWidget(self.label_33, 2, 0, 1, 1)
		self.comboBox = QtWidgets.QComboBox(self.timeline_metadata)
		self.comboBox.setObjectName("comboBox")
		self.comboBox.addItem("")
		self.gridLayout_7.addWidget(self.comboBox, 2, 1, 1, 1)
		self.label_34 = QtWidgets.QLabel(self.timeline_metadata)
		self.label_34.setObjectName("label_34")
		self.gridLayout_7.addWidget(self.label_34, 3, 0, 1, 1)
		self.lineEdit_2 = QtWidgets.QLineEdit(self.timeline_metadata)
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.gridLayout_7.addWidget(self.lineEdit_2, 3, 1, 1, 1)
		self.gridLayout_4.addWidget(self.timeline_metadata, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
		self.timeline_title = QtWidgets.QFrame(self.timeline_header)
		self.timeline_title.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.timeline_title.setFrameShadow(QtWidgets.QFrame.Raised)
		self.timeline_title.setObjectName("timeline_title")
		self.gridLayout_5 = QtWidgets.QGridLayout(self.timeline_title)
		self.gridLayout_5.setObjectName("gridLayout_5")
		self.label_5 = QtWidgets.QLabel(self.timeline_title)
		self.label_5.setObjectName("label_5")
		self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 1)
		self.label_7 = QtWidgets.QLabel(self.timeline_title)
		self.label_7.setObjectName("label_7")
		self.gridLayout_5.addWidget(self.label_7, 1, 0, 1, 1)
		self.lineEdit_3 = QtWidgets.QLineEdit(self.timeline_title)
		self.lineEdit_3.setObjectName("lineEdit_3")
		self.gridLayout_5.addWidget(self.lineEdit_3, 1, 1, 1, 1)
		self.frame_2 = QtWidgets.QFrame(self.timeline_title)
		self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_2.setObjectName("frame_2")
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
		self.pushButton_2.setObjectName("pushButton_2")
		self.horizontalLayout_3.addWidget(self.pushButton_2)
		self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
		self.pushButton_3.setObjectName("pushButton_3")
		self.horizontalLayout_3.addWidget(self.pushButton_3)
		self.gridLayout_5.addWidget(self.frame_2, 2, 1, 1, 1)
		self.label_40 = QtWidgets.QLabel(self.timeline_title)
		self.label_40.setObjectName("label_40")
		self.gridLayout_5.addWidget(self.label_40, 2, 0, 1, 1)
		self.gridLayout_4.addWidget(self.timeline_title, 0, 1, 1, 1, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
		self.gridLayout_6.addWidget(self.timeline_header, 0, 0, 1, 1, QtCore.Qt.AlignTop)
		self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)
		self.gridLayout_11.addWidget(self.scrollArea_2, 0, 1, 1, 1)
		self.visualization_tabs.addTab(self.timeline, "")
		self.gridLayout_9.addWidget(self.visualization_tabs, 0, 1, 1, 1)


		"""retranslateUi"""
		_translate = QtCore.QCoreApplication.translate
		self.radioButton_2.setText(_translate("MainWindow", "Bar Graph"))
		self.radioButton_4.setText(_translate("MainWindow", "Timeline"))
		self.radioButton.setText(_translate("MainWindow", "Pie Chart"))
		self.pushButton_5.setText(_translate("MainWindow", "Generate"))
		self.pushButton_6.setText(_translate("MainWindow", "Export"))
		self.visualization_tabs.setTabText(self.visualization_tabs.indexOf(self.type), _translate("MainWindow", "Type"))
		self.label_91.setText(_translate("MainWindow", "Title"))
		self.label_90.setText(_translate("MainWindow", "Pie Chart Metadata"))
		self.label_92.setText(_translate("MainWindow", "Visualization Result"))
		self.label_93.setText(_translate("MainWindow", "Pie Chart Title"))
		self.visualization_tabs.setTabText(self.visualization_tabs.indexOf(self.pie_chart),
																			_translate("MainWindow", "Pie Chart"))
		self.visualization_tabs.setTabText(self.visualization_tabs.indexOf(self.bar_graph),
																			_translate("MainWindow", "Bar Graph"))
		self.label_35.setText(_translate("MainWindow", "Artifact Key"))
		__sortingEnabled = self.listWidget.isSortingEnabled()
		self.listWidget.setSortingEnabled(False)
		item = self.listWidget.item(0)
		item.setText(_translate("MainWindow", "* Still Screenshot"))
		item = self.listWidget.item(1)
		item.setText(_translate("MainWindow", "* Video"))
		item = self.listWidget.item(2)
		item.setText(_translate("MainWindow", "* Network Packet"))
		item = self.listWidget.item(3)
		item.setText(_translate("MainWindow", "* Process"))
		item = self.listWidget.item(4)
		item.setText(_translate("MainWindow", "* Keystroke"))
		item = self.listWidget.item(5)
		item.setText(_translate("MainWindow", "* Mouse Action"))
		item = self.listWidget.item(6)
		item.setText(_translate("MainWindow", "* Window History"))
		item = self.listWidget.item(7)
		item.setText(_translate("MainWindow", "* System Call"))
		self.listWidget.setSortingEnabled(__sortingEnabled)
		self.label_36.setText(_translate("MainWindow", "9/11/2021"))
		self.label_37.setText(_translate("MainWindow", "9/13/2021"))
		self.label_38.setText(_translate("MainWindow", "9/15/2021"))
		self.label_39.setText(_translate("MainWindow", "9/18/2021"))
		self.label_31.setText(_translate("MainWindow", "Timeline Metadata"))
		self.label_32.setText(_translate("MainWindow", "Title"))
		self.label_33.setText(_translate("MainWindow", "Tick Interval Unit"))
		self.comboBox.setItemText(0, _translate("MainWindow", "Unit"))
		self.label_34.setText(_translate("MainWindow", "TIck Interval Value"))
		self.label_5.setText(_translate("MainWindow", "Visualization Result"))
		self.label_7.setText(_translate("MainWindow", "Timeline Title"))
		self.pushButton_2.setText(_translate("MainWindow", "+"))
		self.pushButton_3.setText(_translate("MainWindow", "-"))
		self.label_40.setText(_translate("MainWindow", "Zoom"))
		self.visualization_tabs.setTabText(self.visualization_tabs.indexOf(self.timeline),
																			_translate("MainWindow", "Timeline"))

	def get_accordion(self):
		return self.visualization_accordion