from PyQt5 import QtWidgets, QtCore, QtGui

class DescriptionKeystroke:
    def __init__(self, selected) -> None:
        self.descriptionkeystroke_tab = QtWidgets.QWidget()
        self.descriptionkeystroke_tab.setObjectName(
            "descriptionkeystroke_tab")
        self.formLayout_11 = QtWidgets.QFormLayout(
            self.descriptionkeystroke_tab)
        self.formLayout_11.setObjectName("formLayout_11")
        self.frame_7 = QtWidgets.QFrame(self.descriptionkeystroke_tab)
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_7.setObjectName("frame_7")
        self.formLayout_10 = QtWidgets.QFormLayout(self.frame_7)
        self.formLayout_10.setObjectName("formLayout_10")
        self.descriptionvideo_timestamp_label_47 = QtWidgets.QLabel(
            self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descriptionvideo_timestamp_label_47.setFont(font)
        self.descriptionvideo_timestamp_label_47.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_47.setObjectName(
            "descriptionvideo_timestamp_label_47")
        self.formLayout_10.setWidget(
            0,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_47)
        self.label_86 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_86.setFont(font)
        self.label_86.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_86.setObjectName("label_86")
        self.formLayout_10.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.label_86)
        self.descriptionvideo_timestamp_label_46 = QtWidgets.QLabel(
            self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descriptionvideo_timestamp_label_46.setFont(font)
        self.descriptionvideo_timestamp_label_46.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_46.setObjectName(
            "descriptionvideo_timestamp_label_46")
        self.formLayout_10.setWidget(
            1,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_46)
        self.label_87 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_87.setFont(font)
        self.label_87.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_87.setObjectName("label_87")
        self.formLayout_10.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.label_87)
        self.formLayout_11.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.frame_7)

        _translate = QtCore.QCoreApplication.translate
        self.descriptionvideo_timestamp_label_47.setText(
            _translate("MainWindow", "Timestamp:"))
        self.label_86.setText(_translate("MainWindow", selected['timestamp']))
        self.descriptionvideo_timestamp_label_46.setText(
            _translate("MainWindow", "Keypress:"))
        self.label_87.setText(_translate("MainWindow", '\'' + selected['data'] + '\''))

    def get_tab(self):
        return self.descriptionkeystroke_tab