from PyQt5 import QtCore, QtGui, QtWidgets


class Configuration:
	def __init__(self):
		self.tab_2 = QtWidgets.QWidget()
		self.tab_2 = QtWidgets.QWidget()
		self.tab_2.setObjectName("tab_2")
		self.gridLayout_53 = QtWidgets.QGridLayout(self.tab_2)
		self.gridLayout_53.setObjectName("gridLayout_53")
		self.scrollArea_4 = QtWidgets.QScrollArea(self.tab_2)
		self.scrollArea_4.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.scrollArea_4.setWidgetResizable(True)
		self.scrollArea_4.setObjectName("scrollArea_4")
		self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
		self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 1232, 718))
		self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
		self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_5)
		self.verticalLayout_10.setObjectName("verticalLayout_10")
		self.configuration_header = QtWidgets.QFrame(self.scrollAreaWidgetContents_5)
		self.configuration_header.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.configuration_header.setFrameShadow(QtWidgets.QFrame.Raised)
		self.configuration_header.setObjectName("configuration_header")
		self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.configuration_header)
		self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout_8.setObjectName("horizontalLayout_8")
		self.frame_17 = QtWidgets.QFrame(self.configuration_header)
		self.frame_17.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_17.setObjectName("frame_17")
		self.gridLayout_55 = QtWidgets.QGridLayout(self.frame_17)
		self.gridLayout_55.setObjectName("gridLayout_55")
		self.StorageThreshLabel = QtWidgets.QLabel(self.frame_17)
		font = QtGui.QFont()
		self.StorageThreshLabel.setFont(font)
		self.StorageThreshLabel.setScaledContents(False)
		self.StorageThreshLabel.setObjectName("StorageThreshLabel")
		self.gridLayout_55.addWidget(self.StorageThreshLabel, 1, 1, 1, 1)
		self.StorageTitle = QtWidgets.QLabel(self.frame_17)
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.StorageTitle.setFont(font)
		self.StorageTitle.setObjectName("StorageTitle")
		self.gridLayout_55.addWidget(self.StorageTitle, 0, 1, 1, 1)
		self.StorageInValue = QtWidgets.QLineEdit(self.frame_17)
		self.StorageInValue.setMinimumSize(QtCore.QSize(150, 0))
		self.StorageInValue.setMaximumSize(QtCore.QSize(150, 16777215))
		self.StorageInValue.setText("")
		self.StorageInValue.setMaxLength(2)
		self.StorageInValue.setObjectName("StorageInValue")
		self.gridLayout_55.addWidget(self.StorageInValue, 2, 1, 1, 1)
		self.horizontalLayout_8.addWidget(self.frame_17, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
		self.video_frame_2 = QtWidgets.QFrame(self.configuration_header)
		self.video_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.video_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
		self.video_frame_2.setObjectName("video_frame_2")
		self.gridLayout_54 = QtWidgets.QGridLayout(self.video_frame_2)
		self.gridLayout_54.setObjectName("gridLayout_54")
		self.VideoStatButtonFrame = QtWidgets.QFrame(self.video_frame_2)
		self.VideoStatButtonFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.VideoStatButtonFrame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.VideoStatButtonFrame.setObjectName("VideoStatButtonFrame")
		self.gridLayout_68 = QtWidgets.QGridLayout(self.VideoStatButtonFrame)
		self.gridLayout_68.setContentsMargins(0, 0, 0, 0)
		self.gridLayout_68.setObjectName("gridLayout_68")
		self.VideoStatOnButton = QtWidgets.QPushButton(self.VideoStatButtonFrame)
		self.VideoStatOnButton.setCheckable(True)
		self.VideoStatOnButton.setChecked(True)
		self.VideoStatOnButton.setObjectName("VideoStatOnButton")
		self.gridLayout_68.addWidget(self.VideoStatOnButton, 0, 0, 1, 1)
		self.VideoStatusOffButton = QtWidgets.QPushButton(self.VideoStatButtonFrame)
		self.VideoStatusOffButton.setCheckable(True)
		self.VideoStatusOffButton.setChecked(False)
		self.VideoStatusOffButton.setObjectName("VideoStatusOffButton")
		self.gridLayout_68.addWidget(self.VideoStatusOffButton, 0, 1, 1, 1)
		self.gridLayout_54.addWidget(self.VideoStatButtonFrame, 4, 0, 1, 1, QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom)
		self.VideoResolutionSelect = QtWidgets.QComboBox(self.video_frame_2)
		self.VideoResolutionSelect.setMaximumSize(QtCore.QSize(150, 20))
		self.VideoResolutionSelect.setObjectName("VideoResolutionSelect")
		self.VideoResolutionSelect.addItem("")
		self.VideoResolutionSelect.addItem("")
		self.VideoResolutionSelect.addItem("")
		self.VideoResolutionSelect.addItem("")
		self.VideoResolutionSelect.addItem("")
		self.gridLayout_54.addWidget(self.VideoResolutionSelect, 0, 2, 1, 1)
		self.WaitValueSelection = QtWidgets.QComboBox(self.video_frame_2)
		self.WaitValueSelection.setMaximumSize(QtCore.QSize(220, 20))
		self.WaitValueSelection.setObjectName("WaitValueSelection")
		self.WaitValueSelection.addItem("")
		self.WaitValueSelection.addItem("")
		self.WaitValueSelection.addItem("")
		self.WaitValueSelection.addItem("")
		self.gridLayout_54.addWidget(self.WaitValueSelection, 3, 2, 1, 1)
		self.VideoTitle = QtWidgets.QLabel(self.video_frame_2)
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.VideoTitle.setFont(font)
		self.VideoTitle.setObjectName("VideoTitle")
		self.gridLayout_54.addWidget(self.VideoTitle, 0, 0, 1, 2)
		self.VideoWaitSelection = QtWidgets.QComboBox(self.video_frame_2)
		self.VideoWaitSelection.setMaximumSize(QtCore.QSize(180, 20))
		self.VideoWaitSelection.setObjectName("VideoWaitSelection")
		self.VideoWaitSelection.addItem("")
		self.VideoWaitSelection.addItem("")
		self.VideoWaitSelection.addItem("")
		self.gridLayout_54.addWidget(self.VideoWaitSelection, 2, 2, 1, 1)
		self.FrameRateSelect = QtWidgets.QComboBox(self.video_frame_2)
		self.FrameRateSelect.setMaximumSize(QtCore.QSize(150, 20))
		self.FrameRateSelect.setObjectName("FrameRateSelect")
		self.FrameRateSelect.addItem("")
		self.FrameRateSelect.addItem("")
		self.FrameRateSelect.addItem("")
		self.gridLayout_54.addWidget(self.FrameRateSelect, 1, 2, 1, 1)
		self.VideoAutoStat = QtWidgets.QLabel(self.video_frame_2)
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.VideoAutoStat.setFont(font)
		self.VideoAutoStat.setScaledContents(False)
		self.VideoAutoStat.setWordWrap(True)
		self.VideoAutoStat.setObjectName("VideoAutoStat")
		self.gridLayout_54.addWidget(self.VideoAutoStat, 2, 0, 2, 2)
		self.horizontalLayout_8.addWidget(self.video_frame_2)
		self.frame_16 = QtWidgets.QFrame(self.configuration_header)
		self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_16.setObjectName("frame_16")
		self.gridLayout_56 = QtWidgets.QGridLayout(self.frame_16)
		self.gridLayout_56.setObjectName("gridLayout_56")
		self.ScreenshotStat = QtWidgets.QLabel(self.frame_16)
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.ScreenshotStat.setFont(font)
		self.ScreenshotStat.setScaledContents(False)
		self.ScreenshotStat.setWordWrap(True)
		self.ScreenshotStat.setObjectName("ScreenshotStat")
		self.gridLayout_56.addWidget(self.ScreenshotStat, 1, 0, 1, 2)
		self.ScreenshotTitle = QtWidgets.QLabel(self.frame_16)
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.ScreenshotTitle.setFont(font)
		self.ScreenshotTitle.setObjectName("ScreenshotTitle")
		self.gridLayout_56.addWidget(self.ScreenshotTitle, 0, 0, 1, 2)
		self.ScreenshotFormatDrop = QtWidgets.QComboBox(self.frame_16)
		self.ScreenshotFormatDrop.setMaximumSize(QtCore.QSize(220, 20))
		self.ScreenshotFormatDrop.setObjectName("ScreenshotFormatDrop")
		self.ScreenshotFormatDrop.addItem("")
		self.ScreenshotFormatDrop.addItem("")
		self.ScreenshotFormatDrop.addItem("")
		self.gridLayout_56.addWidget(self.ScreenshotFormatDrop, 0, 2, 1, 1)
		self.ScreenshotStatButtonFrame = QtWidgets.QFrame(self.frame_16)
		self.ScreenshotStatButtonFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.ScreenshotStatButtonFrame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.ScreenshotStatButtonFrame.setObjectName("ScreenshotStatButtonFrame")
		self.gridLayout_69 = QtWidgets.QGridLayout(self.ScreenshotStatButtonFrame)
		self.gridLayout_69.setContentsMargins(0, 0, 0, 0)
		self.gridLayout_69.setObjectName("gridLayout_69")
		self.ScreenshotStatOnButton = QtWidgets.QPushButton(self.ScreenshotStatButtonFrame)
		self.ScreenshotStatOnButton.setCheckable(True)
		self.ScreenshotStatOnButton.setChecked(True)
		self.ScreenshotStatOnButton.setObjectName("ScreenshotStatOnButton")
		self.gridLayout_69.addWidget(self.ScreenshotStatOnButton, 0, 0, 1, 1)
		self.ScreenshotStatOffButton = QtWidgets.QPushButton(self.ScreenshotStatButtonFrame)
		self.ScreenshotStatOffButton.setCheckable(True)
		self.ScreenshotStatOffButton.setObjectName("ScreenshotStatOffButton")
		self.gridLayout_69.addWidget(self.ScreenshotStatOffButton, 0, 1, 1, 1)
		self.gridLayout_56.addWidget(self.ScreenshotStatButtonFrame, 2, 0, 1, 1,
																	QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom)
		self.horizontalLayout_8.addWidget(self.frame_16)
		self.verticalLayout_10.addWidget(self.configuration_header)
		self.configuration_middle = QtWidgets.QFrame(self.scrollAreaWidgetContents_5)
		self.configuration_middle.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.configuration_middle.setFrameShadow(QtWidgets.QFrame.Raised)
		self.configuration_middle.setObjectName("configuration_middle")
		self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.configuration_middle)
		self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout_7.setObjectName("horizontalLayout_7")
		self.frame_18 = QtWidgets.QFrame(self.configuration_middle)
		self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_18.setObjectName("frame_18")
		self.gridLayout_57 = QtWidgets.QGridLayout(self.frame_18)
		self.gridLayout_57.setObjectName("gridLayout_57")
		self.SysCallStatus = QtWidgets.QLabel(self.frame_18)
		self.SysCallStatus.setMinimumSize(QtCore.QSize(151, 91))
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.SysCallStatus.setFont(font)
		self.SysCallStatus.setScaledContents(False)
		self.SysCallStatus.setWordWrap(True)
		self.SysCallStatus.setObjectName("SysCallStatus")
		self.gridLayout_57.addWidget(self.SysCallStatus, 2, 0, 1, 2)
		self.SystemCallLabel = QtWidgets.QLabel(self.frame_18)
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.SystemCallLabel.setFont(font)
		self.SystemCallLabel.setObjectName("SystemCallLabel")
		self.gridLayout_57.addWidget(self.SystemCallLabel, 1, 0, 1, 1)
		self.SystemCallButtonFrame = QtWidgets.QFrame(self.frame_18)
		self.SystemCallButtonFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.SystemCallButtonFrame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.SystemCallButtonFrame.setObjectName("SystemCallButtonFrame")
		self.gridLayout_65 = QtWidgets.QGridLayout(self.SystemCallButtonFrame)
		self.gridLayout_65.setContentsMargins(0, 0, 0, 0)
		self.gridLayout_65.setObjectName("gridLayout_65")
		self.SystemCallOnButton = QtWidgets.QPushButton(self.SystemCallButtonFrame)
		self.SystemCallOnButton.setCheckable(True)
		self.SystemCallOnButton.setChecked(True)
		self.SystemCallOnButton.setObjectName("SystemCallOnButton")
		self.gridLayout_65.addWidget(self.SystemCallOnButton, 0, 0, 1, 1)
		self.SystemCallOffButton = QtWidgets.QPushButton(self.SystemCallButtonFrame)
		self.SystemCallOffButton.setCheckable(True)
		self.SystemCallOffButton.setObjectName("SystemCallOffButton")
		self.gridLayout_65.addWidget(self.SystemCallOffButton, 0, 1, 1, 1)
		self.gridLayout_57.addWidget(self.SystemCallButtonFrame, 3, 0, 1, 1,
																	QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom)
		self.horizontalLayout_7.addWidget(self.frame_18)
		self.frame_19 = QtWidgets.QFrame(self.configuration_middle)
		self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_19.setObjectName("frame_19")
		self.gridLayout_58 = QtWidgets.QGridLayout(self.frame_19)
		self.gridLayout_58.setObjectName("gridLayout_58")
		self.WindowHistoryWaitVal = QtWidgets.QComboBox(self.frame_19)
		self.WindowHistoryWaitVal.setMaximumSize(QtCore.QSize(220, 20))
		self.WindowHistoryWaitVal.setObjectName("WindowHistoryWaitVal")
		self.WindowHistoryWaitVal.addItem("")
		self.gridLayout_58.addWidget(self.WindowHistoryWaitVal, 1, 2, 1, 1)
		self.WindowHistoryStat = QtWidgets.QLabel(self.frame_19)
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.WindowHistoryStat.setFont(font)
		self.WindowHistoryStat.setScaledContents(False)
		self.WindowHistoryStat.setWordWrap(True)
		self.WindowHistoryStat.setObjectName("WindowHistoryStat")
		self.gridLayout_58.addWidget(self.WindowHistoryStat, 2, 0, 1, 2)
		self.WindowHistLabel = QtWidgets.QLabel(self.frame_19)
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.WindowHistLabel.setFont(font)
		self.WindowHistLabel.setObjectName("WindowHistLabel")
		self.gridLayout_58.addWidget(self.WindowHistLabel, 0, 0, 2, 2)
		self.WindowHistoryDurUnit = QtWidgets.QComboBox(self.frame_19)
		self.WindowHistoryDurUnit.setMaximumSize(QtCore.QSize(250, 20))
		self.WindowHistoryDurUnit.setObjectName("WindowHistoryDurUnit")
		self.WindowHistoryDurUnit.addItem("")
		self.gridLayout_58.addWidget(self.WindowHistoryDurUnit, 0, 2, 1, 1)
		self.WindowHistoryButtonFrame = QtWidgets.QFrame(self.frame_19)
		self.WindowHistoryButtonFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.WindowHistoryButtonFrame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.WindowHistoryButtonFrame.setObjectName("WindowHistoryButtonFrame")
		self.gridLayout_66 = QtWidgets.QGridLayout(self.WindowHistoryButtonFrame)
		self.gridLayout_66.setContentsMargins(0, 0, 0, 0)
		self.gridLayout_66.setObjectName("gridLayout_66")
		self.WindowHistoryOnButton = QtWidgets.QPushButton(self.WindowHistoryButtonFrame)
		self.WindowHistoryOnButton.setCheckable(True)
		self.WindowHistoryOnButton.setChecked(True)
		self.WindowHistoryOnButton.setObjectName("WindowHistoryOnButton")
		self.gridLayout_66.addWidget(self.WindowHistoryOnButton, 0, 0, 1, 1)
		self.WindowHistoryOffButton = QtWidgets.QPushButton(self.WindowHistoryButtonFrame)
		self.WindowHistoryOffButton.setCheckable(True)
		self.WindowHistoryOffButton.setObjectName("WindowHistoryOffButton")
		self.gridLayout_66.addWidget(self.WindowHistoryOffButton, 0, 1, 1, 1)
		self.gridLayout_58.addWidget(self.WindowHistoryButtonFrame, 3, 0, 1, 1,
																	QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom)
		self.horizontalLayout_7.addWidget(self.frame_19)
		self.frame_20 = QtWidgets.QFrame(self.configuration_middle)
		self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_20.setObjectName("frame_20")
		self.gridLayout_59 = QtWidgets.QGridLayout(self.frame_20)
		self.gridLayout_59.setObjectName("gridLayout_59")
		self.KeystrokeStatus = QtWidgets.QLabel(self.frame_20)
		self.KeystrokeStatus.setMinimumSize(QtCore.QSize(151, 91))
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.KeystrokeStatus.setFont(font)
		self.KeystrokeStatus.setScaledContents(False)
		self.KeystrokeStatus.setWordWrap(True)
		self.KeystrokeStatus.setObjectName("KeystrokeStatus")
		self.gridLayout_59.addWidget(self.KeystrokeStatus, 1, 0, 1, 2)
		self.KeystrokeMainLabel = QtWidgets.QLabel(self.frame_20)
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.KeystrokeMainLabel.setFont(font)
		self.KeystrokeMainLabel.setObjectName("KeystrokeMainLabel")
		self.gridLayout_59.addWidget(self.KeystrokeMainLabel, 0, 0, 1, 1)
		self.KeyStrokeStatButtonFrame = QtWidgets.QFrame(self.frame_20)
		self.KeyStrokeStatButtonFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.KeyStrokeStatButtonFrame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.KeyStrokeStatButtonFrame.setObjectName("KeyStrokeStatButtonFrame")
		self.gridLayout_67 = QtWidgets.QGridLayout(self.KeyStrokeStatButtonFrame)
		self.gridLayout_67.setContentsMargins(0, 0, 0, 0)
		self.gridLayout_67.setObjectName("gridLayout_67")
		self.KeyStrokeStatOnButton = QtWidgets.QPushButton(self.KeyStrokeStatButtonFrame)
		self.KeyStrokeStatOnButton.setCheckable(True)
		self.KeyStrokeStatOnButton.setChecked(True)
		self.KeyStrokeStatOnButton.setObjectName("KeyStrokeStatOnButton")
		self.gridLayout_67.addWidget(self.KeyStrokeStatOnButton, 0, 0, 1, 1)
		self.KeyStrokeStatOffButton = QtWidgets.QPushButton(self.KeyStrokeStatButtonFrame)
		self.KeyStrokeStatOffButton.setCheckable(True)
		self.KeyStrokeStatOffButton.setObjectName("KeyStrokeStatOffButton")
		self.gridLayout_67.addWidget(self.KeyStrokeStatOffButton, 0, 1, 1, 1)
		self.gridLayout_59.addWidget(self.KeyStrokeStatButtonFrame, 2, 0, 1, 1,
																	QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom)
		self.horizontalLayout_7.addWidget(self.frame_20)
		self.verticalLayout_10.addWidget(self.configuration_middle)
		self.configuration_footer = QtWidgets.QFrame(self.scrollAreaWidgetContents_5)
		self.configuration_footer.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.configuration_footer.setFrameShadow(QtWidgets.QFrame.Raised)
		self.configuration_footer.setObjectName("configuration_footer")
		self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.configuration_footer)
		self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout_6.setObjectName("horizontalLayout_6")
		self.frame_22 = QtWidgets.QFrame(self.configuration_footer)
		self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_22.setObjectName("frame_22")
		self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_22)
		self.verticalLayout_11.setObjectName("verticalLayout_11")
		self.MouseActionTitle = QtWidgets.QLabel(self.frame_22)
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.MouseActionTitle.setFont(font)
		self.MouseActionTitle.setObjectName("MouseActionTitle")
		self.verticalLayout_11.addWidget(self.MouseActionTitle)
		self.MouseActStatus = QtWidgets.QLabel(self.frame_22)
		self.MouseActStatus.setMinimumSize(QtCore.QSize(151, 91))
		self.MouseActStatus.setMaximumSize(QtCore.QSize(151, 91))
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.MouseActStatus.setFont(font)
		self.MouseActStatus.setScaledContents(False)
		self.MouseActStatus.setWordWrap(True)
		self.MouseActStatus.setObjectName("MouseActStatus")
		self.verticalLayout_11.addWidget(self.MouseActStatus)
		self.MouseActButtonFrame = QtWidgets.QFrame(self.frame_22)
		self.MouseActButtonFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.MouseActButtonFrame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.MouseActButtonFrame.setObjectName("MouseActButtonFrame")
		self.gridLayout_60 = QtWidgets.QGridLayout(self.MouseActButtonFrame)
		self.gridLayout_60.setContentsMargins(0, 0, 0, 0)
		self.gridLayout_60.setObjectName("gridLayout_60")
		self.MouseActOnButton = QtWidgets.QPushButton(self.MouseActButtonFrame)
		self.MouseActOnButton.setCheckable(True)
		self.MouseActOnButton.setChecked(True)
		self.MouseActOnButton.setObjectName("MouseActOnButton")
		self.gridLayout_60.addWidget(self.MouseActOnButton, 0, 0, 1, 1)
		self.MouseActOffButton = QtWidgets.QPushButton(self.MouseActButtonFrame)
		self.MouseActOffButton.setCheckable(True)
		self.MouseActOffButton.setObjectName("MouseActOffButton")
		self.gridLayout_60.addWidget(self.MouseActOffButton, 0, 1, 1, 1)
		self.verticalLayout_11.addWidget(self.MouseActButtonFrame, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom)
		self.horizontalLayout_6.addWidget(self.frame_22)
		self.frame_23 = QtWidgets.QFrame(self.configuration_footer)
		self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_23.setObjectName("frame_23")
		self.gridLayout_61 = QtWidgets.QGridLayout(self.frame_23)
		self.gridLayout_61.setObjectName("gridLayout_61")
		self.NetworkActivityStatus = QtWidgets.QLabel(self.frame_23)
		self.NetworkActivityStatus.setMinimumSize(QtCore.QSize(151, 91))
		self.NetworkActivityStatus.setMaximumSize(QtCore.QSize(151, 91))
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.NetworkActivityStatus.setFont(font)
		self.NetworkActivityStatus.setScaledContents(False)
		self.NetworkActivityStatus.setWordWrap(True)
		self.NetworkActivityStatus.setObjectName("NetworkActivityStatus")
		self.gridLayout_61.addWidget(self.NetworkActivityStatus, 2, 0, 1, 2)
		self.NetworkActivityDataLabel = QtWidgets.QLabel(self.frame_23)
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.NetworkActivityDataLabel.setFont(font)
		self.NetworkActivityDataLabel.setObjectName("NetworkActivityDataLabel")
		self.gridLayout_61.addWidget(self.NetworkActivityDataLabel, 0, 0, 1, 2)
		self.NetworkActivityDataUnit = QtWidgets.QComboBox(self.frame_23)
		self.NetworkActivityDataUnit.setMaximumSize(QtCore.QSize(300, 20))
		self.NetworkActivityDataUnit.setObjectName("NetworkActivityDataUnit")
		self.NetworkActivityDataUnit.addItem("")
		self.gridLayout_61.addWidget(self.NetworkActivityDataUnit, 0, 2, 1, 1)
		self.NetworkActivityDataWaiValue = QtWidgets.QComboBox(self.frame_23)
		self.NetworkActivityDataWaiValue.setMaximumSize(QtCore.QSize(300, 20))
		self.NetworkActivityDataWaiValue.setObjectName("NetworkActivityDataWaiValue")
		self.NetworkActivityDataWaiValue.addItem("")
		self.gridLayout_61.addWidget(self.NetworkActivityDataWaiValue, 1, 2, 1, 1)
		self.NetworkActivityButtonFrame = QtWidgets.QFrame(self.frame_23)
		self.NetworkActivityButtonFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.NetworkActivityButtonFrame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.NetworkActivityButtonFrame.setObjectName("NetworkActivityButtonFrame")
		self.gridLayout_63 = QtWidgets.QGridLayout(self.NetworkActivityButtonFrame)
		self.gridLayout_63.setContentsMargins(0, 0, 0, 0)
		self.gridLayout_63.setObjectName("gridLayout_63")
		self.NetworkActivityDataOnButton = QtWidgets.QPushButton(self.NetworkActivityButtonFrame)
		self.NetworkActivityDataOnButton.setCheckable(True)
		self.NetworkActivityDataOnButton.setChecked(True)
		self.NetworkActivityDataOnButton.setObjectName("NetworkActivityDataOnButton")
		self.gridLayout_63.addWidget(self.NetworkActivityDataOnButton, 0, 0, 1, 1)
		self.NetworkActivityDataOffButton = QtWidgets.QPushButton(self.NetworkActivityButtonFrame)
		self.NetworkActivityDataOffButton.setCheckable(True)
		self.NetworkActivityDataOffButton.setObjectName("NetworkActivityDataOffButton")
		self.gridLayout_63.addWidget(self.NetworkActivityDataOffButton, 0, 1, 1, 1)
		self.gridLayout_61.addWidget(self.NetworkActivityButtonFrame, 3, 0, 1, 1,
																	QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom)
		self.horizontalLayout_6.addWidget(self.frame_23)
		self.frame_24 = QtWidgets.QFrame(self.configuration_footer)
		self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_24.setObjectName("frame_24")
		self.gridLayout_62 = QtWidgets.QGridLayout(self.frame_24)
		self.gridLayout_62.setObjectName("gridLayout_62")
		self.ProcessStatLabel = QtWidgets.QLabel(self.frame_24)
		self.ProcessStatLabel.setMinimumSize(QtCore.QSize(151, 91))
		self.ProcessStatLabel.setMaximumSize(QtCore.QSize(151, 91))
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.ProcessStatLabel.setFont(font)
		self.ProcessStatLabel.setScaledContents(False)
		self.ProcessStatLabel.setWordWrap(True)
		self.ProcessStatLabel.setObjectName("ProcessStatLabel")
		self.gridLayout_62.addWidget(self.ProcessStatLabel, 2, 0, 1, 2)
		self.ProcessTitle = QtWidgets.QLabel(self.frame_24)
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.ProcessTitle.setFont(font)
		self.ProcessTitle.setObjectName("ProcessTitle")
		self.gridLayout_62.addWidget(self.ProcessTitle, 1, 0, 1, 1)
		self.ProcessStatButtonFrame = QtWidgets.QFrame(self.frame_24)
		self.ProcessStatButtonFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.ProcessStatButtonFrame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.ProcessStatButtonFrame.setObjectName("ProcessStatButtonFrame")
		self.gridLayout_64 = QtWidgets.QGridLayout(self.ProcessStatButtonFrame)
		self.gridLayout_64.setContentsMargins(0, 0, 0, 0)
		self.gridLayout_64.setObjectName("gridLayout_64")
		self.ProcessStatOnButton = QtWidgets.QPushButton(self.ProcessStatButtonFrame)
		self.ProcessStatOnButton.setCheckable(True)
		self.ProcessStatOnButton.setChecked(True)
		self.ProcessStatOnButton.setObjectName("ProcessStatOnButton")
		self.gridLayout_64.addWidget(self.ProcessStatOnButton, 0, 0, 1, 1)
		self.ProcessStatOffButton = QtWidgets.QPushButton(self.ProcessStatButtonFrame)
		self.ProcessStatOffButton.setCheckable(True)
		self.ProcessStatOffButton.setObjectName("ProcessStatOffButton")
		self.gridLayout_64.addWidget(self.ProcessStatOffButton, 0, 1, 1, 1)
		self.gridLayout_62.addWidget(self.ProcessStatButtonFrame, 3, 0, 1, 1,
																	QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom)
		self.horizontalLayout_6.addWidget(self.frame_24)
		self.verticalLayout_10.addWidget(self.configuration_footer)
		self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_5)
		self.gridLayout_53.addWidget(self.scrollArea_4, 0, 0, 1, 1)
		# self.tabWidget.addTab(self.tab_2, "")

		_translate = QtCore.QCoreApplication.translate

		self.StorageThreshLabel.setText(_translate("MainWindow", "Storage Threshold"))
		self.StorageTitle.setText(_translate("MainWindow", "Storage"))
		self.StorageInValue.setPlaceholderText(_translate("MainWindow", "Enter Percent"))
		self.VideoStatOnButton.setText(_translate("MainWindow", "On"))
		self.VideoStatusOffButton.setText(_translate("MainWindow", "Off"))
		self.VideoResolutionSelect.setItemText(0, _translate("MainWindow", "Video Resolution"))
		self.VideoResolutionSelect.setItemText(1, _translate("MainWindow", "360"))
		self.VideoResolutionSelect.setItemText(2, _translate("MainWindow", "720"))
		self.VideoResolutionSelect.setItemText(3, _translate("MainWindow", "480"))
		self.VideoResolutionSelect.setItemText(4, _translate("MainWindow", "1080"))
		self.WaitValueSelection.setItemText(0, _translate("MainWindow", "Video Recording Wait Value"))
		self.WaitValueSelection.setItemText(1, _translate("MainWindow", "Seconds"))
		self.WaitValueSelection.setItemText(2, _translate("MainWindow", "Minutes"))
		self.WaitValueSelection.setItemText(3, _translate("MainWindow", "Hours"))
		self.VideoTitle.setText(_translate("MainWindow", "Video"))
		self.VideoWaitSelection.setItemText(0, _translate("MainWindow", "Video Recording Wait"))
		self.VideoWaitSelection.setItemText(1, _translate("MainWindow", "15"))
		self.VideoWaitSelection.setItemText(2, _translate("MainWindow", "30"))
		self.FrameRateSelect.setItemText(0, _translate("MainWindow", "Video Frame Rate"))
		self.FrameRateSelect.setItemText(1, _translate("MainWindow", "15"))
		self.FrameRateSelect.setItemText(2, _translate("MainWindow", "30"))
		self.VideoAutoStat.setText(_translate("MainWindow", "Automatic Video Recording Default Stauts"))
		self.ScreenshotStat.setText(_translate("MainWindow", "Automatic Screenshot Recording Default Stauts"))
		self.ScreenshotTitle.setText(_translate("MainWindow", "Screenshot"))
		self.ScreenshotFormatDrop.setItemText(0, _translate("MainWindow", "Screenshot Format Default"))
		self.ScreenshotFormatDrop.setItemText(1, _translate("MainWindow", "JPG"))
		self.ScreenshotFormatDrop.setItemText(2, _translate("MainWindow", "PNG"))
		self.ScreenshotStatOnButton.setText(_translate("MainWindow", "On"))
		self.ScreenshotStatOffButton.setText(_translate("MainWindow", "Off"))
		self.SysCallStatus.setText(_translate("MainWindow", "Automatic System Call Recording Default Status"))
		self.SystemCallLabel.setText(_translate("MainWindow", "System Call"))
		self.SystemCallOnButton.setText(_translate("MainWindow", "On"))
		self.SystemCallOffButton.setText(_translate("MainWindow", "Off"))
		self.WindowHistoryWaitVal.setItemText(0, _translate("MainWindow", "Window History Wait Value"))
		self.WindowHistoryStat.setText(_translate("MainWindow", "Automatic Video Recording Default Stauts"))
		self.WindowHistLabel.setText(_translate("MainWindow", "Window History"))
		self.WindowHistoryDurUnit.setItemText(0, _translate("MainWindow", "Window History Duration Unit"))
		self.WindowHistoryOnButton.setText(_translate("MainWindow", "On"))
		self.WindowHistoryOffButton.setText(_translate("MainWindow", "Off"))
		self.KeystrokeStatus.setText(_translate("MainWindow", "Automatic Keystroke Recording Default Status"))
		self.KeystrokeMainLabel.setText(_translate("MainWindow", "Keystroke"))
		self.KeyStrokeStatOnButton.setText(_translate("MainWindow", "On"))
		self.KeyStrokeStatOffButton.setText(_translate("MainWindow", "Off"))
		self.MouseActionTitle.setText(_translate("MainWindow", "Mouse Action"))
		self.MouseActStatus.setText(_translate("MainWindow", "Automatic Mouse Action Recording Default Status"))
		self.MouseActOnButton.setText(_translate("MainWindow", "On"))
		self.MouseActOffButton.setText(_translate("MainWindow", "Off"))
		self.NetworkActivityStatus.setText(
				_translate("MainWindow", "Automatic Network Activity Data Recording Default Stauts"))
		self.NetworkActivityDataLabel.setText(_translate("MainWindow", "Network Activity Data"))
		self.NetworkActivityDataUnit.setItemText(0, _translate("MainWindow", "Network Activity Data Duration Unit"))
		self.NetworkActivityDataWaiValue.setItemText(0,
																									_translate("MainWindow", "Network Activity Data Duration Value"))
		self.NetworkActivityDataOnButton.setText(_translate("MainWindow", "On"))
		self.NetworkActivityDataOffButton.setText(_translate("MainWindow", "Off"))
		self.ProcessStatLabel.setText(_translate("MainWindow", "Automatic Process Recording Default Status"))
		self.ProcessTitle.setText(_translate("MainWindow", "Process"))
		self.ProcessStatOnButton.setText(_translate("MainWindow", "On"))
		self.ProcessStatOffButton.setText(_translate("MainWindow", "Off"))
		# self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Configuration"))
	

	def get_tab(self):
		return self.tab_2