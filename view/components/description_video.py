from PyQt5 import QtWidgets, QtCore, QtGui

class DescriptionVideo:
    def __init__(self, selected) -> None:
        self.descriptionvideo_tab = QtWidgets.QWidget()
        self.descriptionvideo_tab.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.descriptionvideo_tab.setObjectName("descriptionvideo_tab")
        self.gridLayout_26 = QtWidgets.QGridLayout(
            self.descriptionvideo_tab)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.descriptionvideo_frame = QtWidgets.QFrame(
            self.descriptionvideo_tab)
        self.descriptionvideo_frame.setMinimumSize(QtCore.QSize(400, 395))
        self.descriptionvideo_frame.setMaximumSize(
            QtCore.QSize(500, 16777215))
        self.descriptionvideo_frame.setFrameShape(
            QtWidgets.QFrame.StyledPanel)
        self.descriptionvideo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.descriptionvideo_frame.setObjectName("descriptionvideo_frame")
        self.gridLayout_28 = QtWidgets.QGridLayout(
            self.descriptionvideo_frame)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.label_88 = QtWidgets.QLabel(self.descriptionvideo_frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum,
            QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(
            self.label_88.sizePolicy().hasHeightForWidth())
        self.label_88.setSizePolicy(sizePolicy)
        self.label_88.setObjectName("label_88")
        self.gridLayout_28.addWidget(self.label_88, 0, 0, 1, 1)
        self.gridLayout_26.addWidget(
            self.descriptionvideo_frame, 0, 0, 1, 1)
        self.descriptionvideo_info = QtWidgets.QFrame(
            self.descriptionvideo_tab)
        self.descriptionvideo_info.setFrameShape(
            QtWidgets.QFrame.StyledPanel)
        self.descriptionvideo_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.descriptionvideo_info.setObjectName("descriptionvideo_info")
        self.formLayout_2 = QtWidgets.QFormLayout(
            self.descriptionvideo_info)
        self.formLayout_2.setHorizontalSpacing(40)
        self.formLayout_2.setObjectName("formLayout_2")
        self.descriptionvideo_timestamp_label = QtWidgets.QLabel(
            self.descriptionvideo_info)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descriptionvideo_timestamp_label.setFont(font)
        self.descriptionvideo_timestamp_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label.setObjectName(
            "descriptionvideo_timestamp_label")
        self.formLayout_2.setWidget(0,
                                    QtWidgets.QFormLayout.LabelRole,
                                    self.descriptionvideo_timestamp_label)
        self.label_41 = QtWidgets.QLabel(self.descriptionvideo_info)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_41.setFont(font)
        self.label_41.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_41.setObjectName("label_41")
        self.formLayout_2.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.label_41)
        self.descriptionvideo_timestamp_label_2 = QtWidgets.QLabel(
            self.descriptionvideo_info)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descriptionvideo_timestamp_label_2.setFont(font)
        self.descriptionvideo_timestamp_label_2.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_2.setObjectName(
            "descriptionvideo_timestamp_label_2")
        self.formLayout_2.setWidget(
            1,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_2)
        self.label_42 = QtWidgets.QLabel(self.descriptionvideo_info)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_42.setFont(font)
        self.label_42.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_42.setObjectName("label_42")
        self.formLayout_2.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.label_42)
        self.descriptionvideo_timestamp_label_3 = QtWidgets.QLabel(
            self.descriptionvideo_info)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descriptionvideo_timestamp_label_3.setFont(font)
        self.descriptionvideo_timestamp_label_3.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_3.setObjectName(
            "descriptionvideo_timestamp_label_3")
        self.formLayout_2.setWidget(
            2,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_3)
        self.label_43 = QtWidgets.QLabel(self.descriptionvideo_info)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_43.setFont(font)
        self.label_43.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_43.setObjectName("label_43")
        self.formLayout_2.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.label_43)
        self.descriptionvideo_timestamp_label_4 = QtWidgets.QLabel(
            self.descriptionvideo_info)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descriptionvideo_timestamp_label_4.setFont(font)
        self.descriptionvideo_timestamp_label_4.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_4.setObjectName(
            "descriptionvideo_timestamp_label_4")
        self.formLayout_2.setWidget(
            3,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_4)
        self.label_44 = QtWidgets.QLabel(self.descriptionvideo_info)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_44.setFont(font)
        self.label_44.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_44.setObjectName("label_44")
        self.formLayout_2.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.label_44)
        self.gridLayout_26.addWidget(
            self.descriptionvideo_info, 0, 1, 1, 1)

        _translate = QtCore.QCoreApplication.translate
        self.label_88.setText(
            _translate(
                "MainWindow",
                "<html><head/><body><p><img src=\":/pics_for_detailedview/video_detailedview.png\"/></p></body></html>"))
        self.descriptionvideo_timestamp_label.setText(
            _translate("MainWindow", "Timestamp:"))
        self.label_41.setText(_translate("MainWindow", selected['timestamp']))
        self.descriptionvideo_timestamp_label_2.setText(
            _translate("MainWindow", "Video Size:"))
        self.label_42.setText(_translate("MainWindow", selected['data']['size']))
        self.descriptionvideo_timestamp_label_3.setText(
            _translate("MainWindow", "Video Resolution:"))
        self.label_43.setText(_translate("MainWindow", selected['data']['dimensions']))
        self.descriptionvideo_timestamp_label_4.setText(
            _translate("MainWindow", "Video Frame Rate:"))
        self.label_44.setText(_translate("MainWindow", selected['data']['framerate']))

    def get_tab(self):
        return self.descriptionvideo_tab