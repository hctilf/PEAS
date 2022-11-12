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

/*
#include <iostream>
using namespace std;*/

// Объединяем два отсортированных подмассива `arr[low…mid]` и `arr[mid+1…high]`
void Merge(int arr[], int aux[], int low, int mid, int high)
{
    int k = low, i = low, j = mid + 1;
 
    // Пока есть элементы в левом и правом прогонах
    while (i <= mid && j <= high)
    {
        if (arr[i] <= arr[j]) {
            aux[k++] = arr[i++];
        }
        else {
            aux[k++] = arr[j++];
        }
    }
 
    // Копируем оставшиеся элементы
    while (i <= mid) {
        aux[k++] = arr[i++];
    }
 
    // Вторую половину копировать не нужно (поскольку остальные элементы
    // уже находятся на своем правильном месте во вспомогательном массиве)
 
    // копируем обратно в исходный массив, чтобы отразить порядок сортировки
    for (int i = low; i <= high; i++) {
        arr[i] = aux[i];
    }
}

// Сортируем массив `arr[low…high]`, используя вспомогательный массив `aux`
void mergesort(int arr[], int aux[], int low, int high, float &delay)
{
	clock_t begin = clock();
    // Базовый вариант
    if (high == low) {        // если размер прогона == 1
        return;
    }
 
    // найти середину
    int mid = (low + ((high - low) >> 1));
 
    // рекурсивное разделение выполняется на две половины до тех пор, пока размер выполнения не станет == 1,
    // затем объединяем их и возвращаемся вверх по цепочке вызовов
 
    mergesort(arr, aux, low, mid, delay);          // разделить/объединить левую половину
    mergesort(arr, aux, mid + 1, high, delay);     // разделить/объединить правую половину
 
    Merge(arr, aux, low, mid, high);        // объединить два полупрогона.

	clock_t end = clock();
	delay = (float)(end-begin)/CLOCKS_PER_SEC;
}

/*
// Функция, сливающая массивы
void Merge(int *A, int first, int last)
{
	int middle, start, end, j;
	int *mas = new int [last];
	
	middle = (first + last) / 2; // Вычисление среднего элемента
	start = first; // Начало левой части
	end = middle + 1; // Начало правой части

	for(j = first; j <= last; j++)
		if ((start <= middle) && ((end > last) || (A[start] < A[end])))
		{
			mas[j] = A[start];
			start++;
		}
		else
		{
			mas[j] = A[end];
			end++;
		}
	// Возвращение результата в список
	for (j = first; j <= last; j++) A[j] = mas[j];
	delete[]mas;
};

// Рекурсивная процедура сортировки слиянием
// A
void MergeSort(int *A, int first, int last, float &delay)
{
	if (first < last)
	{
		clock_t begin = clock();
		
		MergeSort(A, first, (first+last) / 2, delay); //сортировка левой части
		MergeSort(A, (first+last)/2 + 1, last, delay); //сортировка правой части
		Merge(A, first, last); //слияние двух частей
		
		clock_t end = clock();
		delay = (float)(end-begin)/CLOCKS_PER_SEC;
	}
};*/

/*
int main()
{
	int n = 10;
	int *A = new int[n];
	int *aux = new int [n];
	float delay;
	
	//генерируем случайный ввод целых чисел
    for (int i = 0; i < n; i++)
    {
        aux[i] = A[i] = (rand() % 100000) - 50000;
    }
	
	mergesort(A, aux, 0, n - 1, delay);
	
	cout<<"Sorted A"<<endl;
	for (int i = 0; i < n; i++)
	{
		cout << A[i] << " ";
    }
    cout << "\nTime: " << delay;
}*/
