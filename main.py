from PyQt5 import QtCore, QtWidgets
from view.accordion_floating import Ui_Form
from view.avert import Ui_MainWindow
import sys
from controller import controller
from view.components.description import Description
import subprocess as s
import numpy as np
import time

# global values
control = controller.Controller()
attain = []
all_selected = set()
selected = 0
universal_btn_state = 1
pressed = True
filter_used = False  # used to find if a filter has been selected already


class AvertApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(AvertApp, self).__init__()
        self.setupUi(self)
        self.floating_accordion = floatingAccord()
        self.floating_accordion.show()
        """used in tab 1"""
        """COMMENTING OUT UI MODIFICATION"""

        # portion for the tag_table
        # self.tab_1.detailed_view_accordion.tag_table.setSortingEnabled(1)  # allows for the sorting in the columns
        self.tab_1.detailed_view_accordion.tag_add_button.clicked.connect(self.add_tag)
        self.tab_1.detailed_view_accordion.tag_delete_button.clicked.connect(self.deleteTag)
        self.tab_1.universalRecord.clicked.connect(self.universalButton)
        self.tab_2.universalRecord.clicked.connect(self.universalButton)
        self.tab_1.detailed_view_accordion.pushButton_18.clicked.connect(self.add_annotation)
        # search button being activated
        self.tab_1.search_button.clicked.connect(self.searchPressed)
        # select all button
        self.tab_1.select_button.clicked.connect(self.selectAll)
        # export button being activated
        self.tab_1.exportButton.clicked.connect(self.export_pressed)
        # Script Preview button being activated
        self.tab_1.script_accordion.preview_btn.clicked.connect(self.script_preview_btn_pressed)
        # result table cell clicked
        self.tab_1.table_result.avert_result_table.cellClicked.connect(self.annotationDisplay)
        self.tab_1.table_result.avert_result_table.cellClicked.connect(self.tagDisplay)
        self.tab_1.table_result.avert_result_table.cellClicked.connect(self.descriptionDisplay)
        self.tab_1.table_result.avert_result_table.selectionModel().selectionChanged.connect(self.selectionChange)
        self.tab_1.table_result.avert_result_table.horizontalHeader().sectionClicked.connect(self.horizontalHeaderSort)
        self.tab_1.addToScriptButton.clicked.connect(
            lambda: self.tab_1.script_accordion.populateTableHelper(np.array(attain)[list(all_selected)], self))
        self.tab_1.script_accordion.generate_btn.clicked.connect(
            lambda: control.creation_script(self.tab_1.script_accordion.getScriptItems()))
        # self.tab_1.addToScriptButton.clicked.connect(self.test)
        # portion for the floating accordion
        self.floating_accordion.checkBox_Screenshot.clicked.connect(self.toggleButtons)
        self.floating_accordion.checkBox_Video.clicked.connect(self.toggleButtons)
        self.floating_accordion.checkBox_Network.clicked.connect(self.toggleButtons)
        self.floating_accordion.checkBox_Process.clicked.connect(self.toggleButtons)
        self.floating_accordion.checkBox_Keystroke.clicked.connect(self.toggleButtons)
        self.floating_accordion.checkBox_Mouse_Action.clicked.connect(self.toggleButtons)
        self.floating_accordion.checkBox_Window_History.clicked.connect(self.toggleButtons)
        self.floating_accordion.checkBox_System_Call.clicked.connect(self.toggleButtons)

        # portion for the Filters on home tab
        self.tab_1.checkBox_all_artifacts.stateChanged.connect(self.clickedCheckbox)
        self.tab_1.checkBox_screenshot.stateChanged.connect(self.clickedCheckbox)
        self.tab_1.checkBox_video.stateChanged.connect(self.clickedCheckbox)
        self.tab_1.checkBox_network.stateChanged.connect(self.clickedCheckbox)
        self.tab_1.checkBox_process.stateChanged.connect(self.clickedCheckbox)
        self.tab_1.checkBox_keystroke.stateChanged.connect(self.clickedCheckbox)
        self.tab_1.checkBox_mouse_action.stateChanged.connect(self.clickedCheckbox)
        self.tab_1.checkBox_windowHistory.stateChanged.connect(self.clickedCheckbox)
        self.tab_1.checkBox_system_call.stateChanged.connect(self.clickedCheckbox)
        self.tab_1.checkBox_history.stateChanged.connect(self.clickedCheckbox)
        self.tab_1.checkBox_log.stateChanged.connect(self.clickedCheckbox)

        # portion for grpah creation
        self.tab_1.visualization_accordion.pushButton_5.clicked.connect(self.generateGraph)

        """used in tab 2"""
        """COMMENTING OUT UI MODIFICATION"""

        # automatic on button checked
        self.tab_2.VideoStatOnButton.clicked.connect(self.toggleButtons)
        self.tab_2.VideoStatusOffButton.clicked.connect(self.toggleButtons)
        self.tab_2.ScreenshotStatOnButton.clicked.connect(self.toggleButtons)
        self.tab_2.ScreenshotStatOffButton.clicked.connect(self.toggleButtons)
        self.tab_2.SystemCallOnButton.clicked.connect(self.toggleButtons)
        self.tab_2.SystemCallOffButton.clicked.connect(self.toggleButtons)
        self.tab_2.WindowHistoryOnButton.clicked.connect(self.toggleButtons)
        self.tab_2.WindowHistoryOffButton.clicked.connect(self.toggleButtons)
        self.tab_2.KeyStrokeStatOnButton.clicked.connect(self.toggleButtons)
        self.tab_2.KeyStrokeStatOffButton.clicked.connect(self.toggleButtons)
        self.tab_2.MouseActOnButton.clicked.connect(self.toggleButtons)
        self.tab_2.MouseActOffButton.clicked.connect(self.toggleButtons)
        self.tab_2.NetworkActivityDataOnButton.clicked.connect(self.toggleButtons)
        self.tab_2.NetworkActivityDataOffButton.clicked.connect(self.toggleButtons)
        self.tab_2.ProcessStatOnButton.clicked.connect(self.toggleButtons)
        self.tab_2.ProcessStatOffButton.clicked.connect(self.toggleButtons)

        self.tab_2.StorageInValue.editingFinished.connect(self.thresholdChange)

        '''used in tab 3'''
        """Modifications for UI """
        self.tab_3.sync_btn.clicked.connect(lambda: self.clickedSync(self.tab_3))

    def generateGraph(self):
        global control

        type = ''
        if self.tab_1.visualization_accordion.radioButton_4.isChecked():
            make_up = [self.tab_1.visualization_accordion.lineEdit_3.text(),
                       self.tab_1.visualization_accordion.lineEdit.text(),
                       self.tab_1.visualization_accordion.comboBox.currentText(),
                       self.tab_1.visualization_accordion.lineEdit_2.text()]
            type = 'Timeline'

        control.graphGeneration(type, make_up)

    '''
    Allow recording status buttons (on and off) as a toggle buttons
    meaning when one is pressed it stays down and when the other is pressed it stays down
    while the other one pops up
    '''

    def toggleButtons(self):  # called upon by button automatically will know which button
        global control  # individual button on and off

        if self.sender().objectName().__contains__('Screenshot'):  # recording screenshot button hit
            # first we check the checkboxes in the accordion
            if self.sender().objectName().__contains__('checkBox'):
                if self.sender().isChecked():
                    self.floating_accordion.tableWidget.item(0, 1).setText('Recording')
                    self.tab_2.ScreenshotStatOnButton.setChecked(1)
                    self.tab_2.ScreenshotStatOffButton.setChecked(0)
                    control.screenshotRecording(True)

                elif not self.sender().isChecked():
                    self.floating_accordion.tableWidget.item(0, 1).setText('Stopped')
                    self.tab_2.ScreenshotStatOnButton.setChecked(0)  # check off the on button
                    self.tab_2.ScreenshotStatOffButton.setChecked(1)  # check on the off button
                    control.screenshotRecording(False)

            else:  # anything else is a button
                if self.sender().isChecked() and self.sender().objectName().__contains__('On'):  # hitting the one
                    # button
                    self.floating_accordion.tableWidget.item(0, 1).setText('Recording')
                    self.floating_accordion.checkBox_Screenshot.setChecked(1)  # check it due to being off
                    self.tab_2.ScreenshotStatOnButton.setChecked(1)
                    self.tab_2.ScreenshotStatOffButton.setChecked(0)
                    control.screenshotRecording(True)

                elif self.sender().isChecked() and self.sender().objectName().__contains__('Off'):
                    self.floating_accordion.tableWidget.item(0, 1).setText('Stopped')
                    self.floating_accordion.checkBox_Screenshot.setChecked(0)  # check it due to being off
                    self.tab_2.ScreenshotStatOnButton.setChecked(0)  # check off the on button
                    self.tab_2.ScreenshotStatOffButton.setChecked(1)  # check on the off button
                    control.screenshotRecording(False)

        if self.sender().objectName().__contains__('Video'):
            if self.sender().objectName().__contains__('checkBox'):
                if self.sender().isChecked():
                    self.floating_accordion.tableWidget.item(1, 1).setText('Recording')
                    self.tab_2.VideoStatOnButton.setChecked(1)
                    self.tab_2.VideoStatusOffButton.setChecked(0)
                    control.videoRecording(True)

                elif not self.sender().isChecked():
                    self.floating_accordion.tableWidget.item(1, 1).setText('Stopped')
                    self.tab_2.VideoStatOnButton.setChecked(0)  # check off the on button
                    self.tab_2.VideoStatusOffButton.setChecked(1)  # check on the off button
                    control.videoRecording(False)

            else:  # anything else is a button
                if self.sender().isChecked() and self.sender().objectName().__contains__('On'):  # hitting the one
                    # button
                    self.floating_accordion.tableWidget.item(1, 1).setText('Recording')
                    self.floating_accordion.checkBox_Video.setChecked(1)  # check it due to being off
                    self.tab_2.VideoStatOnButton.setChecked(1)
                    self.tab_2.VideoStatusOffButton.setChecked(0)
                    control.videoRecording(True)

                elif self.sender().isChecked() and self.sender().objectName().__contains__('Off'):
                    self.floating_accordion.tableWidget.item(1, 1).setText('Stopped')
                    self.floating_accordion.checkBox_Video.setChecked(0)  # check it due to being off
                    self.tab_2.VideoStatOnButton.setChecked(0)  # check off the on button
                    self.tab_2.VideoStatusOffButton.setChecked(1)  # check on the off button
                    control.videoRecording(False)

        if self.sender().objectName().__contains__('Network'):
            if self.sender().objectName().__contains__('checkBox'):
                if self.sender().isChecked():
                    self.floating_accordion.tableWidget.item(2, 1).setText('Recording')
                    self.tab_2.NetworkActivityDataOnButton.setChecked(1)
                    self.tab_2.NetworkActivityDataOffButton.setChecked(0)
                    control.networkRecording(True)

                elif not self.sender().isChecked():
                    self.floating_accordion.tableWidget.item(2, 1).setText('Stopped')
                    self.tab_2.NetworkActivityDataOnButton.setChecked(0)  # check off the on button
                    self.tab_2.NetworkActivityDataOffButton.setChecked(1)  # check on the off button
                    control.networkRecording(False)

            else:  # anything else is a button
                if self.sender().isChecked() and self.sender().objectName().__contains__('On'):  # hitting the one
                    # button
                    self.floating_accordion.tableWidget.item(2, 1).setText('Recording')
                    self.floating_accordion.checkBox_Network.setChecked(1)  # check it due to being off
                    self.tab_2.NetworkActivityDataOnButton.setChecked(1)
                    self.tab_2.NetworkActivityDataOffButton.setChecked(0)
                    control.networkRecording(True)

                elif self.sender().isChecked() and self.sender().objectName().__contains__('Off'):
                    self.floating_accordion.tableWidget.item(2, 1).setText('Stopped')
                    self.floating_accordion.checkBox_Network.setChecked(0)  # check it due to being off
                    self.tab_2.NetworkActivityDataOnButton.setChecked(0)
                    self.tab_2.NetworkActivityDataOffButton.setChecked(1)
                    control.networkRecording(False)

        if self.sender().objectName().__contains__('Process'):
            if self.sender().objectName().__contains__('checkBox'):
                if self.sender().isChecked():
                    self.floating_accordion.tableWidget.item(3, 1).setText('Recording')
                    self.tab_2.ProcessStatOnButton.setChecked(1)
                    self.tab_2.ProcessStatOffButton.setChecked(0)
                    control.processRecording(True)

                elif not self.sender().isChecked():
                    self.floating_accordion.tableWidget.item(3, 1).setText('Stopped')
                    self.tab_2.ProcessStatOnButton.setChecked(0)
                    self.tab_2.ProcessStatOffButton.setChecked(1)
                    control.processRecording(False)

            else:  # anything else is a button
                if self.sender().isChecked() and self.sender().objectName().__contains__('On'):  # hitting the one
                    self.floating_accordion.tableWidget.item(3, 1).setText('Recording')
                    self.floating_accordion.checkBox_Process.setChecked(1)
                    self.tab_2.ProcessStatOnButton.setChecked(1)
                    self.tab_2.ProcessStatOffButton.setChecked(0)
                    control.processRecording(True)

                elif self.sender().isChecked() and self.sender().objectName().__contains__('Off'):
                    self.floating_accordion.tableWidget.item(3, 1).setText('Stopped')
                    self.floating_accordion.checkBox_Process.setChcked(0)
                    self.tab_2.ProcessStatOnButton.setChecked(0)
                    self.tab_2.ProcessStatOffButton.setChecked(1)
                    control.processRecording(False)

        if self.sender().objectName().__contains__('Keystroke') or self.sender().objectName().__contains__('KeyStroke'):
            if self.sender().objectName().__contains__('checkBox'):
                if self.sender().isChecked():
                    self.floating_accordion.tableWidget.item(4, 1).setText('Recording')
                    self.tab_2.KeyStrokeStatOnButton.setChecked(1)
                    self.tab_2.KeyStrokeStatOffButton.setChecked(0)
                    control.keyboardRecording(True)

                elif not self.sender().isChecked():
                    self.floating_accordion.tableWidget.item(4, 1).setText('Stopped')
                    self.tab_2.KeyStrokeStatOnButton.setChecked(0)
                    self.tab_2.KeyStrokeStatOffButton.setChecked(1)
                    control.keyboardRecording(False)

            else:  # anything else is a button
                if self.sender().isChecked() and self.sender().objectName().__contains__('On'):
                    self.floating_accordion.tableWidget.item(4, 1).setText('Recording')
                    self.floating_accordion.checkBox_Keystroke.setChecked(1)
                    self.tab_2.KeyStrokeStatOnButton.setChecked(1)
                    self.tab_2.KeyStrokeStatOffButton.setChecked(0)
                    control.keyboardRecording(True)

                elif self.sender().isChecked() and self.sender().objectName().__contains__('Off'):
                    self.floating_accordion.tableWidget.item(4, 1).setText('Stopped')
                    self.floating_accordion.checkBox_Keystroke.setChecked(0)
                    self.tab_2.KeyStrokeStatOnButton.setChecked(0)
                    self.tab_2.KeyStrokeStatOffButton.setChecked(1)
                    control.keyboardRecording(False)

        if self.sender().objectName().__contains__('Mouse'):
            if self.sender().objectName().__contains__('checkBox'):
                if self.sender().isChecked():
                    self.floating_accordion.tableWidget.item(5, 1).setText('Recording')
                    self.tab_2.MouseActOnButton.setChecked(1)
                    self.tab_2.MouseActOffButton.setChecked(0)
                    control.mouseActionRecording(True)

                elif not self.sender().isChecked():
                    self.floating_accordion.tableWidget.item(5, 1).setText('Stopped')
                    self.tab_2.MouseActOnButton.setChecked(0)
                    self.tab_2.MouseActOffButton.setChecked(1)
                    control.mouseActionRecording(False)

            else:
                if self.sender().isChecked() and self.sender().objectName().__contains__('On'):
                    self.floating_accordion.tableWidget.item(5, 1).setText('Recording')
                    self.floating_accordion.checkBox_Mouse_Action.setChecked(1)
                    self.tab_2.MouseActOnButton.setChecked(1)
                    self.tab_2.MouseActOffButton.setChecked(0)
                    control.mouseActionRecording(True)

                elif self.sender().isChecked() and self.sender().objectName().__contains__('Off'):
                    self.floating_accordion.tableWidget.item(5, 1).setText('Stopped')
                    self.floating_accordion.checkBox_Mouse_Action.setChecked(0)
                    self.tab_2.MouseActOnButton.setChecked(0)
                    self.tab_2.MouseActOffButton.setChecked(1)
                    control.mouseActionRecording(False)

        if self.sender().objectName().__contains__('Window'):
            if self.sender().objectName().__contains__('checkBox'):
                if self.sender().isChecked():
                    self.floating_accordion.tableWidget.item(6, 1).setText('Recording')
                    self.tab_2.WindowHistoryOnButton.setChecked(1)
                    self.tab_2.WindowHistoryOffButton.setChecked(0)
                    control.windowHistoryRecording(True)

                elif not self.sender().isChecked():
                    self.floating_accordion.tableWidget.item(6, 1).setText('Stopped')
                    self.tab_2.WindowHistoryOnButton.setChecked(0)
                    self.tab_2.WindowHistoryOffButton.setChecked(1)
                    control.windowHistoryRecording(False)

            else:
                if self.sender().isChecked() and self.sender().objectName().__contains__('On'):
                    self.floating_accordion.tableWidget.item(6, 1).setText('Recording')
                    self.floating_accordion.checkBox_Window_History.setChecked(1)
                    self.tab_2.WindowHistoryOnButton.setChecked(1)
                    self.tab_2.WindowHistoryOffButton.setChecked(0)
                    control.windowHistoryRecording(True)

                elif self.sender().isChecked() and self.sender().objectName().__contains__('Off'):
                    self.floating_accordion.tableWidget.item(6, 1).setText('Stopped')
                    self.floating_accordion.checkBox_Window_History.setChecked(0)
                    self.tab_2.WindowHistoryOnButton.setChecked(0)
                    self.tab_2.WindowHistoryOffButton.setChecked(1)
                    control.windowHistoryRecording(False)

        if self.sender().objectName().__contains__('System'):
            if self.sender().objectName().__contains__('checkBox'):
                if self.sender().isChecked():
                    self.floating_accordion.tableWidget.item(7, 1).setText('Recording')
                    self.tab_2.SystemCallOnButton.setChecked(1)
                    self.tab_2.SystemCallOffButton.setChecked(0)
                    control.systemCallRecording(True)

                elif not self.sender().isChecked():
                    self.floating_accordion.tableWidget.item(7, 1).setText('Stopped')
                    self.tab_2.SystemCallOnButton.setChecked(0)
                    self.tab_2.SystemCallOffButton.setChecked(1)
                    control.systemCallRecording(False)

            else:
                if self.sender().isChecked() and self.sender().objectName().__contains__('On'):
                    self.floating_accordion.tableWidget.item(7, 1).setText('Recording')
                    self.floating_accordion.checkBox_System_Call.setChecked(1)
                    self.tab_2.SystemCallOnButton.setChecked(1)
                    self.tab_2.SystemCallOffButton.setChecked(0)
                    control.systemCallRecording(True)

                elif self.sender().isChecked() and self.sender().objectName().__contains__('Off'):
                    self.floating_accordion.tableWidget.item(7, 1).setText('Stopped')
                    self.floating_accordion.checkBox_System_Call.setChecked(0)
                    self.tab_2.SystemCallOnButton.setChecked(0)
                    self.tab_2.SystemCallOffButton.setChecked(1)
                    control.systemCallRecording(False)

    def add_annotation(self, index):  # add a row when the button add is selected
        """
        Add an annotation to the selected artifacts
        """
        global attain, control

        if (len(self.tab_1.detailed_view_accordion.annotation_text.toPlainText().strip()) > 0):
            for index in all_selected:
                control.annotationAdd(self.tab_1.detailed_view_accordion.annotation_text.toPlainText(), attain[index])
            self.annotationDisplay(self.tab_1.table_result.getIndexSelected())

    def add_tag(self):  # add a row when the button add is selected
        """
        create new row in the qwidget table within tag area of
        detailed view
        :return: none
        """
        global attain, control
        index = self.tab_1.table_result.getIndexSelected()

        if len(self.tab_1.detailed_view_accordion.tag_input.text().strip()):
            control.tagAdd(self.tab_1.detailed_view_accordion.tag_input.text(), attain[index])
            self.tagDisplay(self.tab_1.table_result.getIndexSelected())
            self.tab_1.detailed_view_accordion.tag_input.setText('')

    def universalButton(self):
        global universal_btn_state

        if not universal_btn_state:
            universal_btn_state = 1
            control.universalRecording(True)
            '''
             change the text and checked from the press on the universal record button
             will check and uncheck the config buttons
             GUI CHANGES
             '''
            self.tab_1.universalRecord.setText('Record On')
            self.tab_1.universalRecord.setChecked(1)
            self.tab_2.universalRecord.setText('Record On')
            self.tab_2.universalRecord.setChecked(1)

            # check all the on buttons and uncheck the offs
            self.tab_2.VideoStatOnButton.setChecked(1)  # check the button we clicked
            self.tab_2.VideoStatusOffButton.setChecked(0)  # check false the off button incase it is checked
            self.tab_2.ScreenshotStatOnButton.setChecked(1)  # check the button we clicked
            self.tab_2.ScreenshotStatOffButton.setChecked(0)  # check false the off button incase it is checked
            self.tab_2.SystemCallOnButton.setChecked(1)  # check the button we clicked
            self.tab_2.SystemCallOffButton.setChecked(0)  # check false the off button incase it is checked
            self.tab_2.WindowHistoryOnButton.setChecked(1)  # check the button we clicked
            self.tab_2.WindowHistoryOffButton.setChecked(0)  # check false the off button incase it is checked
            self.tab_2.KeyStrokeStatOnButton.setChecked(1)  # check the button we clicked
            self.tab_2.KeyStrokeStatOffButton.setChecked(0)  # check false the off button incase it is checked
            self.tab_2.MouseActOnButton.setChecked(1)  # check the button we clicked
            self.tab_2.MouseActOffButton.setChecked(0)  # check false the off button incase it is checked
            self.tab_2.NetworkActivityDataOnButton.setChecked(1)  # check the button we clicked
            self.tab_2.NetworkActivityDataOffButton.setChecked(0)  # check false the off button incase it is checked
            self.tab_2.ProcessStatOnButton.setChecked(1)  # check the button we clicked
            self.tab_2.ProcessStatOffButton.setChecked(0)  # check false the off button incase it is checked

            # check all the check boxes off
            self.floating_accordion.checkBox_Screenshot.setChecked(1)  # check it due to being off
            self.floating_accordion.tableWidget.item(0, 1).setText('Recording')
            self.floating_accordion.checkBox_Video.setChecked(1)  # check it due to being off
            self.floating_accordion.tableWidget.item(1, 1).setText('Recording')
            self.floating_accordion.checkBox_Network.setChecked(1)  # check it due to being off
            self.floating_accordion.tableWidget.item(2, 1).setText('Recording')
            self.floating_accordion.checkBox_Process.setChecked(1)
            self.floating_accordion.tableWidget.item(3, 1).setText('Recording')
            self.floating_accordion.checkBox_Keystroke.setChecked(1)
            self.floating_accordion.tableWidget.item(4, 1).setText('Recording')
            self.floating_accordion.checkBox_Mouse_Action.setChecked(1)
            self.floating_accordion.tableWidget.item(5, 1).setText('Recording')
            self.floating_accordion.checkBox_Window_History.setChecked(1)
            self.floating_accordion.tableWidget.item(6, 1).setText('Recording')
            self.floating_accordion.checkBox_System_Call.setChecked(1)
            self.floating_accordion.tableWidget.item(7, 1).setText('Recording')

        else:  # if off
            universal_btn_state = 0
            control.universalRecording(False)
            '''
             change the text and checked from the press on the universal record button
             will check and uncheck the config buttons
             GUI CHANGES
             '''
            self.tab_1.universalRecord.setText('Record Off')
            self.tab_1.universalRecord.setChecked(0)
            self.tab_2.universalRecord.setText('Record Off')
            self.tab_2.universalRecord.setChecked(0)
            # check all the off buttons and uncheck ons

            self.tab_2.VideoStatOnButton.setChecked(0)  # check off the on button
            self.tab_2.VideoStatusOffButton.setChecked(1)  # check on the off button
            self.tab_2.ScreenshotStatOnButton.setChecked(0)  # check off the on button
            self.tab_2.ScreenshotStatOffButton.setChecked(1)  # check on the off button
            self.tab_2.SystemCallOnButton.setChecked(0)  # check off the on button
            self.tab_2.SystemCallOffButton.setChecked(1)  # check on the off button
            self.tab_2.WindowHistoryOnButton.setChecked(0)  # check off the on button
            self.tab_2.WindowHistoryOffButton.setChecked(1)  # check on the off button
            self.tab_2.KeyStrokeStatOnButton.setChecked(0)  # check off the on button
            self.tab_2.KeyStrokeStatOffButton.setChecked(1)  # check on the off button
            self.tab_2.MouseActOnButton.setChecked(0)  # check off the on button
            self.tab_2.MouseActOffButton.setChecked(1)  # check on the off button
            self.tab_2.NetworkActivityDataOnButton.setChecked(0)  # check off the on button
            self.tab_2.NetworkActivityDataOffButton.setChecked(1)  # check on the off button
            self.tab_2.ProcessStatOnButton.setChecked(0)  # check off the on button
            self.tab_2.ProcessStatOffButton.setChecked(1)  # check on the off button

            #  doing the checkboxes on the accordion
            self.floating_accordion.checkBox_Screenshot.setChecked(0)  # check it due to being off
            self.floating_accordion.tableWidget.item(0, 1).setText('Stopped')
            self.floating_accordion.checkBox_Video.setChecked(0)  # check it due to being off
            self.floating_accordion.tableWidget.item(1, 1).setText('Stopped')
            self.floating_accordion.checkBox_Network.setChecked(0)  # check it due to being off
            self.floating_accordion.tableWidget.item(2, 1).setText('Stopped')
            self.floating_accordion.checkBox_Process.setChecked(0)
            self.floating_accordion.tableWidget.item(3, 1).setText('Stopped')
            self.floating_accordion.checkBox_Keystroke.setChecked(0)
            self.floating_accordion.tableWidget.item(4, 1).setText('Stopped')
            self.floating_accordion.checkBox_Mouse_Action.setChecked(0)
            self.floating_accordion.tableWidget.item(5, 1).setText('Stopped')
            self.floating_accordion.checkBox_Window_History.setChecked(0)
            self.floating_accordion.tableWidget.item(6, 1).setText('Stopped')
            self.floating_accordion.checkBox_System_Call.setChecked(0)
            self.floating_accordion.tableWidget.item(7, 1).setText('Stopped')

    def thresholdChange(self):
        if self.tab_2.StorageInValue.text() == '':  # in case empty
            control.storageRecording(70)  # set to default as user inputs full number
        else:
            full = control.storageRecording(float(self.tab_2.StorageInValue.text()))  # send the value
        if full:
            QtWidgets.QMessageBox.about(self, 'Storage Alert', 'Storage is full')

    def selectAll(self):
        global pressed
        global selected
        global all_selected
        pressed = not pressed
        if pressed:
            all_selected.clear()
            state = QtCore.Qt.Unchecked
            self.tab_1.select_button.setText("Select All")
        else:
            state = QtCore.Qt.Checked
            self.tab_1.select_button.setText("Deselect All")
            # print("select all pressed")
        for i in range(len(attain)):
            item = self.tab_1.table_result.avert_result_table.item(i, 0)
            item.setCheckState(state)
            if not pressed:
                all_selected.add(i)

    def horizontalHeaderSort(self, index):
        global attain
        if index == 1 or index == 5:
            search_header = 'timestamp'
        elif index == 2:
            search_header = 'name'
        elif index == 3:
            search_header = 'ip_address'
        elif index == 4:
            search_header = 'mac_address'

        self.tab_1.table_result.avert_result_table.clearSelection()
        attain = sorted(attain, key=lambda d: d[search_header])
        self.updateTable(attain)

    def searchPressed(self):  # once search is pressed we must search the given data
        # attain the the value in the search box
        global attain
        search = self.tab_1.search_expression_bar.text()  # attain the text
        attain = control.view(search)
        self.updateTable(attain)

    def annotationDisplay(self, index):
        self.tab_1.table_result.setIndexSelected(index)
        global attain
        self.tab_1.detailed_view_accordion.annotation_table.display_annotation(attain[index])

    def tagDisplay(self, index):  # display the tags for selected
        self.tab_1.table_result.setIndexSelected(index)
        global attain
        self.tab_1.detailed_view_accordion.tag_table.display_tag(attain[index])

    def descriptionDisplay(self, index):
        self.tab_1.table_result.setIndexSelected(index)
        global attain
        self.tab_1.detailed_view_accordion.tab_134.display_tab(attain[index])

    def export_pressed(self, index):
        global attain  # set global variables
        self.tab_1.table_result.setIndexSelected(index)  # set the index selected
        exporter = attain[index]  # add the formatted data to exporter
        control.export(exporter.get('_id'))  # export the selected data using the ID

    def script_preview_btn_pressed(self):
        file_obj = ""  # Variable to write script to

        # Write to variable the script preview
        with open("/home/kali/PycharmProjects/UserInterface/view/components/script_example.py", 'r') as file:
            for line in file:
                file_obj += line

        # Generate the preview window based on written script
        QtWidgets.QMessageBox.about(self, 'Script Preview', file_obj)

    def selectionChange(self, selected, deselected):
        global all_selected

        for i in selected.indexes():
            # print('Selected Row = {0}, Column = {1}'.format(i.row(), i.column()))
            item = self.tab_1.table_result.avert_result_table.item(i.row(), 0)
            item.setCheckState(QtCore.Qt.Checked)
            all_selected.add(i.row())
            # self.tab_1.table_result.avert_result_table.setItem(i.row(), 0, item)
        for i in deselected.indexes():
            # print('Selected Row = {0}, Column = {1}'.format(i.row(), i.column()))
            item = self.tab_1.table_result.avert_result_table.item(i.row(), 0)
            item.setCheckState(QtCore.Qt.Unchecked)
            if (i.row() in all_selected):
                all_selected.remove(i.row())
            # self.tab_1.table_result.avert_result_table.setItem(i.row(), 0, item)

    def updateAttain(self, checked):
        global control
        result = []
        for i in checked:  # same order as array in clicked checkbox
            if not i == 0:
                result = result + control.view_filter(i)
        return result

    def clickedCheckbox(self):
        global attain
        filters_checked = [0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0]  # go in order to see which are checked

        if self.tab_1.checkBox_all_artifacts.isChecked():
            filters_checked[0] = ''
        elif not self.tab_1.checkBox_all_artifacts.isChecked():
            filters_checked[0] = 0

        if self.tab_1.checkBox_keystroke.isChecked():
            filters_checked[1] = 'Keystroke'
        elif not self.tab_1.checkBox_keystroke.isChecked():
            filters_checked[1] = 0

        if self.tab_1.checkBox_mouse_action.isChecked():
            filters_checked[2] = 'Mouse Action'
        elif not self.tab_1.checkBox_mouse_action.isChecked():
            filters_checked[2] = 0

        if self.tab_1.checkBox_system_call.isChecked():
            filters_checked[3] = 'System Call'
        elif not self.tab_1.checkBox_system_call.isChecked():
            filters_checked[3] = 0

        if self.tab_1.checkBox_process.isChecked():
            filters_checked[4] = 'Process'
        elif not self.tab_1.checkBox_process.isChecked():
            filters_checked[4] = 0

        if self.tab_1.checkBox_screenshot.isChecked():
            filters_checked[5] = 'Screenshot'
        elif not self.tab_1.checkBox_screenshot.isChecked():
            filters_checked[5] = 0

        if self.tab_1.checkBox_windowHistory.isChecked():
            filters_checked[6] = 'Window History'
        elif not self.tab_1.checkBox_windowHistory.isChecked():
            filters_checked[6] = 0

        if self.tab_1.checkBox_network.isChecked():
            filters_checked[7] = 'Network'
        elif not self.tab_1.checkBox_network.isChecked():
            filters_checked[7] = 0

        if self.tab_1.checkBox_video.isChecked():
            filters_checked[8] = 'Video'
        elif not self.tab_1.checkBox_video.isChecked():
            filters_checked[8] = 0

        attain = self.updateAttain(filters_checked)
        self.updateTable(attain)

    def deleteTag(self, index):
        global control, attain
        self.tab_1.detailed_view_accordion.tag_table.setIndexSelected(index)

        print(self.tab_1.detailed_view_accordion.tag_table.currentRow())
        # control.tagDelete()

    def test(self):
        print("testing message")
        # global all_selected
        # global attain
        # print(self.sender().objectName())
        # print(all_selected)
        # print(attain)

    def syncButtonsToggle(self):
        if self.sender().objectName().__contains__('excluding'):  # keep button checked
            self.tab_3.allexcludingvideo_btn.setChecked(1)
            self.tab_3.allincludingvideo_btn.setChecked(0)
        else:
            self.tab_3.allexcludingvideo_btn.setChecked(0)
            self.tab_3.allincludingvideo_btn.setChecked(1)

    def clickedSync(self, tab3_widget):
        global control

        if 7 <= len(self.tab_3.toIPval_lineEdit.text().strip()) <= 15:  # ensure that we have something
            ip = self.tab_3.toIPval_lineEdit.text()
        else:
            return  # add error here

        if self.sender().objectName().__contains__('sync'):  # once we press the sync and it
            if self.tab_3.allexcludingvideo_btn.isChecked():
                control.syncBegin('video', ip, tab3_widget)
                self.tab_3.allexcludingvideo_btn.setChecked(0)  # reset

            if self.tab_3.allincludingvideo_btn.isChecked():
                control.syncBegin('None', ip, tab3_widget)
                self.tab_3.allincludingvideo_btn.setChecked(0)  # rest

        if self.sender().objectName().__contains__('cancelall_btn'):
            # here we will have an if started
            if control.syncStatus():
                control.syncBegin(self, '', '', True, tab3_widget)
            else:
                pass  # here we generate the sync error message
        # self.syncPercentages(self)


# def syncPercentages(self):
#     status = control.syncStatus()
#     if status:
#         while True:
#             value = control.getSyncPercentage()
#             if control.getSyncComplete():
#                 return


def avertInit():
    s.Popen("sudo auditctl -a always,exit -S read,write,open,close,mmap,pipe,alarm,getpid,fork,exit,chmod,chown,umask",
            shell=True, stdout=s.PIPE, stderr=s.PIPE)


'''
*** FLOATING ACCORDING CLASS FOR BEHAVIOR ***
'''


class floatingAccord(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(floatingAccord, self).__init__()
        self.setupUi(self)


def main():
    avertInit()
    app = QtWidgets.QApplication(sys.argv)
    form = AvertApp()
    form.show()

    #  floating according
    '''
    form2 = floatingAccord()
    form2.show()
    '''
    app.exec()


if __name__ == '__main__':
    main()
    sys.exit()
'''
    Form = QtWidgets.QWidget()
    form2 = Ui_Form()
    form2.setupUi(Form)
    Form.show()
'''
