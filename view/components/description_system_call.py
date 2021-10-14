from PyQt5 import QtWidgets, QtCore, QtGui

class DescriptionSystemCall:
    def __init__(self) -> None:
        self.descriptionsystemcall_tab = QtWidgets.QWidget()
        self.descriptionsystemcall_tab.setObjectName(
            "descriptionsystemcall_tab")
        self.gridLayout_25 = QtWidgets.QGridLayout(
            self.descriptionsystemcall_tab)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.frame_5 = QtWidgets.QFrame(self.descriptionsystemcall_tab)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.formLayout_7 = QtWidgets.QFormLayout(self.frame_5)
        self.formLayout_7.setHorizontalSpacing(40)
        self.formLayout_7.setObjectName("formLayout_7")
        self.descriptionvideo_timestamp_label_8 = QtWidgets.QLabel(
            self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descriptionvideo_timestamp_label_8.setFont(font)
        self.descriptionvideo_timestamp_label_8.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_8.setObjectName(
            "descriptionvideo_timestamp_label_8")
        self.formLayout_7.setWidget(
            0,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_8)
        self.label_49 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_49.setFont(font)
        self.label_49.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_49.setObjectName("label_49")
        self.formLayout_7.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.label_49)
        self.descriptionvideo_timestamp_label_10 = QtWidgets.QLabel(
            self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descriptionvideo_timestamp_label_10.setFont(font)
        self.descriptionvideo_timestamp_label_10.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_10.setObjectName(
            "descriptionvideo_timestamp_label_10")
        self.formLayout_7.setWidget(
            1,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_10)
        self.label_50 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_50.setFont(font)
        self.label_50.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_50.setObjectName("label_50")
        self.formLayout_7.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.label_50)
        self.descriptionvideo_timestamp_label_9 = QtWidgets.QLabel(
            self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descriptionvideo_timestamp_label_9.setFont(font)
        self.descriptionvideo_timestamp_label_9.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_9.setObjectName(
            "descriptionvideo_timestamp_label_9")
        self.formLayout_7.setWidget(
            2,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_9)
        self.label_48 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_48.setFont(font)
        self.label_48.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_48.setObjectName("label_48")
        self.formLayout_7.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.label_48)
        self.descriptionvideo_timestamp_label_user_profile = QtWidgets.QLabel(
            self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descriptionvideo_timestamp_label_user_profile.setFont(font)
        self.descriptionvideo_timestamp_label_user_profile.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_user_profile.setObjectName(
            "descriptionvideo_timestamp_label_user_profile")
        self.formLayout_7.setWidget(
            3,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_user_profile)
        self.label_52 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_52.setFont(font)
        self.label_52.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_52.setObjectName("label_52")
        self.formLayout_7.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.label_52)
        self.descriptionvideo_timestamp_label_filters = QtWidgets.QLabel(
            self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descriptionvideo_timestamp_label_filters.setFont(font)
        self.descriptionvideo_timestamp_label_filters.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_filters.setObjectName(
            "descriptionvideo_timestamp_label_filters")
        self.formLayout_7.setWidget(
            4,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_filters)
        self.label_53 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_53.setFont(font)
        self.label_53.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_53.setObjectName("label_53")
        self.formLayout_7.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.label_53)
        self.gridLayout_25.addWidget(self.frame_5, 0, 0, 1, 1)

        _translate = QtCore.QCoreApplication.translate
        self.descriptionvideo_timestamp_label_8.setText(
            _translate("MainWindow", "Timestamp:"))
        self.label_49.setText(_translate("MainWindow", "10-6-26 02:31:29"))
        self.descriptionvideo_timestamp_label_10.setText(
            _translate("MainWindow", "System Call Name:"))
        self.label_50.setText(
            _translate(
                "MainWindow",
                "systcall_getdents"))
        self.descriptionvideo_timestamp_label_9.setText(
            _translate("MainWindow", "System Call Argument:"))
        self.label_48.setText(_translate("MainWindow", "None"))
        self.descriptionvideo_timestamp_label_user_profile.setText(
            _translate("MainWindow", "System Call Return Value:"))
        self.label_52.setText(_translate("MainWindow", "d_type"))
        self.descriptionvideo_timestamp_label_filters.setText(
            _translate("MainWindow", "System Call Type:"))
        self.label_53.setText(_translate("MainWindow", "Process Control"))

    def get_tab(self):
        return self.descriptionsystemcall_tab