from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog1(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")

        Dialog.resize(600, 300)
        Dialog.setMinimumSize(QtCore.QSize(600, 300))

        Dialog.setStyleSheet("background-color: rgb(61, 56, 70);")

        #Dialog.setSizeGripEnabled(True)
        #Dialog.setModal(True)

        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # текст Выберите способ оптимизации
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setStyleSheet("font: 16pt \"Ubuntu\"; color: rgb(34, 217, 217);")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 0)
        
        # ЧЕК-БОКСЫ
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setCheckable(True)
        self.checkBox.setStyleSheet("color: rgb(37, 217, 217); font: 16pt \"Ubuntu\";")
        self.gridLayout.addWidget(self.checkBox, 1, 0, 1, 1)

        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.setCheckable(True)
        self.checkBox_2.setStyleSheet("color: rgb(37, 217, 217); font: 16pt \"Ubuntu\";")
        self.gridLayout.addWidget(self.checkBox_2, 2, 0, 1, 1)
        
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_3.setCheckable(True)
        self.checkBox_3.setStyleSheet("color: rgb(37, 217, 217); font: 16pt \"Ubuntu\";")
        self.gridLayout.addWidget(self.checkBox_3, 3, 0, 1, 1)

        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_4.setCheckable(True)
        self.checkBox_4.setStyleSheet("color: rgb(37, 217, 217); font: 16pt \"Ubuntu\";")
        self.gridLayout.addWidget(self.checkBox_4, 4, 0, 1, 1)
        
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_5.setCheckable(True)
        self.checkBox_5.setStyleSheet("color: rgb(37, 217, 217); font: 16pt \"Ubuntu\";")
        self.gridLayout.addWidget(self.checkBox_5, 5, 0, 1, 1)

        '''
        # кнопка ok
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setObjectName("okButton")
        self.okButton.setStyleSheet("background-color: rgb(94, 92, 100); font: 16pt \"Ubuntu\"; color: rgb(250, 250, 250);")
        self.gridLayout.addWidget(self.okButton, 6, 2, 1, 1)
        '''

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Optimization"))
        
        self.label.setText(_translate("Dialog", "Select optimization method"))
        
        self.checkBox.setText(_translate("Dialog", "Optimization 1"))
        self.checkBox_2.setText(_translate("Dialog", "Optimization 2"))
        self.checkBox_3.setText(_translate("Dialog", "Optimization 3"))
        self.checkBox_4.setText(_translate("Dialog", "Optimization 4"))
        self.checkBox_5.setText(_translate("Dialog", "Optimization 5"))
        #self.okButton.setText(_translate("MainWindow", "Ok"))

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