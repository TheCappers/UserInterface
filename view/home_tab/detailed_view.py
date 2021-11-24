from PyQt5 import QtWidgets, QtCore
from view.components import annotation_table, tag_table
from view.components.description import Description
from view.home_tab import process_interface

global tag_table
all_selected_tag = []


class DetailedView:
    def __init__(self):
        self.detailed_view_accordion = QtWidgets.QWidget()
        self.detailed_view_accordion.setGeometry(QtCore.QRect(0, 0, 1204, 535))
        self.detailed_view_accordion.setObjectName("detailed_view_accordion")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(
            self.detailed_view_accordion)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.DetailedViewScroll = QtWidgets.QScrollArea(
            self.detailed_view_accordion)
        self.DetailedViewScroll.setWidgetResizable(True)
        self.DetailedViewScroll.setObjectName("DetailedViewScroll")

        self.scrollAreaWidgetContents_58 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_58.setGeometry(
            QtCore.QRect(0, 0, 1176, 523))
        self.scrollAreaWidgetContents_58.setObjectName(
            "scrollAreaWidgetContents_58")
        self.gridLayout_21 = QtWidgets.QGridLayout(
            self.scrollAreaWidgetContents_58)
        self.gridLayout_21.setObjectName("gridLayout_21")

        self.DetailedViewTab = QtWidgets.QTabWidget(
            self.scrollAreaWidgetContents_58)
        self.DetailedViewTab.setMinimumSize(QtCore.QSize(0, 0))
        self.DetailedViewTab.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.DetailedViewTab.setObjectName("DetailedViewTab")
        self.tab_133 = QtWidgets.QWidget()
        self.tab_133.setObjectName("tab_133")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.tab_133)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.scrollArea_54 = QtWidgets.QScrollArea(self.tab_133)
        self.scrollArea_54.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_54.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea_54.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_54.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_54.setWidgetResizable(True)
        self.scrollArea_54.setObjectName("scrollArea_54")
        self.scrollAreaWidgetContents_59 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_59.setGeometry(
            QtCore.QRect(0, 0, 1128, 454))
        self.scrollAreaWidgetContents_59.setObjectName(
            "scrollAreaWidgetContents_59")
        self.gridLayout_22 = QtWidgets.QGridLayout(
            self.scrollAreaWidgetContents_59)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.tableWidget_38 = QtWidgets.QTableWidget(
            self.scrollAreaWidgetContents_59)
        self.tableWidget_38.setObjectName("tableWidget_38")
        self.tableWidget_38.setColumnCount(2)
        self.tableWidget_38.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_38.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_38.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_38.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_38.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_38.setItem(0, 1, item)
        self.tableWidget_38.horizontalHeader().setDefaultSectionSize(400)
        self.tableWidget_38.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_38.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_22.addWidget(self.tableWidget_38, 0, 0, 1, 1)
        self.scrollArea_54.setWidget(self.scrollAreaWidgetContents_59)
        self.gridLayout_23.addWidget(self.scrollArea_54, 0, 0, 1, 1)

        self.DetailedViewTab.addTab(self.tab_133, "")

        self.tab_134 = Description()
        self.DetailedViewTab.addTab(self.tab_134.get_tab(), "")

        '''
        testing
        '''
        # self.widget_2 = QtWidgets.QWidget(self.tab_134.get_tab())
        # self.widget_2.setObjectName("widget_2")
        # self.tab_134.gridLayout_24.addWidget(self.widget_2, 0, 0, 1, 1)

        ''' ANNOTATION TAB  '''
        self.AnnotationTab = QtWidgets.QWidget()
        self.AnnotationTab.setObjectName("AnnotationTab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.AnnotationTab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        """ ANNNOTATIONTA """
        global annotation_table
        annotation_table = annotation_table.AnnotationTable()
        annotation_table.startTable(QtWidgets.QTableWidget(self.AnnotationTab))
        self.annotation_table = annotation_table

        self.verticalLayout_6.addWidget(annotation_table.getTable())
        self.annotation_text = QtWidgets.QTextEdit(self.AnnotationTab)
        self.annotation_text.setObjectName("annotation_text")
        self.verticalLayout_6.addWidget(self.annotation_text)
        self.pushButton_18 = QtWidgets.QPushButton(self.AnnotationTab)
        self.pushButton_18.setObjectName("pushButton_18")
        self.verticalLayout_6.addWidget(
            self.pushButton_18, 0, QtCore.Qt.AlignLeft)
        self.DetailedViewTab.addTab(self.AnnotationTab, "")

        ''' TAGS TAB '''
        self.tags_tab = QtWidgets.QWidget()
        self.tags_tab.setObjectName("tags_tab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tags_tab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        ''' TAG TABLE '''
        global tag_table
        tag_table = tag_table.TagTable()
        tag_table.startTable(QtWidgets.QTableWidget(self.tags_tab))
        self.tag_table = tag_table
        # self.tag_table.cellClicked.connect(self.exportRow)

        ''' TAG TABLE START '''
        self.verticalLayout_7.addWidget(tag_table.getTable())
        self.frame_11 = QtWidgets.QFrame(self.tags_tab)
        self.frame_11.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_11.setMaximumSize(QtCore.QSize(400, 50))
        self.frame_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        ''' ADD TAG TEXT BOX '''
        self.tag_input = QtWidgets.QLineEdit(self.tags_tab)
        self.tag_input.setClearButtonEnabled(False)
        self.tag_input.setObjectName("tag_input")
        self.horizontalLayout_2.addWidget(self.tag_input)

        self.tag_add_button = QtWidgets.QPushButton(self.frame_11)
        self.tag_add_button.setObjectName("tag_add_button")
        self.horizontalLayout_2.addWidget(self.tag_add_button)
        self.tag_delete_button = QtWidgets.QPushButton(self.frame_11)
        self.tag_delete_button.setObjectName("tag_delete_button")
        self.horizontalLayout_2.addWidget(self.tag_delete_button)

        self.verticalLayout_7.addWidget(self.frame_11)
        self.frame_9 = QtWidgets.QFrame(self.tags_tab)
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.verticalLayout_7.addWidget(self.frame_9)
        self.DetailedViewTab.addTab(self.tags_tab, "")
        self.gridLayout_21.addWidget(self.DetailedViewTab, 0, 0, 1, 1)
        self.DetailedViewScroll.setWidget(self.scrollAreaWidgetContents_58)
        self.verticalLayout_31.addWidget(self.DetailedViewScroll)

        """retranslateUi"""
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidget_38.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "User"))
        item = self.tableWidget_38.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "IP Address"))
        item = self.tableWidget_38.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "MAC Address"))
        __sortingEnabled = self.tableWidget_38.isSortingEnabled()
        self.tableWidget_38.setSortingEnabled(False)
        item = self.tableWidget_38.item(0, 0)
        item.setText(_translate("MainWindow", "192.111.222.16"))
        item = self.tableWidget_38.item(0, 1)
        item.setText(_translate("MainWindow", "AA:BB:CCC"))
        self.tableWidget_38.setSortingEnabled(__sortingEnabled)

        # process = process_interface.ProcessInterface()
        # process.start_table(self.tab_134.get_tab())

        self.DetailedViewTab.setTabText(
            self.DetailedViewTab.indexOf(
                self.tab_133), _translate(
                "MainWindow", "User Profile"))

        self.DetailedViewTab.setTabText(
            self.DetailedViewTab.indexOf(
                self.tab_134.get_tab()), _translate(
                "MainWindow", "Description"))

        self.annotation_text.setPlaceholderText(
            _translate("MainWindow", "Annotation"))
        self.pushButton_18.setText(_translate("MainWindow", "Add"))
        self.DetailedViewTab.setTabText(
            self.DetailedViewTab.indexOf(
                self.AnnotationTab), _translate(
                "MainWindow", "Annotation"))

        self.tag_input.setPlaceholderText(_translate("MainWindow", "Tag"))
        self.tag_add_button.setText(_translate("MainWindow", "Add"))
        self.tag_delete_button.setText(_translate("MainWindow", "Delete"))
        self.DetailedViewTab.setTabText(
            self.DetailedViewTab.indexOf(
                self.tags_tab), _translate(
                "MainWindow", "Tags"))
        # self.tag_table.tag_table.cellClicked.connect(self.exportRow)

    def get_accordion(self):
        return self.detailed_view_accordion

    def exportRow(self, index):
        # print("THIS IS exportRow")
        if index not in all_selected_tag:
            self.tag_table.setIndexSelected(index)
            all_selected_tag.append(index)
        else:
            all_selected_tag.remove(index)
            selected = None

    def clearSelectedTags(self):
        global all_selected_tag
        all_selected_tag = []
