import numpy as np

# Read the matrix and compute eigenvalues and eigenvectors
M = np.loadtxt('tests/matrix_input.txt', delimiter=',')
eigenvalues, eigenvectors = np.linalg.eig(M)

# Combine eigenvalues and eigenvectors into a single array
EVV = np.column_stack((eigenvalues, eigenvectors.T))  # Transpose eigenvectors for correct alignment

# Write the combined data to a file
np.savetxt('tests/matrix_output.txt', EVV, fmt='%1.15f')

