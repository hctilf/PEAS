from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        MainWindow.resize(800, 400)
        MainWindow.setMinimumSize(QtCore.QSize(800, 400))

        MainWindow.setStyleSheet("background-color: rgb(61, 56, 70);")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # текст1
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setObjectName("label_1")
        self.label_1.setStyleSheet("font: 16pt \"Ubuntu\"; color: rgb(34, 217, 217);")
        self.label_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)

        # текст2
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("font: 16pt \"Ubuntu\"; color: rgb(34, 217, 217);")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        # виджет отображения каталога 1
        self.textEdit_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_1.setObjectName("textEdit_1")
        self.textEdit_1.setReadOnly(True)
        self.textEdit_1.setMaximumSize(QtCore.QSize(16777215, 40))
        self.textEdit_1.setStyleSheet("background-color: rgb(94, 92, 100); font: 16pt \"Ubuntu\"; color:rgb(250, 250, 250);")
        self.gridLayout.addWidget(self.textEdit_1, 1, 0, 1, 2)

        # виджет отображения каталога 2
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.textEdit_2.setStyleSheet("background-color: rgb(94, 92, 100); font: 16pt \"Ubuntu\"; color:rgb(250, 250, 250);")
        self.gridLayout.addWidget(self.textEdit_2, 7, 0, 1, 2)

        # кнопка открыть путь до библиотеки
        self.libButton = QtWidgets.QPushButton(self.centralwidget)
        self.libButton.setObjectName("libButton")
        self.libButton.setStyleSheet("background-color: rgb(94, 92, 100); font: 16pt \"Ubuntu\"; color: rgb(250, 250, 250);")
        self.gridLayout.addWidget(self.libButton, 0, 1, 1, 1)

        # кнопка открыть путь до .h файлов
        self.hButton = QtWidgets.QPushButton(self.centralwidget)
        self.hButton.setObjectName("hButton")
        self.hButton.setStyleSheet("background-color: rgb(94, 92, 100); font: 16pt \"Ubuntu\"; color: rgb(250, 250, 250);")
        self.gridLayout.addWidget(self.hButton, 4, 1, 1, 1)

        # кнопка добавить каталог
        self.addDirButton = QtWidgets.QPushButton(self.centralwidget)
        self.addDirButton.setObjectName("addDirButton")
        self.addDirButton.setStyleSheet("background-color: rgb(94, 92, 100); font: 16pt \"Ubuntu\"; color: rgb(250, 250, 250);")
        self.gridLayout.addWidget(self.addDirButton, 8, 1, 1, 1)

        # кнопка очистить последний добавленный каталог
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setObjectName("clearButton")
        self.clearButton.setStyleSheet("background-color: rgb(94, 92, 100); font: 16pt \"Ubuntu\"; color: rgb(250, 250, 250);")
        self.gridLayout.addWidget(self.clearButton, 9, 1, 1, 1)

        # кнопка посмотреть результаты последнего теста
        self.lastTestButton = QtWidgets.QPushButton(self.centralwidget)
        self.lastTestButton.setObjectName("lastTestButton")
        self.lastTestButton.setStyleSheet("background-color: rgb(94, 92, 100); font: 16pt \"Ubuntu\"; color: rgb(250, 250, 250);")
        self.gridLayout.addWidget(self.lastTestButton, 10, 0, 1, 1)

        # кнопка тест
        self.testButton = QtWidgets.QPushButton(self.centralwidget)
        self.testButton.setObjectName("testButton")
        self.testButton.setStyleSheet("background-color: rgb(94, 92, 100); font: 16pt \"Ubuntu\"; color: rgb(250, 250, 250);")
        self.gridLayout.addWidget(self.testButton, 10, 1, 1, 1)

        # check-box библиотека собрана
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(False)
        self.checkBox.setAutoRepeat(False)
        self.checkBox.setStyleSheet("color: rgb(37, 217, 217); font: 16pt \"Ubuntu\";")
        self.gridLayout.addWidget(self.checkBox, 8, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ProgramEfficiency"))

        self.label_1.setText(_translate("MainWindow", "Select .cpp library file"))
        self.label_2.setText(_translate("MainWindow", "Select .h file"))

        self.libButton.setText(_translate("MainWindow", "Browse"))
        self.hButton.setText(_translate("MainWindow", "Browse"))
        self.testButton.setText(_translate("MainWindow", "Test!"))
        self.addDirButton.setText(_translate("MainWindow", "Add head file"))
        self.clearButton.setText(_translate("MainWindow", "Clear head paths"))
        self.lastTestButton.setText(_translate("MainWindow", "Show last test results"))
        
        self.checkBox.setText(_translate("MainWindow", "Library builded"))

'''
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
'''