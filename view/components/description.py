from PyQt5 import QtWidgets, QtCore, QtGui
from view.components.description_history import DescriptionHistory
from view.components.description_keystroke import DescriptionKeystroke
from view.components.description_mouse import DescriptionMouse
from view.components.description_network import DescriptionNetwork
from view.components.description_process import DescriptionProcess
from view.components.description_screenshot import DescriptionScreenshot
from view.components.description_system_call import DescriptionSystemCall

from view.components.description_video import DescriptionVideo


class Description:
    def __init__(self) -> None:
        self.tab_134 = QtWidgets.QWidget()
        self.tab_134.setObjectName("tab_134")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.tab_134)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.description_tab = QtWidgets.QTabWidget(self.tab_134)
        self.description_tab.setMaximumSize(QtCore.QSize(16777215, 500))
        self.description_tab.setFocusPolicy(QtCore.Qt.NoFocus)
        self.description_tab.setAutoFillBackground(False)
        self.description_tab.setUsesScrollButtons(False)
        self.description_tab.setObjectName("description_tab")

        """Description Video"""
        self.descriptionvideo_tab = DescriptionVideo()
        # self.description_tab.addTab(self.descriptionvideo_tab.get_tab(), "")

        """Description Screenshot"""
        self.descriptionstillscreenshot_tab = DescriptionScreenshot()
        # self.description_tab.addTab(self.descriptionstillscreenshot_tab.get_tab(), "")

        """Description System Call"""
        self.descriptionsystemcall_tab = DescriptionSystemCall()
        # self.description_tab.addTab(self.descriptionsystemcall_tab.get_tab(), "")

        """Description Process"""
        self.descriptionprocess_tab = DescriptionProcess()
        # self.description_tab.addTab(self.descriptionprocess_tab.get_tab(), "")

        """Description Window History"""
        self.descriptionwindowhistory_tab = DescriptionHistory()
        # self.description_tab.addTab(self.descriptionwindowhistory_tab.get_tab(), "")

        """Description Network"""
        self.descriptionnetwork_tab = DescriptionNetwork()
        # self.description_tab.addTab(self.descriptionnetwork_tab.get_tab(), "")

        """Description Mouse"""
        self.descriptionmouse_tab = DescriptionMouse()
        # self.description_tab.addTab(self.descriptionmouse_tab.get_tab(), "")

        """Description Keystroke"""
        self.descriptionkeystroke_tab = DescriptionKeystroke()
        # self.description_tab.addTab(self.descriptionkeystroke_tab.get_tab(), "")

        self.gridLayout_24.addWidget(self.description_tab, 0, 0, 1, 1)

        _translate = QtCore.QCoreApplication.translate
        
        self.description_tab.setTabText(
            self.description_tab.indexOf(
                self.descriptionstillscreenshot_tab.get_tab()), _translate(
                "MainWindow", "Still Screenshot"))
        
        self.description_tab.setTabText(
            self.description_tab.indexOf(
                self.descriptionsystemcall_tab.get_tab()), _translate(
                "MainWindow", "System Call"))
        
        self.description_tab.setTabText(
            self.description_tab.indexOf(
                self.descriptionprocess_tab.get_tab()), _translate(
                "MainWindow", "Process"))
        
        self.description_tab.setTabText(
            self.description_tab.indexOf(
                self.descriptionwindowhistory_tab.get_tab()), _translate(
                "MainWindow", "Window History"))
        
        self.description_tab.setTabText(
            self.description_tab.indexOf(
                self.descriptionnetwork_tab.get_tab()), _translate(
                "MainWindow", "Network Packet"))
        
        self.description_tab.setTabText(
            self.description_tab.indexOf(
                self.descriptionmouse_tab.get_tab()), _translate(
                "MainWindow", "Mouse Action"))
        
        self.description_tab.setTabText(
            self.description_tab.indexOf(
                self.descriptionkeystroke_tab.get_tab()), _translate(
                "MainWindow", "Keystroke"))

        self.description_tab.setTabText(
            self.description_tab.indexOf(
                self.descriptionvideo_tab.get_tab()), _translate(
                "MainWindow", "Video"))

    def get_tab(self):
        return self.tab_134
