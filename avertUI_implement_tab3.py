
import time
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtChart import QChart, QChartView, QPieSeries
from PyQt5.QtGui import QPen
from PyQt5.QtCore import Qt

import addition_for_synctab


def getAllFrameForTab3():

    def toggleButtons(val):
        if val == "allecludingvideo_btn":
            allexcludingvideo_btn.setChecked(1)
            allincludingvideo_btn.setChecked(0)
        
        if val == "allincludingvideo_btn":
            allexcludingvideo_btn.setChecked(0)
            allincludingvideo_btn.setChecked(1)
    
    def syncbuttonpressed():
        if not (allexcludingvideo_btn.isChecked() or allincludingvideo_btn.isChecked()):
            errormessage.setHidden(False)
        else: #start progress bar
            errormessage.setHidden(True)


    #tab 3
    tab_3 = QtWidgets.QWidget()
    tab_3.setObjectName("tab_3")

    # Sync Basic Information Content Area (SRS 57)
    syncbasicinformation_frame = QtWidgets.QFrame(tab_3)
    syncbasicinformation_frame.setGeometry(QtCore.QRect(50, 60, 511, 111))
    syncbasicinformation_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    syncbasicinformation_frame.setFrameShadow(QtWidgets.QFrame.Raised)
    syncbasicinformation_frame.setObjectName("syncbasicinformation_frame")
    fromIPlabel_label = QtWidgets.QLabel(syncbasicinformation_frame)
    fromIPlabel_label.setGeometry(QtCore.QRect(10, 10, 231, 31))
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(fromIPlabel_label.sizePolicy().hasHeightForWidth())
    fromIPlabel_label.setSizePolicy(sizePolicy)
    font = QtGui.QFont()
    font.setPointSize(16)
    fromIPlabel_label.setFont(font)
    fromIPlabel_label.setObjectName("fromIPlabel_label")
    fromMAClabel_label = QtWidgets.QLabel(syncbasicinformation_frame)
    fromMAClabel_label.setGeometry(QtCore.QRect(10, 40, 231, 31))
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(fromMAClabel_label.sizePolicy().hasHeightForWidth())
    fromMAClabel_label.setSizePolicy(sizePolicy)
    font = QtGui.QFont()
    font.setPointSize(16)
    fromMAClabel_label.setFont(font)
    fromMAClabel_label.setObjectName("fromMAClabel_label")
    toIPlabel_label = QtWidgets.QLabel(syncbasicinformation_frame)
    toIPlabel_label.setGeometry(QtCore.QRect(10, 70, 231, 31))
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(toIPlabel_label.sizePolicy().hasHeightForWidth())
    toIPlabel_label.setSizePolicy(sizePolicy)
    font = QtGui.QFont()
    font.setPointSize(16)
    toIPlabel_label.setFont(font)
    toIPlabel_label.setObjectName("toIPlabel_label")
    fromIPval_label = QtWidgets.QLabel(syncbasicinformation_frame)
    fromIPval_label.setGeometry(QtCore.QRect(290, 10, 191, 31))
    font = QtGui.QFont()
    font.setPointSize(16)
    fromIPval_label.setFont(font)
    fromIPval_label.setObjectName("fromIPval_label")
    fromMACval_label = QtWidgets.QLabel(syncbasicinformation_frame)
    fromMACval_label.setGeometry(QtCore.QRect(290, 40, 191, 31))
    font = QtGui.QFont()
    font.setPointSize(16)
    fromMACval_label.setFont(font)
    fromMACval_label.setObjectName("fromMACval_label")
    toIPval_lineEdit = QtWidgets.QLineEdit(syncbasicinformation_frame)
    toIPval_lineEdit.setGeometry(QtCore.QRect(290, 70, 211, 31))
    font = QtGui.QFont()
    font.setPointSize(16)
    toIPval_lineEdit.setFont(font)
    toIPval_lineEdit.setText("")
    toIPval_lineEdit.setObjectName("toIPval_lineEdit")


    progresssection = QtWidgets.QGroupBox(tab_3)
    progresssection.setGeometry(QtCore.QRect(0, 250, 1761, 771))
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                       QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(
        progresssection.sizePolicy().hasHeightForWidth())
    progresssection.setSizePolicy(sizePolicy)
    progresssection.setObjectName("progresssection")

    """still screenshot"""
    style =''' 
    QProgressBar
    {
        border: 1px solid grey;
        border-radius: 3px;
        text-align: center;
    }
    '''

    stillscreenshot_frame = QtWidgets.QFrame(progresssection)
    stillscreenshot_frame.setGeometry(QtCore.QRect(220, 30, 581, 141))
    stillscreenshot_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    stillscreenshot_frame.setFrameShadow(QtWidgets.QFrame.Raised)
    stillscreenshot_frame.setObjectName("stillscreenshot_frame")
    stillscreenshot_progressBar = QtWidgets.QProgressBar(stillscreenshot_frame)
    stillscreenshot_progressBar.setMaximum(100)
    stillscreenshot_progressBar.setMinimum(0)
    stillscreenshot_progressBar.setStyleSheet(style)
    # stillscreenshot_progressBar.setFormat('some text')
    stillscreenshot_progressBar.setValue(0)
    stillscreenshot_progressBar.setTextVisible(True)
    stillscreenshot_progressBar.setGeometry(QtCore.QRect(10, 70, 541, 31))
    stillscreenshot_progressBar.setObjectName("stillscreenshot_progressBar")
    stillscreenshot_pushButton = QtWidgets.QPushButton(stillscreenshot_frame)
    stillscreenshot_pushButton.setGeometry(QtCore.QRect(190, 110, 211, 31))
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                       QtWidgets.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(
        stillscreenshot_pushButton.sizePolicy().hasHeightForWidth())
    stillscreenshot_pushButton.setSizePolicy(sizePolicy)
    stillscreenshot_pushButton.setObjectName("stillscreenshot_pushButton")
    stillscreenshot_label_0 = QtWidgets.QLabel(stillscreenshot_frame)
    stillscreenshot_label_0.setGeometry(QtCore.QRect(0, 90, 21, 16))
    stillscreenshot_label_0.setObjectName("stillscreenshot_label_0")
    stillscreenshot_label_100 = QtWidgets.QLabel(stillscreenshot_frame)
    stillscreenshot_label_100.setGeometry(QtCore.QRect(530, 90, 41, 16))
    stillscreenshot_label_100.setObjectName("stillscreenshot_label_100")
    stillscreenshot_label = QtWidgets.QLabel(stillscreenshot_frame)
    stillscreenshot_label.setGeometry(QtCore.QRect(0, 30, 581, 31))
    font = QtGui.QFont()
    font.setFamily("Avenir Next Condensed")
    font.setPointSize(28)
    font.setItalic(True)
    stillscreenshot_label.setFont(font)
    stillscreenshot_label.setAlignment(QtCore.Qt.AlignCenter)
    stillscreenshot_label.setObjectName("stillscreenshot_label")
    """still screenshot"""

    """process"""
    process_frame = QtWidgets.QFrame(progresssection)
    process_frame.setGeometry(QtCore.QRect(220, 170, 581, 141))
    process_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    process_frame.setFrameShadow(QtWidgets.QFrame.Raised)
    process_frame.setObjectName("process_frame")
    process_progressBar = QtWidgets.QProgressBar(process_frame)
    process_progressBar.setGeometry(QtCore.QRect(10, 70, 541, 31))
    process_progressBar.setProperty("value", 24)
    process_progressBar.setObjectName("process_progressBar")
    process_pushButton = QtWidgets.QPushButton(process_frame)
    process_pushButton.setGeometry(QtCore.QRect(210, 110, 151, 31))
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                       QtWidgets.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(
        process_pushButton.sizePolicy().hasHeightForWidth())
    process_pushButton.setSizePolicy(sizePolicy)
    process_pushButton.setObjectName("process_pushButton")
    process_label_0 = QtWidgets.QLabel(process_frame)
    process_label_0.setGeometry(QtCore.QRect(0, 90, 21, 16))
    process_label_0.setObjectName("process_label_0")
    process_label_100 = QtWidgets.QLabel(process_frame)
    process_label_100.setGeometry(QtCore.QRect(530, 90, 41, 16))
    process_label_100.setObjectName("process_label_100")
    process_label = QtWidgets.QLabel(process_frame)
    process_label.setGeometry(QtCore.QRect(0, 30, 581, 31))
    font = QtGui.QFont()
    font.setFamily("Avenir Next Condensed")
    font.setPointSize(28)
    font.setItalic(True)
    process_label.setFont(font)
    process_label.setAlignment(QtCore.Qt.AlignCenter)
    process_label.setObjectName("process_label")
    """process"""

    """keystroke"""
    keystroke_frame = QtWidgets.QFrame(progresssection)
    keystroke_frame.setGeometry(QtCore.QRect(220, 310, 581, 141))
    keystroke_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    keystroke_frame.setFrameShadow(QtWidgets.QFrame.Raised)
    keystroke_frame.setObjectName("keystroke_frame")
    keystroke_progressBar = QtWidgets.QProgressBar(keystroke_frame)
    keystroke_progressBar.setGeometry(QtCore.QRect(10, 70, 541, 31))
    keystroke_progressBar.setProperty("value", 24)
    keystroke_progressBar.setObjectName("keystroke_progressBar")
    keystroke_pushButton = QtWidgets.QPushButton(keystroke_frame)
    keystroke_pushButton.setGeometry(QtCore.QRect(200, 100, 171, 31))
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                       QtWidgets.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(
        keystroke_pushButton.sizePolicy().hasHeightForWidth())
    keystroke_pushButton.setSizePolicy(sizePolicy)
    keystroke_pushButton.setObjectName("keystroke_pushButton")
    keystroke_label_0 = QtWidgets.QLabel(keystroke_frame)
    keystroke_label_0.setGeometry(QtCore.QRect(0, 90, 21, 16))
    keystroke_label_0.setObjectName("keystroke_label_0")
    keystroke_label_100 = QtWidgets.QLabel(keystroke_frame)
    keystroke_label_100.setGeometry(QtCore.QRect(530, 90, 41, 16))
    keystroke_label_100.setObjectName("keystroke_label_100")
    keystroke_label = QtWidgets.QLabel(keystroke_frame)
    keystroke_label.setGeometry(QtCore.QRect(0, 30, 581, 31))
    font = QtGui.QFont()
    font.setFamily("Avenir Next Condensed")
    font.setPointSize(28)
    font.setItalic(True)
    keystroke_label.setFont(font)
    keystroke_label.setAlignment(QtCore.Qt.AlignCenter)
    keystroke_label.setObjectName("keystroke_label")
    """keystroke"""

    """window history"""
    windowhistory_frame = QtWidgets.QFrame(progresssection)
    windowhistory_frame.setGeometry(QtCore.QRect(220, 450, 581, 141))
    windowhistory_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    windowhistory_frame.setFrameShadow(QtWidgets.QFrame.Raised)
    windowhistory_frame.setObjectName("windowhistory_frame")
    windowhistory_progressBar = QtWidgets.QProgressBar(windowhistory_frame)
    windowhistory_progressBar.setGeometry(QtCore.QRect(10, 70, 541, 31))
    windowhistory_progressBar.setProperty("value", 24)
    windowhistory_progressBar.setObjectName("windowhistory_progressBar")
    windowhistory_pushButton = QtWidgets.QPushButton(windowhistory_frame)
    windowhistory_pushButton.setGeometry(QtCore.QRect(190, 100, 211, 31))
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                       QtWidgets.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(
        windowhistory_pushButton.sizePolicy().hasHeightForWidth())
    windowhistory_pushButton.setSizePolicy(sizePolicy)
    windowhistory_pushButton.setObjectName("windowhistory_pushButton")
    windowhistory_label_0 = QtWidgets.QLabel(windowhistory_frame)
    windowhistory_label_0.setGeometry(QtCore.QRect(0, 90, 21, 16))
    windowhistory_label_0.setObjectName("windowhistory_label_0")
    windowhistory_label_100 = QtWidgets.QLabel(windowhistory_frame)
    windowhistory_label_100.setGeometry(QtCore.QRect(530, 90, 41, 16))
    windowhistory_label_100.setObjectName("windowhistory_label_100")
    windowhistory_label = QtWidgets.QLabel(windowhistory_frame)
    windowhistory_label.setGeometry(QtCore.QRect(0, 30, 581, 31))
    font = QtGui.QFont()
    font.setFamily("Avenir Next Condensed")
    font.setPointSize(28)
    font.setItalic(True)
    windowhistory_label.setFont(font)
    windowhistory_label.setAlignment(QtCore.Qt.AlignCenter)
    windowhistory_label.setObjectName("windowhistory_label")
    """window history"""

    """history"""
    history_frame = QtWidgets.QFrame(progresssection)
    history_frame.setGeometry(QtCore.QRect(220, 590, 581, 141))
    history_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    history_frame.setFrameShadow(QtWidgets.QFrame.Raised)
    history_frame.setObjectName("history_frame")
    history_progressBar = QtWidgets.QProgressBar(history_frame)
    history_progressBar.setGeometry(QtCore.QRect(10, 70, 541, 31))
    history_progressBar.setProperty("value", 24)
    history_progressBar.setObjectName("history_progressBar")
    history_pushButton = QtWidgets.QPushButton(history_frame)
    history_pushButton.setGeometry(QtCore.QRect(210, 100, 161, 31))
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                       QtWidgets.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(
        history_pushButton.sizePolicy().hasHeightForWidth())
    history_pushButton.setSizePolicy(sizePolicy)
    history_pushButton.setObjectName("history_pushButton")
    history_label_0 = QtWidgets.QLabel(history_frame)
    history_label_0.setGeometry(QtCore.QRect(0, 90, 21, 16))
    history_label_0.setObjectName("history_label_0")
    history_label_100 = QtWidgets.QLabel(history_frame)
    history_label_100.setGeometry(QtCore.QRect(530, 90, 41, 16))
    history_label_100.setObjectName("history_label_100")
    history_label = QtWidgets.QLabel(history_frame)
    history_label.setGeometry(QtCore.QRect(0, 30, 581, 31))
    font = QtGui.QFont()
    font.setFamily("Avenir Next Condensed")
    font.setPointSize(28)
    font.setItalic(True)
    history_label.setFont(font)
    history_label.setAlignment(QtCore.Qt.AlignCenter)
    history_label.setObjectName("history_label")
    """history"""

    """video"""
    video_frame = QtWidgets.QFrame(progresssection)
    video_frame.setGeometry(QtCore.QRect(1000, 30, 581, 141))
    video_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    video_frame.setFrameShadow(QtWidgets.QFrame.Raised)
    video_frame.setObjectName("video_frame")
    video_progressBar = QtWidgets.QProgressBar(video_frame)
    video_progressBar.setGeometry(QtCore.QRect(10, 70, 541, 31))
    video_progressBar.setProperty("value", 24)
    video_progressBar.setObjectName("video_progressBar")
    video_pushButton = QtWidgets.QPushButton(video_frame)
    video_pushButton.setGeometry(QtCore.QRect(220, 110, 151, 31))
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                       QtWidgets.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(
        video_pushButton.sizePolicy().hasHeightForWidth())
    video_pushButton.setSizePolicy(sizePolicy)
    video_pushButton.setObjectName("video_pushButton")
    video_label_0 = QtWidgets.QLabel(video_frame)
    video_label_0.setGeometry(QtCore.QRect(0, 90, 21, 16))
    video_label_0.setObjectName("video_label_0")
    video_label_100 = QtWidgets.QLabel(video_frame)
    video_label_100.setGeometry(QtCore.QRect(530, 90, 41, 16))
    video_label_100.setObjectName("video_label_100")
    video_label = QtWidgets.QLabel(video_frame)
    video_label.setGeometry(QtCore.QRect(0, 30, 581, 31))
    font = QtGui.QFont()
    font.setFamily("Avenir Next Condensed")
    font.setPointSize(28)
    font.setItalic(True)
    video_label.setFont(font)
    video_label.setAlignment(QtCore.Qt.AlignCenter)
    video_label.setObjectName("video_label")
    """video"""

    """network activity"""
    networkactivitydata_frame = QtWidgets.QFrame(progresssection)
    networkactivitydata_frame.setGeometry(QtCore.QRect(1000, 170, 581, 141))
    networkactivitydata_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    networkactivitydata_frame.setFrameShadow(QtWidgets.QFrame.Raised)
    networkactivitydata_frame.setObjectName("networkactivitydata_frame")
    networkactivitydata_progressBar = QtWidgets.QProgressBar(
        networkactivitydata_frame)
    networkactivitydata_progressBar.setGeometry(QtCore.QRect(10, 70, 541, 31))
    networkactivitydata_progressBar.setProperty("value", 24)
    networkactivitydata_progressBar.setObjectName(
        "networkactivitydata_progressBar")
    networkactivitydata_pushButton = QtWidgets.QPushButton(
        networkactivitydata_frame)
    networkactivitydata_pushButton.setGeometry(QtCore.QRect(180, 110, 241, 31))
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                       QtWidgets.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(
        networkactivitydata_pushButton.sizePolicy().hasHeightForWidth())
    networkactivitydata_pushButton.setSizePolicy(sizePolicy)
    networkactivitydata_pushButton.setObjectName(
        "networkactivitydata_pushButton")
    networkactivitydata_label_0 = QtWidgets.QLabel(networkactivitydata_frame)
    networkactivitydata_label_0.setGeometry(QtCore.QRect(0, 90, 21, 16))
    networkactivitydata_label_0.setObjectName("networkactivitydata_label_0")
    networkactivitydata_label_100 = QtWidgets.QLabel(networkactivitydata_frame)
    networkactivitydata_label_100.setGeometry(QtCore.QRect(530, 90, 41, 16))
    networkactivitydata_label_100.setObjectName(
        "networkactivitydata_label_100")
    networkactivitydata_label = QtWidgets.QLabel(networkactivitydata_frame)
    networkactivitydata_label.setGeometry(QtCore.QRect(0, 30, 581, 31))
    font = QtGui.QFont()
    font.setFamily("Avenir Next Condensed")
    font.setPointSize(28)
    font.setItalic(True)
    networkactivitydata_label.setFont(font)
    networkactivitydata_label.setAlignment(QtCore.Qt.AlignCenter)
    networkactivitydata_label.setObjectName("networkactivitydata_label")
    """network activity"""

    """system call"""
    systemcall_frame = QtWidgets.QFrame(progresssection)
    systemcall_frame.setGeometry(QtCore.QRect(1000, 450, 581, 141))
    systemcall_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    systemcall_frame.setFrameShadow(QtWidgets.QFrame.Raised)
    systemcall_frame.setObjectName("systemcall_frame")
    systemcall_progressBar = QtWidgets.QProgressBar(systemcall_frame)
    systemcall_progressBar.setGeometry(QtCore.QRect(10, 70, 541, 31))
    systemcall_progressBar.setProperty("value", 24)
    systemcall_progressBar.setObjectName("systemcall_progressBar")
    systemcall_pushButton = QtWidgets.QPushButton(systemcall_frame)
    systemcall_pushButton.setGeometry(QtCore.QRect(200, 100, 181, 31))
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                       QtWidgets.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(
        systemcall_pushButton.sizePolicy().hasHeightForWidth())
    systemcall_pushButton.setSizePolicy(sizePolicy)
    systemcall_pushButton.setObjectName("systemcall_pushButton")
    systemcall_label_0 = QtWidgets.QLabel(systemcall_frame)
    systemcall_label_0.setGeometry(QtCore.QRect(0, 90, 21, 16))
    systemcall_label_0.setObjectName("systemcall_label_0")
    systemcall_label_100 = QtWidgets.QLabel(systemcall_frame)
    systemcall_label_100.setGeometry(QtCore.QRect(530, 90, 41, 16))
    systemcall_label_100.setObjectName("systemcall_label_100")
    systemcall_label = QtWidgets.QLabel(systemcall_frame)
    systemcall_label.setGeometry(QtCore.QRect(0, 30, 581, 31))
    font = QtGui.QFont()
    font.setFamily("Avenir Next Condensed")
    font.setPointSize(28)
    font.setItalic(True)
    systemcall_label.setFont(font)
    systemcall_label.setAlignment(QtCore.Qt.AlignCenter)
    systemcall_label.setObjectName("systemcall_label")
    """system call"""

    """mouse action"""
    mouseaction_frame = QtWidgets.QFrame(progresssection)
    mouseaction_frame.setGeometry(QtCore.QRect(1000, 310, 581, 141))
    mouseaction_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    mouseaction_frame.setFrameShadow(QtWidgets.QFrame.Raised)
    mouseaction_frame.setObjectName("mouseaction_frame")
    mouseaction_progressBar = QtWidgets.QProgressBar(mouseaction_frame)
    mouseaction_progressBar.setGeometry(QtCore.QRect(10, 70, 541, 31))
    mouseaction_progressBar.setProperty("value", 24)
    mouseaction_progressBar.setObjectName("mouseaction_progressBar")
    mouseaction_pushButton = QtWidgets.QPushButton(mouseaction_frame)
    mouseaction_pushButton.setGeometry(QtCore.QRect(190, 110, 191, 31))
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                       QtWidgets.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(
        mouseaction_pushButton.sizePolicy().hasHeightForWidth())
    mouseaction_pushButton.setSizePolicy(sizePolicy)
    mouseaction_pushButton.setObjectName("mouseaction_pushButton")
    mouseaction_label_0 = QtWidgets.QLabel(mouseaction_frame)
    mouseaction_label_0.setGeometry(QtCore.QRect(0, 90, 21, 16))
    mouseaction_label_0.setObjectName("mouseaction_label_0")
    mouseaction_label_100 = QtWidgets.QLabel(mouseaction_frame)
    mouseaction_label_100.setGeometry(QtCore.QRect(530, 90, 41, 16))
    mouseaction_label_100.setObjectName("mouseaction_label_100")
    mouseaction_label = QtWidgets.QLabel(mouseaction_frame)
    mouseaction_label.setGeometry(QtCore.QRect(0, 30, 581, 31))
    font = QtGui.QFont()
    font.setFamily("Avenir Next Condensed")
    font.setPointSize(28)
    font.setItalic(True)
    mouseaction_label.setFont(font)
    mouseaction_label.setAlignment(QtCore.Qt.AlignCenter)
    mouseaction_label.setObjectName("mouseaction_label")
    """mouse action"""

    """log"""
    log_frame = QtWidgets.QFrame(progresssection)
    log_frame.setGeometry(QtCore.QRect(1000, 590, 581, 141))
    log_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    log_frame.setFrameShadow(QtWidgets.QFrame.Raised)
    log_frame.setObjectName("log_frame")
    log_progressBar = QtWidgets.QProgressBar(log_frame)
    log_progressBar.setGeometry(QtCore.QRect(10, 70, 541, 31))
    log_progressBar.setProperty("value", 24)
    log_progressBar.setObjectName("log_progressBar")
    log_pushButton = QtWidgets.QPushButton(log_frame)
    log_pushButton.setGeometry(QtCore.QRect(230, 100, 131, 31))
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                       QtWidgets.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(
        log_pushButton.sizePolicy().hasHeightForWidth())
    log_pushButton.setSizePolicy(sizePolicy)
    log_pushButton.setObjectName("log_pushButton")
    log_label_0 = QtWidgets.QLabel(log_frame)
    log_label_0.setGeometry(QtCore.QRect(0, 90, 21, 16))
    log_label_0.setObjectName("log_label_0")
    log_label_100 = QtWidgets.QLabel(log_frame)
    log_label_100.setGeometry(QtCore.QRect(530, 90, 41, 16))
    log_label_100.setObjectName("log_label_100")
    log_label = QtWidgets.QLabel(log_frame)
    log_label.setGeometry(QtCore.QRect(0, 30, 581, 31))
    font = QtGui.QFont()
    font.setFamily("Avenir Next Condensed")
    font.setPointSize(28)
    font.setItalic(True)
    log_label.setFont(font)
    log_label.setAlignment(QtCore.Qt.AlignCenter)
    log_label.setObjectName("log_label")
    """log"""

    """btn groups"""
    allincludingvideo_btn = QtWidgets.QPushButton(tab_3)
    allincludingvideo_btn.setGeometry(QtCore.QRect(1520, 65, 181, 32))
    allincludingvideo_btn.setCheckable(True)
    allincludingvideo_btn.setChecked(False)
    font = QtGui.QFont()
    font.setPointSize(16)
    allincludingvideo_btn.setFont(font)
    allincludingvideo_btn.setObjectName("allincludingvideo_btn")

    allexcludingvideo_btn = QtWidgets.QPushButton(tab_3)
    allexcludingvideo_btn.setGeometry(QtCore.QRect(1300, 65, 181, 32))
    allexcludingvideo_btn.setCheckable(True)
    allexcludingvideo_btn.setChecked(False)
    font = QtGui.QFont()
    font.setPointSize(16)
    allexcludingvideo_btn.setFont(font)
    allexcludingvideo_btn.setObjectName("allexcludingvideo_btn")

    cancelall_btn = QtWidgets.QPushButton(tab_3)
    cancelall_btn.setGeometry(QtCore.QRect(810, 980, 171, 31)) #x, y, w, h
    font = QtGui.QFont()
    font.setPointSize(16)
    cancelall_btn.setFont(font)
    cancelall_btn.setObjectName("cancelall_btn")

    sync_btn = QtWidgets.QPushButton(tab_3)
    sync_btn.setGeometry(QtCore.QRect(1470, 145, 71, 32))
    font = QtGui.QFont()
    font.setPointSize(16)
    sync_btn.setFont(font)
    sync_btn.setObjectName("sync_btn")

    errormessage = QtWidgets.QLabel(tab_3)
    errormessage.setGeometry(QtCore.QRect(1350, 105, 300, 16))
    errormessage.setObjectName("errormessage")
    errormessage.setStyleSheet("color: red")
    errormessage.setHidden(True)
    """btn groups"""



    """PIE CHART CONTENT START"""
    # series = QPieSeries()
    # series.append("Available", 80)
    # series.append("Used Space", 30)

    # my_slice = series.slices()[0]
    # my_slice.setExploded(True)
    # my_slice.setLabelVisible(True)
    # my_slice.setPen(QPen(Qt.green, 4))
    # my_slice.setBrush(Qt.green)

    # my_slice = series.slices()[1]
    # my_slice.setExploded(True)
    # my_slice.setLabelVisible(True)
    # my_slice.setPen(QPen(Qt.green, 4))
    # my_slice.setBrush(Qt.green)

    # chart = QChart()
    # chart.addSeries(series)
    # chart.setAnimationOptions(QChart.SeriesAnimations)
    # chart.setTitle("Hard Drive Space")
    # chart.setTheme(QChart.ChartThemeDark)
    # chart.setGeometry(QtCore.QRectF(1310, 110, 171, 31))

    # charview = QChartView(chart)
    # charview.setGeometry(QtCore.QRect(1310, 110, 171, 31))

    # charview = addition_for_synctab.piechart_for_synctab()

    vox = QtWidgets.QVBoxLayout(tab_3)
    vox.setContentsMargins(580, 5, 580, 1070) #ltrb
    vox.addWidget(addition_for_synctab.piechart_for_synctab())
    """PIE CHART CONTENT END"""


    _translate = QtCore.QCoreApplication.translate
    
    fromIPlabel_label.setText(_translate("MainWindow", "From Analyst\'s IP Address:"))
    fromMAClabel_label.setText(_translate("MainWindow", "From Analyst\'s MAC Address:"))
    toIPlabel_label.setText(_translate("MainWindow", "To Analyst\'s IP Address:"))
    fromIPval_label.setText(_translate("MainWindow", "127.0.0.1"))
    fromMACval_label.setText(_translate("MainWindow", "3D-9F-1A-82-2C-0E"))
    toIPval_lineEdit.setPlaceholderText(_translate("MainWindow", "Enter IP Address"))
    progresssection.setTitle(_translate("MainWindow", "Prgress Section"))
    stillscreenshot_pushButton.setText(_translate("MainWindow", "Cancel Still Screenshot Sync"))
    stillscreenshot_label_0.setText(_translate("MainWindow", "0%"))
    stillscreenshot_label_100.setText(_translate("MainWindow", "100%"))
    stillscreenshot_label.setText(_translate("MainWindow", "Still Screenshot"))
    process_pushButton.setText(_translate("MainWindow", "Cancel Process Sync"))
    process_label_0.setText(_translate("MainWindow", "0%"))
    process_label_100.setText(_translate("MainWindow", "100%"))
    process_label.setText(_translate("MainWindow", "Process"))
    keystroke_pushButton.setText(_translate("MainWindow", "Cancel Keystroke Sync"))
    keystroke_label_0.setText(_translate("MainWindow", "0%"))
    keystroke_label_100.setText(_translate("MainWindow", "100%"))
    keystroke_label.setText(_translate("MainWindow", "Keystroke"))
    windowhistory_pushButton.setText(_translate("MainWindow", "Cancel Window History Sync"))
    windowhistory_label_0.setText(_translate("MainWindow", "0%"))
    windowhistory_label_100.setText(_translate("MainWindow", "100%"))
    windowhistory_label.setText(_translate("MainWindow", "Window HIstory"))
    history_pushButton.setText(_translate("MainWindow", "Cancel History Sync"))
    history_label_0.setText(_translate("MainWindow", "0%"))
    history_label_100.setText(_translate("MainWindow", "100%"))
    history_label.setText(_translate("MainWindow", "History"))
    video_pushButton.setText(_translate("MainWindow", "Cancel Video Sync"))
    video_label_0.setText(_translate("MainWindow", "0%"))
    video_label_100.setText(_translate("MainWindow", "100%"))
    video_label.setText(_translate("MainWindow", "Video"))
    networkactivitydata_pushButton.setText(_translate("MainWindow", "Cancel Network Activity Data Sync"))
    networkactivitydata_label_0.setText(_translate("MainWindow", "0%"))
    networkactivitydata_label_100.setText(_translate("MainWindow", "100%"))
    networkactivitydata_label.setText(_translate("MainWindow", "Network Activity Data"))
    systemcall_pushButton.setText(_translate("MainWindow", "Cancel System Call Sync"))
    systemcall_label_0.setText(_translate("MainWindow", "0%"))
    systemcall_label_100.setText(_translate("MainWindow", "100%"))
    systemcall_label.setText(_translate("MainWindow", "System Call"))
    mouseaction_pushButton.setText(_translate("MainWindow", "Cancel Mouse Action Sync"))
    mouseaction_label_0.setText(_translate("MainWindow", "0%"))
    mouseaction_label_100.setText(_translate("MainWindow", "100%"))
    mouseaction_label.setText(_translate("MainWindow", "Mouse Action"))
    log_pushButton.setText(_translate("MainWindow", "Cancel Log Sync"))
    log_label_0.setText(_translate("MainWindow", "0%"))
    log_label_100.setText(_translate("MainWindow", "100%"))
    log_label.setText(_translate("MainWindow", "Log"))
    allincludingvideo_btn.setText(_translate("MainWindow", "All Including Video"))
    allexcludingvideo_btn.setText(_translate("MainWindow", "All Excluding Video"))
    cancelall_btn.setText(_translate("MainWindow", "Cancel All Sync"))
    sync_btn.setText(_translate("MainWindow", "Sycn"))    
    errormessage.setText(_translate("MainWindow", "Error: Please select video sync scope above."))

    """Adding Functinality"""
    # allexcludingvideo_btn.clicked.connect(lambda:toggleButtons('e', allexcludingvideo_btn)) # NOTE: to send as parameter; use lambda
    allexcludingvideo_btn.clicked.connect(lambda: toggleButtons('allecludingvideo_btn'))
    allincludingvideo_btn.clicked.connect(lambda: toggleButtons('allincludingvideo_btn'))
    sync_btn.clicked.connect(syncbuttonpressed)


    return tab_3

