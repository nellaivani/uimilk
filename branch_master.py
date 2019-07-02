# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'branch_master.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(50, 0, 331, 191))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(90, 10, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(90, 30, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(0, 60, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(0, 90, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.txt_sup_code = QtGui.QLineEdit(self.frame)
        self.txt_sup_code.setGeometry(QtCore.QRect(90, 60, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txt_sup_code.setFont(font)
        self.txt_sup_code.setObjectName(_fromUtf8("txt_sup_code"))
        self.txt_sup_name = QtGui.QLineEdit(self.frame)
        self.txt_sup_name.setGeometry(QtCore.QRect(90, 90, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txt_sup_name.setFont(font)
        self.txt_sup_name.setObjectName(_fromUtf8("txt_sup_name"))
        self.pb_add = QtGui.QPushButton(self.frame)
        self.pb_add.setGeometry(QtCore.QRect(10, 130, 75, 23))
        self.pb_add.setObjectName(_fromUtf8("pb_add"))
        self.pb_update = QtGui.QPushButton(self.frame)
        self.pb_update.setGeometry(QtCore.QRect(90, 130, 75, 23))
        self.pb_update.setObjectName(_fromUtf8("pb_update"))
        self.pb_delete = QtGui.QPushButton(self.frame)
        self.pb_delete.setGeometry(QtCore.QRect(170, 130, 75, 23))
        self.pb_delete.setObjectName(_fromUtf8("pb_delete"))
        self.pb_view = QtGui.QPushButton(self.frame)
        self.pb_view.setGeometry(QtCore.QRect(250, 130, 75, 23))
        self.pb_view.setObjectName(_fromUtf8("pb_view"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "aavin::Tirunelveli", None))
        self.label_2.setText(_translate("Dialog", "Branch Master", None))
        self.label_3.setText(_translate("Dialog", "Branch Code", None))
        self.label_4.setText(_translate("Dialog", "Branch Name", None))
        self.pb_add.setText(_translate("Dialog", "Add New", None))
        self.pb_update.setText(_translate("Dialog", "Update", None))
        self.pb_delete.setText(_translate("Dialog", "Remove", None))
        self.pb_view.setText(_translate("Dialog", "View", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

