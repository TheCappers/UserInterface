from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice, QBarSet
from view.components import result_table, annotation_table, bar_graph, pie_chart
from view.components.pie_chart import PieChart
from view.components.bar_graph import BarGraph
from controller.controller import Controller

controller = Controller()
''' Test Data For Pie Chart '''
screenshot_data = QPieSlice('Screenshot', controller.collection_total_size('Screenshot'))
video_data = QPieSlice('Video',controller.collection_total_size('Video'))
network_data = QPieSlice('Network',controller.collection_total_size('Network'))
process_data = QPieSlice('Processes',controller.collection_total_size('Processes'))
keystroke_data = QPieSlice('Keystroke',controller.collection_total_size('Keystroke'))
mouse_action_data = QPieSlice('Mouse_Actions',controller.collection_total_size('Mouse_Actions'))
window_history_data = QPieSlice('Window_History',controller.collection_total_size('Window_History'))
system_call_data = QPieSlice('System_Calls',controller.collection_total_size('System_Calls'))

artifact_data = [screenshot_data, video_data, network_data, process_data,
keystroke_data,mouse_action_data, window_history_data, system_call_data]


bar_graph_artifact_data = []

for artifact in artifact_data:
	set = QBarSet(artifact.label())
	set.append(artifact.value())
	bar_graph_artifact_data.append(set)



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

		''' Type tab '''
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

		''' Pie Chart Tab '''

		self.pie_chart_class = PieChart()
		self.pie_chart_class.add_pie_chart(artifact_data)
		self.pie_chart_graph = self.pie_chart_class.get_chart_view()

		self.pie_chart = QtWidgets.QWidget()
		self.pie_chart.setObjectName("pie_chart")
		self.gridLayout_10 = QtWidgets.QGridLayout(self.pie_chart)
		self.gridLayout_10.setObjectName("gridLayout_10")
		self.pie_chart_scroll_area = QtWidgets.QScrollArea(self.pie_chart)
		self.pie_chart_scroll_area.setWidgetResizable(True)
		self.pie_chart_scroll_area.setObjectName("pie_chart_scroll_area")
		self.pie_chart_scroll_area_widget_contents = QtWidgets.QWidget()
		self.pie_chart_scroll_area_widget_contents.setGeometry(QtCore.QRect(0, 0, 72, 16))
		self.pie_chart_scroll_area_widget_contents.setObjectName("pie_chart_scroll_area_widget_contents")
		self.pie_chart_scroll_area.setWidget(self.pie_chart_scroll_area_widget_contents)

		''' Pie Chart Checkboxes '''
		font = QtGui.QFont()

		self.label_pie_chart_all = QtWidgets.QLabel()
		self.label_pie_chart_all.setObjectName("label_pie_chart_all")
		self.gridLayout_10.addWidget(self.label_pie_chart_all, 0, 0, 1, 1)
		self.pie_tab_all_artifacts_checkbox = QtWidgets.QCheckBox()
		self.pie_tab_all_artifacts_checkbox.setText("All Artifacts")
		self.pie_tab_all_artifacts_checkbox.setObjectName("pie_tab_all_artifacts_checkbox")
		self.pie_tab_all_artifacts_checkbox.setChecked(True)
		self.pie_tab_all_artifacts_checkbox.clicked.connect(self.check_pie_chart_boxes)
		self.gridLayout_10.addWidget(self.pie_tab_all_artifacts_checkbox, 0, 0, 1, 1)

		self.label_pie_chart_screenshot = QtWidgets.QLabel()
		self.label_pie_chart_screenshot.setObjectName("label_pie_chart_screenshot")
		self.gridLayout_10.addWidget(self.label_pie_chart_screenshot, 1, 0, 1, 1)
		self.pie_tab_screenshot_checkbox = QtWidgets.QCheckBox()
		self.pie_tab_screenshot_checkbox.setText("Screenshots")
		self.pie_tab_screenshot_checkbox.setChecked(True)
		self.pie_tab_screenshot_checkbox.setObjectName("pie_tab_screenshot_checkbox")
		self.gridLayout_10.addWidget(self.pie_tab_screenshot_checkbox, 1, 0, 1, 1)

		self.label_pie_chart_video = QtWidgets.QLabel()
		self.label_pie_chart_video.setObjectName("label_pie_chart_video")
		self.gridLayout_10.addWidget(self.label_pie_chart_video, 2, 0, 1, 1)
		self.pie_tab_video_checkbox = QtWidgets.QCheckBox()
		self.pie_tab_video_checkbox.setText("Videos")
		self.pie_tab_video_checkbox.setChecked(True)
		self.pie_tab_video_checkbox.setObjectName("pie_tab_video_checkbox")
		self.gridLayout_10.addWidget(self.pie_tab_video_checkbox, 2, 0, 1, 1)

		self.label_pie_chart_network = QtWidgets.QLabel()
		self.label_pie_chart_network.setObjectName("label_pie_chart_network")
		self.gridLayout_10.addWidget(self.label_pie_chart_network, 3, 0, 1, 1)
		self.pie_tab_network_checkbox = QtWidgets.QCheckBox()
		self.pie_tab_network_checkbox.setText("Network Data")
		self.pie_tab_network_checkbox.setChecked(True)
		self.pie_tab_network_checkbox.setObjectName("pie_tab_network_checkbox")
		self.gridLayout_10.addWidget(self.pie_tab_network_checkbox, 3, 0, 1, 1)

		self.label_pie_chart_process = QtWidgets.QLabel()
		self.label_pie_chart_process.setObjectName("label_pie_chart_process")
		self.gridLayout_10.addWidget(self.label_pie_chart_process, 4, 0, 1, 1)
		self.pie_tab_process_checkbox = QtWidgets.QCheckBox()
		self.pie_tab_process_checkbox.setText("Processes")
		self.pie_tab_process_checkbox.setChecked(True)
		self.pie_tab_process_checkbox.setObjectName("pie_tab_process_checkbox")
		self.gridLayout_10.addWidget(self.pie_tab_process_checkbox, 4, 0, 1, 1)

		self.label_pie_chart_keystroke = QtWidgets.QLabel()
		self.label_pie_chart_keystroke.setObjectName("label_pie_chart_keystroke")
		self.gridLayout_10.addWidget(self.label_pie_chart_keystroke, 5, 0, 1, 1)
		self.pie_tab_keystroke_checkbox = QtWidgets.QCheckBox()
		self.pie_tab_keystroke_checkbox.setText("Keystrokes")
		self.pie_tab_keystroke_checkbox.setChecked(True)
		self.pie_tab_keystroke_checkbox.setObjectName("pie_tab_keystroke_checkbox")
		self.gridLayout_10.addWidget(self.pie_tab_keystroke_checkbox, 5, 0, 1, 1)

		self.label_pie_chart_mouse_action = QtWidgets.QLabel()
		self.label_pie_chart_mouse_action.setObjectName("label_pie_chart_mouse_action")
		self.gridLayout_10.addWidget(self.label_pie_chart_video, 6, 0, 1, 1)
		self.pie_tab_mouse_action_checkbox = QtWidgets.QCheckBox()
		self.pie_tab_mouse_action_checkbox.setText("Mouse Actions")
		self.pie_tab_mouse_action_checkbox.setChecked(True)
		self.pie_tab_mouse_action_checkbox.setObjectName("pie_tab_mouse_action_checkbox")
		self.gridLayout_10.addWidget(self.pie_tab_mouse_action_checkbox, 6, 0, 1, 1)

		self.label_pie_chart_window_history = QtWidgets.QLabel()
		self.label_pie_chart_window_history.setObjectName("label_pie_chart_window_history")
		self.gridLayout_10.addWidget(self.label_pie_chart_window_history, 7, 0, 1, 1)
		self.pie_tab_window_history_checkbox = QtWidgets.QCheckBox()
		self.pie_tab_window_history_checkbox.setText("Window History")
		self.pie_tab_window_history_checkbox.setChecked(True)
		self.pie_tab_window_history_checkbox.setObjectName("pie_tab_window_history_checkbox")
		self.gridLayout_10.addWidget(self.pie_tab_window_history_checkbox, 7, 0, 1, 1)

		self.label_pie_chart_system_call = QtWidgets.QLabel()
		self.label_pie_chart_system_call.setObjectName("label_pie_chart_system_call")
		self.gridLayout_10.addWidget(self.label_pie_chart_system_call, 8, 0, 1, 1)
		self.pie_tab_system_call_checkbox = QtWidgets.QCheckBox()
		self.pie_tab_system_call_checkbox.setText("System Calls")
		self.pie_tab_system_call_checkbox.setChecked(True)
		self.pie_tab_system_call_checkbox.setObjectName("pie_tab_system_call_checkbox")
		self.gridLayout_10.addWidget(self.pie_tab_system_call_checkbox, 8, 0, 1, 1)

		self.export_button_pie_chart = QtWidgets.QPushButton()
		self.export_button_pie_chart.setObjectName("export_button_pie_chart")
		self.export_button_pie_chart.setText('Export')
		self.gridLayout_10.addWidget(self.export_button_pie_chart, 9, 0, 1, 1)

		'''END PieChart CHECKBOXES'''

		# pie chart addition
		self.pie_chart_scroll_area.setWidget(self.pie_chart_graph)
		self.gridLayout_10.addWidget(self.pie_chart_scroll_area, 0, 1, 9, 1)
		self.visualization_tabs.addTab(self.pie_chart, "")

		#Checkbox Methods
		self.pie_tab_all_artifacts_checkbox.clicked.connect(self.update_pie_chart_graph)
		self.pie_tab_screenshot_checkbox.clicked.connect(self.update_pie_chart_graph)
		self.pie_tab_video_checkbox.clicked.connect(self.update_pie_chart_graph)
		self.pie_tab_network_checkbox.clicked.connect(self.update_pie_chart_graph)
		self.pie_tab_process_checkbox.clicked.connect(self.update_pie_chart_graph)
		self.pie_tab_keystroke_checkbox.clicked.connect(self.update_pie_chart_graph)
		self.pie_tab_mouse_action_checkbox.clicked.connect(self.update_pie_chart_graph)
		self.pie_tab_system_call_checkbox.clicked.connect(self.update_pie_chart_graph)
		self.pie_tab_window_history_checkbox.clicked.connect(self.update_pie_chart_graph)

		self.artifacts_pie_data = [(screenshot_data,self.pie_tab_screenshot_checkbox), (video_data,self.pie_tab_video_checkbox),
		(network_data, self.pie_tab_network_checkbox), (process_data, self.pie_tab_process_checkbox),
		(keystroke_data,self.pie_tab_keystroke_checkbox),(mouse_action_data,self.pie_tab_mouse_action_checkbox),
		(window_history_data,self.pie_tab_window_history_checkbox), (system_call_data,self.pie_tab_system_call_checkbox)]


		''' Bar Graph Tab '''

		self.bar_graph_class = BarGraph()
		self.bar_graph_class.add_bar_graph(bar_graph_artifact_data)
		self.bar_graph_diagram = self.bar_graph_class.get_chart_view()

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

		''' Bar Graph Checkboxes '''
		self.label_bar_graph_all = QtWidgets.QLabel()
		self.label_bar_graph_all.setObjectName("label_bar_graph_all")
		self.gridLayout_37.addWidget(self.label_bar_graph_all, 0, 0, 1, 1)
		self.bar_tab_all_artifacts_checkbox = QtWidgets.QCheckBox()
		self.bar_tab_all_artifacts_checkbox.setText("All Artifacts")
		self.bar_tab_all_artifacts_checkbox.setObjectName("bar_tab_all_artifacts_checkbox")
		self.bar_tab_all_artifacts_checkbox.setChecked(True)
		self.bar_tab_all_artifacts_checkbox.clicked.connect(self.check_bar_graph_boxes)
		self.gridLayout_37.addWidget(self.bar_tab_all_artifacts_checkbox, 0, 0, 1, 1)

		self.label_bar_graph_screenshot = QtWidgets.QLabel()
		self.label_bar_graph_screenshot.setObjectName("label_bar_graph_screenshot")
		self.gridLayout_37.addWidget(self.label_bar_graph_screenshot, 1, 0, 1, 1)
		self.bar_tab_screenshot_checkbox = QtWidgets.QCheckBox()
		self.bar_tab_screenshot_checkbox.setText("Screenshots")
		self.bar_tab_screenshot_checkbox.setChecked(True)
		self.bar_tab_screenshot_checkbox.setObjectName("bar_tab_screenshot_checkbox")
		self.gridLayout_37.addWidget(self.bar_tab_screenshot_checkbox, 1, 0, 1, 1)

		self.label_bar_graph_video = QtWidgets.QLabel()
		self.label_bar_graph_video.setObjectName("label_bar_graph_video")
		self.gridLayout_37.addWidget(self.label_bar_graph_video, 2, 0, 1, 1)
		self.bar_tab_video_checkbox = QtWidgets.QCheckBox()
		self.bar_tab_video_checkbox.setText("Videos")
		self.bar_tab_video_checkbox.setChecked(True)
		self.bar_tab_video_checkbox.setObjectName("bar_tab_video_checkbox")
		self.gridLayout_37.addWidget(self.bar_tab_video_checkbox, 2, 0, 1, 1)

		self.label_bar_graph_network = QtWidgets.QLabel()
		self.label_bar_graph_network.setObjectName("label_bar_graph_network")
		self.gridLayout_37.addWidget(self.label_bar_graph_network, 3, 0, 1, 1)
		self.bar_tab_network_checkbox = QtWidgets.QCheckBox()
		self.bar_tab_network_checkbox.setText("Network Data")
		self.bar_tab_network_checkbox.setChecked(True)
		self.bar_tab_network_checkbox.setObjectName("bar_tab_network_checkbox")
		self.gridLayout_37.addWidget(self.bar_tab_network_checkbox, 3, 0, 1, 1)

		self.label_bar_graph_process = QtWidgets.QLabel()
		self.label_bar_graph_process.setObjectName("label_bar_graph_process")
		self.gridLayout_37.addWidget(self.label_bar_graph_process, 4, 0, 1, 1)
		self.bar_tab_process_checkbox = QtWidgets.QCheckBox()
		self.bar_tab_process_checkbox.setText("Processes")
		self.bar_tab_process_checkbox.setChecked(True)
		self.bar_tab_process_checkbox.setObjectName("bar_tab_process_checkbox")
		self.gridLayout_37.addWidget(self.bar_tab_process_checkbox, 4, 0, 1, 1)

		self.label_bar_graph_keystroke = QtWidgets.QLabel()
		self.label_bar_graph_keystroke.setObjectName("label_bar_graph_keystroke")
		self.gridLayout_37.addWidget(self.label_bar_graph_keystroke, 5, 0, 1, 1)
		self.bar_tab_keystroke_checkbox = QtWidgets.QCheckBox()
		self.bar_tab_keystroke_checkbox.setText("Keystrokes")
		self.bar_tab_keystroke_checkbox.setChecked(True)
		self.bar_tab_keystroke_checkbox.setObjectName("bar_tab_keystroke_checkbox")
		self.gridLayout_37.addWidget(self.bar_tab_keystroke_checkbox, 5, 0, 1, 1)

		self.label_bar_graph_mouse_action = QtWidgets.QLabel()
		self.label_bar_graph_mouse_action.setObjectName("label_bar_graph_mouse_action")
		self.gridLayout_37.addWidget(self.label_bar_graph_video, 6, 0, 1, 1)
		self.bar_tab_mouse_action_checkbox = QtWidgets.QCheckBox()
		self.bar_tab_mouse_action_checkbox.setText("Mouse Actions")
		self.bar_tab_mouse_action_checkbox.setChecked(True)
		self.bar_tab_mouse_action_checkbox.setObjectName("bar_tab_mouse_action_checkbox")
		self.gridLayout_37.addWidget(self.bar_tab_mouse_action_checkbox, 6, 0, 1, 1)

		self.label_bar_graph_window_history = QtWidgets.QLabel()
		self.label_bar_graph_window_history.setObjectName("label_bar_graph_window_history")
		self.gridLayout_37.addWidget(self.label_bar_graph_window_history, 7, 0, 1, 1)
		self.bar_tab_window_history_checkbox = QtWidgets.QCheckBox()
		self.bar_tab_window_history_checkbox.setText("Window History")
		self.bar_tab_window_history_checkbox.setChecked(True)
		self.bar_tab_window_history_checkbox.setObjectName("bar_tab_window_history_checkbox")
		self.gridLayout_37.addWidget(self.bar_tab_window_history_checkbox, 7, 0, 1, 1)

		self.label_bar_graph_system_call = QtWidgets.QLabel()
		self.label_bar_graph_system_call.setObjectName("label_bar_graph_system_call")
		self.gridLayout_37.addWidget(self.label_bar_graph_system_call, 8, 0, 1, 1)
		self.bar_tab_system_call_checkbox = QtWidgets.QCheckBox()
		self.bar_tab_system_call_checkbox.setText("System Calls")
		self.bar_tab_system_call_checkbox.setChecked(True)
		self.bar_tab_system_call_checkbox.setObjectName("bar_tab_system_call_checkbox")
		self.gridLayout_37.addWidget(self.bar_tab_system_call_checkbox, 8, 0, 1, 1)

		self.export_button_bar_graph = QtWidgets.QPushButton()
		self.export_button_bar_graph.setObjectName("export_button_bar_graph")
		self.export_button_bar_graph.setText('Export')
		self.gridLayout_37.addWidget(self.export_button_bar_graph, 9, 0, 1, 1)
		'''End Bar Graph Checkboxes'''


		# bar graph addition
		self.Bar_Graph_Area_123.setWidget(self.bar_graph_diagram)
		self.gridLayout_37.addWidget(self.Bar_Graph_Area_123, 0, 1, 9, 1)
		self.visualization_tabs.addTab(self.bar_graph, "")

		#Bar Graph Methods
		self.bar_tab_all_artifacts_checkbox.clicked.connect(self.update_bar_graph_graph)
		self.bar_tab_screenshot_checkbox.clicked.connect(self.update_bar_graph_graph)
		self.bar_tab_video_checkbox.clicked.connect(self.update_bar_graph_graph)
		self.bar_tab_network_checkbox.clicked.connect(self.update_bar_graph_graph)
		self.bar_tab_process_checkbox.clicked.connect(self.update_bar_graph_graph)
		self.bar_tab_keystroke_checkbox.clicked.connect(self.update_bar_graph_graph)
		self.bar_tab_mouse_action_checkbox.clicked.connect(self.update_bar_graph_graph)
		self.bar_tab_system_call_checkbox.clicked.connect(self.update_bar_graph_graph)
		self.bar_tab_window_history_checkbox.clicked.connect(self.update_bar_graph_graph)

		self.artifacts_bar_data = [ (bar_graph_artifact_data[0],self.bar_tab_screenshot_checkbox), (bar_graph_artifact_data[1],self.bar_tab_video_checkbox),
		(bar_graph_artifact_data[2], self.bar_tab_network_checkbox), (bar_graph_artifact_data[3], self.bar_tab_process_checkbox),
		(bar_graph_artifact_data[4],self.bar_tab_keystroke_checkbox),(bar_graph_artifact_data[5],self.bar_tab_mouse_action_checkbox),
		(bar_graph_artifact_data[6],self.bar_tab_window_history_checkbox), (bar_graph_artifact_data[7],self.bar_tab_system_call_checkbox)]



		''' Timeline Tab '''
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
		self.line_2.setStyleSheet("background-color: rgb(170, 0, 0);\n" "border-color: rgb(170, 0, 0);")
		self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.line_3 = QtWidgets.QFrame(self.frame_3)
		self.line_3.setGeometry(QtCore.QRect(70, 0, 3, 61))
		self.line_3.setStyleSheet("background-color: rgb(170, 0, 0);\n" "border-color: rgb(170, 0, 0);")
		self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_3.setObjectName("line_3")
		self.line_5 = QtWidgets.QFrame(self.frame_3)
		self.line_5.setGeometry(QtCore.QRect(230, 0, 3, 61))
		self.line_5.setStyleSheet("background-color: rgb(170, 0, 0);\n" "border-color: rgb(170, 0, 0);")
		self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_5.setObjectName("line_5")
		self.line_6 = QtWidgets.QFrame(self.frame_3)
		self.line_6.setGeometry(QtCore.QRect(280, 60, 3, 61))
		self.line_6.setStyleSheet("background-color: rgb(170, 0, 0);\n" "border-color: rgb(170, 0, 0);")
		self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_6.setObjectName("line_6")
		self.line_7 = QtWidgets.QFrame(self.frame_3)
		self.line_7.setGeometry(QtCore.QRect(340, 0, 3, 61))
		self.line_7.setStyleSheet(
			"background-color: rgb(170, 0, 0);\n" "border-color: rgb(170, 0, 0);")
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
		#self.label_91.setText(_translate("MainWindow", "Title"))
		#self.label_90.setText(_translate("MainWindow", "Pie Chart Metadata"))
		#self.label_92.setText(_translate("MainWindow", "Visualization Result"))
		#self.label_93.setText(_translate("MainWindow", "Pie Chart Title"))
		self.visualization_tabs.setTabText(self.visualization_tabs.indexOf(
			self.pie_chart), _translate("MainWindow", "Pie Chart"))
		self.visualization_tabs.setTabText(self.visualization_tabs.indexOf(
			self.bar_graph), _translate("MainWindow", "Bar Graph"))
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
		self.visualization_tabs.setTabText(
			self.visualization_tabs.indexOf(self.timeline), _translate("MainWindow", "Timeline"))

	def get_accordion(self):
		return self.visualization_accordion

	def check_pie_chart_boxes(self):
		on = self.pie_tab_all_artifacts_checkbox.isChecked()

		self.pie_tab_video_checkbox.setChecked(on)
		self.pie_tab_video_checkbox.setChecked(on)
		self.pie_tab_network_checkbox.setChecked(on)
		self.pie_tab_process_checkbox.setChecked(on)
		self.pie_tab_keystroke_checkbox.setChecked(on)
		self.pie_tab_screenshot_checkbox.setChecked(on)
		self.pie_tab_system_call_checkbox.setChecked(on)
		self.pie_tab_mouse_action_checkbox.setChecked(on)
		self.pie_tab_window_history_checkbox.setChecked(on)

	def check_bar_graph_boxes(self):
	  on = self.bar_tab_all_artifacts_checkbox.isChecked()

	  self.bar_tab_video_checkbox.setChecked(on)
	  self.bar_tab_video_checkbox.setChecked(on)
	  self.bar_tab_network_checkbox.setChecked(on)
	  self.bar_tab_process_checkbox.setChecked(on)
	  self.bar_tab_keystroke_checkbox.setChecked(on)
	  self.bar_tab_screenshot_checkbox.setChecked(on)
	  self.bar_tab_system_call_checkbox.setChecked(on)
	  self.bar_tab_mouse_action_checkbox.setChecked(on)
	  self.bar_tab_window_history_checkbox.setChecked(on)

	def update_pie_chart_graph(self):
		#artifact[0] is the slices
		#artifactt[1] is the checkboxes
		for artifact in self.artifacts_pie_data:
			if (artifact[1].isChecked()):
				if not(artifact[0] in artifact_data):
					self.pie_chart_class.series.append(artifact[0])
					artifact_data.append(artifact[0])
			else:
				if (artifact[0] in artifact_data):
					artifact_data.remove(artifact[0])
					self.pie_chart_class.series.take(artifact[0])


	def update_bar_graph_graph(self):
		#artifact[0] is the slices
		#artifactt[1] is the checkboxes
		for artifact in self.artifacts_bar_data:
			if (artifact[1].isChecked()):
				if not(artifact[0] in artifact_data):
					self.bar_graph_class.series.append(artifact[0])
					artifact_data.append(artifact[0])
			else:
				if (artifact[0] in artifact_data):
					artifact_data.remove(artifact[0])
					self.bar_graph_class.series.take(artifact[0])
