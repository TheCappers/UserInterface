from PyQt5 import QtWidgets, QtCore, QtGui


class DescriptionMouse:
    def __init__(self, selected) -> None:
        self.descriptionmouse_tab = QtWidgets.QWidget()
        self.descriptionmouse_tab.setObjectName("descriptionmouse_tab")
        self.formLayout_9 = QtWidgets.QFormLayout(
            self.descriptionmouse_tab)
        self.formLayout_9.setObjectName("formLayout_9")
        self.frame_6 = QtWidgets.QFrame(self.descriptionmouse_tab)
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_6.setObjectName("frame_6")
        self.formLayout_8 = QtWidgets.QFormLayout(self.frame_6)
        self.formLayout_8.setObjectName("formLayout_8")
        self.descriptionvideo_timestamp_label_41 = QtWidgets.QLabel(
            self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descriptionvideo_timestamp_label_41.setFont(font)
        self.descriptionvideo_timestamp_label_41.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_41.setObjectName(
            "descriptionvideo_timestamp_label_41")
        self.formLayout_8.setWidget(
            0,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_41)
        self.label_80 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_80.setFont(font)
        self.label_80.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_80.setObjectName("label_80")
        self.formLayout_8.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.label_80)
        self.descriptionvideo_timestamp_label_43 = QtWidgets.QLabel(
            self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descriptionvideo_timestamp_label_43.setFont(font)
        self.descriptionvideo_timestamp_label_43.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_43.setObjectName(
            "descriptionvideo_timestamp_label_43")
        self.formLayout_8.setWidget(
            1,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_43)
        self.label_73 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_73.setFont(font)
        self.label_73.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_73.setObjectName("label_73")
        self.formLayout_8.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.label_73)
        self.descriptionvideo_timestamp_label_44 = QtWidgets.QLabel(
            self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descriptionvideo_timestamp_label_44.setFont(font)
        self.descriptionvideo_timestamp_label_44.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_44.setObjectName(
            "descriptionvideo_timestamp_label_44")
        self.formLayout_8.setWidget(
            2,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_44)
        self.label_83 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_83.setFont(font)
        self.label_83.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_83.setObjectName("label_83")
        self.formLayout_8.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.label_83)
        self.descriptionvideo_timestamp_label_log = QtWidgets.QLabel(
            self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descriptionvideo_timestamp_label_log.setFont(font)
        self.descriptionvideo_timestamp_label_log.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_log.setObjectName(
            "descriptionvideo_timestamp_label_log")
        self.formLayout_8.setWidget(
            3,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_log)
        self.label_84 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_84.setFont(font)
        self.label_84.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_84.setObjectName("label_84")
        self.formLayout_8.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.label_84)
        self.descriptionvideo_timestamp_label_37 = QtWidgets.QLabel(
            self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descriptionvideo_timestamp_label_37.setFont(font)
        self.descriptionvideo_timestamp_label_37.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_37.setObjectName(
            "descriptionvideo_timestamp_label_37")
        self.formLayout_8.setWidget(
            4,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_37)
        self.label_79 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_79.setFont(font)
        self.label_79.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_79.setObjectName("label_79")
        self.formLayout_8.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.label_79)
        self.descriptionvideo_timestamp_label_45 = QtWidgets.QLabel(
            self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descriptionvideo_timestamp_label_45.setFont(font)
        self.descriptionvideo_timestamp_label_45.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_45.setObjectName(
            "descriptionvideo_timestamp_label_45")
        self.formLayout_8.setWidget(
            5,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_45)
        self.label_85 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_85.setFont(font)
        self.label_85.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_85.setObjectName("label_85")
        self.formLayout_8.setWidget(
            5, QtWidgets.QFormLayout.FieldRole, self.label_85)
        self.formLayout_9.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.frame_6)

        _translate = QtCore.QCoreApplication.translate
        self.descriptionvideo_timestamp_label_41.setText(
            _translate("MainWindow", "Timestamp:"))
        self.label_80.setText(_translate("MainWindow", selected['timestamp']))
        self.descriptionvideo_timestamp_label_43.setText(
            _translate("MainWindow", "Button:"))
        self.label_73.setText(_translate(
            "MainWindow", 'None' if not selected['data']['clicked'] else selected['data']['button']))
        self.descriptionvideo_timestamp_label_44.setText(
            _translate("MainWindow", "Mouse Action:"))
        self.label_83.setText(_translate("MainWindow", 'Movement' if not selected['data']['clicked'] else 'Click'))
        self.descriptionvideo_timestamp_label_log.setText(
            _translate("MainWindow", "Mouse Action Value:"))
        self.label_84.setText(_translate(
            "MainWindow", str(selected['data']['position'][0]) + ',' + str(selected['data']['position'][1])))
        self.descriptionvideo_timestamp_label_37.setText(
            _translate("MainWindow", "Active Window:"))
        self.label_79.setText(_translate("MainWindow", "terminal"))
        self.descriptionvideo_timestamp_label_45.setText(
            _translate("MainWindow", "Window Focus:"))
        self.label_85.setText(_translate("MainWindow", "terminal"))

    def get_tab(self):
        return self.descriptionmouse_tab
