from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")

        Dialog.resize(800, 400)
        Dialog.setMinimumSize(QtCore.QSize(800, 400))

        Dialog.setStyleSheet("background-color: rgb(61, 56, 70);")

        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 16777215, 16777215))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        # текст
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.label.setStyleSheet("font: 16pt \"Ubuntu\"; color: rgb(34, 217, 217);")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 0)

        # виджет отображения
        self.textEdit_1 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_1.setObjectName("textEdit")
        self.textEdit_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        #self.textEdit_1.setReadOnly(True)
        self.textEdit_1.setStyleSheet("background-color: rgb(94, 92, 100); font: 16pt \"Ubuntu\"; color:rgb(250, 250, 250);")
        self.gridLayout.addWidget(self.textEdit_1, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

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
    ui = Ui_Dialog2()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
'''