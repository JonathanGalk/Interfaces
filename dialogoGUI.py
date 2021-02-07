# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogImg.ui',
# licensing of 'dialogImg.ui' applies.
#
# Created: Wed Nov  6 18:51:30 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.resize(273, 171)
        Form.setMinimumSize(QtCore.QSize(273, 171))
        Form.setMaximumSize(QtCore.QSize(273, 171))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons/image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.altura = QtWidgets.QSpinBox(Form)
        self.altura.setMinimum(16)
        self.altura.setMaximum(999999999)
        self.altura.setObjectName("altura")
        self.gridLayout.addWidget(self.altura, 3, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.largura = QtWidgets.QSpinBox(Form)
        self.largura.setMinimum(16)
        self.largura.setMaximum(999999999)
        self.largura.setObjectName("largura")
        self.gridLayout.addWidget(self.largura, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        self.btnOpen = QtWidgets.QPushButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icons/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOpen.setIcon(icon1)
        self.btnOpen.setObjectName("btnOpen")
        self.gridLayout.addWidget(self.btnOpen, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked(bool)"), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Abrir Imagem", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("Form", "Cancelar", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Largura:</span></p></body></html>", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Px</span></p></body></html>", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Form", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Px</span></p></body></html>", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Form", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Altura:</span></p></body></html>", None, -1))
        self.btnOpen.setText(QtWidgets.QApplication.translate("Form", "Abrir", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "OK", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Imagem:</span></p></body></html>", None, -1))

import recursos_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

