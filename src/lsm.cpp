#include <iostream>
#include <cmath>

int gauss(int n, double **matrica_a, double *massiv_b, double *x)
{
	int i,	j,	k,	r;
	double c, M, s;
	double max; double **a, *b;
	a = new double *[n];
	for(i = 0; i < n; i++)
		a[i] = new double [n];
	b =	new double [n];
	for(i = 0; i < n; i++)
		for(j = 0; j < n; j++)
			a[i][j] = matrica_a[i][j];
	for(i = 0; i < n; i++)
		b[i] = massiv_b[i];
	for(k = 0; k < n; k++)
	{
		max = std::abs(a[k][k]);
		r = k;
		for(i = k+1; i < n; i++)
			if (std::abs(a[i][k]) > max)
		{
			max = std::abs(a[i][k]);
			r = i;
		}
		for(j = 0;j < n; j++)
		{
			c = a[k][j];
			a[k][j] = a[r][j];
			a[r][j] = c;
		}
		c = b[k];
		b[k] = b[r];
		b[r] = c;
		for(i = k + 1; i < n; i++)
		{
			for(M = a[i][k]/a[k][k], j = k; j < n; j++)
				a[i][j] -= M*a[k][j];
			b[i] -= M*b[k];
		}
	}
	if (std::abs(a[n-1][n-1]) == 0)
		if(std::abs(b[n-1]) == 0)
			return -1;
		else return -2;
	else
	{
		for(i=n-1;i>=0;i--)
		{
			for(s=0,j=i+1;j<n;j++)
				s+=a[i][j]*x[j];
			x[i]=(b[i]-s)/a[i][i];
		}
	return 0;
	}
	for(i=0;i<n;i++)
		delete [] a[i];
	delete [] a;
	delete [] b;
}


void errors(int n, double *x, double *y, double *a, double &sq_err, double &avg_err, double &rel_err, double &corr_coef)
{
	int m = n;
	double My = 0, Mx = 0, avg = 0, fi = 0, r0 = 0, r1 = 0, r2 = 0;
	for(int i = 0; i < m; i++)
	{
		for(int j = 0; j < n; j++) fi += a[j]*pow(x[j], j); 
		sq_err += pow(y[i] - fi,2); 
		My += y[i]; Mx += x[i]; fi = 0;
	}

	My /= m; Mx /= m;
	avg_err += sqrt(sq_err)/n;

	for(int i = 0; i < m; i++)
	{
		avg += pow(y[i] - My,2);
		r0 += (x[i] - Mx)*(y[i] - My);
		r1 += (x[i] - Mx)*(x[i] - Mx);
		r2 += (y[i] - My)*(y[i] - My);
	}
	
	corr_coef = r0/sqrt(r1*r2);
	corr_coef = sqrt(1 - sq_err/(r1*r2));


	//std::cout << avg << std::endl;
	//std::cout << sq_err << std::endl;
	//std::cout << 1-(sq_err)/(avg) << std::endl;


	


	sq_err = sqrt(sq_err); 
	avg_err = sq_err/m;
	rel_err = avg_err/My;

	

}


double *square(int n, double *x, double *y)
{
	int m = n;
	double **A = new double*[n], *B = new double[n], *result = new double[n];
	for(int i = 0; i < n; i++)
	{
		A[i] = new double[n];
		
		for(int j = 0; j < n; j++)
			for(int k = 0; k < m; k++)
			{
				B[i] += y[k]*pow(x[k], i);
				A[i][j] += pow(x[k], i+j); 
			}
	}
	A[0][0] = n;
	gauss(n, A, B, result);

	//double sq_err = 0, d = 0, avg_err = 0, corr, My = 0, avg = 0;
	for(int i = 0; i < n; i++)
		delete [] A[i];
	delete [] A;
	return result;
}


double *cubik(int m, double *x, double *y)
{
	int n = 3;
	double **A = new double*[n], *B = new double[n], *X = new double [n*2], *result = new double[n];
	
	for(int i = 0; i < n; i++)
	{
		A[i] = new double[n];
		
		for(int j = 0; j < n; j++)
			for(int k = 0; k < m; k++)
			{
				if (i < 2) B[i] += y[k]*pow(x[k], i);
				else B[i] += y[k]*pow(x[k], i+1);
				if((i < 2) && (j < 2)){
					A[i][j] += pow(x[k], i+j);
					//std::cout << A[i][j] << "\n";
				} 
				if((i < 2) && (j = 2)) A[i][j] += pow(x[k], i+j+1);
				else A[i][j] += pow(x[k], i+j+2);
			}

	}
	/*A[0][0] = n;
	for(int i = 0; i < n; i++)
	{
		for(int j = 0; j < n; j++)
			std::cout << A[i][j] << "		";
		std::cout << "\n";
	}*/
	gauss(n, A, B, result);

	for(int i = 0; i < n; i++)
		delete [] A[i];
	delete [] A;

	return result;
}
