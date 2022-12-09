import matplotlib.pyplot as plt

class Graph():
    def __init__(self, testNames, values, yDescription, title):
        self.testNames = testNames # Список тестов
        self.values = values # Список значений
        self.yDescription = yDescription # Описание ординаты
        self.title = title # Название графа

    def create_graph(self):
        fig, ax = plt.subplots()

        ax.bar(self.testNames, self.values, color = 'tab:blue')
        ax.set_ylabel(self.yDescription)
        ax.set_title(self.title)

        plt.show()


if __name__ == '__main__':
    title1 = 'Graph (operations per second)'
    title2 = 'Graph (instruction per cycle)'
    title3 = 'Main Graph (elapsed time)'

    yDescription1 = 'op/s'
    yDescription2 = 'i/c'
    yDescription3 = 'sec'

    testNames = ['TestXO0', 'TestXO1', 'TestXO2', 'TestXO3', 'TestXOfast']
    
    values1 = [100, 200, 300, 500, 600]
    values2 = [100, 200, 300, 500, 600]
    values3 = [600, 500, 400, 200, 80]

    Graph1 = Graph(testNames, values1, yDescription1, title1)
    Graph2 = Graph(testNames, values2, yDescription2, title2)
    Graph3 = Graph(testNames, values3, yDescription3, title3)

    Graph1.create_graph()
    Graph2.create_graph()
    Graph3.create_graph()
