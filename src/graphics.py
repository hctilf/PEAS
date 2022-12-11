import os
import matplotlib.pyplot as plt

plt.rc('font', size = 14) # размер шрифта
class Graph():
    def __init__(self, testNames, values1, values2, values3):
        self.testNames = testNames # Список тестов
        self.values1 = values1 # Список значений operations per second
        self.values2 = values2 # Список значений instructions per cycle
        self.values3 = values3 # Список значений main graph
        self.height = 5 # Высота окна
        self.width = 12 # Ширина окна

    # Построение графа operations per second
    def create_graph_ops(self):
        fig, ax = plt.subplots()
        fig.set_size_inches(self.width, self.height)

        ax.bar(self.testNames, self.values2, color = 'tab:blue')
        plt.xlabel('Test name')
        plt.ylabel('op/s')
        ax.set_title('Graph (operations per second)')

        plt.show()

    # Построение графа instructions per cycle
    def create_graph_ips(self):
        fig, ax = plt.subplots()
        fig.set_size_inches(self.width, self.height)

        ax.bar(self.testNames, self.values2, color = 'tab:blue')
        plt.xlabel('Test name')
        plt.ylabel('in/c')
        ax.set_title('Graph (instruction per cycle)')

        plt.show()

    # Построение графа main graph
    def create_graph_main(self):
        fig, ax = plt.subplots()
        fig.set_size_inches(self.width, self.height)

        ax.bar(self.testNames, self.values3, color = 'tab:blue')
        plt.xlabel('Test name')
        plt.ylabel('sec')
        ax.set_title('Main Graph (elapsed time)')

        plt.show()

    # Вызов всех функций построения графов
    def create_graph(self):
        self.create_graph_ops()
        self.create_graph_ips()
        self.create_graph_main()

'''
if __name__ == '__main__':
    testNames = ['testsquare' + 'O0', 'testsquare' + 'O1', 'testsquare' + 'O2', 'testsquare' + 'O3', 'testsquare' + 'Ofast']
    
    values1 = [100, 200, 300, 500, 600]
    values2 = [100, 200, 300, 500, 600]
    values3 = [600, 500, 400, 200, 80]

    Graph1 = Graph(testNames, values1)
    Graph2 = Graph(testNames, values2)
    Graph3 = Graph(testNames, values3)

    Graph1.create_graph()
    Graph2.create_graph()
    Graph3.create_graph()
'''