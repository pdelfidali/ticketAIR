# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LOGINWindow(object):
    def setupUi(self, LOGINWindow):
        LOGINWindow.setObjectName("LOGINWindow")
        LOGINWindow.resize(691, 775)
        LOGINWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(LOGINWindow)
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
        self.ERRORFrame = QtWidgets.QFrame(self.top_bar)
        self.ERRORFrame.setMaximumSize(QtCore.QSize(450, 16777215))
        self.ERRORFrame.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"border-radius: 5px;")
        self.ERRORFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ERRORFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ERRORFrame.setObjectName("ERRORFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.ERRORFrame)
        self.horizontalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ERRORLabel = QtWidgets.QLabel(self.ERRORFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ERRORLabel.setFont(font)
        self.ERRORLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ERRORLabel.setObjectName("ERRORLabel")
        self.horizontalLayout_3.addWidget(self.ERRORLabel)
        self.ERRORXButton = QtWidgets.QPushButton(self.ERRORFrame)
        self.ERRORXButton.setMaximumSize(QtCore.QSize(20, 20))
        self.ERRORXButton.setStyleSheet("QPushButton {\n"
"    border-raadius: 5px;\n"
"    background-position: centre;\n"
"    border: 2px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);\n"
"    color: rgb(255, 234, 70);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(255, 234, 70);\n"
"}")
        self.ERRORXButton.setObjectName("ERRORXButton")
        self.horizontalLayout_3.addWidget(self.ERRORXButton)
        self.horizontalLayout_2.addWidget(self.ERRORFrame)
        self.verticalLayout.addWidget(self.top_bar)
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PASSWORDLabel = QtWidgets.QFrame(self.content)
        self.PASSWORDLabel.setMaximumSize(QtCore.QSize(450, 550))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PASSWORDLabel.setFont(font)
        self.PASSWORDLabel.setStyleSheet("background-color: rgb(57, 57, 57);\n"
"border-radius: 10px;")
        self.PASSWORDLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PASSWORDLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PASSWORDLabel.setObjectName("PASSWORDLabel")
        self.logo = QtWidgets.QFrame(self.PASSWORDLabel)
        self.logo.setGeometry(QtCore.QRect(130, 0, 201, 161))
        self.logo.setStyleSheet("background-image: url(:/LogoImage/logo.png);\n"
"background-repeat: no-repeat;\n"
"background-position:center;")
        self.logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.avatar = QtWidgets.QFrame(self.PASSWORDLabel)
        self.avatar.setGeometry(QtCore.QRect(190, 270, 61, 61))
        self.avatar.setStyleSheet("QFrame {\n"
"    background-image: url(:/User/userv3.png);\n"
"    border: 7px solid;\n"
"}\n"
"")
        self.avatar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.avatar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.avatar.setObjectName("avatar")
        self.avatar.setStyleSheet("background-image: url(:/User/avatarv3.png);\n")
        self.USERLabel = QtWidgets.QLineEdit(self.PASSWORDLabel)
        self.USERLabel.setGeometry(QtCore.QRect(120, 340, 200, 45))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.USERLabel.setFont(font)
        self.USERLabel.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45,45,45);\n"
"    border-radius: 5px;    \n"
"    padding: 15 px;\n"
"    background-color: rgb(30,30,30);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(55,55,55);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(255,255,127);\n"
"    color: rgb(200,200,200)\n"
"}")
        self.USERLabel.setText("")
        self.USERLabel.setMaxLength(100)
        self.USERLabel.setObjectName("USERLabel")
        self.PASSWORDLabel_2 = QtWidgets.QLineEdit(self.PASSWORDLabel)
        self.PASSWORDLabel_2.setGeometry(QtCore.QRect(120, 390, 200, 45))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.PASSWORDLabel_2.setFont(font)
        self.PASSWORDLabel_2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45,45,45);\n"
"    border-radius: 5px;    \n"
"    padding: 15 px;\n"
"    background-color: rgb(30,30,30);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(55,55,55);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(255,255,127);\n"
"    color: rgb(200,200,200)\n"
"}")
        self.PASSWORDLabel_2.setText("")
        self.PASSWORDLabel_2.setMaxLength(100)
        self.PASSWORDLabel_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PASSWORDLabel_2.setObjectName("PASSWORDLabel_2")
        self.NEWUSERBox = QtWidgets.QCheckBox(self.PASSWORDLabel)
        self.NEWUSERBox.setGeometry(QtCore.QRect(120, 440, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.NEWUSERBox.setFont(font)
        self.NEWUSERBox.setStyleSheet("QCheckBox::indicator {\n"
"    border: 3px solid rgb(100,100,100);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(135, 135, 135);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 3px solid rgb(255,255,0);\n"
"    background-color: rgb(255, 255, 127);\n"
"}")
        self.NEWUSERBox.setObjectName("NEWUSERBox")
        self.LOGINButton = QtWidgets.QPushButton(self.PASSWORDLabel)
        self.LOGINButton.setGeometry(QtCore.QRect(130, 480, 201, 31))
        self.LOGINButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 2px solid rgb(60,60,60);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(70,70,70);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 127);\n"
"    border: 2px solid rgb(0,0,0);\n"
"    border-radius: 5px;\n"
"    \n"
"    color: rgb(35, 35, 35);\n"
"}")
        self.LOGINButton.setObjectName("LOGINButton")
        self.horizontalLayout.addWidget(self.PASSWORDLabel)
        self.verticalLayout.addWidget(self.content)
        self.bottom = QtWidgets.QFrame(self.centralwidget)
        self.bottom.setMaximumSize(QtCore.QSize(16777215, 35))
        self.bottom.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom.setObjectName("bottom")
        self.verticalLayout.addWidget(self.bottom)
        LOGINWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LOGINWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 691, 18))
        self.menubar.setObjectName("menubar")
        LOGINWindow.setMenuBar(self.menubar)

        self.retranslateUi(LOGINWindow)
        QtCore.QMetaObject.connectSlotsByName(LOGINWindow)

    def retranslateUi(self, LOGINWindow):
        _translate = QtCore.QCoreApplication.translate
        LOGINWindow.setWindowTitle(_translate("LOGINWindow", "Login"))
        self.ERRORLabel.setText(_translate("LOGINWindow", "ERROR"))
        self.ERRORXButton.setText(_translate("LOGINWindow", "X"))
        self.USERLabel.setPlaceholderText(_translate("LOGINWindow", "USER"))
        self.PASSWORDLabel_2.setPlaceholderText(_translate("LOGINWindow", "PASSWORD"))
        self.NEWUSERBox.setText(_translate("LOGINWindow", "NEW USER"))
        self.LOGINButton.setText(_translate("LOGINWindow", "LOGIN "))
import file


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LOGINWindow = QtWidgets.QMainWindow()
    ui = Ui_LOGINWindow()
    ui.setupUi(LOGINWindow)
    LOGINWindow.show()
    sys.exit(app.exec_())