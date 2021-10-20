from PyQt5 import QtWidgets, QtCore, QtGui

class DescriptionScreenshot:
    def __init__(self, selected) -> None:
        self.descriptionstillscreenshot_tab = QtWidgets.QWidget()
        self.descriptionstillscreenshot_tab.setObjectName(
            "descriptionstillscreenshot_tab")
        self.gridLayout_27 = QtWidgets.QGridLayout(
            self.descriptionstillscreenshot_tab)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.descriptionvideo_frame_2 = QtWidgets.QFrame(
            self.descriptionstillscreenshot_tab)
        self.descriptionvideo_frame_2.setMaximumSize(
            QtCore.QSize(500, 16777215))
        self.descriptionvideo_frame_2.setFrameShape(
            QtWidgets.QFrame.StyledPanel)
        self.descriptionvideo_frame_2.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.descriptionvideo_frame_2.setObjectName(
            "descriptionvideo_frame_2")
        self.gridLayout_29 = QtWidgets.QGridLayout(
            self.descriptionvideo_frame_2)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.label_89 = QtWidgets.QLabel(self.descriptionvideo_frame_2)
        self.label_89.setMinimumSize(QtCore.QSize(400, 379))
        self.label_89.setObjectName("label_89")
        image = QtGui.QPixmap(selected['data']['path'])
        image = image.scaled(200,200,QtCore.Qt.KeepAspectRatio)
        self.label_89.setPixmap(QtGui.QPixmap(selected['data']['path']))
        self.gridLayout_29.addWidget(self.label_89, 0, 0, 1, 1)
        self.gridLayout_27.addWidget(
            self.descriptionvideo_frame_2, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.descriptionstillscreenshot_tab)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout_3 = QtWidgets.QFormLayout(self.frame)
        self.formLayout_3.setHorizontalSpacing(40)
        self.formLayout_3.setObjectName("formLayout_3")
        self.descriptionvideo_timestamp_label_7 = QtWidgets.QLabel(
            self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descriptionvideo_timestamp_label_7.setFont(font)
        self.descriptionvideo_timestamp_label_7.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_7.setObjectName(
            "descriptionvideo_timestamp_label_7")
        self.formLayout_3.setWidget(
            0,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_7)
        self.label_47 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_47.setFont(font)
        self.label_47.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_47.setObjectName("label_47")
        self.formLayout_3.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.label_47)
        self.descriptionvideo_timestamp_label_6 = QtWidgets.QLabel(
            self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descriptionvideo_timestamp_label_6.setFont(font)
        self.descriptionvideo_timestamp_label_6.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_6.setObjectName(
            "descriptionvideo_timestamp_label_6")
        self.formLayout_3.setWidget(
            1,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_6)
        self.label_46 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_46.setFont(font)
        self.label_46.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_46.setObjectName("label_46")
        self.formLayout_3.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.label_46)
        self.descriptionvideo_timestamp_label_5 = QtWidgets.QLabel(
            self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descriptionvideo_timestamp_label_5.setFont(font)
        self.descriptionvideo_timestamp_label_5.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_5.setObjectName(
            "descriptionvideo_timestamp_label_5")
        self.formLayout_3.setWidget(
            2,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_5)
        self.label_45 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_45.setFont(font)
        self.label_45.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_45.setObjectName("label_45")
        self.formLayout_3.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.label_45)
        self.gridLayout_27.addWidget(self.frame, 0, 1, 1, 1)

        _translate = QtCore.QCoreApplication.translate
        # self.label_89.setText(
        #     _translate(
        #         "MainWindow",
        #         "<html><head/><body><p><img src=\":/pics_for_detailedview/stillscreenshot_detailedview.jpg\"/></p></body></html>"))
        self.descriptionvideo_timestamp_label_7.setText(
            _translate("MainWindow", "Timestamp:"))
        self.label_47.setText(_translate("MainWindow", selected['timestamp']))
        self.descriptionvideo_timestamp_label_6.setText(
            _translate("MainWindow", "Still Screenshot Size:"))
        self.label_46.setText(_translate("MainWindow", str(selected['data']['size']) + "b"))
        self.descriptionvideo_timestamp_label_5.setText(
            _translate("MainWindow", "Still Screenshot Format:"))
        self.label_45.setText(_translate("MainWindow", selected['data']['type'].upper()))

    def get_tab(self):
        return self.descriptionstillscreenshot_tab