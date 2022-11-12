/*
 * Создать статическую и динамическую библиотеки,
 * содержащие следующие функции:  сортировка слиянием,
 * пирамидальная сортировка. Написать программу,
 * тестирующую функции из библиотеки.
 * 
 * Создать файл сборки для компиляции библиотечных файлов,
 * сборки  и запуска исполняемого файла, удаления объектных файлов.
 */

// Функция, сливающая массивы
void Merge(int *A, int first, int last)
{
	int middle, start, end, j;
	int *mas=new int [last];
	
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
void MergeSort(int *A, int first, int last)
{
	if (first < last)
	{
		MergeSort(A, first, (first+last) / 2); //сортировка левой части
		MergeSort(A, (first+last)/2 + 1, last); //сортировка правой части
		Merge(A, first, last); //слияние двух частей
	}
};

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
