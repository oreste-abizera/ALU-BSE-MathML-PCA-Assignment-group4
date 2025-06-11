"""
Example showing the usage of the alumath_kheoml Matrix class.
"""

import numpy as np
from alumath_kheoml import Matrix, matrix_multiply

def demonstrate_matrix_operations():
    print("=" * 50)
    print("MATRIX OPERATIONS DEMONSTRATION")
    print("=" * 50)
    
    # Create matrices
    print("Creating matrices A and B:")
    A = np.array([[1, 2, 3],
                 [4, 5, 6]])  # 2x3 matrix
                 
    B = np.array([[7, 8],
                 [9, 10],
                 [11, 12]])  # 3x2 matrix
    
    print("Matrix A:")
    print(A)
    print(f"Shape of A: {A.shape}")
    
    print("\nMatrix B:")
    print(B)
    print(f"Shape of B: {B.shape}")
    
    # Convert to Matrix objects
    matrix_A = Matrix(A)
    matrix_B = Matrix(B)
    
    # Multiply using matrix_multiply function
    print("\n1. Using matrix_multiply function:")
    C = matrix_multiply(A, B)
    print("Result of A * B:")
    print(C)
    print(f"Shape of result: {C.shape}")
    
    # Multiply using the Matrix class
    print("\n2. Using Matrix class multiply method:")
    matrix_C = matrix_A.multiply(matrix_B)
    print("Result of Matrix A * Matrix B:")
    print(matrix_C)
    
    # Using the @ operator
    print("\n3. Using @ operator with Matrix class:")
    matrix_D = matrix_A @ matrix_B
    print("Result of Matrix A @ Matrix B:")
    print(matrix_D)
    
    # Transpose operation
    print("\n4. Matrix transpose:")
    matrix_E = matrix_A.transpose()
    print("Transpose of Matrix A:")
    print(matrix_E)
    
    # Handling incompatible matrices
    try:
        print("\n5. Attempting to multiply incompatible matrices:")
        incompatible_matrix = Matrix(np.array([[1, 2], [3, 4]]))  # 2x2 matrix
        result = matrix_B @ incompatible_matrix  # This should fail
    except ValueError as e:
        print(f"Error caught: {e}")

if __name__ == "__main__":
    demonstrate_matrix_operations()
