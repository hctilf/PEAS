#define ANKERL_NANOBENCH_IMPLEMENT
#include <iostream>
#include <fstream>
#include <cmath>
#include <ctime>
#include <nanobench.h>

using namespace std;

class matrix
{
public:
		int n;
		double **a;
		matrix(int,int,int);
		matrix(int,int);
		matrix operator +(matrix);
		matrix operator -(matrix);
		matrix operator *(matrix);
		void show();
		void razdelenie(matrix,matrix,matrix,matrix,matrix,int);
		matrix together(matrix,matrix,matrix,matrix,int);
		matrix shtrass(matrix,matrix,int);
		matrix Mult(matrix, matrix,matrix,int,int);

};

//Проверка, является ли размерность матрицы степенью 2
// Если нет, то возвращается число больше проверяемого и являющиеся степенью 2
int proverka2(int n)
{
	int m=1,s=0;
	while (m<n)
	{
		m*=2;
		s+=1;
	}
	if (n==m) return n;
	return pow(2,s);
}
//Функция деления матрицы на 4 части
void razdelenie(matrix a,matrix a11,matrix a12,matrix a21,matrix a22,int size)
{
	int n=size/2,i,j;
	for(i=0;i<n;i++)
	{
		for (j=0;j<n;a11.a[i][j]=a.a[i][j],j++);
		for(j=n;j<size; a12.a[i][j-n]=a.a[i][j],j++);

	}

	for(i=n;i<size;i++)
	{
		for(j=0;j<n;a21.a[i-n][j]=a.a[i][j],j++);
		for(j=n;j<size;a22.a[i-n][j-n]=a.a[i][j],j++);
	}
}
//Функция соединения 4х матриц в одну
matrix together(matrix a11,matrix a12,matrix a21,matrix a22,int size)
{
	int n=size*2,i,j;
	matrix a(n,false);
	for(i=0;i<size;i++)
	{
		for (j=0;j<size;a.a[i][j]=a11.a[i][j],j++);
		for(j=size;j<n;a.a[i][j]=a12.a[i][j-size],j++);
	}
	for(i=size;i<n;i++)
	{
		for(j=0;j<size;a.a[i][j]=a21.a[i-size][j],j++);
		for(j=size;j<n;a.a[i][j]=a22.a[i-size][j-size],j++);
	}
	return a;
}


