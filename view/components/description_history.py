from PyQt5 import QtWidgets, QtCore, QtGui

class DescriptionHistory:
    def __init__(self, selected) -> None:
        self.descriptionwindowhistory_tab = QtWidgets.QWidget()
        self.descriptionwindowhistory_tab.setObjectName(
            "descriptionwindowhistory_tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(
            self.descriptionwindowhistory_tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_10 = QtWidgets.QFrame(self.descriptionwindowhistory_tab)
        self.frame_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_10.setObjectName("frame_10")
        self.formLayout_6 = QtWidgets.QFormLayout(self.frame_10)
        self.formLayout_6.setHorizontalSpacing(40)
        self.formLayout_6.setObjectName("formLayout_6")
        self.descriptionvideo_timestamp_label_42 = QtWidgets.QLabel(
            self.frame_10)
        self.descriptionvideo_timestamp_label_42.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_42.setObjectName(
            "descriptionvideo_timestamp_label_42")
        self.formLayout_6.setWidget(
            0,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_42)
        self.label_68 = QtWidgets.QLabel(self.frame_10)
        self.label_68.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_68.setObjectName("label_68")
        self.formLayout_6.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.label_68)
        self.descriptionvideo_timestamp_label_36 = QtWidgets.QLabel(
            self.frame_10)
        self.descriptionvideo_timestamp_label_36.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_36.setObjectName(
            "descriptionvideo_timestamp_label_36")
        self.formLayout_6.setWidget(
            1,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_36)
        self.label_81 = QtWidgets.QLabel(self.frame_10)
        self.label_81.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_81.setObjectName("label_81")
        self.formLayout_6.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.label_81)
        self.descriptionvideo_timestamp_label_33 = QtWidgets.QLabel(
            self.frame_10)
        self.descriptionvideo_timestamp_label_33.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_33.setObjectName(
            "descriptionvideo_timestamp_label_33")
        self.formLayout_6.setWidget(
            2,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_33)
        self.label_70 = QtWidgets.QLabel(self.frame_10)
        self.label_70.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_70.setObjectName("label_70")
        self.formLayout_6.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.label_70)
        self.descriptionvideo_timestamp_label_date_time = QtWidgets.QLabel(
            self.frame_10)
        self.descriptionvideo_timestamp_label_date_time.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_date_time.setObjectName(
            "descriptionvideo_timestamp_label_date_time")
        self.formLayout_6.setWidget(
            3,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_date_time)
        self.label_82 = QtWidgets.QLabel(self.frame_10)
        self.label_82.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_82.setObjectName("label_82")
        self.formLayout_6.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.label_82)
        self.descriptionvideo_timestamp_label_38 = QtWidgets.QLabel(
            self.frame_10)
        self.descriptionvideo_timestamp_label_38.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_38.setObjectName(
            "descriptionvideo_timestamp_label_38")
        self.formLayout_6.setWidget(
            4,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_38)
        self.label_78 = QtWidgets.QLabel(self.frame_10)
        self.label_78.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_78.setObjectName("label_78")
        self.formLayout_6.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.label_78)
        self.descriptionvideo_timestamp_label_40 = QtWidgets.QLabel(
            self.frame_10)
        self.descriptionvideo_timestamp_label_40.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_40.setObjectName(
            "descriptionvideo_timestamp_label_40")
        self.formLayout_6.setWidget(
            5,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_40)
        self.label_75 = QtWidgets.QLabel(self.frame_10)
        self.label_75.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_75.setObjectName("label_75")
        self.formLayout_6.setWidget(
            5, QtWidgets.QFormLayout.FieldRole, self.label_75)
        self.descriptionvideo_timestamp_label_34 = QtWidgets.QLabel(
            self.frame_10)
        self.descriptionvideo_timestamp_label_34.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_34.setObjectName(
            "descriptionvideo_timestamp_label_34")
        self.formLayout_6.setWidget(
            6,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_34)
        self.label_77 = QtWidgets.QLabel(self.frame_10)
        self.label_77.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_77.setObjectName("label_77")
        self.formLayout_6.setWidget(
            6, QtWidgets.QFormLayout.FieldRole, self.label_77)
        self.descriptionvideo_timestamp_label_value_date_time = QtWidgets.QLabel(
            self.frame_10)
        self.descriptionvideo_timestamp_label_value_date_time.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_value_date_time.setObjectName(
            "descriptionvideo_timestamp_label_value_date_time")
        self.formLayout_6.setWidget(
            7,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_value_date_time)
        self.label_71 = QtWidgets.QLabel(self.frame_10)
        self.label_71.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_71.setObjectName("label_71")
        self.formLayout_6.setWidget(
            7, QtWidgets.QFormLayout.FieldRole, self.label_71)
        self.descriptionvideo_timestamp_label_39 = QtWidgets.QLabel(
            self.frame_10)
        self.descriptionvideo_timestamp_label_39.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_39.setObjectName(
            "descriptionvideo_timestamp_label_39")
        self.formLayout_6.setWidget(
            8,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_39)
        self.label_69 = QtWidgets.QLabel(self.frame_10)
        self.label_69.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_69.setObjectName("label_69")
        self.formLayout_6.setWidget(
            8, QtWidgets.QFormLayout.FieldRole, self.label_69)
        self.descriptionvideo_timestamp_label_31 = QtWidgets.QLabel(
            self.frame_10)
        self.descriptionvideo_timestamp_label_31.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_31.setObjectName(
            "descriptionvideo_timestamp_label_31")
        self.formLayout_6.setWidget(
            9,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_31)
        self.label_74 = QtWidgets.QLabel(self.frame_10)
        self.label_74.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_74.setObjectName("label_74")
        self.formLayout_6.setWidget(
            9, QtWidgets.QFormLayout.FieldRole, self.label_74)
        self.descriptionvideo_timestamp_label_32 = QtWidgets.QLabel(
            self.frame_10)
        self.descriptionvideo_timestamp_label_32.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_32.setObjectName(
            "descriptionvideo_timestamp_label_32")
        self.formLayout_6.setWidget(
            10,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_32)
        self.label_72 = QtWidgets.QLabel(self.frame_10)
        self.label_72.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_72.setObjectName("label_72")
        self.formLayout_6.setWidget(
            10, QtWidgets.QFormLayout.FieldRole, self.label_72)
        self.descriptionvideo_timestamp_label_35 = QtWidgets.QLabel(
            self.frame_10)
        self.descriptionvideo_timestamp_label_35.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_35.setObjectName(
            "descriptionvideo_timestamp_label_35")
        self.formLayout_6.setWidget(
            11,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_35)
        self.label_76 = QtWidgets.QLabel(self.frame_10)
        self.label_76.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_76.setObjectName("label_76")
        self.formLayout_6.setWidget(
            11, QtWidgets.QFormLayout.FieldRole, self.label_76)

        self.verticalLayout_5.addWidget(
            self.frame_10, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        _translate = QtCore.QCoreApplication.translate
        self.descriptionvideo_timestamp_label_42.setText(
            _translate("MainWindow", "Window Placement Command:"))
        self.label_68.setText(_translate("MainWindow", "10-6-26 02:31:29"))
        self.descriptionvideo_timestamp_label_36.setText(
            _translate("MainWindow", "Minimized:"))
        self.label_81.setText(_translate("MainWindow", "False"))
        self.descriptionvideo_timestamp_label_33.setText(
            _translate("MainWindow", "Maximized:"))
        self.label_70.setText(_translate("MainWindow", "False"))
        self.descriptionvideo_timestamp_label_date_time.setText(
            _translate("MainWindow", "Application Name:"))
        self.label_82.setText(_translate("MainWindow", "AVERT"))
        self.descriptionvideo_timestamp_label_38.setText(
            _translate("MainWindow", "Timestamp:"))
        self.label_78.setText(_translate("MainWindow", "10-6-26 02:31:29"))
        self.descriptionvideo_timestamp_label_40.setText(
            _translate("MainWindow", "Window Position:"))
        self.label_75.setText(_translate("MainWindow", "0, 1860, 0, 1543"))
        self.descriptionvideo_timestamp_label_34.setText(
            _translate("MainWindow", "Primary Screen Resolution:"))
        self.label_77.setText(_translate("MainWindow", "1860, 1543"))
        self.descriptionvideo_timestamp_label_value_date_time.setText(
            _translate("MainWindow", "Visible:"))
        self.label_71.setText(_translate("MainWindow", "True"))
        self.descriptionvideo_timestamp_label_39.setText(
            _translate("MainWindow", "Window Style:"))
        self.label_69.setText(_translate("MainWindow", "10-6-26 02:31:29"))
        self.descriptionvideo_timestamp_label_31.setText(
            _translate("MainWindow", "Window Title:"))
        self.label_74.setText(_translate("MainWindow", "avert"))
        self.descriptionvideo_timestamp_label_32.setText(
            _translate("MainWindow", "Window Creation Time:"))
        self.label_72.setText(_translate("MainWindow", "10-6-26 02:31:29"))
        self.descriptionvideo_timestamp_label_35.setText(
            _translate("MainWindow", "Window Destruction Time:"))
        self.label_76.setText(_translate("MainWindow", "10-6-26 02:35:29"))

    def get_tab(self):
        return self.descriptionwindowhistory_tab