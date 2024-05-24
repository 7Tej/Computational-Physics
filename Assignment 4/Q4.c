/** To generate 10,000 random numbers from an 
exponential distribution with mean 0.5 using transformation method
*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define N 10000

// Function to generate an exponentially distributed random number
double exponential_random(double mean) {
    double u = ((double) rand()) / RAND_MAX; // Generate a uniform random number between 0 and 1
    return -mean * log(1 - u); // Transform using the inverse CDF
}

int main() {
    double mean = 0.5;
    double numbers[N];

    // Seed the random number generator
    srand(time(NULL));

    // Generate the random numbers and store them in the array
    for(int i = 0; i < N; i++) {
        numbers[i] = exponential_random(mean);
    }

    printf("Generated %d exponential random numbers with mean %f\n", N, mean);

    // Print the generated numbers
    printf("Generated Numbers:\n");
    for (int i = 0; i < N; i++) {
        printf("%f\n", numbers[i]);
    }

    return 0;
}
