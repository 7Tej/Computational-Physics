//2

#include <stdio.h>
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_linalg.h>

int main() {
    const int n = 3;

    // 2nd matrix
    double data[3][3] = {
        {10, -1, 0},
        {-1, 10, -2},
        {0, -2, 10}
    };

    // Creating the 1st matrix
    gsl_matrix_view A = gsl_matrix_view_array(&data[0][0], n, n);

    // Performing LU decomposition
    gsl_permutation *p = gsl_permutation_alloc(n);
    int signum;
    gsl_linalg_LU_decomp(&A.matrix, p, &signum);

    // Output of the decomposed matrix
    printf("Matrix L:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (j > i) {
                printf("%8.3f ", 0.0);
            } else if (i == j) {
                printf("%8.3f ", 1.0);
            } else {
                printf("%8.3f ", gsl_matrix_get(&A.matrix, i, j));
            }
        }
        printf("\n");
    }

    printf("Matrix U:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (j >= i) {
                printf("%8.3f ", gsl_matrix_get(&A.matrix, i, j));
            } else {
                printf("%8.3f ", 0.0);
            }
        }
        printf("\n");
    }

    // Freeing memory
    gsl_permutation_free(p);

    return 0;
}
