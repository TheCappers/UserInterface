from PyQt5 import QtCore, QtWidgets
from view.accordion_floating import Ui_Form
from view.avert import Ui_MainWindow
import sys
from controller import controller
from view.components.description import Description

# global values
control = controller.Controller()
attain = []
clicks = []
selected = 0


class AvertApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(AvertApp, self).__init__()
        self.setupUi(self)

        """used in tab 1"""
        """COMMENTING OUT UI MODIFICATION"""

        # portion for the tag_table
        #self.tab_1.detailed_view_accordion.tag_table.setSortingEnabled(1)  # allows for the sorting in the columns
        self.tab_2.ProcessStatOffButton.clicked.connect(self.toggleButtons)
        self.tab_1.detailed_view_accordion.tag_add_button.clicked.connect(self.add_tag)
        self.tab_1.universalRecord.clicked.connect(self.universalButton)
        self.tab_1.detailed_view_accordion.pushButton_18.clicked.connect(self.add_annotation)
        # search button being activated
        self.tab_1.search_button.clicked.connect(self.searchPressed)
        # export button being activated
        self.tab_1.exportButton.clicked.connect(self.exportPressed)
        # result table cell clicked
        self.tab_1.table_result.avert_result_table.cellClicked.connect(self.annotationDisplay)
        self.tab_1.table_result.avert_result_table.cellClicked.connect(self.tagDisplay)
        self.tab_1.table_result.avert_result_table.cellClicked.connect(self.descriptionDisplay)

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

        # threshold changing
        self.tab_2.StorageInValue.textEdited.connect(self.thresholdChange)



        # self.table_result.avert_result_table.cellClicked.connect(self.annotationDisplay)



    # button toggle method
    '''
    Allow recording status buttons (on and off) as a toggle buttons
    meaning when one is pressed it stays down and when the other is pressed it stays down
    while the other one pops up
    '''

    def toggleButtons(self):  # called upon by button automatically will know which button
        if self.sender().objectName().__contains__("Video") and self.sender().objectName().__contains__('On'):
            self.tab_2.VideoStatOnButton.setChecked(1)  # check the button we clicked
            self.tab_2.VideoStatusOffButton.setChecked(0)  # check false the off button incase it is checked

        if self.sender().objectName().__contains__("Video") and self.sender().objectName().__contains__('Off'):
            self.tab_2.VideoStatOnButton.setChecked(0)  # check off the on button
            self.tab_2.VideoStatusOffButton.setChecked(1)  # check on the off button

        if self.sender().objectName().__contains__("Screenshot") and self.sender().objectName().__contains__('On'):
            self.tab_2.ScreenshotStatOnButton.setChecked(1)  # check the button we clicked
            self.tab_2.ScreenshotStatOffButton.setChecked(0)  # check false the off button incase it is checked

        if self.sender().objectName().__contains__("Screenshot") and self.sender().objectName().__contains__('Off'):
            self.tab_2.ScreenshotStatOnButton.setChecked(0)  # check off the on button
            self.tab_2.ScreenshotStatOffButton.setChecked(1)  # check on the off button

        if self.sender().objectName().__contains__("Sys") and self.sender().objectName().__contains__('On'):
            self.tab_2.SystemCallOnButton.setChecked(1)  # check the button we clicked
            self.tab_2.SystemCallOffButton.setChecked(0)  # check false the off button incase it is checked

        if self.sender().objectName().__contains__("Sys") and self.sender().objectName().__contains__('Off'):
            self.tab_2.SystemCallOnButton.setChecked(0)  # check off the on button
            self.tab_2.SystemCallOffButton.setChecked(1)  # check on the off button

        if self.sender().objectName().__contains__("Win") and self.sender().objectName().__contains__('On'):
            self.tab_2.WindowHistoryOnButton.setChecked(1)  # check the button we clicked
            self.tab_2.WindowHistoryOffButton.setChecked(0)  # check false the off button incase it is checked

        if self.sender().objectName().__contains__("Win") and self.sender().objectName().__contains__('Off'):
            self.tab_2.WindowHistoryOnButton.setChecked(0)  # check off the on button
            self.tab_2.WindowHistoryOffButton.setChecked(1)  # check on the off button

        if self.sender().objectName().__contains__("KeyStroke") and self.sender().objectName().__contains__('On'):
            self.tab_2.KeyStrokeStatOnButton.setChecked(1)  # check the button we clicked
            self.tab_2.KeyStrokeStatOffButton.setChecked(0)  # check false the off button incase it is checked

        if self.sender().objectName().__contains__("KeyStroke") and self.sender().objectName().__contains__('Off'):
            self.tab_2.KeyStrokeStatOnButton.setChecked(0)  # check off the on button
            self.tab_2.KeyStrokeStatOffButton.setChecked(1)  # check on the off button

        if self.sender().objectName().__contains__("Mouse") and self.sender().objectName().__contains__('On'):
            self.tab_2.MouseActOnButton.setChecked(1)  # check the button we clicked
            self.tab_2.MouseActOffButton.setChecked(0)  # check false the off button incase it is checked

        if self.sender().objectName().__contains__("Mouse") and self.sender().objectName().__contains__('Off'):
            self.tab_2.MouseActOnButton.setChecked(0)  # check off the on button
            self.tab_2.MouseActOffButton.setChecked(1)  # check on the off button

        if self.sender().objectName().__contains__("Network") and self.sender().objectName().__contains__('On'):
            self.tab_2.NetworkActivityDataOnButton.setChecked(1)  # check the button we clicked
            self.tab_2.NetworkActivityDataOffButton.setChecked(0)  # check false the off button incase it is checked

        if self.sender().objectName().__contains__("Network") and self.sender().objectName().__contains__('Off'):
            self.tab_2.NetworkActivityDataOnButton.setChecked(0)  # check off the on button
            self.tab_2.NetworkActivityDataOffButton.setChecked(1)  # check on the off button

        if self.sender().objectName().__contains__("Process") and self.sender().objectName().__contains__('On'):
            self.tab_2.ProcessStatOnButton.setChecked(1)  # check the button we clicked
            self.tab_2.ProcessStatOffButton.setChecked(0)  # check false the off button incase it is checked

        if self.sender().objectName().__contains__("Process") and self.sender().objectName().__contains__('Off'):
            self.tab_2.ProcessStatOnButton.setChecked(0)  # check off the on button
            self.tab_2.ProcessStatOffButton.setChecked(1)  # check on the off button

    def add_annotation(self,index):  # add a row when the button add is selected
        """
        Add an annotation to the selected artifact
        """
        global attain, control
        index = self.tab_1.table_result.getIndexSelected()

        if len(self.tab_1.detailed_view_accordion.annotation_text.toPlainText().strip()):
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
        if self.tab_1.universalRecord.isChecked():  # if on
            control.universalRecording(True)
            '''
             change the text and checked from the press on the universal record button
             will check and uncheck the config buttons
             GUI CHANGES
             '''
            self.tab_1.universalRecord.setText('Record On')

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
        else:  # if off
            control.universalRecording(False)
            '''
             change the text and checked from the press on the universal record button
             will check and uncheck the config buttons
             GUI CHANGES
             '''
            self.tab_1.universalRecord.setText('Record Off')
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

    def thresholdChange(self):
        if self.tab_2.StorageInValue.text() == '':  # in case empty
            control.storageRecording(70)  # set to default as user inputs full number
       # else:
        #    full = control.storageRecording(float(self.StorageInValue.text()))  # send the value
         #   if full:
          #      QtWidgets.QMessageBox.about(self, 'Storage Alert', 'Storage is full')

    def searchPressed(self):  # once search is pressed we must search the given data
        # attain the the value in the search box
        global attain
        search = self.tab_1.search_expression_bar.text()  # attain the text
        attain = control.view(search)
        self.updateTable(attain)

        # table_result.populateTable(attain)
        # print(attain)
        # ResultTable().populateTable(self, attain)

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
        

    def deleteTag(self, index):
        info = attain[index]
        info = info['tag']

    def exportPressed(self, index):
        global selected
        if index not in clicks:
            clicks.append(index)
            selected = index
            print(selected)
        else:
            clicks.remove(index)
            selected = None
        # print(self.table_tag.itemClicked)

    def clickedCheckbox(self):
        global attain
        if self.tab_1.checkBox_all_artifacts.isChecked():
            attain = control.view('')  # empty string for all data
            self.updateTable(attain)

        if self.tab_1.checkBox_keystroke.isChecked():
            attain = control.view('Keystroke')  # keystroke collection
            self.updateTable(attain)

        if self.tab_1.checkBox_mouse_action.isChecked():
            attain = control.view('Mouse Action')
            self.updateTable(attain)
        '''
        ALL OTHER ARTIFACTS FOLLOW THIS PATTERN
    
        if self.tab_1.checkBox_ARTIFACT_NAME.isChecked():
            attain = control.view('ARTIFACT_NAME')   
            self.updateTable(attain)
        '''
'''
*** FLOATING ACCORDING CLASS FOR BEHAVIOR ***
class floatingAccord(QtWidgets.QWidget):
    def __init__(self, form):
        super(floatingAccord, self).__init__()
        ui = Ui_Form()
        ui.setupUi(form)
'''
def main():
    app = QtWidgets.QApplication(sys.argv)
    form = AvertApp()
    form.show()

    Form = QtWidgets.QWidget()
    form2 = Ui_Form()
    form2.setupUi(Form)
    Form.show()
    app.exec()

if __name__ == '__main__':
    main()
