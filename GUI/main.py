import sys

from PyQt5.QtWidgets import *
from mainWindow import *
from optimizationWindow import *
from resultsWindow import *

class mainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        # вызываем функцию get_library_dir по нажатию кнопки libButton
        self.libButton.clicked.connect(self.get_library_dir)

        # вызываем функцию get_h_dir по нажатию кнопки hButton
        self.hButton.clicked.connect(self.get_h_dir)

        # вызываем функцию optimization по нажатию кнопки testButton
        self.testButton.clicked.connect(self.optimization)
    
    def get_library_dir(self):
        # открытие проводника для выбора каталога файлов библиотеки
        library_dir = QFileDialog.getExistingDirectory(self,)
        self.textEdit_1.append(library_dir)

    def get_h_dir(self):
        # открытие проводника для выбора каталога .h файлов
        h_dir = QFileDialog.getExistingDirectory(self)
        self.textEdit_2.append(h_dir)

    def optimization(self):
        window2 = OptimizationWindow()
        window2.exec_()

    def results(self):
        window3 = ResultsWindow()
        window3.exec_()

class OptimizationWindow(QDialog, Ui_Dialog1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        pass

class ResultsWindow(QDialog, Ui_Dialog2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        pass



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window1 = mainWindow()
    window1.show()

    sys.exit(app.exec_())