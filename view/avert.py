# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AvertUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from view.components import annotation_table
from view.home_tab.home import Home
from view.configuration_tab.configuration import Configuration
from view.sync_tab.sync import Sync

table_result = None
all_selected = []
selected = None
attain = []


class Ui_MainWindow():
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1272, 835)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")

        """tab_1 start"""
        self.tab_1 = Home()
        self.tabWidget.addTab(self.tab_1.get_tab(), "HOME")
        self.tab_1.table_result.avert_result_table.cellClicked.connect(self.exportRow)
        """tab_1 end"""

        """tab_2 start"""
        self.tab_2 = Configuration()
        self.tabWidget.addTab(self.tab_2.get_tab(), "Configuration")
        """tab_2 end"""

        """tab_3 start"""
        self.tab_3 = Sync()
        self.tabWidget.addTab(self.tab_3.get_tab(), "Sync")
        """tab_3 end"""

        self.gridLayout_20.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1272, 24))
        self.menubar.setObjectName("menubar")
        self.menuAVERT = QtWidgets.QMenu(self.menubar)
        self.menuAVERT.setObjectName("menuAVERT")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuAVERT.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        # self.DetailedViewTab.setCurrentIndex(0)
        # self.description_tab.setCurrentIndex(0)
        # self.toolBox.setCurrentIndex(0)
        # self.visualization_tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AVERT"))

        self.menuAVERT.setTitle(_translate("MainWindow", "AVERT"))

        """COMMENTING OUT UI MODIFICATION"""

    def updateTable(self, attain):
        self.tab_1.table_result.populateTable(attain)
        # self.verticalLayout_3.addWidget(table_result.getTable()) si jala
        # print(attain)

    def getResultTable(self):
        global table_result
        return table_result

    def exportRow(self, index):
        global selected
        if index not in all_selected:
            all_selected.append(index)
            selected = index
            self.changeDetailView(selected)
        else:
            all_selected.remove(index)
            selected = None

    def updateTable(self, attain1):
        global attain
        attain = attain1
        self.tab_1.table_result.populateTable(attain)

    def changeDetailView(self, selected):
        _translate = QtCore.QCoreApplication.translate
        global attain
        curdata = attain[selected]
        item = self.tab_1.detailed_view_accordion.tableWidget_38.item(0, 0)
        item.setText(_translate("MainWindow", curdata['ip_address']))
        item = self.tab_1.detailed_view_accordion.tableWidget_38.item(0, 1)
        item.setText(_translate("MainWindow", curdata['mac_address']))
