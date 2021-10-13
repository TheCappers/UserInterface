from PyQt5 import QtWidgets, QtCore, QtGui
from view.components import result_table, annotation_table, bar_graph
from view.home_tab.detailed_view import DetailedView
from view.home_tab.visualization import Visualization
from view.home_tab.script_accordion import Script_Accordion
from view.home_tab.history_accordion import History_Accordion
from view.home_tab.log_accordion import Log_Accordion

class Home:
	def __init__(self):
		self.tab_1 = QtWidgets.QWidget()
		self.tab_1.setObjectName("tab_1")
		self.gridLayout_tab_1 = QtWidgets.QGridLayout(self.tab_1)
		self.gridLayout_tab_1.setObjectName("gridLayout_tab_1")
		self.scrollArea = QtWidgets.QScrollArea(self.tab_1)
		self.scrollArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setObjectName("scrollArea")
		self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
		self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 1222, 1452))
		self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
		self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
		self.verticalLayout_4.setObjectName("verticalLayout_4")
		self.home_top_view = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
		self.home_top_view.setObjectName("home_top_view")
		self.gridLayout_70 = QtWidgets.QGridLayout(self.home_top_view)
		self.gridLayout_70.setObjectName("gridLayout_70")
		self.search_bar = QtWidgets.QFrame(self.home_top_view)
		self.search_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.search_bar.setFrameShadow(QtWidgets.QFrame.Plain)
		self.search_bar.setObjectName("search_bar")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.search_bar)
		self.verticalLayout.setContentsMargins(9, 9, -1, -1)
		self.verticalLayout.setSpacing(4)
		self.verticalLayout.setObjectName("verticalLayout")
		self.label_10 = QtWidgets.QLabel(self.search_bar)
		self.label_10.setStyleSheet("")
		self.label_10.setObjectName("label_10")
		self.verticalLayout.addWidget(self.label_10)
		self.search_expression_bar = QtWidgets.QLineEdit(self.search_bar)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.search_expression_bar.sizePolicy().hasHeightForWidth())
		self.search_expression_bar.setSizePolicy(sizePolicy)
		self.search_expression_bar.setMinimumSize(QtCore.QSize(200, 30))
		self.search_expression_bar.setMaximumSize(QtCore.QSize(300, 30))
		self.search_expression_bar.setText("")
		self.search_expression_bar.setObjectName("search_expression_bar")
		self.verticalLayout.addWidget(self.search_expression_bar)
		self.tagSearch_2 = QtWidgets.QFrame(self.search_bar)
		self.tagSearch_2.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.tagSearch_2.setFrameShadow(QtWidgets.QFrame.Raised)
		self.tagSearch_2.setObjectName("tagSearch_2")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.tagSearch_2)
		self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout.setSpacing(0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.tagSearch = QtWidgets.QFrame(self.tagSearch_2)
		self.tagSearch.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.tagSearch.setFrameShadow(QtWidgets.QFrame.Plain)
		self.tagSearch.setObjectName("tagSearch")
		self.gridLayout_18 = QtWidgets.QGridLayout(self.tagSearch)
		self.gridLayout_18.setObjectName("gridLayout_18")
		self.label_8 = QtWidgets.QLabel(self.tagSearch)
		self.label_8.setObjectName("label_8")
		self.gridLayout_18.addWidget(self.label_8, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
		self.search_tag = QtWidgets.QComboBox(self.tagSearch)
		self.search_tag.setMinimumSize(QtCore.QSize(80, 0))
		self.search_tag.setMaximumSize(QtCore.QSize(150, 27))
		self.search_tag.setPlaceholderText("")
		self.search_tag.setObjectName("search_tag")
		self.search_tag.addItem("")
		self.search_tag.addItem("")
		self.gridLayout_18.addWidget(self.search_tag, 0, 2, 1, 1)
		spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout_18.addItem(spacerItem, 0, 1, 1, 1)
		self.horizontalLayout.addWidget(self.tagSearch, 0, QtCore.Qt.AlignLeft)
		self.search_button = QtWidgets.QPushButton(self.tagSearch_2)
		self.search_button.setMaximumSize(QtCore.QSize(150, 16777215))
		self.search_button.setObjectName("search_button")
		self.horizontalLayout.addWidget(self.search_button)
		self.verticalLayout.addWidget(self.tagSearch_2, 0, QtCore.Qt.AlignLeft)
		self.gridLayout_70.addWidget(self.search_bar, 0, 0, 1, 2)
		self.frame_21 = QtWidgets.QFrame(self.home_top_view)
		self.frame_21.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_21.setObjectName("frame_21")
		self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_21)
		self.gridLayout_3.setObjectName("gridLayout_3")
		self.universalRecord = QtWidgets.QPushButton(self.frame_21)
		self.universalRecord.setCheckable(True)
		self.universalRecord.setChecked(True)
		self.universalRecord.setObjectName("universalRecord")
		self.gridLayout_3.addWidget(self.universalRecord, 0, 0, 1, 1)
		self.gridLayout_70.addWidget(self.frame_21, 0, 2, 1, 1, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)


		""" FILTER START """

		self.search_filters = QtWidgets.QFrame(self.home_top_view)
		self.search_filters.setMinimumSize(QtCore.QSize(250, 0))
		self.search_filters.setMaximumSize(QtCore.QSize(250, 16777215))
		self.search_filters.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.search_filters.setObjectName("search_filters")

		self.gridLayout_2 = QtWidgets.QGridLayout(self.search_filters)
		self.gridLayout_2.setVerticalSpacing(7)
		self.gridLayout_2.setObjectName("gridLayout_2")

		self.label_filters = QtWidgets.QLabel(self.search_filters)
		self.label_filters.setMaximumSize(QtCore.QSize(16777215, 80))
		self.label_filters.setStyleSheet("")
		self.label_filters.setObjectName("label_filters")

		self.label_value_filter = QtWidgets.QLabel(self.search_filters)
		self.label_value_filter.setMaximumSize(QtCore.QSize(16777215, 12))
		self.label_value_filter.setObjectName("label_value_filter")
		self.gridLayout_2.addWidget(self.label_value_filter, 0, 1, 1, 1)

		self.label_user_profile = QtWidgets.QLabel(self.search_filters)
		self.label_user_profile.setMaximumSize(QtCore.QSize(16777215, 12))
		self.label_user_profile.setObjectName("label_user_profile")
		self.gridLayout_2.addWidget(self.label_user_profile, 1, 0, 1, 1)

		self.label_ip_address = QtWidgets.QLabel(self.search_filters)
		self.label_ip_address.setMaximumSize(QtCore.QSize(100, 16777215))
		self.label_ip_address.setObjectName("label_ip_address")
		self.gridLayout_2.addWidget(self.label_ip_address, 2, 0, 1, 1)
		self.ip_dropdown = QtWidgets.QComboBox(self.search_filters)
		self.ip_dropdown.setMaximumSize(QtCore.QSize(150, 20))
		self.ip_dropdown.setObjectName("ip_dropdown")
		self.ip_dropdown.addItem("goodbye")
		self.ip_dropdown.addItem("")
		self.ip_dropdown.addItem("")
		self.gridLayout_2.addWidget(self.ip_dropdown, 2, 1, 1, 1)

		self.label_mac_address = QtWidgets.QLabel(self.search_filters)
		self.label_mac_address.setMaximumSize(QtCore.QSize(100, 16777215))
		self.label_mac_address.setObjectName("label_mac_address")
		self.gridLayout_2.addWidget(self.label_mac_address, 3, 0, 1, 1)
		self.mac_dropdown = QtWidgets.QComboBox(self.search_filters)
		self.mac_dropdown.setMaximumSize(QtCore.QSize(150, 20))
		self.mac_dropdown.setObjectName("mac_dropdown")
		self.mac_dropdown.addItem("hello")
		self.mac_dropdown.addItem("")
		self.mac_dropdown.addItem("")
		self.gridLayout_2.addWidget(self.mac_dropdown, 3, 1, 1, 1)

		self.label_type = QtWidgets.QLabel(self.search_filters)
		self.label_type.setMaximumSize(QtCore.QSize(16777215, 15))
		self.label_type.setObjectName("label_type")
		self.gridLayout_2.addWidget(self.label_type, 4, 0, 1, 1)

		self.label_value_type = QtWidgets.QLabel(self.search_filters)
		self.label_value_type.setObjectName("label_2")
		self.gridLayout_2.addWidget(self.label_value_type, 4, 1, 1, 1)


		"""  FILTER CHECKBOXES    """

		self.checkBox_all_artifacts = QtWidgets.QCheckBox(self.search_filters)
		self.checkBox_all_artifacts.setText("")
		self.checkBox_all_artifacts.setObjectName("checkBox_all_artifacts")
		self.gridLayout_2.addWidget(self.checkBox_all_artifacts, 5, 1, 1, 1)
		self.label_all_artifacts = QtWidgets.QLabel(self.search_filters)
		font = QtGui.QFont()
		self.label_all_artifacts.setFont(font)
		self.label_all_artifacts.setObjectName("label_all_artifacts")
		self.gridLayout_2.addWidget(self.label_all_artifacts, 5, 0, 1, 1)

		self.checkBox_screenshot = QtWidgets.QCheckBox(self.search_filters)
		self.checkBox_screenshot.setText("")
		self.checkBox_screenshot.setObjectName("checkBox_screenshot")
		self.gridLayout_2.addWidget(self.checkBox_screenshot, 6, 1, 1, 1)
		self.label_screenshot = QtWidgets.QLabel(self.search_filters)
		self.label_screenshot.setObjectName("label_screenshot")
		self.gridLayout_2.addWidget(self.label_screenshot, 6, 0, 1, 1)

		self.checkBox_video = QtWidgets.QCheckBox(self.search_filters)
		self.checkBox_video.setText("")
		self.checkBox_video.setObjectName("checkBox_video")
		self.gridLayout_2.addWidget(self.checkBox_video, 7, 1, 1, 1)
		self.label_video = QtWidgets.QLabel(self.search_filters)
		self.label_video.setObjectName("label_video")
		self.gridLayout_2.addWidget(self.label_video, 7, 0, 1, 1)

		self.checkBox_network = QtWidgets.QCheckBox(self.search_filters)
		self.checkBox_network.setText("")
		self.checkBox_network.setObjectName("checkBox_network")
		self.gridLayout_2.addWidget(self.checkBox_network, 8, 1, 1, 1)
		self.label_network = QtWidgets.QLabel(self.search_filters)
		self.label_network.setObjectName("label_network")
		self.gridLayout_2.addWidget(self.label_network, 8, 0, 1, 1)

		self.checkBox_process = QtWidgets.QCheckBox(self.search_filters)
		self.checkBox_process.setText("")
		self.checkBox_process.setObjectName("checkBox_process")
		self.gridLayout_2.addWidget(self.checkBox_process, 9, 1, 1, 1)
		self.label_process = QtWidgets.QLabel(self.search_filters)
		self.label_process.setObjectName("label_process")
		self.gridLayout_2.addWidget(self.label_process, 9, 0, 1, 1)

		self.checkBox_keystroke = QtWidgets.QCheckBox(self.search_filters)
		self.checkBox_keystroke.setText("")
		self.checkBox_keystroke.setObjectName("checkBox_keystroke")
		self.gridLayout_2.addWidget(self.checkBox_keystroke, 10, 1, 1, 1)
		self.label_keystroke = QtWidgets.QLabel(self.search_filters)
		self.label_keystroke.setObjectName("label_keystroke")
		self.gridLayout_2.addWidget(self.label_keystroke, 10, 0, 1, 1)

		self.checkBox_mouse_action = QtWidgets.QCheckBox(self.search_filters)
		self.checkBox_mouse_action.setText("")
		self.checkBox_mouse_action.setObjectName("checkBox_mouse_action")
		self.gridLayout_2.addWidget(self.checkBox_mouse_action, 11, 1, 1, 1)
		self.label_mouse_action = QtWidgets.QLabel(self.search_filters)
		self.label_mouse_action.setObjectName("label_mouse_action")
		self.gridLayout_2.addWidget(self.label_mouse_action, 11, 0, 1, 1)

		self.checkBox_windowHistory = QtWidgets.QCheckBox(self.search_filters)
		self.checkBox_windowHistory.setText("")
		self.checkBox_windowHistory.setObjectName("checkBox_windowHistory")
		self.gridLayout_2.addWidget(self.checkBox_windowHistory, 12, 1, 1, 1)
		self.label_window_history = QtWidgets.QLabel(self.search_filters)
		self.label_window_history.setObjectName("label_window_history")
		self.gridLayout_2.addWidget(self.label_window_history, 12, 0, 1, 1)

		self.checkBox_system_call = QtWidgets.QCheckBox(self.search_filters)
		self.checkBox_system_call.setText("")
		self.checkBox_system_call.setObjectName("checkBox_system_call")
		self.gridLayout_2.addWidget(self.checkBox_system_call, 13, 1, 1, 1)
		self.label_system_call = QtWidgets.QLabel(self.search_filters)
		self.label_system_call.setObjectName("label_system_call")
		self.gridLayout_2.addWidget(self.label_system_call, 13, 0, 1, 1)

		self.checkBox_history = QtWidgets.QCheckBox(self.search_filters)
		self.checkBox_history.setText("")
		self.checkBox_history.setObjectName("checkBox_history")
		self.gridLayout_2.addWidget(self.checkBox_history, 14, 1, 1, 1)
		self.label_history = QtWidgets.QLabel(self.search_filters)
		self.label_history.setObjectName("label_history")
		self.gridLayout_2.addWidget(self.label_history, 14, 0, 1, 1)

		self.checkBox_log = QtWidgets.QCheckBox(self.search_filters)
		self.checkBox_log.setText("")
		self.checkBox_log.setObjectName("checkBox_log")
		self.gridLayout_2.addWidget(self.checkBox_log, 15, 1, 1, 1)
		self.label_log = QtWidgets.QLabel(self.search_filters)
		self.label_log.setObjectName("label_log")
		self.gridLayout_2.addWidget(self.label_log, 15, 0, 1, 1)

		""" FILTER CHECKBOXES END """

		self.label_date_time = QtWidgets.QLabel(self.search_filters)
		self.label_date_time.setMaximumSize(QtCore.QSize(16777215, 80))
		self.label_date_time.setStyleSheet("")
		self.label_date_time.setObjectName("label_date_time")
		self.gridLayout_2.addWidget(self.label_date_time, 16, 0, 1, 1)
		self.gridLayout_2.addWidget(self.label_filters, 0, 0, 1, 1)
		self.label_value_date_time = QtWidgets.QLabel(self.search_filters)
		self.label_value_date_time.setStyleSheet("")
		self.label_value_date_time.setObjectName("label_value_date_time")
		self.gridLayout_2.addWidget(self.label_value_date_time, 16, 1, 1, 1)

		self.label_start_date = QtWidgets.QLabel(self.search_filters)
		self.label_start_date.setObjectName("label_start_date")
		self.gridLayout_2.addWidget(self.label_start_date, 17, 0, 1, 1)
		self.start_date_widget = QtWidgets.QDateEdit(self.search_filters)
		self.start_date_widget.setObjectName("dateEdit")
		self.gridLayout_2.addWidget(self.start_date_widget, 17, 1, 1, 1)

		self.label_start_time = QtWidgets.QLabel(self.search_filters)
		self.label_start_time.setObjectName("label_start_time")
		self.gridLayout_2.addWidget(self.label_start_time, 18, 0, 1, 1)
		self.start_time_widget = QtWidgets.QTimeEdit(self.search_filters)
		self.start_time_widget.setObjectName("timeEdit")
		self.gridLayout_2.addWidget(self.start_time_widget, 18, 1, 1, 1)

		self.label_end_date = QtWidgets.QLabel(self.search_filters)
		self.label_end_date.setObjectName("label_end_date")
		self.gridLayout_2.addWidget(self.label_end_date, 19, 0, 1, 1)
		self.end_date_widget = QtWidgets.QDateEdit(self.search_filters)
		self.end_date_widget.setObjectName("end_date_widget")
		self.gridLayout_2.addWidget(self.end_date_widget, 19, 1, 1, 1)

		self.end_time_widget = QtWidgets.QTimeEdit(self.search_filters)
		self.end_time_widget.setObjectName("end_time_widget")
		self.gridLayout_2.addWidget(self.end_time_widget, 20, 1, 1, 1)
		self.label_end_time = QtWidgets.QLabel(self.search_filters)
		self.label_end_time.setObjectName("label_end_time")
		self.gridLayout_2.addWidget(self.label_end_time, 20, 0, 1, 1)

		self.gridLayout_70.addWidget(self.search_filters, 1, 0, 1, 1)

		""" FILTERS END """

		self.avert_table = QtWidgets.QFrame(self.home_top_view)
		self.avert_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.avert_table.setFrameShadow(QtWidgets.QFrame.Plain)
		self.avert_table.setObjectName("avert_table")
		self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.avert_table)
		self.verticalLayout_3.setObjectName("verticalLayout_3")
		self.label_9 = QtWidgets.QLabel(self.avert_table)
		font = QtGui.QFont()
		self.label_9.setFont(font)
		self.label_9.setObjectName("label_9")
		self.verticalLayout_3.addWidget(self.label_9)

		# global table_result
		# table_result = QtWidgets.QTableWidget(self.avert_table)
		# table_result = result_table.ResultTable(table_result)

		global table_result
		table_result = result_table.ResultTable()
		table_result.startTable(QtWidgets.QTableWidget(self.avert_table))
		self.table_result = table_result

		self.verticalLayout_3.addWidget(table_result.getTable())
		self.frame_14 = QtWidgets.QFrame(self.avert_table)
		self.frame_14.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.frame_14.setFrameShadow(QtWidgets.QFrame.Plain)
		self.frame_14.setObjectName("frame_14")
		self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_14)
		self.horizontalLayout_5.setObjectName("horizontalLayout_5")
		self.exportButton = QtWidgets.QPushButton(self.frame_14)
		self.exportButton.setObjectName("exportButton")
		self.horizontalLayout_5.addWidget(self.exportButton)

		self.pushButton_15 = QtWidgets.QPushButton(self.frame_14)
		self.pushButton_15.setObjectName("pushButton_15")
		self.horizontalLayout_5.addWidget(self.pushButton_15)

		self.pushButton_16 = QtWidgets.QPushButton(self.frame_14)
		self.pushButton_16.setObjectName("pushButton_16")
		self.horizontalLayout_5.addWidget(self.pushButton_16)
		self.verticalLayout_3.addWidget(self.frame_14, 0, QtCore.Qt.AlignLeft)
		self.gridLayout_70.addWidget(self.avert_table, 1, 1, 1, 2)
		self.verticalLayout_4.addWidget(self.home_top_view)

		""" Accordions Start """

		self.toolBox_accordion = QtWidgets.QToolBox(self.scrollAreaWidgetContents_3)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.toolBox_accordion.sizePolicy().hasHeightForWidth())
		self.toolBox_accordion.setSizePolicy(sizePolicy)
		self.toolBox_accordion.setMinimumSize(QtCore.QSize(0, 700))
		self.toolBox_accordion.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.toolBox_accordion.setObjectName("toolBox_accordion")


		""" DetailedViewAccordion Start """
		self.detailed_view_accordion = DetailedView()
		self.toolBox_accordion.addItem(self.detailed_view_accordion.get_accordion(), "Detailed_View_Accordion")
		""" DetailedViewAccordion End """

		"""Visualization Start"""
		self.visualization_accordion = Visualization()
		self.toolBox_accordion.addItem(self.visualization_accordion.get_accordion(), "Visualization_Accordion")
		"""Visualization End"""

		"""Script Start"""
		self.script_accordion = Script_Accordion()
		self.toolBox_accordion.addItem(self.script_accordion.get_accordion(), "Script_Accordion")
		"""Script End"""

		"""History Start"""
		self.history_accordion = History_Accordion()
		self.toolBox_accordion.addItem(self.history_accordion.get_accordion(), "History_Accordion")
		"""History End"""


		""" Log Start """
		self.log_accordion = Log_Accordion()
		self.toolBox_accordion.addItem(self.log_accordion.get_accordion(), "Log_Accordion")
		""" Log End """

		self.verticalLayout_4.addWidget(self.toolBox_accordion)
		self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
		self.gridLayout_tab_1.addWidget(self.scrollArea, 0, 0, 1, 1)

		_translate = QtCore.QCoreApplication.translate


		self.label_10.setText(_translate("MainWindow", "Search"))
		self.search_expression_bar.setPlaceholderText(_translate("MainWindow", "Search Expression"))
		self.label_8.setText(_translate("MainWindow", "Tag"))
		self.search_tag.setItemText(0, _translate("MainWindow", "Tag"))
		self.search_tag.setItemText(1, _translate("MainWindow", "Tag"))
		self.search_button.setText(_translate("MainWindow", "Search"))
		self.universalRecord.setText(_translate("MainWindow", "Record On"))


		self.mac_dropdown.setItemText(0, _translate("MainWindow", "7D:93:74:82:7B:71"))
		self.mac_dropdown.setItemText(1, _translate("MainWindow", "7D:93:74:82:7B:71"))
		self.mac_dropdown.setItemText(2, _translate("MainWindow", "7D:93:74:82:7B:71"))

		self.label_filters.setText(_translate("MainWindow", "Filters"))
		self.label_value_filter.setText(_translate("MainWindow", "Value"))

		self.label_user_profile.setText(_translate("MainWindow", "User Profile"))
		self.label_ip_address.setText(_translate("MainWindow", "IP Address"))
		self.label_mac_address.setText(_translate("MainWindow", "MAC Address"))
		self.label_type.setText(_translate("MainWindow", "Type"))
		self.label_value_type.setText(_translate("MainWindow", "Value"))


		self.label_all_artifacts.setText(_translate("MainWindow", "All Arifact Types"))
		self.label_screenshot.setText(_translate("MainWindow", "Still Screenshot"))
		self.label_video.setText(_translate("MainWindow", "Video"))
		self.label_network.setText(_translate("MainWindow", "Network Packet"))
		self.label_process.setText(_translate("MainWindow", "Process"))
		self.label_keystroke.setText(_translate("MainWindow", "Keystroke"))
		self.label_mouse_action.setText(_translate("MainWindow", "Mouse Action"))
		self.label_window_history.setText(_translate("MainWindow", "Window History"))
		self.label_system_call.setText(_translate("MainWindow", "System Call"))
		self.label_history.setText(_translate("MainWindow", "History"))
		self.label_log.setText(_translate("MainWindow", "Log"))


		self.label_date_time.setText(_translate("MainWindow", "Date and Time"))
		self.label_value_date_time.setText(_translate("MainWindow", "Value"))
		self.label_start_date.setText(_translate("MainWindow", "Start Date"))
		self.label_start_time.setText(_translate("MainWindow", "Start Time"))
		self.label_end_date.setText(_translate("MainWindow", "End Date"))
		self.label_end_time.setText(_translate("MainWindow", "End Time"))


		self.ip_dropdown.setItemText(0, _translate("MainWindow", "195.273.25.4"))
		self.ip_dropdown.setItemText(1, _translate("MainWindow", "195.273.25.4"))
		self.ip_dropdown.setItemText(2, _translate("MainWindow", "195.273.25.4"))

		self.label_9.setText(_translate("MainWindow", "AVERT RESULT"))
		self.exportButton.setText(_translate("MainWindow", "Export"))
		self.pushButton_15.setText(_translate("MainWindow", "Delete"))
		self.pushButton_16.setText(_translate("MainWindow", "Add Selected to Script Creation"))


		self.toolBox_accordion.setItemText(self.toolBox_accordion.indexOf(self.detailed_view_accordion.get_accordion()),
																_translate("MainWindow", "Detailed View of Selected Artifact"))
		self.toolBox_accordion.setItemText(self.toolBox_accordion.indexOf(self.visualization_accordion.get_accordion()),
																_translate("MainWindow", "Visualization"))
		self.toolBox_accordion.setItemText(self.toolBox_accordion.indexOf(self.script_accordion.get_accordion()),
																_translate("MainWindow", "Script"))
		self.toolBox_accordion.setItemText(self.toolBox_accordion.indexOf(self.history_accordion.get_accordion()),
																_translate("MainWindow", "History"))
		self.toolBox_accordion.setItemText(self.toolBox_accordion.indexOf(self.log_accordion.get_accordion()),
																_translate("MainWindow", "Log Content"))

	def get_tab(self):
		return self.tab_1
