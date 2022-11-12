/*
 * Создать статическую и динамическую библиотеки,
 * содержащие следующие функции:  сортировка слиянием,
 * пирамидальная сортировка. Написать программу,
 * тестирующую функции из библиотеки.
 * 
 * Создать файл сборки для компиляции библиотечных файлов,
 * сборки  и запуска исполняемого файла, удаления объектных файлов.
 */

#include <time.h>

// Процедура для преобразования в двоичную кучу поддерева с корневым узлом i
void Heap(int *arr, int m, int i)
{
    int largest = i;
    int temp;
       
	// Инициализируем наибольший элемент как корень
    int l = 2*i + 1; // Левый = 2*i + 1
    int r = 2*i + 2; // Правый = 2*i + 2

	// Если левый дочерний элемент больше корня
    if (l < m && arr[l] > arr[largest])
        largest = l;

	// Если правый дочерний элемент больше, чем самый большой элемент на данный момент
    if (r < m && arr[r] > arr[largest])
        largest = r;

    // Если самый большой элемент не корень
    if (largest != i)
    {
		temp = arr[i];
		arr[i] = arr[largest];
		arr[largest] = temp;

		// Рекурсивно преобразуем в двоичную кучу затронутое поддерево
        Heap(arr, m, largest);
    }
}

// Основная функция, выполняющая пирамидальную сортировку
// B
void HeapSort(int *arr, int n, float &delay)
{
	int temp;
	
	clock_t begin = clock();
	// Построение кучи (перегруппируем массив)
    for (int i = n / 2 - 1; i >= 0; i--)
        Heap(arr, n, i);

	// Один за другим извлекаем элементы из кучи
    for (int i=n-1; i>=0; i--)
    {
        // Перемещаем текущий корень в конец
        temp = arr[0];
        arr[0] = arr[i];
        arr[i] = temp;

        // вызываем процедуру Heap на уменьшенной куче
        Heap(arr, i, 0);
    }
    
    clock_t end = clock();
    delay = (float)(end-begin)/CLOCKS_PER_SEC;
}

/*
int main()
{
	int n = 11, m = 8;
	int *A = new int[n];
	int *B = new int[m];
	
	cout << "A:" <<endl;
	for (int i = 1; i <= n; i++)
	{
		A[i] = (rand()%1000) - 500;
		cout << A[i] << " ";
	}
	
	cout << "\n\nB:" <<endl;
	for (int i = 1; i <= m; i++)
	{
		B[i]=(rand()%1000) - 500;
		cout << B[i] << " ";
	}
	
	MergeSort(A, 1, n);
	HeapSort(B, m+1);
	
	cout<<"\n\nУпорядоченный массив A: " << endl;
	for (int i = 1; i <= n; i++)
		cout << A[i] << " ";
		
	cout<<"\n\nУпорядоченный массив B: " << endl;
	for (int i = 1; i <= m; i++)
		cout << B[i] << " ";
}*/
