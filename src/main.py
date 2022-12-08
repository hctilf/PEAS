import sys, os, subprocess, psutil

from generator import *
from executor import *

from PyQt5.QtWidgets import *
from mainWindow import *
from optimizationWindow import *
from resultsWindow import *


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

        # сохранение пути до библиотеки в текстовый файл
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
        # сохранение пути до h файлов в LibraryPath.txt        
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
        # чтение пути до h файлов для generator и builder
        
        h_file = open(f'{parDir}/hPath.txt', "r")
        h_common_way = h_file.read()
        h_way = h_common_way[0:h_common_way.rfind("/") + 1]
        h_file.close()
        # python3 generator.py /home/vadim/PEAS/src/
        mem_req = generator(parDir, h_way)

        # Чтение пути до библиотеки для builder
        library_file = open(f'{parDir}/LibraryPath.txt', "r")
        lib_way = library_file.read()
        library_file.close()
        # python3 builder.py /home/vadim/PEAS/src/lsm.py /home/vadim/PEAS/src/
        subprocess.run(['python3', f'{curDir}/builder_threads.py', lib_way, h_way, nanobench])

        #execute(mem_req)
        #subprocess.run(['python3', 'executor.py'])

        # Вывод окна с результатами
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