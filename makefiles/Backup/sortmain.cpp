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
#include "merge.h"
#include "heap.h"
#include <time.h>

using namespace std;

int main(int argc, char **argv)
{
	int n = 100000, m = 100000;
	int *A = new int[n];
	int *aux = new int [n];
	int *B = new int[m];
	float delay = 0;
	
	//Генерация массива А
	std::cout << "A:" << std::endl;
	for (int i = 0; i < n; i++)
	{
		aux[i] = A[i] = (rand()%100000) - 50000;
		//std::cout << A[i] << " ";
	}
	
	mergesort(A, aux, 0, n - 1, delay);
	/*std::cout << "\n\nУпорядоченный массив A (слияние): " << std::endl;
	for (int i = 0; i < n; i++)
		std::cout << A[i] << " ";*/
	std::cout << "\n Time merge sort: " << delay << std::endl;
	
	//Генерация массива В
	std::cout << "\n\nB:" << std::endl;
	for (int i = 1; i <= m; i++)
	{
		B[i] = (rand()%100000) - 50000;
		//std::cout << B[i] << " ";
	}
		
	HeapSort(B, m+1, delay);
	/*std::cout << "\n\nУпорядоченный массив B (пирамидальная): " << std::endl;
	for (int i = 1; i <= m; i++)
		std::cout << B[i] << " ";*/
	std::cout << "\n Time heap sort: " << delay << std::endl;
		
	return 0;
}
