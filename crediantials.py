# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'credintials.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui,Qtwidgets
import  MySqlDB as  mdb
from PyQt4.QtSql import *
db = QSqlDatabase.addDatabase(“QMYSQL”)
db.setDatabaseName(“milk”)
db.setUserName(“root”)
db.setPassword(“”)

db.open()

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 70, 91, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txt_user = QtGui.QLineEdit(Dialog)
        self.txt_user.setGeometry(QtCore.QRect(110, 70, 113, 20))
        self.txt_user.setObjectName(_fromUtf8("txt_user"))
        self.txt_password = QtGui.QLineEdit(Dialog)
        self.txt_password.setGeometry(QtCore.QRect(110, 90, 113, 20))
        self.txt_password.setObjectName(_fromUtf8("txt_password"))
        self.pb_signin = QtGui.QPushButton(Dialog)
        self.pb_signin.setGeometry(QtCore.QRect(110, 130, 75, 23))
        self.pb_signin.setObjectName(_fromUtf8("pb_signin"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 130, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pb_signup"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "User Name", None))
        self.label_2.setText(_translate("Dialog", "Pass Word", None))
        self.pb_signin.setText(_translate("Dialog", "Sign In", None))
        self.pushButton_2.setText(_translate("Dialog", "Sign Up", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

