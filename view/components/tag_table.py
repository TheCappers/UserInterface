from PyQt5 import QtCore, QtWidgets


class TagTable:
    def __init__(self):
        self.tag_table = ''  # empty values
        self.indexSelected = 0

    def setIndexSelected(self, index):
        self.indexSelected = index

    def getIndexSelected(self):
        return self.indexSelected

    def startTable(self, tag_table):  # initiation of the table
        self.tag_table = tag_table  # must begin with table created already
        self.tag_table.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tag_table.setAcceptDrops(False)
        self.tag_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tag_table.setAlternatingRowColors(True)
        self.tag_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tag_table.setCornerButtonEnabled(True)

        self.tag_table.setRowCount(1)
        self.tag_table.setObjectName('tag_table')  # name the item

        ''' ADDING COLUMNS  '''
        self.tag_table.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tag_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tag_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tag_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tag_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tag_table.setHorizontalHeaderItem(3, item)

        ''' FILLING OUT COLUMNS '''
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tag_table.setItem(0, 0, item)  # fill column 0

        item = QtWidgets.QTableWidgetItem()
        self.tag_table.setItem(0, 1, item)  # fill column 1-3
        item = QtWidgets.QTableWidgetItem()
        self.tag_table.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tag_table.setItem(0, 3, item)

        '''  TABLE VALUES AND DETAILS '''
        self.tag_table.horizontalHeader().setCascadingSectionResizes(True)
        self.tag_table.horizontalHeader().setDefaultSectionSize(200)
        self.tag_table.horizontalHeader().setMinimumSectionSize(200)
        self.tag_table.horizontalHeader().setSortIndicatorShown(True)
        self.tag_table.horizontalHeader().setStretchLastSection(True)
        self.tag_table.verticalHeader().setVisible(False)

        '''' SETTING THE TEXT '''
        _translate = QtCore.QCoreApplication.translate  # translate Qt

        item = self.tag_table.horizontalHeaderItem(0)
        item.setText(_translate('MainWindow', ''))

        item = self.tag_table.horizontalHeaderItem(1)
        item.setText(_translate('', 'IP Address'))

        item = self.tag_table.horizontalHeaderItem(2)
        item.setText(_translate('MainWindow', 'MAC Address'))

        item = self.tag_table.horizontalHeaderItem(3)
        item.setText(_translate('MainWindow', 'Tag'))

        return tag_table

    def getTable(self):
        return self.tag_table

    def display_tag(self, selected):  # refresh and update the tags for the item
        if selected:
            self.tag_table.setRowCount(len(selected['tag']))
            _translate = QtCore.QCoreApplication.translate

            ip = selected['ip_address']
            mac = selected['mac_address']
            i = 0
            for tag in selected['tag']:  # iterate through the tags on the item
                item = QtWidgets.QTableWidgetItem()
                item.setCheckState(False)
                self.tag_table.setItem(i, 0, item)
                item = self.tag_table.item(i, 0)
                item.setText(_translate('MainWindow', ''))

                item = QtWidgets.QTableWidgetItem()
                self.tag_table.setItem(i, 1, item)
                item = self.tag_table.item(i, 1)
                item.setText(_translate('MainWindow', ip))

                item = QtWidgets.QTableWidgetItem()
                self.tag_table.setItem(i, 2, item)
                item = self.tag_table.item(i, 2)
                item.setText(_translate('MainWindow', mac))

                item = QtWidgets.QTableWidgetItem()
                self.tag_table.setItem(i, 3, item)
                item = self.tag_table.item(i, 3)
                item.setText(_translate('MainWindow', tag))

                i += 1
