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

        self.gridLayout_24.addWidget(self.description_tab, 0, 0, 1, 1)

    def get_tab(self):
        return self.tab_134

    def display_tab(self, selected):
        self.description_tab.removeTab(0)
        name = ''
        tab_1 = None
        if selected['name'] == 'Keystroke':
            tab_1 = DescriptionKeystroke(selected)
            name = 'Keystroke'

        elif selected['name'] == 'Mouse_Action':
            tab_1 = DescriptionMouse(selected)
            name = 'Mouse Action'

        elif selected['name'] == 'Process':
            tab_1 = DescriptionProcess(selected)
            name = 'Process'

        if tab_1:
            self.description_tab.addTab(tab_1.get_tab(), name)

        
        
