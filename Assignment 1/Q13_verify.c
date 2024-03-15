//Verify

#include <stdio.h>
#include <gsl/gsl_matrix.h>

// Function to check if a matrix is upper triangular
int isUpperTriangular(const gsl_matrix *matrix) {
    size_t n = matrix->size1;
    for (size_t i = 1; i < n; i++) {
        for (size_t j = 0; j < i; j++) {
            if (gsl_matrix_get(matrix, i, j) != 0.0) {
                return 0; // Not upper triangular
            }
        }
    }
    return 1; // Upper triangular
}

// Function to check if a matrix is lower triangular
int isLowerTriangular(const gsl_matrix *matrix) {
    size_t n = matrix->size1;
    for (size_t i = 0; i < n; i++) {
        for (size_t j = i + 1; j < n; j++) {
            if (gsl_matrix_get(matrix, i, j) != 0.0) {
                return 0; // Not lower triangular
            }
        }
    }
    return 1; // Lower triangular
}

int main() {
    // Variables to store user input
    int rows, cols;
    
    // To get dimensions of the matrix from the user
    printf("Enter number of rows for the matrix: ");
    scanf("%d", &rows);
    printf("Enter number of columns for the matrix: ");
    scanf("%d", &cols);
    
    // To allocate memory for the matrix
    gsl_matrix *matrix = gsl_matrix_alloc(rows, cols);
    
    // To get matrix elements from the user
    printf("Enter elements of the matrix:\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            double element;
            printf("Enter element at position (%d, %d): ", i+1, j+1);
            scanf("%lf", &element);
            gsl_matrix_set(matrix, i, j, element);
        }
    }
    
    // To check if the matrix is upper triangular
    if (isUpperTriangular(matrix)) {
        printf("The matrix is upper triangular.\n");
    } else {
        printf("The matrix is not upper triangular.\n");
    }
    
    // To check if the matrix is lower triangular
    if (isLowerTriangular(matrix)) {
        printf("The matrix is lower triangular.\n");
    } else {
        printf("The matrix is not lower triangular.\n");
    }

    // Freeing up allocated memory
    gsl_matrix_free(matrix);

    return 0;
}
