from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QInputDialog

import avert
from avert import Ui_MainWindow

import sys


class SectionExpandButton(QPushButton):
    """a QPushbutton that can expand or collapse its section
    """
    def __init__(self, item, text = "", parent = None):
        super().__init__(text, parent)
        self.section = item
        self.clicked.connect(self.on_clicked)

    def on_clicked(self):
        """toggle expand/collapse of section by clicking
        """
        if self.section.isExpanded():
            self.section.setExpanded(False)
        else:
            self.section.setExpanded(True)

class AvertApp(QtWidgets.QMainWindow, avert.Ui_MainWindow):
    def __init__(self):
        super(AvertApp, self).__init__()
        self.setupUi(self)

        # portion for the tag_table
        self.table_tag.setSortingEnabled(1) # allows for the sorting in the columns

        # portion needed for the accordion view
        self.tree = QtWidgets.QTreeWidget()
        self.tree.setHeaderHidden(True)
        self.sections = []
        self.define_sections()
        self.add_sections()

        self.VideoStatOnButton.clicked.connect(self.toggleButtons)
        self.VideoStatusOffButton.clicked.connect(self.toggleButtons)
        self.ScreenshotStatOnButton.clicked.connect(self.toggleButtons)
        self.ScreenshotStatOffButton.clicked.connect(self.toggleButtons)
        self.SystemCallOnButton.clicked.connect(self.toggleButtons)
        self.SystemCallOffButton.clicked.connect(self.toggleButtons)
        self.WindowHistoryOnButton.clicked.connect(self.toggleButtons)
        self.WindowHistoryOffButton.clicked.connect(self.toggleButtons)
        self.KeyStrokeStatOnButton.clicked.connect(self.toggleButtons)
        self.KeyStrokeStatOffButton.clicked.connect(self.toggleButtons)
        self.MouseActOnButton.clicked.connect(self.toggleButtons)
        self.MouseActOffButton.clicked.connect(self.toggleButtons)
        self.NetworkActivityDataOnButton.clicked.connect(self.toggleButtons)
        self.NetworkActivityDataOffButton.clicked.connect(self.toggleButtons)
        self.ProcessStatOnButton.clicked.connect(self.toggleButtons)
        self.ProcessStatOffButton.clicked.connect(self.toggleButtons)

    # button toggle method
    '''
    Author: David Amparan Date: 9/7/2021
    Purpose: Allow recording status buttons (on and off) as a toggle buttons
    meaning when one is pressed it stays down and when the other is pressed it stays down 
    while the other one pops up
    '''

    def toggleButtons(self):  # called upon by button automatically will know which button

        if self.sender().objectName().__contains__("Video") and self.sender().objectName().__contains__('On'):
            self.VideoStatOnButton.setChecked(1)  # check the button we clicked
            self.VideoStatusOffButton.setChecked(0)  # check false the off button incase it is checked

        if self.sender().objectName().__contains__("Video") and self.sender().objectName().__contains__('off'):
            self.VideoStatOnButton.setChecked(0)  # check off the on button
            self.VideoStatusOffButton.setChecked(1)  # check on the off button

        if self.sender().objectName().__contains__("Screenshot") and self.sender().objectName().__contains__('On'):
            self.ScreenshotStatOnButton.setChecked(1)  # check the button we clicked
            self.ScreenshotStatOffButton.setChecked(0)  # check false the off button incase it is checked

        if self.sender().objectName().__contains__("Screenshot") and self.sender().objectName().__contains__('Off'):
            self.ScreenshotStatOnButton.setChecked(0)  # check off the on button
            self.ScreenshotStatOffButton.setChecked(1)  # check on the off button

        if self.sender().objectName().__contains__("Sys") and self.sender().objectName().__contains__('On'):
            self.SystemCallOnButton.setChecked(1)  # check the button we clicked
            self.SystemCallOffButton.setChecked(0)  # check false the off button incase it is checked

        if self.sender().objectName().__contains__("Sys") and self.sender().objectName().__contains__('Off'):
            self.SystemCallOnButton.setChecked(0)  # check off the on button
            self.SystemCallOffButton.setChecked(1)  # check on the off button

        if self.sender().objectName().__contains__("Win") and self.sender().objectName().__contains__('On'):
            self.WindowHistoryOnButton.setChecked(1)  # check the button we clicked
            self.WindowHistoryOffButton.setChecked(0)  # check false the off button incase it is checked

        if self.sender().objectName().__contains__("Win") and self.sender().objectName().__contains__('Off'):
            self.WindowHistoryOnButton.setChecked(0)  # check off the on button
            self.WindowHistoryOffButton.setChecked(1)  # check on the off button

        if self.sender().objectName().__contains__("KeyStroke") and self.sender().objectName().__contains__('On'):
            self.KeyStrokeStatOnButton.setChecked(1)  # check the button we clicked
            self.KeyStrokeStatOffButton.setChecked(0)  # check false the off button incase it is checked

        if self.sender().objectName().__contains__("KeyStroke") and self.sender().objectName().__contains__('Off'):
            self.KeyStrokeStatOnButton.setChecked(0)  # check off the on button
            self.KeyStrokeStatOffButton.setChecked(1)  # check on the off button

        if self.sender().objectName().__contains__("Mouse") and self.sender().objectName().__contains__('On'):
            self.MouseActOnButton.setChecked(1)  # check the button we clicked
            self.MouseActOffButton.setChecked(0)  # check false the off button incase it is checked

        if self.sender().objectName().__contains__("Mouse") and self.sender().objectName().__contains__('Off'):
            self.MouseActOnButton.setChecked(0)  # check off the on button
            self.MouseActOffButton.setChecked(1)  # check on the off button

        if self.sender().objectName().__contains__("Network") and self.sender().objectName().__contains__('On'):
            self.NetworkActivityDataOnButton.setChecked(1)  # check the button we clicked
            self.NetworkActivityDataOffButton.setChecked(0)  # check false the off button incase it is checked

        if self.sender().objectName().__contains__("Network") and self.sender().objectName().__contains__('Off'):
            self.NetworkActivityDataOnButton.setChecked(0)  # check off the on button
            self.NetworkActivityDataOffButton.setChecked(1)  # check on the off button

        if self.sender().objectName().__contains__("Process") and self.sender().objectName().__contains__('On'):
            self.ProcessStatOnButton.setChecked(1)  # check the button we clicked
            self.ProcessStatOffButton.setChecked(0)  # check false the off button incase it is checked

        if self.sender().objectName().__contains__("Process") and self.sender().objectName().__contains__('Off'):
            self.ProcessStatOnButton.setChecked(0)  # check off the on button
            self.ProcessStatOffButton.setChecked(1)  # check on the off button

    def add_sections(self):
        """adds a collapsible sections for every
        (title, widget) tuple in self.sections
        """
        for (title, widget) in self.sections:
            button1 = self.add_button(title)
            section1 = self.add_widget(button1, widget)
            button1.addChild(section1)

    def define_sections(self):
        """reimplement this to define all your sections
        and add them as (title, widget) tuples to self.sections
        """
        widget = QtWidgets.QFrame(self.tree)
        layout = QtWidgets.QHBoxLayout(widget)
        layout.addWidget(QtWidgets.QCalendarWidget())
        title = "Selected Artifacts"
        self.sections.append((title, widget))

        widget = QtWidgets.QFrame(self.tree)
        layout = QtWidgets.QHBoxLayout(widget)
        self.checkBox_Visualization = QtWidgets.QCheckBox()
        self.checkBox_Visualization.setObjectName("checkBox_Visualization")
        layout.addWidget(self.checkBox_Visualization)

        title = "Visualization"
        self.sections.append((title, widget))

        widget = QtWidgets.QFrame(self.tree)
        # self.tab_2 = QtWidgets.QWidget(widget)
        # self.tab_2.setObjectName("tab_2")
        layout = QtWidgets.QVBoxLayout(widget)

        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.checkBox = QtWidgets.QCheckBox()
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_6.addWidget(QtWidgets.QCheckBox())
        self.verticalLayout_6.addWidget(QtWidgets.QCheckBox())
        self.verticalLayout_6.addWidget(QtWidgets.QCheckBox())
        self.verticalLayout_6.addWidget(self.checkBox)
        layout.addLayout(self.verticalLayout_6)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_31 = QtWidgets.QLabel()
        self.label_31.setObjectName("label_31")
        self.gridLayout_4.addWidget(self.label_31, 6, 1, 1, 1)
        self.textEdit_3 = QtWidgets.QTextEdit()
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.textEdit_3.sizePolicy().hasHeightForWidth())
        # self.textEdit_3.setSizePolicy(sizePolicy)
        self.textEdit_3.setMaximumSize(QtCore.QSize(400, 25))
        self.textEdit_3.setObjectName("textEdit_3")
        self.gridLayout_4.addWidget(self.textEdit_3, 2, 0, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton()
        self.pushButton_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.pushButton_2, 6, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel()
        self.label_32.setStyleSheet("")
        self.label_32.setObjectName("label_32")
        self.gridLayout_4.addWidget(self.label_32, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel()
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 12))
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_33 = QtWidgets.QLabel()
        self.verticalLayout_6.addLayout(self.gridLayout_4)

        title = "Script"
        self.sections.append((title, widget))

        widget = QtWidgets.QFrame(self.tree)
        layout = QtWidgets.QHBoxLayout(widget)
        layout.addWidget(QtWidgets.QCheckBox())
        title = "History"
        self.sections.append((title, widget))

        widget = QtWidgets.QFrame(self.tree)
        layout = QtWidgets.QHBoxLayout(widget)
        layout.addWidget(QtWidgets.QCheckBox())
        title = "Log Content"
        self.sections.append((title, widget))
        # self.gridLayout_2.addWidget(widget, 7, 2, 1, 1)

    def add_button(self, title):
        """creates a QTreeWidgetItem containing a button
        to expand or collapse its section
        """
        item = QtWidgets.QTreeWidgetItem()
        self.tree.addTopLevelItem(item)
        self.tree.setItemWidget(item, 0, SectionExpandButton(item, text=title))
        return item

    def add_widget(self, button, widget):
        """creates a QWidgetItem containing the widget,
        as child of the button-QWidgetItem
        """
        section = QtWidgets.QTreeWidgetItem(button)
        section.setDisabled(True)
        self.tree.setItemWidget(section, 0, widget)
        return section

def main():
    app = QApplication(sys.argv)
    form = AvertApp()
    form.show()

    app.exec()


if __name__ == '__main__':
    main()



'''
    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        mainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow
        ui.setupUi(mainWindow)
        mainWindow.show()
        app.exec()

'''