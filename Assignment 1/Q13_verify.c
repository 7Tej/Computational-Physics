//Verify

#include <stdio.h>
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_blas.h>

int isUpperTriangular(gsl_matrix *m);
int isLowerTriangular(gsl_matrix *m);

void printMatrix(gsl_matrix *m) {
    for (size_t i = 0; i < m->size1; i++) {
        for (size_t j = 0; j < m->size2; j++) {
            printf("%.2f\t", gsl_matrix_get(m, i, j));
        }
        printf("\n");
    }
}

void printTriangularType(gsl_matrix *m, const char* matrix_name) {
    if (isUpperTriangular(m)) {
        printf("Matrix %s is upper triangular.\n", matrix_name);
    } else if (isLowerTriangular(m)) {
        printf("Matrix %s is lower triangular.\n", matrix_name);
    } else {
        printf("Matrix %s is neither upper nor lower triangular.\n", matrix_name);
    }
}

int isUpperTriangular(gsl_matrix *m) {
    size_t n = m->size1;
    for (size_t i = 1; i < n; i++) {
        for (size_t j = 0; j < i; j++) {
            if (gsl_matrix_get(m, i, j) != 0) {
                return 0; // Not upper triangular
            }
        }
    }
    return 1; // Upper triangular
}

int isLowerTriangular(gsl_matrix *m) {
    size_t n = m->size1;
    for (size_t i = 0; i < n; i++) {
        for (size_t j = i + 1; j < n; j++) {
            if (gsl_matrix_get(m, i, j) != 0) {
                return 0; // Not lower triangular
            }
        }
    }
    return 1; // Lower triangular
}

int main() {
    int rows1, cols1, rows2, cols2;

    // Input for first matrix
    printf("Enter dimensions of the first matrix (rows columns): ");
    scanf("%d %d", &rows1, &cols1);

    gsl_matrix *matrix1 = gsl_matrix_alloc(rows1, cols1);
    printf("Enter elements of the first matrix:\n");
    for (int i = 0; i < rows1; i++) {
        for (int j = 0; j < cols1; j++) {
            double value;
            scanf("%lf", &value);
            gsl_matrix_set(matrix1, i, j, value);
        }
    }

    // Input for second matrix
    printf("Enter dimensions of the second matrix (rows columns): ");
    scanf("%d %d", &rows2, &cols2);

    gsl_matrix *matrix2 = gsl_matrix_alloc(rows2, cols2);
    printf("Enter elements of the second matrix:\n");
    for (int i = 0; i < rows2; i++) {
        for (int j = 0; j < cols2; j++) {
            double value;
            scanf("%lf", &value);
            gsl_matrix_set(matrix2, i, j, value);
        }
    }

    // To verify triangular properties
    printTriangularType(matrix1, "1");
    printTriangularType(matrix2, "2");

    // To multiply the matrices
    gsl_matrix *result = gsl_matrix_alloc(rows1, cols2);
    gsl_blas_dgemm(CblasNoTrans, CblasNoTrans, 1.0, matrix1, matrix2, 0.0, result);

    // To print the result
    printf("\nProduct of the two matrices:\n");
    printMatrix(result);

    // Freeing allocated memory
    gsl_matrix_free(matrix1);
    gsl_matrix_free(matrix2);
    gsl_matrix_free(result);

    return 0;
}
