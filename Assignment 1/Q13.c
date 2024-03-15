//LU decomposition for arbitraty dimension

#include <stdio.h>
#include <gsl/gsl_linalg.h>

void printMatrix(int rows, int cols, double matrix[][cols]) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%.2f\t", matrix[i][j]);
        }
        printf("\n");
    }
}

void printLU(gsl_matrix *LU) {
    int n = LU->size1;
    printf("L matrix:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j)
                printf("1.00\t");
            else if (i > j)
                printf("%.2f\t", gsl_matrix_get(LU, i, j));
            else
                printf("0.00\t");
        }
        printf("\n");
    }

    printf("\nU matrix:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i <= j)
                printf("%.2f\t", gsl_matrix_get(LU, i, j));
            else
                printf("0.00\t");
        }
        printf("\n");
    }
}

int main() {
    int n;
    printf("Enter the dimension of the square matrix: ");
    scanf("%d", &n);

    double matrix[n][n];
    printf("Enter the elements of the matrix:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%lf", &matrix[i][j]);
        }
    }

    // Convert matrix to GSL matrix
    gsl_matrix_view m = gsl_matrix_view_array(&matrix[0][0], n, n);

    // Perform LU decomposition
    gsl_permutation *p = gsl_permutation_alloc(n);
    int signum;
    gsl_linalg_LU_decomp(&m.matrix, p, &signum);

    printf("\nLU decomposition of the matrix:\n");
    printLU(&m.matrix);

    gsl_permutation_free(p);

    return 0;
}

