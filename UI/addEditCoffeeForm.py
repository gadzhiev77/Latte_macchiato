# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogAddDevice(object):
    def setupUi(self, DialogAddDevice):
        DialogAddDevice.setObjectName("DialogAddDevice")
        DialogAddDevice.resize(380, 197)
        self.gridLayout = QtWidgets.QGridLayout(DialogAddDevice)
        self.gridLayout.setObjectName("gridLayout")
        self.labelName = QtWidgets.QLabel(DialogAddDevice)
        self.labelName.setObjectName("labelName")
        self.gridLayout.addWidget(self.labelName, 0, 0, 1, 1)
        self.NameLineEdit = QtWidgets.QLineEdit(DialogAddDevice)
        self.NameLineEdit.setObjectName("NameLineEdit")
        self.gridLayout.addWidget(self.NameLineEdit, 0, 1, 1, 2)
        self.labelRoasting = QtWidgets.QLabel(DialogAddDevice)
        self.labelRoasting.setObjectName("labelRoasting")
        self.gridLayout.addWidget(self.labelRoasting, 1, 0, 1, 1)
        self.RoastingLineEdit = QtWidgets.QLineEdit(DialogAddDevice)
        self.RoastingLineEdit.setObjectName("RoastingLineEdit")
        self.gridLayout.addWidget(self.RoastingLineEdit, 1, 1, 1, 2)
        self.labelType = QtWidgets.QLabel(DialogAddDevice)
        self.labelType.setObjectName("labelType")
        self.gridLayout.addWidget(self.labelType, 2, 0, 1, 1)
        self.TypeLineEdit = QtWidgets.QLineEdit(DialogAddDevice)
        self.TypeLineEdit.setObjectName("TypeLineEdit")
        self.gridLayout.addWidget(self.TypeLineEdit, 2, 1, 1, 2)
        self.labelTaste = QtWidgets.QLabel(DialogAddDevice)
        self.labelTaste.setObjectName("labelTaste")
        self.gridLayout.addWidget(self.labelTaste, 3, 0, 1, 1)
        self.TasteLineEdit = QtWidgets.QLineEdit(DialogAddDevice)
        self.TasteLineEdit.setObjectName("TasteLineEdit")
        self.gridLayout.addWidget(self.TasteLineEdit, 3, 1, 1, 2)
        self.labelPrice = QtWidgets.QLabel(DialogAddDevice)
        self.labelPrice.setObjectName("labelPrice")
        self.gridLayout.addWidget(self.labelPrice, 4, 0, 1, 1)
        self.PriceLineEdit = QtWidgets.QLineEdit(DialogAddDevice)
        self.PriceLineEdit.setObjectName("PriceLineEdit")
        self.gridLayout.addWidget(self.PriceLineEdit, 4, 1, 1, 2)
        self.labelSize = QtWidgets.QLabel(DialogAddDevice)
        self.labelSize.setObjectName("labelSize")
        self.gridLayout.addWidget(self.labelSize, 5, 0, 1, 1)
        self.SizeLineEdit = QtWidgets.QLineEdit(DialogAddDevice)
        self.SizeLineEdit.setObjectName("SizeLineEdit")
        self.gridLayout.addWidget(self.SizeLineEdit, 5, 1, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogAddDevice)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 6, 0, 1, 3)

        self.retranslateUi(DialogAddDevice)
        self.buttonBox.accepted.connect(DialogAddDevice.accept) # type: ignore
        self.buttonBox.rejected.connect(DialogAddDevice.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DialogAddDevice)

    def retranslateUi(self, DialogAddDevice):
        _translate = QtCore.QCoreApplication.translate
        DialogAddDevice.setWindowTitle(_translate("DialogAddDevice", "Dialog"))
        self.labelName.setText(_translate("DialogAddDevice", "Name"))
        self.labelRoasting.setText(_translate("DialogAddDevice", "Roasting"))
        self.labelType.setText(_translate("DialogAddDevice", "Type"))
        self.labelTaste.setText(_translate("DialogAddDevice", "Taste"))
        self.labelPrice.setText(_translate("DialogAddDevice", "Price"))
        self.labelSize.setText(_translate("DialogAddDevice", "Size"))
