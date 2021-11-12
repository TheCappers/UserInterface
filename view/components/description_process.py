from PyQt5 import QtWidgets, QtCore, QtGui


class DescriptionProcess:
    def __init__(self, selected) -> None:
        self.descriptionprocess_tab = QtWidgets.QWidget()
        self.descriptionprocess_tab.setObjectName("descriptionprocess_tab")
        self.formLayout_4 = QtWidgets.QFormLayout(
            self.descriptionprocess_tab)
        self.formLayout_4.setObjectName("formLayout_4")
        self.frame_8 = QtWidgets.QFrame(self.descriptionprocess_tab)
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.formLayout_5 = QtWidgets.QFormLayout(self.frame_8)
        self.formLayout_5.setObjectName("formLayout_5")
        self.descriptionvideo_timestamp_label_keystroke = QtWidgets.QLabel(
            self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descriptionvideo_timestamp_label_keystroke.setFont(font)
        self.descriptionvideo_timestamp_label_keystroke.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_keystroke.setObjectName(
            "descriptionvideo_timestamp_label_keystroke")
        self.formLayout_5.setWidget(
            0,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_keystroke)
        self.label_63 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_63.setFont(font)
        self.label_63.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_63.setObjectName("label_63")
        self.formLayout_5.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.label_63)
        self.descriptionvideo_timestamp_label_26 = QtWidgets.QLabel(
            self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descriptionvideo_timestamp_label_26.setFont(font)
        self.descriptionvideo_timestamp_label_26.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_26.setObjectName(
            "descriptionvideo_timestamp_label_26")
        self.formLayout_5.setWidget(
            1,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_26)
        self.label_64 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_64.setFont(font)
        self.label_64.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_64.setObjectName("label_64")
        self.formLayout_5.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.label_64)
        self.descriptionvideo_timestamp_label_history = QtWidgets.QLabel(
            self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descriptionvideo_timestamp_label_history.setFont(font)
        self.descriptionvideo_timestamp_label_history.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_history.setObjectName(
            "descriptionvideo_timestamp_label_history")
        self.formLayout_5.setWidget(
            2,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_history)
        self.label_66 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_66.setFont(font)
        self.label_66.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_66.setObjectName("label_66")
        self.formLayout_5.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.label_66)
        self.descriptionvideo_timestamp_label_mouse_action = QtWidgets.QLabel(
            self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descriptionvideo_timestamp_label_mouse_action.setFont(font)
        self.descriptionvideo_timestamp_label_mouse_action.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_mouse_action.setObjectName(
            "descriptionvideo_timestamp_label_mouse_action")
        self.formLayout_5.setWidget(
            3,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_mouse_action)
        self.label_65 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_65.setFont(font)
        self.label_65.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_65.setObjectName("label_65")
        self.formLayout_5.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.label_65)
        self.descriptionvideo_timestamp_label_window_history = QtWidgets.QLabel(
            self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descriptionvideo_timestamp_label_window_history.setFont(font)
        self.descriptionvideo_timestamp_label_window_history.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_window_history.setObjectName(
            "descriptionvideo_timestamp_label_window_history")
        self.formLayout_5.setWidget(
            4,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_window_history)
        self.label_67 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_67.setFont(font)
        self.label_67.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_67.setObjectName("label_67")
        self.formLayout_5.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.label_67)
        self.descriptionvideo_timestamp_label_video = QtWidgets.QLabel(
            self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descriptionvideo_timestamp_label_video.setFont(font)
        self.descriptionvideo_timestamp_label_video.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_video.setObjectName(
            "descriptionvideo_timestamp_label_video")
        self.formLayout_5.setWidget(
            5,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_video)
        self.label_60 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_60.setFont(font)
        self.label_60.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_60.setObjectName("label_60")
        self.formLayout_5.setWidget(
            5, QtWidgets.QFormLayout.FieldRole, self.label_60)
        self.descriptionvideo_timestamp_label_network = QtWidgets.QLabel(
            self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descriptionvideo_timestamp_label_network.setFont(font)
        self.descriptionvideo_timestamp_label_network.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_network.setObjectName(
            "descriptionvideo_timestamp_label_network")
        self.formLayout_5.setWidget(
            6,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_network)
        self.label_58 = QtWidgets.QLabel(self.frame_8)
        self.label_58.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_58.setObjectName("label_58")
        self.formLayout_5.setWidget(
            6, QtWidgets.QFormLayout.FieldRole, self.label_58)
        self.descriptionvideo_timestamp_label_process = QtWidgets.QLabel(
            self.frame_8)
        self.descriptionvideo_timestamp_label_process.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_process.setObjectName(
            "descriptionvideo_timestamp_label_process")
        self.formLayout_5.setWidget(
            7,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_process)
        self.label_61 = QtWidgets.QLabel(self.frame_8)
        self.label_61.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_61.setObjectName("label_61")
        self.formLayout_5.setWidget(
            7, QtWidgets.QFormLayout.FieldRole, self.label_61)
        self.descriptionvideo_timestamp_label_all_artifacts = QtWidgets.QLabel(
            self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descriptionvideo_timestamp_label_all_artifacts.setFont(font)
        self.descriptionvideo_timestamp_label_all_artifacts.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_all_artifacts.setObjectName(
            "descriptionvideo_timestamp_label_all_artifacts")
        self.formLayout_5.setWidget(
            8,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_all_artifacts)
        self.label_56 = QtWidgets.QLabel(self.frame_8)
        self.label_56.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_56.setObjectName("label_56")
        self.formLayout_5.setWidget(
            8, QtWidgets.QFormLayout.FieldRole, self.label_56)
        self.descriptionvideo_timestamp_label_screenshot = QtWidgets.QLabel(
            self.frame_8)
        self.descriptionvideo_timestamp_label_screenshot.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_screenshot.setObjectName(
            "descriptionvideo_timestamp_label_screenshot")
        self.formLayout_5.setWidget(
            9,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_screenshot)
        self.label_59 = QtWidgets.QLabel(self.frame_8)
        self.label_59.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_59.setObjectName("label_59")
        self.formLayout_5.setWidget(
            9, QtWidgets.QFormLayout.FieldRole, self.label_59)
        self.descriptionvideo_timestamp_label_mac_address = QtWidgets.QLabel(
            self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descriptionvideo_timestamp_label_mac_address.setFont(font)
        self.descriptionvideo_timestamp_label_mac_address.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_mac_address.setObjectName(
            "descriptionvideo_timestamp_label_mac_address")
        self.formLayout_5.setWidget(
            10,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_mac_address)
        self.label_55 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_55.setFont(font)
        self.label_55.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_55.setObjectName("label_55")
        self.formLayout_5.setWidget(
            10, QtWidgets.QFormLayout.FieldRole, self.label_55)
        self.descriptionvideo_timestamp_label_type = QtWidgets.QLabel(
            self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descriptionvideo_timestamp_label_type.setFont(font)
        self.descriptionvideo_timestamp_label_type.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_type.setObjectName(
            "descriptionvideo_timestamp_label_type")
        self.formLayout_5.setWidget(
            11,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_type)
        self.label_62 = QtWidgets.QLabel(self.frame_8)
        self.label_62.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_62.setObjectName("label_62")
        self.formLayout_5.setWidget(
            11, QtWidgets.QFormLayout.FieldRole, self.label_62)
        self.descriptionvideo_timestamp_label_start_time = QtWidgets.QLabel(
            self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descriptionvideo_timestamp_label_start_time.setFont(font)
        self.descriptionvideo_timestamp_label_start_time.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_start_time.setObjectName(
            "descriptionvideo_timestamp_label_start_time")
        self.formLayout_5.setWidget(
            12,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_start_time)
        self.label_51 = QtWidgets.QLabel(self.frame_8)
        self.label_51.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_51.setObjectName("label_51")
        self.formLayout_5.setWidget(
            12, QtWidgets.QFormLayout.FieldRole, self.label_51)
        self.descriptionvideo_timestamp_label_ip_address = QtWidgets.QLabel(
            self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descriptionvideo_timestamp_label_ip_address.setFont(font)
        self.descriptionvideo_timestamp_label_ip_address.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_ip_address.setObjectName(
            "descriptionvideo_timestamp_label_ip_address")
        self.formLayout_5.setWidget(
            13,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_ip_address)
        self.label_57 = QtWidgets.QLabel(self.frame_8)
        self.label_57.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_57.setObjectName("label_57")
        self.formLayout_5.setWidget(
            13, QtWidgets.QFormLayout.FieldRole, self.label_57)
        self.descriptionvideo_timestamp_label_value_filter = QtWidgets.QLabel(
            self.frame_8)
        self.descriptionvideo_timestamp_label_value_filter.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.descriptionvideo_timestamp_label_value_filter.setObjectName(
            "descriptionvideo_timestamp_label_value_filter")
        self.formLayout_5.setWidget(
            14,
            QtWidgets.QFormLayout.LabelRole,
            self.descriptionvideo_timestamp_label_value_filter)
        self.label_54 = QtWidgets.QLabel(self.frame_8)
        self.label_54.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_54.setObjectName("label_54")
        self.formLayout_5.setWidget(
            14, QtWidgets.QFormLayout.FieldRole, self.label_54)
        self.formLayout_4.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.frame_8)

        process_dictionary = selected['data']
        _translate = QtCore.QCoreApplication.translate
        self.descriptionvideo_timestamp_label_keystroke.setText(
            _translate("MainWindow", "No. of Thread:"))
        self.label_63.setText(_translate("MainWindow", str(process_dictionary['num_threads'])))
        self.descriptionvideo_timestamp_label_26.setText(
            _translate("MainWindow", "CPU Percentage:"))
        self.label_64.setText(_translate("MainWindow", str(process_dictionary['cpu_usage'])))
        self.descriptionvideo_timestamp_label_history.setText(
            _translate("MainWindow", "Process Privileges:"))
        self.label_66.setText(_translate("MainWindow", str(process_dictionary['process_privileges'])))
        self.descriptionvideo_timestamp_label_mouse_action.setText(
            _translate("MainWindow", "Process Priority:"))
        self.label_65.setText(_translate("MainWindow", str(process_dictionary['process_priority'])))
        self.descriptionvideo_timestamp_label_window_history.setText(
            _translate("MainWindow", "Process Type:"))
        self.label_67.setText(_translate("MainWindow", str(process_dictionary['process_type'])))
        self.descriptionvideo_timestamp_label_video.setText(
            _translate("MainWindow", "Start Time:"))
        self.label_60.setText(_translate("MainWindow", process_dictionary['creation_time']))
        self.descriptionvideo_timestamp_label_network.setText(
            _translate("MainWindow", "Command:"))
        self.label_58.setText(_translate("MainWindow", process_dictionary['command']))
        self.descriptionvideo_timestamp_label_process.setText(
            _translate("MainWindow", "Terminal:"))
        self.label_61.setText(_translate("MainWindow", process_dictionary['terminal']))
        self.descriptionvideo_timestamp_label_all_artifacts.setText(
            _translate("MainWindow", "Status:"))
        self.label_56.setText(_translate("MainWindow", process_dictionary['status']))
        self.descriptionvideo_timestamp_label_screenshot.setText(
            _translate("MainWindow", "Memory Usage"))
        self.label_59.setText(_translate("MainWindow", str(process_dictionary['memory_usage'])))
        self.descriptionvideo_timestamp_label_mac_address.setText(
            _translate("MainWindow", "Timestamp:"))
        self.label_55.setText(_translate("MainWindow", str(process_dictionary['creation_time'])))
        self.descriptionvideo_timestamp_label_type.setText(
            _translate("MainWindow", "User Name:"))
        self.label_62.setText(_translate("MainWindow", process_dictionary['username']))
        self.descriptionvideo_timestamp_label_start_time.setText(
            _translate("MainWindow", "Process Name:"))
        self.label_51.setText(_translate("MainWindow", process_dictionary['p_name']))
        self.descriptionvideo_timestamp_label_ip_address.setText(
            _translate("MainWindow", "Process ID:"))
        self.label_57.setText(_translate("MainWindow", str(process_dictionary['pid'])))
        self.descriptionvideo_timestamp_label_value_filter.setText(
            _translate("MainWindow", "Parent Process ID:"))
        self.label_54.setText(_translate("MainWindow", str(process_dictionary['ppid'])))

    def get_tab(self):
        return self.descriptionprocess_tab