matrix shtrass(matrix a,matrix b,int n)
{
	if (n<=64)
		return a*b;
	n/=2;
	matrix a11(n,2),a12(n,2),a21(n,2),a22(n,2);
	matrix b11(n,2),b12(n,2),b21(n,2),b22(n,2);
	matrix m1(n,2),m2(n,2),m3(n,2),m4(n,2),m5(n,2),m6(n,2),m7(n,2);
	matrix c11(n,2),c12(n,2),c21(n,2),c22(n,2);
	razdelenie(a,a11,a12,a21,a22,2*n);
	razdelenie(b,b11,b12,b21,b22,2*n);

	m1=shtrass(a11+a22,b11+b22,n);
	m2=shtrass(a21+a22,b11,n);
	m3=shtrass(a11,b12-b22,n);
	m4=shtrass(a22,b21-b11,n);
	m5=shtrass(a11+a12,b22,n);
	m6=shtrass(a21-a11,b11+b12,n);
	m7=shtrass(a12-a22,b21+b22,n);
	c11=m1+m4-m5+m7;
	c12=m3+m5;
	c21=m2+m4;
	c22=m1+m3-m2+m6;

    return together(c11,c12,c21,c22,n);
}
matrix Mult(matrix a,matrix b,matrix c,int n, int N)
{
    if (N>n) c=a*b;
    else{
    for(int k=0;k<n;k+=N)
        for(int i=0;i<n;i+=N)
            for(int j=0;j<n;j+=N)
                for(int kk=k;kk<k+N;kk++)
                    for(int ii=i;ii<i+N;ii++)
                        for(int jj=j;jj<j+N;jj++)
                            c.a[ii][jj]+=a.a[ii][kk]*b.a[kk][jj];}
    return c;
}
int main()
{
    int n,N;
	cout<<"Введите размерность матриц ";
	cin>>n;
	N=proverka2(n);
	matrix x(N,n,1),y(N,n,1),z(N,n,0),z1(N,n,0),z2(N,n,0);
	/*cout<<"Матрица А:"<<endl;
	for(int i=0;i<n;i++){
        for(int j=0;j<n;j++)
        cout<<x.a[i][j]<<"  ";
        cout<<endl;}
	cout<<"Матрица B:"<<endl;
	for(int i=0;i<n;i++){
        for(int j=0;j<n;j++)
        cout<<y.a[i][j]<<"  ";
        cout<<endl;}

    int t1 = clock();
    cout<<t1<<"  "<<endl;*/

   /* ankerl::nanobench::Bench().run("Mult_512", [&] {

        Mult(x,y,z2,N,512);

    });*/
  //  for(int k=0;k<3;k++){
	ofstream file;
    file.open("matrix_linear.json", ios_base::out);

    ankerl::nanobench::Bench().output(nullptr).run("Shtrass", [&] {
	ankerl::nanobench::doNotOptimizeAway(z=shtrass(x,y,N));
    }).render(ankerl::nanobench::templates::json(), file);
    //}

/*	int t2 = clock();
    cout<<t2<<"  "<<endl;

    int t3 = t2-t1;
    cout << "Время:  " <<t3<< endl;
    z=shtrass(x,y,N);
    cout<<"Результат А*В(по методу Штрассена) :"<<endl;
	for(int i=0;i<n;i++){
        for(int j=0;j<n;j++)
        cout<<z.a[i][j]<<"  ";
        cout<<endl;}
    z1=x*y;
    cout<<"Результат А*В(классический метод) :"<<endl;
	for(int i=0;i<n;i++){
        for(int j=0;j<n;j++)
        cout<<z1.a[i][j]<<"  ";
        cout<<endl;}
    Mult(x,y,z2,N,2);
    cout<<"Результат А*В:(блочный метод)"<<endl;
	for(int i=0;i<n;i++){
        for(int j=0;j<n;j++)
        cout<<z2.a[i][j]<<"  ";
        cout<<endl;}*/
	file.close();
	return 0;
}
//Создаем матрицу n1*n1; Если fl=0 то элементы матрицы =0
matrix::matrix(int n1, int fl)
{
	n=n1;
	int i,j;
	a=new double *[n];
		for(i=0;i<n;a[i]=new double [n],i++);
	if (fl==0)
		for(i=0;i<n;i++)
			for(j=0;j<n;a[i][j]=0,j++);
}
//Создаем  матрицу N1*N1, но элементы от n1 до N1 =0
matrix::matrix (int N1,int n1, int fl)
{
	int N=N1;
	n=n1;
	int i,j;
		if (N==0)
		{
			a=new double *[n];
			for(i=0;i<n;a[i]=new double [n],i++);
			if (fl!=0)
			for(i=0;i<n;i++)
				for(j=0;j<n;a[i][j]=rand()%2+1,j++);
			else
				for(i=0;i<n;i++)
					for(j=0;j<n;a[i][j]=0,j++);
		}
		else
		{
			swap(n,N);
				a=new double *[n];
                for(i=0;i<n;a[i]=new double [n],i++);

				for(i=0;i<n;i++)
					for(j=0;j<n;a[i][j]=0,j++);
				if (fl!=0)
				for(i=0;i<N;i++)
					for(j=0;j<N;a[i][j]=rand()%9+1,j++);
		}
}
// Оператор сложения матриц
matrix matrix::operator +(matrix b)
{
	int i,j,n=b.n;
	matrix temp(b.n, 0);

	for(i=0;i<n;i++)
    for(j=0;j<n;j++)
            temp.a[i][j]=a[i][j]+b.a[i][j];
	return temp;
}
matrix matrix::operator -(matrix b)
{
	int i,j,n=b.n;
	matrix temp(b.n,0);

	for(i=0;i<n;i++)
    for(j=0;j<n;j++)
            temp.a[i][j]=a[i][j]-b.a[i][j];
	return temp;
}
matrix matrix::operator *(matrix b)
{
	int i,j,k,n=b.n;
	matrix temp(n,0);
    for(k=0;k<n;k++)
        for(i=0;i<n;i++)
            for(j=0;j<n;j++)
                temp.a[i][j]+=a[i][k]*b.a[k][j];
	return temp;

}
void matrix::show()
{
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++)
            cout << a[i][j] << ' ';
        cout << endl;
    }
}
