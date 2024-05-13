#include <stdio.h>
#include <math.h>
#include <gsl/gsl_fft_complex.h>
#include <complex.h>

#define REAL(z,i) ((z)[2*(i)])     // Real part of z
#define IMAG(z,i) ((z)[2*(i)+1])   // Imaginary part of z

// sinc function
double sinc(double x) {
    if (x == 0.0) {
        return 1.0;
    } else {
        return sin(x) / x;
    }
}

// Analytical FT
double analytical_ft(double k, double pi){
    if(k<=1.0 && k>=-1.0){
       return sqrt(pi/2);
    }
    else{
       return 0.0;
    }
}

int main(){
    int n = 1024; // No. of sample points
    double Pi = acos(-1.0);
    double f[2*n],k[n],factor;

    // Defining x range
    double xmin = -50.;
    double xmax = 50.;
    double dx = (xmax - xmin)/n;
    
    for (int i=0; i<n; ++i){      
         REAL(f,i)=sinc(xmin+i*dx);  
         IMAG(f,i)=0.0;
    }

    gsl_fft_complex_radix2_forward(f, 1, n);  
  
    FILE *output_file1 = fopen("box1.dat", "w"); 
    FILE *output_file2 = fopen("box2.dat", "w"); 

    /*
         The output array is generated with the first element for k=0, the next N/2-1 values are returned for positive k values
         and the next N/2 values; adjusting k 
    */
    for (int i=0; i<n; ++i){
         if (i==0){
             k[i] = 0;
         }
         else if (i<n/2){
             k[i] = i / (n * dx);
         }
         else {
             k[i] = -(n-i) / (n * dx);
         }
         // Calculating normalized FFT
         factor = dx * sqrt(1.0/(2*Pi)) * creal(cexp(I*k[i]*2*Pi*xmin));
         // chnaging k to angular freq
         fprintf(output_file1, "%f %f\n", 2* Pi* k[i], factor*REAL(f,i));
         fprintf(output_file2, "%f %f\n", 2*Pi*k[i], analytical_ft(2*Pi*k[i], Pi));
    }
    fclose(output_file1);
    fclose(output_file2);
    return 0;
}

