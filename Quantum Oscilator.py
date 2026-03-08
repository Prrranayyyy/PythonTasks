import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh

# constants
hbar = 1
m = 1
omega = 1

# spatial grid
N = 400
x = np.linspace(-5,5,N)
dx = x[1] - x[0]

# potential
V = 0.5*m*omega**2 * x**2

# kinetic matrix
T = np.zeros((N,N))

for i in range(N):
    T[i,i] = -2
    if i > 0:
        T[i,i-1] = 1
    if i < N-1:
        T[i,i+1] = 1

T = -(hbar**2)/(2*m*dx**2) * T

# potential matrix
V_matrix = np.diag(V)

# Hamiltonian
H = T + V_matrix

# solve eigenvalue problem
energies, wavefunctions = eigh(H)

print(energies[:5])

for i in range(3):
    plt.plot(x, wavefunctions[:,i]**2)

plt.title("First Three Probability Densities")
plt.xlabel("x")
plt.ylabel("|ψ|^2")
plt.show()
plt.savefig("wavefunction.png")
