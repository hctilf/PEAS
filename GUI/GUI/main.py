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
        library_dir = QFileDialog.getExistingDirectory(self)
        self.textEdit_1.append(library_dir)

    def get_h_dir(self):
        # открытие проводника для выбора каталога .h файлов
        h_dir = QFileDialog.getOpenFileName(self)[0]
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

    # словарь с директориями h файлов
    dir = {}

    # функция добавления в словарь
    def add_h_dir(self):
        # в way хранится значение поля textEdit_2
        way = window1.textEdit_2.toPlainText()

        # отделяем название h файла от директории
        i = way.rindex("/", 0, len(way))
        dirName = way[0 : i]           # название директории
        hName = way[i + 1 : len(way)]  # название h файла

        # заносим в словарь имя h файла и директории
        dir[hName] = dirName
        print("Added!", dir)

        # очищаем поле textEdit_2
        window1.textEdit_2.setPlainText("")

    # функция очищения словаря
    def clear_h_dir(self):
        dir.clear()
        print("Cleared!", dir)
        window1.textEdit_2.setPlainText("")
    
    # вызываем функцию add_h_dir по нажатию кнопки addDirButton
    window1.addDirButton.clicked.connect(add_h_dir)

    # вызываем функцию clear_h_dir по нажатию кнопки clearButton
    window1.clearButton.clicked.connect(clear_h_dir)

    sys.exit(app.exec_())