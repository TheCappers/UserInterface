from PyQt5 import QtCore, QtWidgets
from view.accordion_floating import Ui_Form
from view.avert import Ui_MainWindow
import sys
from controller import controller

# global values
control = controller.Controller()
attain = []
clicks = []
selected = 0


class AvertApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(AvertApp, self).__init__()
        self.setupUi(self)
        # portion for the tag_table
        self.table_tag.setSortingEnabled(1)  # allows for the sorting in the columns

        # automatic on button checked
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
        self.tag_add_button.clicked.connect(self.add_row)
        self.universalRecord.clicked.connect(self.universalButton)
        
        self.pushButton_18.clicked.connect(self.add_annotation)

        # threshold changing
        self.StorageInValue.textEdited.connect(self.thresholdChange)

        # search button being activated
        self.search_button.clicked.connect(self.searchPressed)

        # export button being activated
        self.exportButton.clicked.connect(self.exportPressed)

        
        self.table_result.avert_result_table.cellClicked.connect(self.annotationTest)



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

        if self.sender().objectName().__contains__("Video") and self.sender().objectName().__contains__('Off'):
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
            
    def add_annotation(self):  # add a row when the button add is selected
        """
        create new row in the qwidget table within tag area of
        detailed view
        :return: none
        """
        row_position = self.annotation_table.rowCount()  # the total rows

        rest_item = QtWidgets.QTableWidgetItem()
        rest_item.setFlags(QtCore.Qt.ItemIsSelectable)
        rest_item1 = QtWidgets.QTableWidgetItem()
        rest_item1.setFlags(QtCore.Qt.ItemIsSelectable)
        rest_item2 = QtWidgets.QTableWidgetItem()
        rest_item2.setFlags(QtCore.Qt.ItemIsSelectable)
        rest_item2.setText(self.annotation_text.toPlainText())


        self.annotation_table.insertRow(row_position)
        self.annotation_table.setItem(row_position, 0, rest_item)
        self.annotation_table.setItem(row_position, 1, rest_item1)
        self.annotation_table.setItem(row_position, 2, rest_item2)


    def add_row(self):  # add a row when the button add is selected
        """
        create new row in the qwidget table within tag area of
        detailed view
        :return: none
        """
        row_position = self.table_tag.rowCount()  # the total rows

        check_item = QtWidgets.QTableWidgetItem()
        check_item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        check_item.setCheckState(QtCore.Qt.Unchecked)
        rest_item = QtWidgets.QTableWidgetItem()
        rest_item.setFlags(QtCore.Qt.ItemIsSelectable)

        self.table_tag.insertRow(row_position)
        self.table_tag.setItem(row_position, 0, check_item)
        self.table_tag.setItem(row_position, 1, rest_item)
        self.table_tag.setItem(row_position, 2, check_item)

    def universalButton(self):
        if self.universalRecord.isChecked():  # if on
            control.universalRecording(True)
            '''
             change the text and checked from the press on the universal record button
             will check and uncheck the config buttons
             GUI CHANGES
             '''
            self.universalRecord.setText('Record On')

            # check all the on buttons and uncheck the offs
            self.VideoStatOnButton.setChecked(1)  # check the button we clicked
            self.VideoStatusOffButton.setChecked(0)  # check false the off button incase it is checked
            self.ScreenshotStatOnButton.setChecked(1)  # check the button we clicked
            self.ScreenshotStatOffButton.setChecked(0)  # check false the off button incase it is checked
            self.SystemCallOnButton.setChecked(1)  # check the button we clicked
            self.SystemCallOffButton.setChecked(0)  # check false the off button incase it is checked
            self.WindowHistoryOnButton.setChecked(1)  # check the button we clicked
            self.WindowHistoryOffButton.setChecked(0)  # check false the off button incase it is checked
            self.KeyStrokeStatOnButton.setChecked(1)  # check the button we clicked
            self.KeyStrokeStatOffButton.setChecked(0)  # check false the off button incase it is checked
            self.MouseActOnButton.setChecked(1)  # check the button we clicked
            self.MouseActOffButton.setChecked(0)  # check false the off button incase it is checked
            self.NetworkActivityDataOnButton.setChecked(1)  # check the button we clicked
            self.NetworkActivityDataOffButton.setChecked(0)  # check false the off button incase it is checked
            self.ProcessStatOnButton.setChecked(1)  # check the button we clicked
            self.ProcessStatOffButton.setChecked(0)  # check false the off button incase it is checked
        else:  # if off
            control.universalRecording(False)
            '''
             change the text and checked from the press on the universal record button
             will check and uncheck the config buttons
             GUI CHANGES
             '''
            self.universalRecord.setText('Record Off')
            # check all the off buttons and uncheck ons

            self.VideoStatOnButton.setChecked(0)  # check off the on button
            self.VideoStatusOffButton.setChecked(1)  # check on the off button
            self.ScreenshotStatOnButton.setChecked(0)  # check off the on button
            self.ScreenshotStatOffButton.setChecked(1)  # check on the off button
            self.SystemCallOnButton.setChecked(0)  # check off the on button
            self.SystemCallOffButton.setChecked(1)  # check on the off button
            self.WindowHistoryOnButton.setChecked(0)  # check off the on button
            self.WindowHistoryOffButton.setChecked(1)  # check on the off button
            self.KeyStrokeStatOnButton.setChecked(0)  # check off the on button
            self.KeyStrokeStatOffButton.setChecked(1)  # check on the off button
            self.MouseActOnButton.setChecked(0)  # check off the on button
            self.MouseActOffButton.setChecked(1)  # check on the off button
            self.NetworkActivityDataOnButton.setChecked(0)  # check off the on button
            self.NetworkActivityDataOffButton.setChecked(1)  # check on the off button
            self.ProcessStatOnButton.setChecked(0)  # check off the on button
            self.ProcessStatOffButton.setChecked(1)  # check on the off button

    def thresholdChange(self):
        if self.StorageInValue.text() == '':  # in case empty
            control.storageRecording(70)  # set to default as user inputs full number
        else:
            full = control.storageRecording(float(self.StorageInValue.text()))  # send the value
            if full:
                QtWidgets.QMessageBox.about(self, 'Storage Alert', 'Storage is full')

    def searchPressed(self):  # once search is pressed we must search the given data
        # attain the the value in the search box
        global attain
        search = self.search_expression_bar.text()  # attain the text
        attain = control.view(search)
        self.updateTable(attain)

        # table_result.populateTable(attain)
        # print(attain)
        # ResultTable().populateTable(self, attain)

    def annotationTest(self):
        print('hello')
        global selected, attain
        print(selected)
        self.annotation_table.display_annotation(attain[selected])
        print('after hello')
        # if index not in clicks:
        #     clicks.append(index)
        #     selected = index
        #     print(selected)
        # else:
        #     clicks.remove(index)
        #     selected = None

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
