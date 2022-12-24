import sys, os, subprocess, psutil

from generator import *
from executor import *

from PyQt5.QtWidgets import *
from mainWindow import *
from optimizationWindow import *
from resultsWindow import *
from graphics import *
from parse_json import jsonAnalyzer


curDir = f'/home/{os.getlogin()}/PEAS/src'
nanobench = parDir = f'/home/{os.getlogin()}/PEAS'
tmpDir = f'{parDir}/tmp'

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
        self.lastTestButton.clicked.connect(self.show_last_test)
    
    # функция выбора и добавления директории до библиотеки
    def get_library_dir(self):

        library_dir = QFileDialog.getOpenFileName(self)[0]
        self.textEdit_1.append("Saved.")

        # сохранение пути до библиотеки в текстовый файл
        library_file = open(f'{parDir}/LibraryPath.txt', "w+")
        library_file.write(library_dir)
        library_file.close()
        self.clear_h_dir()


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

    def results_window(self, item_list):
        window3 = ResultsWindow()
        window3.initUI(item_list)
        window3.exec_()

    # Функция вывода результатов последнего теста
    def show_last_test(self):
        try:
            self.results_window(need_to_clear)
        except NameError:
            print("Results not found!")

    def clear_tmp(self, need_to_clear):
        for tmp in need_to_clear:
            try: os.remove(f'{parDir}/{tmp}.cpp')
            except FileNotFoundError:
                print('generated .cpp removed')
            try: 
                for tmpSub in os.listdir(tmpDir):
                    #print(f'{tmpDir}/{tmpSub}')
                    for fileName in os.listdir(f'{tmpDir}/{tmpSub}'):
                        if not fileName.endswith('json'):
                            #print('need to remove', fileName)
                            os.remove(f'{tmpDir}/{tmpSub}/{fileName}')
            except FileNotFoundError:
                print('generated binaries removed')

    # функция сборки и вывода окна с результатами
    def results(self):
        #boosting performance
        subprocess.run(['sudo', 'bash', f'.{parDir}/cpu_max.sh', 'max', 'performance'])
        # чтение пути до h файлов для generator и builder
        h_file = open(f'{parDir}/hPath.txt', "r")
        h_common_way = h_file.read()
        h_way = h_common_way[0:h_common_way.rfind("/") + 1]
        h_file.close()
        # python3 generator.py /home/vadim/PEAS/src/
        mem_req = generator(parDir, h_way, h_common_way[h_common_way.rfind("/")+1: len(h_common_way)-1])

        # Чтение пути до библиотеки для builder
        library_file = open(f'{parDir}/LibraryPath.txt', "r")
        lib_way = library_file.read()
        library_file.close()
        #python3 builder.py /home/vadim/PEAS/src/lsm.py /home/vadim/PEAS/src/
        
        #subprocess.run(['python3', f'{curDir}/builder_threads.py', lib_way, h_way, nanobench])
        global cpu_util
        cpu_util = execute(mem_req)
        
        global need_to_clear
        need_to_clear = [tmp[0] for tmp in mem_req]
        need_to_clear.sort()
        
        #self.clear_tmp(need_to_clear)
        
        window3 = ResultsWindow()
        window3.initUI(need_to_clear)
        window3.exec_()
        
'''
class OptimizationWindow(QDialog, Ui_Dialog1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        pass
'''

class ResultsWindow(QDialog, Ui_Dialog2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def initUI(self, item_list):
        for i in item_list:
            self.listWidget.addItem(i)
        self.okButton.clicked.connect(self.build_graph)

    # Функция построения графиков
    def build_graph(self):
        data = jsonAnalyzer()
        # Словарь данных
        data_dict = data.get_res()

        # Список всех названий тестов
        all_test_names = list(data_dict.keys())
        all_test_names.sort()

        # Списки значений для построения графиков
        all_test_ops = []
        all_test_ipc = []
        all_test_time = []
        all_test_cpuUtil = []

        for id, i in enumerate(all_test_names):
            all_test_ops.append(round(data_dict[i]['op/s'], 2)) # 'op/s'
            all_test_ipc.append(round(data_dict[i]['IPC'], 2))
            all_test_time.append(data_dict[i]['median(elapsed)'])
            all_test_cpuUtil.append(cpu_util[i]*all_test_time[id])
        
        list_graph = []
        for i in range(int(len(all_test_names)/5)):
            list_graph.append(Graph(all_test_names[5*i:5*i+5], 
        all_test_ops[5*i:5*i+5], all_test_ipc[5*i:5*i+5], 
        all_test_time[5*i:5*i+5], all_test_cpuUtil[5*i:5*i+5]))
        
        # Построение графиков
        list_graph[self.listWidget.currentRow()].create_graph() # Убрать + 1, если не совпадают

        self.hide()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    # создание текстового файла для h директорий
    h_file = open(f'{parDir}hPath.txt', "w+")
    h_file.close()

    window1 = mainWindow()
    window1.show()

    sys.exit(app.exec_())