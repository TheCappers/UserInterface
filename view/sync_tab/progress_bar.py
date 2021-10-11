from PyQt5 import QtWidgets, QtGui, QtCore

class ProgressBar:
	def __init__(self, parent_item, label_text):

		self.frame = QtWidgets.QFrame(parent_item)
		self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtWidgets.QFrame.Raised)

		self.gridLayout_41 = QtWidgets.QGridLayout(self.frame)
		self.label = QtWidgets.QLabel(self.frame)
		font = QtGui.QFont()
		font.setFamily("Avenir Next Condensed")
		font.setPointSize(28)
		font.setItalic(True)
		self.label.setFont(font)
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.gridLayout_41.addWidget(self.label, 0, 0, 1, 5)

		self.progress_bar = QtWidgets.QProgressBar(self.frame)
		self.progress_bar.setProperty("value", 24)
		self.gridLayout_41.addWidget(self.progress_bar, 1, 1, 2, 4)
		self.label_0 = QtWidgets.QLabel(self.frame)
		self.gridLayout_41.addWidget(self.label_0, 2, 0, 1, 1)
		self.label_100 = QtWidgets.QLabel(self.frame)
		self.gridLayout_41.addWidget(self.label_100, 2, 4, 1, 1)
		self.push_button = QtWidgets.QPushButton(self.frame)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.push_button.sizePolicy().hasHeightForWidth())
		self.push_button.setSizePolicy(sizePolicy)
		self.gridLayout_41.addWidget(self.push_button, 3, 3, 1, 1)

		"""set text"""
		_translate = QtCore.QCoreApplication.translate
		self.label.setText(_translate("MainWindow", label_text))
		self.push_button.setText(_translate("MainWindow", "Cancel " + label_text +" Sync"))
		
	def getPBarFrame(self):
		return self.frame