#define ANKERL_NANOBENCH_IMPLEMENT
#include <nanobench.h>
#include <cstdlib>
#include <omp.h>
#include <iostream>
#include <fstream>

using namespace std;

#define matr_size 256

void mult_mat(int ** A, int ** B, int ** C, int N){
    int i = 0, j = 0, k = 0, tmp = 0;
    #pragma omp parallel for private(i,j,k) reduction(+:tmp)
    for (i = 0; i < N; i++)
    {
        for (j = 0; j < N; j++)
        {
            for (k = 0; k < N; k++)
            {
                tmp += A[i][k] * B[k][j];
            }
            C[i][j] = tmp;
        }
    }
}

int main(){

    
    ofstream file;
    file.open("./out/matrix_parallel.json", ios_base::out);
    if (file.is_open() != true){
        cout << "*Failed to open file*";
        exit(0);
    }

    int ** A = new int * [matr_size];
    int ** B = new int * [matr_size];
    int ** C = new int * [matr_size];
    for (size_t i = 0; i != matr_size; ++i)
    {
        A[i] = new int [matr_size];
        B[i] = new int [matr_size];
        C[i] = new int [matr_size];
    }
    for (size_t i = 0; i != matr_size; i++){
        for (size_t j = 0; j != matr_size; j++){
            A[i][j] = rand()%100; B[i][j] = rand()%100;
        }
    }
    
    ankerl::nanobench::Bench().output(nullptr).warmup(11).epochs(11).run("matrix mul", [&] {
            mult_mat(A,B,C,matr_size);
    }).render(ankerl::nanobench::templates::pyperf(), file);

    for (size_t i = 0; i != matr_size; i++){
        delete [] A[i]; delete [] B[i]; delete [] C[i];}
    delete [] A; delete [] B; delete [] C;

    file.close();

    return 0;
}