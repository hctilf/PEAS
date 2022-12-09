import sys, os, subprocess, psutil

from generator import *
from executor import *

from PyQt5.QtWidgets import *
from mainWindow import *
from optimizationWindow import *
from resultsWindow import *
from graphics import *


curDir = f'/home/{os.getlogin()}/PEAS/src'
nanobench = parDir = f'/home/{os.getlogin()}/PEAS'

class mainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.libButton.clicked.connect(self.get_library_dir)
        self.hButton.clicked.connect(self.get_h_dir)
        self.testButton.clicked.connect(self.results)
        self.addDirButton.clicked.connect(self.add_h_dir)
        self.clearButton.clicked.connect(self.clear_h_dir)
    
    # функция выбора и добавления директории до библиотеки
    def get_library_dir(self):
        library_dir = QFileDialog.getOpenFileName(self)[0]
        self.textEdit_1.append("Directory saved.")
        library_file = open(f'{parDir}/LibraryPath.txt', "w+")
        library_file.write(library_dir)
        library_file.close()

    # функция выбора директории до h файлов
    def get_h_dir(self):
        h_dir = QFileDialog.getOpenFileName(self)[0]
        self.textEdit_2.append(h_dir)

    # функция добавления директории до h файла (их может быть несколько)
    def add_h_dir(self):
        way = self.textEdit_2.toPlainText()
        self.textEdit_2.setPlainText("")    
        h_file = open(f'{parDir}/hPath.txt', "a")
        h_file.write(way + "\n")
        h_file.close()

    # функция очистки документа с директориями h файлов
    def clear_h_dir(self):
        self.textEdit_2.setPlainText("")
        h_file = open(f'{parDir}/hPath.txt', "w+")
        h_file.close()

    # функция вызова окна оптимизации
    def optimization(self):
        window2 = OptimizationWindow()
        window2.exec_()

    # функция сборки и вывода окна с результатами
    def results(self):
        h_file = open(f'{parDir}/hPath.txt', "r")
        h_common_way = h_file.read()
        h_way = h_common_way[0:h_common_way.rfind("/") + 1]
        h_file.close()
        mem_req = generator(h_way)

        library_file = open(f'{parDir}/LibraryPath.txt', "r")
        lib_way = library_file.read()
        library_file.close()
 
        subprocess.run(['python3', f'{curDir}/builder_threads.py', lib_way, h_way, nanobench])
        execute(mem_req)

        # Вывод окна с результатами
        testsquare_name = ['testsquareO0', 'testsquareO1', 'testsquareO2', 'testsquareO3', 'testsquareOfast']
        testsquare_value1 = [100, 200, 300, 400, 500]
        testsquare_value2 = [100, 200, 300, 400, 500]
        testsquare_value3 = [100, 200, 300, 400, 500]
        testsquare1 = Graph(testsquare_name, testsquare_value1, testsquare_value2, testsquare_value3)
        testsquare1.create_graph()

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

    h_file = open("hPath.txt", "w+")
    h_file.close()

    window1 = mainWindow()
    window1.show()

    sys.exit(app.exec_())