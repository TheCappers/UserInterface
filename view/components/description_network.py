from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QScrollArea

# class for scrollable label
class ScrollLabel(QScrollArea):
    # constructor
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)
        # making widget resizable
        self.setWidgetResizable(True)
        # making qwidget object
        content = QtWidgets.QWidget(self)
        self.setWidget(content)
        # vertical box layout
        lay = QtWidgets.QVBoxLayout(content)
        # creating label
        self.label = QtWidgets.QLabel(content)
        # setting alignment to the text
        self.label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        # making label multi-line
        self.label.setWordWrap(True) 
        # adding label to the layout
        lay.addWidget(self.label)

    # the setText method
    def setText(self, text):
        # setting text to the label
        self.label.setText(text)


class DescriptionNetwork:
    def __init__(self, selected) -> None:
        self.descriptionnetwork_tab = QtWidgets.QWidget()
        self.gridLayout_33 = QtWidgets.QGridLayout(
            self.descriptionnetwork_tab)
        
        self.toolBox = QtWidgets.QToolBox(self.descriptionnetwork_tab)
        self.network_1 = QtWidgets.QWidget()
        self.network_1.setGeometry(QtCore.QRect(0, 0, 92, 80))
        self.gridLayout_30 = QtWidgets.QGridLayout(self.network_1)
        self.label = ScrollLabel(self.network_1)
        self.label.setWidgetResizable(True)
        self.label.setText(selected['tree'])
        self.gridLayout_30.addWidget(self.label)

        self.toolBox.addItem(self.network_1, "Tree")

        self.network_2 = QtWidgets.QWidget()
        self.network_2.setGeometry(QtCore.QRect(0, 0, 92, 80))
        self.gridLayout_31 = QtWidgets.QGridLayout(self.network_2)
        self.listWidget_3 = QtWidgets.QListWidget(self.network_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.listWidget_3.setFont(font)

        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)

        self.gridLayout_31.addWidget(self.listWidget_3, 0, 0, 1, 1)
        self.toolBox.addItem(self.network_2, "Raw Data")

        self.gridLayout_33.addWidget(self.toolBox, 0, 0, 1, 1)

        _translate = QtCore.QCoreApplication.translate

        item = self.listWidget_3.item(0)
        item.setText(_translate("MainWindow", selected['raw_hex']))

    def get_tab(self):
        return self.descriptionnetwork_tab
