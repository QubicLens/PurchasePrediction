import numpy as np
from scipy.integrate import simps


TAU = 2 * np.pi
PI2 = np.pi / 2


def cat_coeff(x, u, m=23, p=1999):
    t = np.linspace(0, TAU, p)  # Number of samples for integration
    m = np.arange(-m, m + 1)  # Number of terms in CAT Series

    # Approximate Data Transform using Simpson's Rule
    rho = 1j * PI2 * np.floor((t[:, None] @ m[None, :]) / PI2)
    A = simps(np.einsum("tj,tk->tjk ", np.exp(-rho), np.exp(rho)), t, axis=0)
    B = simps(np.einsum("t,tj->tj", x(t), np.exp(-rho)), t, axis=0)

    # Compute coefficients in Frequency Domain
    c = [1, 1j, -1, -1j, 1][4 * u]
    return np.linalg.solve(c * A, B)


def magnitude(Y):
    # Amplitude of each respective term in CAT Series
    return np.around(np.abs(Y) * np.abs(Y))


if __name__ == "__main__":
    x = lambda t: np.piecewise(
        t,
        [
            (0 <= t) * (t < PI2),
            (PI2 <= t) * (t < np.pi),
            (np.pi <= t) * (t < 3 * PI2),
            (3 * PI2 <= t) * (t <= TAU),
        ],
        [2, 0, -2, 0],
    )

    print(magnitude(cat_coeff(x, 0)))
