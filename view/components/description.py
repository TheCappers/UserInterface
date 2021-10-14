from PyQt5 import QtWidgets, QtCore, QtGui


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
        # self.description_tab.addTab(self.descriptionvideo_tab, "")
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
        # self.description_tab.addTab(self.descriptionstillscreenshot_tab, "")
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
        # self.description_tab.addTab(self.descriptionsystemcall_tab, "")
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
        # self.description_tab.addTab(self.descriptionprocess_tab, "")
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
        # self.description_tab.addTab(self.descriptionwindowhistory_tab, "")

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
        # self.description_tab.addTab(self.descriptionnetwork_tab, "")
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
        # self.description_tab.addTab(self.descriptionmouse_tab, "")
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
        # self.description_tab.addTab(self.descriptionkeystroke_tab, "")
        # self.gridLayout_24.addWidget(self.description_tab, 0, 0, 1, 1)

        _translate = QtCore.QCoreApplication.translate
        self.label_89.setText(
            _translate(
                "MainWindow",
                "<html><head/><body><p><img src=\":/pics_for_detailedview/stillscreenshot_detailedview.jpg\"/></p></body></html>"))
        self.descriptionvideo_timestamp_label_7.setText(
            _translate("MainWindow", "Timestamp:"))
        self.label_47.setText(_translate("MainWindow", "10-6-26 02:31:29"))
        self.descriptionvideo_timestamp_label_6.setText(
            _translate("MainWindow", "Still Screenshot Size:"))
        self.label_46.setText(_translate("MainWindow", "60MB"))
        self.descriptionvideo_timestamp_label_5.setText(
            _translate("MainWindow", "Still Screenshot Format:"))
        self.label_45.setText(_translate("MainWindow", "PNG"))
        self.description_tab.setTabText(
            self.description_tab.indexOf(
                self.descriptionstillscreenshot_tab), _translate(
                "MainWindow", "Still Screenshot"))
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
        self.description_tab.setTabText(
            self.description_tab.indexOf(
                self.descriptionsystemcall_tab), _translate(
                "MainWindow", "System Call"))
        self.descriptionvideo_timestamp_label_keystroke.setText(
            _translate("MainWindow", "No. of Thread:"))
        self.label_63.setText(_translate("MainWindow", "5"))
        self.descriptionvideo_timestamp_label_26.setText(
            _translate("MainWindow", "CPU Percentage:"))
        self.label_64.setText(_translate("MainWindow", "12.4%"))
        self.descriptionvideo_timestamp_label_history.setText(
            _translate("MainWindow", "Process Privileges:"))
        self.label_66.setText(_translate("MainWindow", "root"))
        self.descriptionvideo_timestamp_label_mouse_action.setText(
            _translate("MainWindow", "Process Priority:"))
        self.label_65.setText(_translate("MainWindow", "88"))
        self.descriptionvideo_timestamp_label_window_history.setText(
            _translate("MainWindow", "Process Type:"))
        self.label_67.setText(_translate("MainWindow", "Foreground"))
        self.descriptionvideo_timestamp_label_video.setText(
            _translate("MainWindow", "Start Time:"))
        self.label_60.setText(_translate("MainWindow", "10-6-26 02:31:29"))
        self.descriptionvideo_timestamp_label_network.setText(
            _translate("MainWindow", "Command:"))
        self.label_58.setText(_translate("MainWindow", "init"))
        self.descriptionvideo_timestamp_label_process.setText(
            _translate("MainWindow", "Terminal:"))
        self.label_61.setText(_translate("MainWindow", "shell"))
        self.descriptionvideo_timestamp_label_all_artifacts.setText(
            _translate("MainWindow", "Status:"))
        self.label_56.setText(_translate("MainWindow", "idle"))
        self.descriptionvideo_timestamp_label_screenshot.setText(
            _translate("MainWindow", "Memory Usage"))
        self.label_59.setText(_translate("MainWindow", "3.4MB"))
        self.descriptionvideo_timestamp_label_mac_address.setText(
            _translate("MainWindow", "Timestamp:"))
        self.label_55.setText(_translate("MainWindow", "10-6-26 02:31:29"))
        self.descriptionvideo_timestamp_label_type.setText(
            _translate("MainWindow", "User Name:"))
        self.label_62.setText(_translate("MainWindow", "root"))
        self.descriptionvideo_timestamp_label_start_time.setText(
            _translate("MainWindow", "Process Name:"))
        self.label_51.setText(_translate("MainWindow", "_windowserver"))
        self.descriptionvideo_timestamp_label_ip_address.setText(
            _translate("MainWindow", "Process ID:"))
        self.label_57.setText(_translate("MainWindow", "45"))
        self.descriptionvideo_timestamp_label_value_filter.setText(
            _translate("MainWindow", "Parent Process Name:"))
        self.label_54.setText(_translate("MainWindow", "455"))
        self.description_tab.setTabText(
            self.description_tab.indexOf(
                self.descriptionprocess_tab), _translate(
                "MainWindow", "Process"))
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
        self.description_tab.setTabText(
            self.description_tab.indexOf(
                self.descriptionwindowhistory_tab), _translate(
                "MainWindow", "Window History"))
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
        self.description_tab.setTabText(
            self.description_tab.indexOf(
                self.descriptionnetwork_tab), _translate(
                "MainWindow", "Network Packet"))
        self.descriptionvideo_timestamp_label_41.setText(
            _translate("MainWindow", "Timestamp:"))
        self.label_80.setText(_translate("MainWindow", "10-6-26 02:31:29"))
        self.descriptionvideo_timestamp_label_43.setText(
            _translate("MainWindow", "Button:"))
        self.label_73.setText(_translate("MainWindow", "Left"))
        self.descriptionvideo_timestamp_label_44.setText(
            _translate("MainWindow", "Mouse Action:"))
        self.label_83.setText(_translate("MainWindow", "Click"))
        self.descriptionvideo_timestamp_label_log.setText(
            _translate("MainWindow", "Mouse Action Value:"))
        self.label_84.setText(_translate("MainWindow", "400,100"))
        self.descriptionvideo_timestamp_label_37.setText(
            _translate("MainWindow", "Active Window:"))
        self.label_79.setText(_translate("MainWindow", "terminal"))
        self.descriptionvideo_timestamp_label_45.setText(
            _translate("MainWindow", "Window Focus:"))
        self.label_85.setText(_translate("MainWindow", "terminal"))
        self.description_tab.setTabText(
            self.description_tab.indexOf(
                self.descriptionmouse_tab), _translate(
                "MainWindow", "Mouse Action"))
        self.descriptionvideo_timestamp_label_47.setText(
            _translate("MainWindow", "Timestamp:"))
        self.label_86.setText(_translate("MainWindow", "10-6-26 02:31:29"))
        self.descriptionvideo_timestamp_label_46.setText(
            _translate("MainWindow", "Keypress:"))
        self.label_87.setText(_translate("MainWindow", "f"))
        self.description_tab.setTabText(
            self.description_tab.indexOf(
                self.descriptionkeystroke_tab), _translate(
                "MainWindow", "Keystroke"))

        self.label_88.setText(
            _translate(
                "MainWindow",
                "<html><head/><body><p><img src=\":/pics_for_detailedview/video_detailedview.png\"/></p></body></html>"))
        self.descriptionvideo_timestamp_label.setText(
            _translate("MainWindow", "Timestamp:"))
        self.label_41.setText(_translate("MainWindow", "10-6-26 02:31:29"))
        self.descriptionvideo_timestamp_label_2.setText(
            _translate("MainWindow", "Video Size:"))
        self.label_42.setText(_translate("MainWindow", "60MB"))
        self.descriptionvideo_timestamp_label_3.setText(
            _translate("MainWindow", "Video Resolution:"))
        self.label_43.setText(_translate("MainWindow", "1260 x 680"))
        self.descriptionvideo_timestamp_label_4.setText(
            _translate("MainWindow", "Video Frame Rate:"))
        self.label_44.setText(_translate("MainWindow", "24fps"))
        self.description_tab.setTabText(
            self.description_tab.indexOf(
                self.descriptionvideo_tab), _translate(
                "MainWindow", "Video"))

    def get_tab(self):
        return self.tab_134
