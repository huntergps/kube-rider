# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/configuration_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Configuration(object):
    def setupUi(self, Configuration):
        Configuration.setObjectName("Configuration")
        Configuration.setWindowModality(QtCore.Qt.WindowModal)
        Configuration.resize(486, 255)
        Configuration.setModal(True)
        self.tabWidget = QtWidgets.QTabWidget(Configuration)
        self.tabWidget.setGeometry(QtCore.QRect(12, 6, 461, 201))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.txt_kubectl = QtWidgets.QLineEdit(self.tab)
        self.txt_kubectl.setGeometry(QtCore.QRect(10, 10, 441, 21))
        self.txt_kubectl.setObjectName("txt_kubectl")
        self.tabWidget.addTab(self.tab, "")
        self.update = QtWidgets.QWidget()
        self.update.setObjectName("update")
        self.chk_updates_startup = QtWidgets.QCheckBox(self.update)
        self.chk_updates_startup.setEnabled(False)
        self.chk_updates_startup.setGeometry(QtCore.QRect(20, 20, 221, 20))
        self.chk_updates_startup.setCheckable(True)
        self.chk_updates_startup.setChecked(False)
        self.chk_updates_startup.setObjectName("chk_updates_startup")
        self.tabWidget.addTab(self.update, "")
        self.btn_save_configuration = QtWidgets.QPushButton(Configuration)
        self.btn_save_configuration.setGeometry(QtCore.QRect(360, 210, 113, 32))
        self.btn_save_configuration.setObjectName("btn_save_configuration")
        self.btn_cancel_configuration = QtWidgets.QPushButton(Configuration)
        self.btn_cancel_configuration.setGeometry(QtCore.QRect(250, 210, 113, 32))
        self.btn_cancel_configuration.setObjectName("btn_cancel_configuration")

        self.retranslateUi(Configuration)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Configuration)

    def retranslateUi(self, Configuration):
        _translate = QtCore.QCoreApplication.translate
        Configuration.setWindowTitle(_translate("Configuration", "Settings"))
        self.txt_kubectl.setText(_translate("Configuration", "kubectl"))
        self.txt_kubectl.setPlaceholderText(_translate("Configuration", "path to kubectl ..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Configuration", "Settings"))
        self.chk_updates_startup.setText(_translate("Configuration", "Check for updates on start up"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.update), _translate("Configuration", "Updates"))
        self.btn_save_configuration.setText(_translate("Configuration", "OK"))
        self.btn_cancel_configuration.setText(_translate("Configuration", "Cancel"))


