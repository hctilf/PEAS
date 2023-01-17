from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")

        Dialog.resize(400, 400)
        Dialog.setMinimumSize(QtCore.QSize(400, 400))

        Dialog.setStyleSheet("background-color: rgb(61, 56, 70);")

        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 380, 380))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.label.setStyleSheet("font: 16pt \"Ubuntu\"; color: rgb(34, 217, 217);")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.listWidget = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setStyleSheet("font: 16pt \"Ubuntu\"; color: rgb(34, 217, 217);")
        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 1)

        self.okButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.okButton.setObjectName("okButton")
        self.okButton.setStyleSheet("background-color: rgb(94, 92, 100); font: 16pt \"Ubuntu\"; color: rgb(250, 250, 250);")
        self.gridLayout.addWidget(self.okButton, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        #QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Results"))
        self.label.setText(_translate("Dialog", "Choose test\'s name to show results"))
        self.okButton.setText(_translate("Dialog", "Ok"))


'''
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
'''