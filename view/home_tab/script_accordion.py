from PyQt5 import QtWidgets, QtCore, QtGui
from view.components import result_table, annotation_table, bar_graph


class Script_Accordion:
    def __init__(self):
        self.accordion = ""
        self.script_items = []

    def startAccordion(self):
        _translate = QtCore.QCoreApplication.translate
        self.accordion = QtWidgets.QWidget()
        self.accordion.setGeometry(QtCore.QRect(0, 0, 548, 197))
        self.accordion.setObjectName("script_accordion")
        self.verticallayout = QtWidgets.QVBoxLayout(self.accordion)
        self.verticallayout.setObjectName("script_verticallayout")

        # Script Table Content Area BEGIN
        self.table = QtWidgets.QTableWidget(self.accordion)
        self.table.setAcceptDrops(False)
        self.table.setEditTriggers(
            QtWidgets.QAbstractItemView.AnyKeyPressed | QtWidgets.QAbstractItemView.DoubleClicked)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.setCornerButtonEnabled(True)
        self.table.setRowCount(0)
        self.table.setObjectName("table")
        self.table.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        item.setText(_translate("MainWindow", "Select"))
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText(_translate("MainWindow", "Added Artifact"))
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText(_translate("MainWindow", "Time Stamp"))
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText(_translate("MainWindow", "Artifact Type"))
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText(_translate("MainWindow", "Tag"))
        self.table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText(_translate("MainWindow", "MAC Address"))
        self.table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText(_translate("MainWindow", "Description"))
        self.table.setHorizontalHeaderItem(6, item)

        self.table.horizontalHeader().setCascadingSectionResizes(True)
        self.table.horizontalHeader().setDefaultSectionSize(150)
        self.table.horizontalHeader().setMinimumSectionSize(20)
        self.table.horizontalHeader().setSortIndicatorShown(True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setCascadingSectionResizes(True)
        self.table.verticalHeader().setSortIndicatorShown(True)
        # Script Table Content Area END

        # Script Button Content Area START
        self.verticallayout.addWidget(self.table)
        self.pushbutton_frame = QtWidgets.QFrame(self.accordion)
        self.pushbutton_frame.setMaximumSize(QtCore.QSize(16777215, 111))
        self.pushbutton_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pushbutton_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pushbutton_frame.setObjectName("script_pushbutton_frame")
        self.pushbutton_gridlayout = QtWidgets.QGridLayout(self.pushbutton_frame)
        self.pushbutton_gridlayout.setObjectName("script_pushbutton_gridlayout")
        self.moveup_btn = QtWidgets.QPushButton(self.pushbutton_frame)
        self.moveup_btn.setObjectName("script_moveup_btn")
        self.moveup_btn.setText(_translate("MainWindow", "Up"))
        self.pushbutton_gridlayout.addWidget(self.moveup_btn, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.movedown_btn = QtWidgets.QPushButton(self.pushbutton_frame)
        self.movedown_btn.setObjectName("script_movedown_btn")
        self.movedown_btn.setText(_translate("MainWindow", "Down"))

        self.pushbutton_gridlayout.addWidget(self.movedown_btn, 0, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.remove_btn = QtWidgets.QPushButton(self.pushbutton_frame)
        self.remove_btn.setObjectName("script_remove_btn")
        self.remove_btn.setText(_translate("MainWindow", "Remove"))

        self.pushbutton_gridlayout.addWidget(self.remove_btn, 0, 2, 1, 1, QtCore.Qt.AlignLeft)
        self.generate_btn = QtWidgets.QPushButton(self.pushbutton_frame)
        self.generate_btn.setObjectName("script_generate_btn")
        self.generate_btn.setText(_translate("MainWindow", "Generate"))
        self.pushbutton_gridlayout.addWidget(self.generate_btn, 0, 3, 1, 1, QtCore.Qt.AlignLeft)
        self.export_btn = QtWidgets.QPushButton(self.pushbutton_frame)
        self.export_btn.setObjectName("script_export_btn")
        self.export_btn.setText(_translate("MainWindow", "Export"))
        self.pushbutton_gridlayout.addWidget(self.export_btn, 0, 4, 1, 1, QtCore.Qt.AlignLeft)
        self.preview_btn = QtWidgets.QPushButton(self.pushbutton_frame)
        self.preview_btn.setObjectName("script_preview_btn")
        self.preview_btn.setText(_translate("MainWindow", "Preview"))
        self.pushbutton_gridlayout.addWidget(self.preview_btn, 0, 5, 1, 1, QtCore.Qt.AlignLeft)
        self.moveup_text = QtWidgets.QPlainTextEdit(self.pushbutton_frame)
        self.moveup_text.setReadOnly(True)
        self.moveup_text.setBackgroundVisible(False)
        self.moveup_text.setObjectName("script_moveup_text")
        self.moveup_text.setPlainText(_translate("MainWindow", "Move Artifact Up"))
        self.pushbutton_gridlayout.addWidget(self.moveup_text, 1, 0, 1, 1)
        self.movedown_text = QtWidgets.QPlainTextEdit(self.pushbutton_frame)
        self.movedown_text.setReadOnly(True)
        self.movedown_text.setObjectName("script_movedown_text")
        self.movedown_text.setPlainText(_translate("MainWindow", "Move Artifact Down"))
        self.pushbutton_gridlayout.addWidget(self.movedown_text, 1, 1, 1, 1)
        self.remove_text = QtWidgets.QPlainTextEdit(self.pushbutton_frame)
        self.remove_text.setReadOnly(True)
        self.remove_text.setObjectName("script_remove_text")
        self.remove_text.setPlainText(_translate("MainWindow", "Remove Artifact from Script Creation Table"))
        self.pushbutton_gridlayout.addWidget(self.remove_text, 1, 2, 1, 1)
        self.generate_text = QtWidgets.QPlainTextEdit(self.pushbutton_frame)
        self.generate_text.setReadOnly(True)
        self.generate_text.setObjectName("script_generate_text")
        self.generate_text.setPlainText(_translate("MainWindow", "Generate Script"))
        self.pushbutton_gridlayout.addWidget(self.generate_text, 1, 3, 1, 1)
        self.export_text = QtWidgets.QPlainTextEdit(self.pushbutton_frame)
        self.export_text.setReadOnly(True)
        self.export_text.setObjectName("script_export_text")
        self.export_text.setPlainText(_translate("MainWindow", "Export Script"))
        self.pushbutton_gridlayout.addWidget(self.export_text, 1, 4, 1, 1)
        self.preview_text = QtWidgets.QPlainTextEdit(self.pushbutton_frame)
        self.preview_text.setReadOnly(True)
        self.preview_text.setObjectName("script_preview_text")
        self.preview_text.setPlainText(_translate("MainWindow", "Generate Script Preview Window"))
        self.pushbutton_gridlayout.addWidget(self.preview_text, 1, 5, 1, 1)
        self.verticallayout.addWidget(self.pushbutton_frame)
        # Script Button content Area END

        __sortingEnabled = self.table.isSortingEnabled()
        self.table.setSortingEnabled(False)
        self.table.setSortingEnabled(__sortingEnabled)

    def get_accordion(self):
        return self.accordion

    def populateTable(self, selected_items, isAllChecked):
        if isAllChecked:
            #  print("NOT SELECTED ALL")
            return
        else:
            print("SELECT ALL!")
        _translate = QtCore.QCoreApplication.translate
        print("THIS IS populateTable")
        # print(selected_items)

        isChanged = False

        for d in selected_items:
            if not d in self.script_items:
                self.script_items.append(d)
                isChanged = True

        if isChanged:
            #  print("SET CHANGED")
            self.table.setRowCount(len(self.script_items))
            i = 0
            for d in self.script_items:
                item = QtWidgets.QTableWidgetItem()
                item.setCheckState(QtCore.Qt.Unchecked)
                self.table.setItem(i, 0, item)

                item = QtWidgets.QTableWidgetItem()
                # item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item.setText(_translate("MainWindow", 'data'))
                self.table.setItem(i, 1, item)

                item = QtWidgets.QTableWidgetItem()
                # item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item.setText(_translate("MainWindow", d['timestamp']))
                self.table.setItem(i, 2, item)

                item = QtWidgets.QTableWidgetItem()
                # item.setFlags(QtCore.Qt.ItemIsSelectable)
                item.setText(_translate("MainWindow", d['name']))
                self.table.setItem(i, 3, item)

                item = QtWidgets.QTableWidgetItem()
                # item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled)
                item.setText(_translate("MainWindow", ' '.join(d['tag'])))
                self.table.setItem(i, 4, item)

                item = QtWidgets.QTableWidgetItem()
                # item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item.setText(_translate("MainWindow", d['mac_address']))
                self.table.setItem(i, 5, item)

                item = QtWidgets.QTableWidgetItem()
                # item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                # ### What is description???
                item.setText(_translate("MainWindow", "description?"))
                self.table.setItem(i, 6, item)
                i += 1

    def getScriptItems(self):
        return self.script_items
