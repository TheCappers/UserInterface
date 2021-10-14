from PyQt5 import QtWidgets, QtCore, QtGui

class DescriptionNetwork:
    def __init__(self) -> None:
        self.descriptionnetwork_tab = QtWidgets.QWidget()
        self.descriptionnetwork_tab.setObjectName("descriptionnetwork_tab")
        self.gridLayout_33 = QtWidgets.QGridLayout(
            self.descriptionnetwork_tab)
        self.gridLayout_33.setObjectName("gridLayout_33")
        self.toolBox = QtWidgets.QToolBox(self.descriptionnetwork_tab)
        self.toolBox.setObjectName("toolBox")
        self.network_1 = QtWidgets.QWidget()
        self.network_1.setGeometry(QtCore.QRect(0, 0, 92, 80))
        self.network_1.setObjectName("network_1")
        self.gridLayout_30 = QtWidgets.QGridLayout(self.network_1)
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.listWidget_4 = QtWidgets.QListWidget(self.network_1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.listWidget_4.setFont(font)
        self.listWidget_4.setObjectName("listWidget_4")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        self.gridLayout_30.addWidget(self.listWidget_4, 0, 0, 1, 1)
        self.toolBox.addItem(self.network_1, "")
        self.network_2 = QtWidgets.QWidget()
        self.network_2.setGeometry(QtCore.QRect(0, 0, 92, 80))
        self.network_2.setObjectName("network_2")
        self.gridLayout_31 = QtWidgets.QGridLayout(self.network_2)
        self.gridLayout_31.setObjectName("gridLayout_31")
        self.listWidget_3 = QtWidgets.QListWidget(self.network_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.listWidget_3.setFont(font)
        self.listWidget_3.setObjectName("listWidget_3")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        self.gridLayout_31.addWidget(self.listWidget_3, 0, 0, 1, 1)
        self.toolBox.addItem(self.network_2, "")
        self.network_3 = QtWidgets.QWidget()
        self.network_3.setGeometry(QtCore.QRect(0, 0, 92, 80))
        self.network_3.setObjectName("network_3")
        self.gridLayout_32 = QtWidgets.QGridLayout(self.network_3)
        self.gridLayout_32.setObjectName("gridLayout_32")
        self.listWidget_2 = QtWidgets.QListWidget(self.network_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.gridLayout_32.addWidget(self.listWidget_2, 0, 0, 1, 1)
        self.toolBox.addItem(self.network_3, "")
        self.gridLayout_33.addWidget(self.toolBox, 0, 0, 1, 1)

        _translate = QtCore.QCoreApplication.translate
        __sortingEnabled = self.listWidget_4.isSortingEnabled()
        self.listWidget_4.setSortingEnabled(False)
        item = self.listWidget_4.item(0)
        item.setText(_translate("MainWindow", "Interface id: 0 (en0)"))
        item = self.listWidget_4.item(1)
        item.setText(
            _translate(
                "MainWindow",
                "Encapsulation type: Ethernet (1)"))
        item = self.listWidget_4.item(2)
        item.setText(
            _translate(
                "MainWindow",
                "Arrival Time: Sep 12, 2021 15:26:42.576923000 MDT"))
        item = self.listWidget_4.item(3)
        item.setText(
            _translate(
                "MainWindow",
                "[Time shift for this packet: 0.000000000 seconds]"))
        item = self.listWidget_4.item(4)
        item.setText(
            _translate(
                "MainWindow",
                "Epoch Time: 1631482002.576923000 seconds"))
        item = self.listWidget_4.item(5)
        item.setText(
            _translate(
                "MainWindow",
                "[Time delta from previous captured frame: 0.034637000 seconds]"))
        item = self.listWidget_4.item(6)
        item.setText(
            _translate(
                "MainWindow",
                "[Time delta from previous displayed frame: 0.034637000 seconds]"))
        item = self.listWidget_4.item(7)
        item.setText(
            _translate(
                "MainWindow",
                "[Time since reference or first frame: 23.113211000 seconds]"))
        item = self.listWidget_4.item(8)
        item.setText(_translate("MainWindow", "Frame Number: 107"))
        item = self.listWidget_4.item(9)
        item.setText(
            _translate(
                "MainWindow",
                "Frame Length: 121 bytes (968 bits)"))
        item = self.listWidget_4.item(10)
        item.setText(
            _translate(
                "MainWindow",
                "Capture Length: 121 bytes (968 bits)"))
        item = self.listWidget_4.item(11)
        item.setText(_translate("MainWindow", "[Frame is marked: False]"))
        item = self.listWidget_4.item(12)
        item.setText(_translate("MainWindow", "[Frame is ignored: False]"))
        item = self.listWidget_4.item(13)
        item.setText(
            _translate(
                "MainWindow",
                "[Protocols in frame: eth:ethertype:data]"))
        item = self.listWidget_4.item(14)
        item.setText(
            _translate(
                "MainWindow",
                "[Coloring Rule Name: Broadcast]"))
        item = self.listWidget_4.item(15)
        item.setText(
            _translate(
                "MainWindow",
                "[Coloring Rule String: eth[0] & 1]"))
        self.listWidget_4.setSortingEnabled(__sortingEnabled)
        self.toolBox.setItemText(
            self.toolBox.indexOf(
                self.network_1),
            _translate(
                "MainWindow",
                "Frame 107: 121 bytes on wire (968 bits), 121 bytes captured (968 bits) on interface en0, id 0"))
        __sortingEnabled = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        item = self.listWidget_3.item(0)
        item.setText(
            _translate(
                "MainWindow",
                "Destination: Broadcast (ff:ff:ff:ff:ff:ff)"))
        item = self.listWidget_3.item(1)
        item.setText(
            _translate(
                "MainWindow",
                "Source: 86:ef:16:75:3c:23 (86:ef:16:75:3c:23)"))
        item = self.listWidget_3.item(2)
        item.setText(_translate("MainWindow", "Type: Unknown (0x7373)"))
        self.listWidget_3.setSortingEnabled(__sortingEnabled)
        self.toolBox.setItemText(
            self.toolBox.indexOf(
                self.network_2),
            _translate(
                "MainWindow",
                "Ethernet II, Src: 86:ef:16:75:3c:23 (86:ef:16:75:3c:23), Dst: Broadcast(ff:ff:ff:ff:ff:ff)"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(
            _translate(
                "MainWindow",
                "Data: 121100000043f5cb114103ac1b368f8013380a496e868dc52e97008cbead8ae5402c46ef…"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("MainWindow", "[Length: 107]"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.toolBox.setItemText(
            self.toolBox.indexOf(
                self.network_3), _translate(
                "MainWindow", "Data (107 Bytes)"))

    def get_tab(self):
        return self.descriptionnetwork_tab