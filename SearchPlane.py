# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchPlane.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from TicketAir import Plane

class Ui_SearchPlane(object):
    def setupUi(self, SearchPlane):
        SearchPlane.setObjectName("SearchPlane")
        SearchPlane.resize(1140, 678)
        SearchPlane.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(SearchPlane)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_bar = QtWidgets.QFrame(self.centralwidget)
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.top_bar.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.top_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout.addWidget(self.top_bar)
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Label = QtWidgets.QFrame(self.content)
        self.Label.setMaximumSize(QtCore.QSize(800, 550))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Label.setFont(font)
        self.Label.setStyleSheet("background-color: rgb(57, 57, 57);")
        self.Label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Label.setObjectName("Label")
        self.PLANEIcon = QtWidgets.QFrame(self.Label)
        self.PLANEIcon.setGeometry(QtCore.QRect(70, 30, 331, 481))
        self.PLANEIcon.setStyleSheet("background-image: url(:/newPrefix/img/PlaneSearchResize.jpg);")
        self.PLANEIcon.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PLANEIcon.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PLANEIcon.setObjectName("PLANEIcon")
        self.TAILNUMBERLabel = QtWidgets.QLabel(self.Label)
        self.TAILNUMBERLabel.setGeometry(QtCore.QRect(450, 70, 341, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.TAILNUMBERLabel.setFont(font)
        self.TAILNUMBERLabel.setStyleSheet("color: rgb(8, 148, 255);")
        self.TAILNUMBERLabel.setObjectName("TAILNUMBERLabel")
        self.label_2 = QtWidgets.QLabel(self.Label)
        self.label_2.setGeometry(QtCore.QRect(440, 240, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.Label)
        self.label_3.setGeometry(QtCore.QRect(440, 310, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.Label)
        self.label_4.setGeometry(QtCore.QRect(440, 380, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.YEAROFPRLabel = QtWidgets.QLabel(self.Label)
        self.YEAROFPRLabel.setGeometry(QtCore.QRect(690, 260, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.YEAROFPRLabel.setFont(font)
        self.YEAROFPRLabel.setStyleSheet("color: rgb(169, 169, 169);")
        self.YEAROFPRLabel.setObjectName("YEAROFPRLabel")
        self.FLIGHTMILESLabel = QtWidgets.QLabel(self.Label)
        self.FLIGHTMILESLabel.setGeometry(QtCore.QRect(610, 330, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.FLIGHTMILESLabel.setFont(font)
        self.FLIGHTMILESLabel.setStyleSheet("color: rgb(169, 169, 169);")
        self.FLIGHTMILESLabel.setObjectName("FLIGHTMILESLabel")
        self.CAPACITYLabel = QtWidgets.QLabel(self.Label)
        self.CAPACITYLabel.setGeometry(QtCore.QRect(570, 400, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.CAPACITYLabel.setFont(font)
        self.CAPACITYLabel.setStyleSheet("color: rgb(169, 169, 169);")
        self.CAPACITYLabel.setObjectName("CAPACITYLabel")
        self.horizontalLayout.addWidget(self.Label)
        self.verticalLayout.addWidget(self.content)
        self.bottom = QtWidgets.QFrame(self.centralwidget)
        self.bottom.setMaximumSize(QtCore.QSize(16777215, 35))
        self.bottom.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom.setObjectName("bottom")
        self.verticalLayout.addWidget(self.bottom)
        SearchPlane.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SearchPlane)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1140, 18))
        self.menubar.setObjectName("menubar")
        SearchPlane.setMenuBar(self.menubar)
        self.retranslateUi(SearchPlane)
        QtCore.QMetaObject.connectSlotsByName(SearchPlane)

    def retranslateUi(self, SearchPlane):
        _translate = QtCore.QCoreApplication.translate
        SearchPlane.setWindowTitle(_translate("SearchPlane", "Search Plane"))
        self.TAILNUMBERLabel.setText(_translate("SearchPlane", "A-13445"))
        self.label_2.setText(_translate("SearchPlane", "YEAR OF PRODUCTION:"))
        self.label_3.setText(_translate("SearchPlane", "FLIGHT MILES:"))
        self.label_4.setText(_translate("SearchPlane", "CAPACITY:"))
        self.YEAROFPRLabel.setText(_translate("SearchPlane", "2008"))
        self.FLIGHTMILESLabel.setText(_translate("SearchPlane", "15998"))
        self.CAPACITYLabel.setText(_translate("SearchPlane", "650"))

    def setPlane(self, plane):
        _translate = QtCore.QCoreApplication.translate
        self.TAILNUMBERLabel.setText(_translate("SearchPlane", str(plane.tailNumber)))
        self.label_2.setText(_translate("SearchPlane", "YEAR OF PRODUCTION:"))
        self.label_3.setText(_translate("SearchPlane", "FLIGHT MILES:"))
        self.label_4.setText(_translate("SearchPlane", "CAPACITY:"))
        self.YEAROFPRLabel.setText(_translate("SearchPlane", str(plane.yearOfProduction)))
        self.FLIGHTMILESLabel.setText(_translate("SearchPlane", str(plane.flightMiles)))
        self.CAPACITYLabel.setText(_translate("SearchPlane", str(plane.capacity)))
import file




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SearchPlane = QtWidgets.QMainWindow()
    ui = Ui_SearchPlane()
    ui.setupUi(SearchPlane)
    SearchPlane.show()
    boeing737 = Plane(2000, 0, 150, 'LOTPL2115')
    ui.setPlane(boeing737)
    sys.exit(app.exec_())
