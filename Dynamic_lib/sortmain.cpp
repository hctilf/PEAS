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
#include "sort.h"

using namespace std;

int main(int argc, char **argv)
{
	int n = 11, m = 8;
	int *A = new int[n];
	int *B = new int[m];
	
	std::cout << "A:" << std::endl;
	for (int i = 1; i <= n; i++)
	{
		A[i] = (rand()%1000) - 500;
		std::cout << A[i] << " ";
	}
	
	std::cout << "\n\nB:" << std::endl;
	for (int i = 1; i <= m; i++)
	{
		B[i]=(rand()%1000) - 500;
		std::cout << B[i] << " ";
	}
	
	MergeSort(A, 1, n);
	HeapSort(B, m+1);
	
	std::cout<<"\n\nУпорядоченный массив A: " << std::endl;
	for (int i = 1; i <= n; i++)
		std::cout << A[i] << " ";
		
	std::cout<<"\n\nУпорядоченный массив B: " << std::endl;
	for (int i = 1; i <= m; i++)
		std::cout << B[i] << " ";
		
	return 0;
}
