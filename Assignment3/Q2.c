#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <fftw3.h>
#include <complex.h>

#define N 1024 // Number of samples

// Defines the sinc function
double sinc(double x){
    if (x == 0.0){
        return 1.0;
    }
    else{
        return sin(x)/x;
    }
}

// Defines the analytical fourier transform of sinc function
double analytical_ft(double k, double pi){
    if(k<=1.0 && k>=-1.0){
       return sqrt(pi/2);
    }
    else{
       return 0.0;
    }
}

int main() {
    int i;
    double x[N], k[N], f[N], delta_x, factor;
    fftw_complex *in, *out;
    fftw_plan p;
    
    // Defining Pi
    double PI = acos(-1.0);
    
    // Defining xmin, xmax
    double xmin = -50.0;
    double xmax = 50.0;
    delta_x = (xmax-xmin)/N;
    
    // Initializeing FFTW arrays
    in = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);
    out = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);
    
    // Creating file that will store the data values of sinc function
    FILE *analytical_file = fopen("sinc.dat", "w"); 
    for (i = 0; i < N; ++i) {
        x[i] = xmin + i * delta_x;
        fprintf(analytical_file, "%f %f\n", x[i], sinc(x[i]));
        in[i][0] = sinc(x[i]); // Real part of the function to be fourier transform
        in[i][1] = 0.0; // Imaginary part of the function to be fourier transform
    }
    fclose(analytical_file);
    
    p = fftw_plan_dft_1d(N, in, out, FFTW_FORWARD, FFTW_ESTIMATE); // Creating plan
    // FFTW returns the fourier transform without any prefactor of 1/sqrt(n)
    
    fftw_execute(p); // Executing FFT
    
    FILE *output_file = fopen("box.dat", "w"); // Writing output to a file ''box.dat''
    FILE *output_file2 = fopen("box2.dat", "w"); // Writing analytical solution to a file ''box.2dat''
    
  
    for (i = 0; i < N; ++i) {
        if (i==0){
           k[i] = 0;
        }
        else if (i<N/2){
            k[i] = i / (N * delta_x);
        }
        else {
            k[i] = -(N-i) / (N * delta_x);
        }
        // Calculates and normalizes FFT
        factor = delta_x * sqrt(1.0/(2*PI)) * creal(cexp(I*k[i]*2*PI*xmin));
        // Converting K(freqiencies) to angular frequencies
        fprintf(output_file, "%f %f\n", 2*PI*k[i], fabs(factor * out[i][0]));
        fprintf(output_file2, "%f %f\n", 2*PI*k[i], analytical_ft(2*PI*k[i], PI));
    }
    fclose(output_file);
    fclose(output_file2);
    
    // Clean up
    fftw_destroy_plan(p);
    fftw_free(in);
    fftw_free(out);

    return 0;
}
