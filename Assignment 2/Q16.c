#include <stdio.h>
#include <math.h>

// Define the ODE dy/dt = f(t, y)
double f(double t, double y) {
    return y - t * t + 1; // y' = y - t^2 + 1
}

// True solution for comparison
double true_solution(double t) {
    return pow(t + 1, 2) - 0.5 * exp(t);
}

// Euler method implementation
void euler_method(double t0, double y0, double t_end, double h) {
    double t = t0;
    double y = y0;

    // Initialize variables for error calculation
    double error, error_upper_bound;

    // Print initial values
    printf("t = %.4f, y = %.4f, error = %.4f\n", t, y, 0.0);

    // Perform Euler method
    while (t < t_end) {
        // Calculate next value using Euler method
        double y_next = y + h * f(t, y);
        
        // Calculate error
        error = fabs(true_solution(t + h) - y_next); // True solution: y = (t + 1)^2 - 0.5 * e^t

        // Calculate upper bound for error
        double M = 2 + 4 * t_end + exp(t_end);
        double L = 1;
        error_upper_bound = (h * M / (2 * L)) * (exp((t + h) * L) - 1);

        // Print values for this step
        printf("t = %.4f, y = %.4f, error = %.4f, error_upper_bound = %.4f\n", t + h, y_next, error, error_upper_bound);

        // Update t and y for the next step
        t += h;
        y = y_next;
    }
}

int main() {
    double t0 = 0.0;     // Initial time
    double y0 = 0.5;     // Initial value of y
    double t_end = 2.0;  // End time
    double h = 0.2;      // Step size

    // Solve the ODE using Euler method
    euler_method(t0, y0, t_end, h);
