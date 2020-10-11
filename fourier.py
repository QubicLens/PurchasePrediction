import numpy as np
from numpy import newaxis
from scipy.integrate import simps


TAU = 2 * np.pi
PI2 = np.pi / 2


def cat_coeff(x, u, k, s):
    # Number of samples for integration
    t = np.linspace(0, TAU, s)

    # Approximate Data Transform using Simpson's Rule
    rho = 1j * PI2 * np.floor((t[:, newaxis] @ k[newaxis, :]) / PI2)
    A = simps(np.einsum("tj,tk->tjk", np.exp(-rho), np.exp(rho)), t, axis=0)
    B = simps(np.einsum("t,tj->tj", x(t), np.exp(-rho)), t, axis=0)

    # Compute coefficients in Frequency Domain
    c = [1, 1j, -1, -1j, 1][4 * u]
    return np.linalg.solve(c * A, B)


def phi(k, t, u):
    t = np.mod(t, TAU)  # Expand CAT function to that of a periodic function
    return np.exp(1j * PI2 * np.floor((t[:, newaxis] @ k[newaxis, :]) / PI2 + 4 * u))


def predict(x, t, k=23, s=1999):
    u = 0  # TODO: calculating phase, time scaling

    # Compute coefficients of 2k+1 terms in CAT Series
    k = np.arange(-k, k + 1)
    Yk = cat_coeff(x, u, k, s)

    # Compute category at each time t
    return np.real(np.einsum("tk,k->t", phi(k, t, u), Yk))


if __name__ == "__main__":
    x0 = lambda t: np.piecewise(
        t,
        [
            (0 <= t) * (t < PI2),
            (PI2 <= t) * (t < np.pi),
            (np.pi <= t) * (t < 3 * PI2),
            (3 * PI2 <= t) * (t < TAU),
        ],
        [1, 0, 2, 0],
    )

    x = lambda t: x0(np.mod(t, TAU))
    xp = predict(x, np.linspace(0, TAU, 18), 10, 19999)

    print(f"Quasi-Category: {xp}\n")
    print(f"Predicted: {np.maximum(0, np.around(xp))}\n")
    print(f"Actual: {x(np.linspace(0, TAU, 18))}\n")
