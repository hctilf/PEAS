/*
 * Создать статическую и динамическую библиотеки,
 * содержащие следующие функции:  сортировка слиянием,
 * пирамидальная сортировка. Написать программу,
 * тестирующую функции из библиотеки.
 * 
 * Создать файл сборки для компиляции библиотечных файлов,
 * сборки  и запуска исполняемого файла, удаления объектных файлов.
 */

#include <iostream>
#include <cstdlib>
#include "merge.h"
#include "heap.h"
#include <time.h>

using namespace std;

int compare(const void *x1, const void *x2)
{
	return (*(int*)x1 - *(int*)x2);
}

int main(int argc, char **argv)
{
	int n = 1000000;
	int *A = new int[n];
	int *aux1 = new int [n];
	int *aux2 = new int[n];
	int *aux3 = new int[n];
	float delay = 0;
	
	//Генерация массива А
	//std::cout << "Исходный массив A:" << std::endl;
	for (int i = 0; i < n; i++)
	{
		aux1[i] = aux2[i] = aux3[i] = A[i] = (rand()%100000) - 50000;
		//std::cout << A[i] << " ";
	}
	
	mergesort(aux1, A, 0, n - 1, delay);
	/*std::cout << "\n\nУпорядоченный массив(слияние): " << std::endl;
	for (int i = 0; i < n; i++)
		std::cout << aux1[i] << " ";*/
	std::cout << "\n Time merge sort: " << delay << std::endl;
		
	HeapSort(aux2, n + 1, delay);
	/*std::cout << "\n\nУпорядоченный массив (пирамидальная): " << std::endl;
	for (int i = 0; i < n; i++)
		std::cout << aux2[i] << " ";*/
	std::cout << "\n Time heap sort: " << delay << std::endl;
	
	clock_t begin = clock();
	qsort(aux3, n, sizeof(int), compare);
	clock_t end = clock();
    delay = (float)(end-begin)/CLOCKS_PER_SEC;
    
    /*std::cout << "\n\nУпорядоченный массив (qsort): " << std::endl;
	for (int i = 0; i < n; i++)
		std::cout << aux3[i] << " ";*/
    
	std::cout << "\n Time qsort: " << delay << std::endl;
	
	return 0;
}
