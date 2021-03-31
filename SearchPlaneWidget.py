# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchPlaneWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SEARCHPLANEPanel(object):
    def setupUi(self, SEARCHPLANEPanel):
        SEARCHPLANEPanel.setObjectName("SEARCHPLANEPanel")
        SEARCHPLANEPanel.resize(845, 785)
        SEARCHPLANEPanel.setMinimumSize(QtCore.QSize(500, 700))
        self.verticalLayout = QtWidgets.QVBoxLayout(SEARCHPLANEPanel)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top = QtWidgets.QFrame(SEARCHPLANEPanel)
        self.top.setMaximumSize(QtCore.QSize(16777215, 40))
        self.top.setBaseSize(QtCore.QSize(0, 0))
        self.top.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top.setObjectName("top")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout.addWidget(self.top)
        self.content = QtWidgets.QFrame(SEARCHPLANEPanel)
        self.content.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.main = QtWidgets.QFrame(self.content)
        self.main.setMaximumSize(QtCore.QSize(800, 550))
        self.main.setStyleSheet("background-color: rgb(57, 57, 57);\n"
"border-radius: 10px;")
        self.main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main.setObjectName("main")
        self.TAILNUMBERLabel = QtWidgets.QLabel(self.main)
        self.TAILNUMBERLabel.setGeometry(QtCore.QRect(450, 90, 341, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.TAILNUMBERLabel.setFont(font)
        self.TAILNUMBERLabel.setStyleSheet("color: rgb(8, 148, 255);\n"
"color: rgb(127, 191, 191);")
        self.TAILNUMBERLabel.setObjectName("TAILNUMBERLabel")
        self.YEAROFPR = QtWidgets.QLabel(self.main)
        self.YEAROFPR.setGeometry(QtCore.QRect(440, 210, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.YEAROFPR.setFont(font)
        self.YEAROFPR.setStyleSheet("color: rgb(255, 255, 255);")
        self.YEAROFPR.setWordWrap(False)
        self.YEAROFPR.setObjectName("YEAROFPR")
        self.YEAROFPRLabel = QtWidgets.QLabel(self.main)
        self.YEAROFPRLabel.setGeometry(QtCore.QRect(690, 230, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.YEAROFPRLabel.setFont(font)
        self.YEAROFPRLabel.setStyleSheet("color: rgb(169, 169, 169);")
        self.YEAROFPRLabel.setObjectName("YEAROFPRLabel")
        self.FLIGHTMILES = QtWidgets.QLabel(self.main)
        self.FLIGHTMILES.setGeometry(QtCore.QRect(440, 260, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.FLIGHTMILES.setFont(font)
        self.FLIGHTMILES.setStyleSheet("color: rgb(255, 255, 255);")
        self.FLIGHTMILES.setWordWrap(False)
        self.FLIGHTMILES.setObjectName("FLIGHTMILES")
        self.FLIGHTMILESLabel = QtWidgets.QLabel(self.main)
        self.FLIGHTMILESLabel.setGeometry(QtCore.QRect(650, 280, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.FLIGHTMILESLabel.setFont(font)
        self.FLIGHTMILESLabel.setStyleSheet("color: rgb(169, 169, 169);")
        self.FLIGHTMILESLabel.setObjectName("FLIGHTMILESLabel")
        self.CAPACITY = QtWidgets.QLabel(self.main)
        self.CAPACITY.setGeometry(QtCore.QRect(440, 310, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.CAPACITY.setFont(font)
        self.CAPACITY.setStyleSheet("color: rgb(255, 255, 255);")
        self.CAPACITY.setWordWrap(False)
        self.CAPACITY.setObjectName("CAPACITY")
        self.CAPACITYLabel = QtWidgets.QLabel(self.main)
        self.CAPACITYLabel.setGeometry(QtCore.QRect(630, 330, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.CAPACITYLabel.setFont(font)
        self.CAPACITYLabel.setStyleSheet("color: rgb(169, 169, 169);")
        self.CAPACITYLabel.setObjectName("CAPACITYLabel")
        self.PLANEIcon = QtWidgets.QFrame(self.main)
        self.PLANEIcon.setGeometry(QtCore.QRect(60, 20, 321, 491))
        self.PLANEIcon.setStyleSheet("background-image: url(:/newPrefix/img/PlaneSearchResize.jpg);")
        self.PLANEIcon.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PLANEIcon.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PLANEIcon.setObjectName("PLANEIcon")
        self.horizontalLayout.addWidget(self.main)
        self.verticalLayout.addWidget(self.content)
        self.bottom = QtWidgets.QFrame(SEARCHPLANEPanel)
        self.bottom.setMaximumSize(QtCore.QSize(16777215, 40))
        self.bottom.setBaseSize(QtCore.QSize(0, 0))
        self.bottom.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom.setObjectName("bottom")
        self.verticalLayout.addWidget(self.bottom)

        self.retranslateUi(SEARCHPLANEPanel)
        QtCore.QMetaObject.connectSlotsByName(SEARCHPLANEPanel)

    def retranslateUi(self, SEARCHPLANEPanel):
        _translate = QtCore.QCoreApplication.translate
        SEARCHPLANEPanel.setWindowTitle(_translate("SEARCHPLANEPanel", "SEARCH PLANE"))
        self.TAILNUMBERLabel.setText(_translate("SEARCHPLANEPanel", "A-13445"))
        self.YEAROFPR.setText(_translate("SEARCHPLANEPanel", "YEAR OF PRODUCTION:"))
        self.YEAROFPRLabel.setText(_translate("SEARCHPLANEPanel", "2008"))
        self.FLIGHTMILES.setText(_translate("SEARCHPLANEPanel", "FLIGHT MILES:"))
        self.FLIGHTMILESLabel.setText(_translate("SEARCHPLANEPanel", "15998"))
        self.CAPACITY.setText(_translate("SEARCHPLANEPanel", "CAPACITY:"))
        self.CAPACITYLabel.setText(_translate("SEARCHPLANEPanel", "650"))
import file


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SEARCHPLANEPanel = QtWidgets.QWidget()
    ui = Ui_SEARCHPLANEPanel()
    ui.setupUi(SEARCHPLANEPanel)
    SEARCHPLANEPanel.show()
    sys.exit(app.exec_())
