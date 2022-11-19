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
        self.libButton.clicked.connect(self.get_library_dir)
        self.hButton.clicked.connect(self.get_h_dir)
        self.testButton.clicked.connect(self.optimization)
        self.addDirButton.clicked.connect(self.add_h_dir)
        self.clearButton.clicked.connect(self.clear_h_dir)
    
    def get_library_dir(self):
        # открытие проводника для выбора каталога файлов библиотеки
        library_dir = QFileDialog.getExistingDirectory(self)
        self.textEdit_1.append("Directory saved.")

        # сохранение пути до библиотеки в текстовый файл
        library_file = open("LibraryPath.txt", "w+")
        library_file.write(library_dir)
        library_file.close()

    def get_h_dir(self):
        # открытие проводника для выбора каталога .h файлов
        h_dir = QFileDialog.getOpenFileName(self)[0]
        self.textEdit_2.append(h_dir)

    def add_h_dir(self):
        # в way хранится значение поля textEdit_2
        way = self.textEdit_2.toPlainText()
        self.textEdit_2.setPlainText("")

        # сохранение пути до библиотеки в LibraryPath.txt
        h_file = open("hPath.txt", "a")
        h_file.write(way + "\n")
        h_file.close()

    def clear_h_dir(self):
        self.textEdit_2.setPlainText("")

        # очиcтка текстового документа 
        h_file = open("hPath.txt", "w+")
        h_file.close()

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

    # создание текстового файла для h директорий
    h_file = open("hPath.txt", "w+")
    h_file.close()

    window1 = mainWindow()
    window1.show()

    sys.exit(app.exec_())