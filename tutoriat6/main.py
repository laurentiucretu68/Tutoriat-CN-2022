import numpy as np
import matplotlib.pyplot as plt


def spline_liniara(X, Y, z):
    """
    X: X = [X0, X1, ..., Xn]
    Y: [Y0=f(X0), Y1=F(X1), ..., Yn=f(Xn)]
    z: Punct in care se doreste o valoare aproximata a functiei
    """
    n = np.shape(X)[0]-1
    t = 0

    # Pasul 1
    for i in range(n):
        # Pasul 2
        if X[i] <= z <= X[i + 1]:
            a = Y[i]
            b = (Y[i+1] - Y[i]) / (X[i+1] - X[i])
            t = a + b*(z-X[i])
            break

    # Pasul 3
    return t  # Valoarea aproximata calculata in z


def spline_patratica(X, Y, dfa, z):
    """
    X: X = [X0, X1, ..., Xn]
    Y: [Y0=f(X0), Y1=F(X1), ..., Yn=f(Xn)]
    dfa: Valoarea derivatei in capatul din stanga al intervalului folosit
    z: Punct in care se doreste o valoare aproximata a functiei
    """
    n = np.shape(X)[0] - 1
    b = np.zeros(n)
    c = np.zeros(n)
    # Pasul 1
    b[0] = dfa
    t = dt = 0

    # Pasul 2
    for i in range(n-1):
        b[i+1] = 2*(Y[i+1] - Y[i]) / (X[i+1] - X[i]) - b[i]

    # Pasul 3
    for i in range(n):
        c[i] = (Y[i+1] - Y[i] - (X[i+1] - X[i])*b[i]) / ((X[i+1] - X[i]) * (X[i+1] - X[i]))

    # Pasul 4
    for i in range(n):
        if X[i] <= z <= X[i+1]:
            t = Y[i] + b[i]*(z-X[i]) + c[i]*(z-X[i])*(z-X[i])
            dt = b[i] + 2*c[i]*(z - X[i])

    # Pasul 5
    return t, dt  # Valoarea aproximata calculata in z


def func(x):
    y = np.sin(2*x) - 2*np.cos(3*x)
    return y


def dfunc(x):
    y = 2*np.cos(2*x) + 6*np.sin(3*x)
    return y


def interp_direct(X, Y, z):
    n = np.shape(X)[0]
    A = np.vander(X, n, increasing=True)

    a = np.linalg.solve(A, Y)
    t = a[:] @ np.power(z, range(n))

    return t


def ex():
    interval = [-np.pi, np.pi]  # domeniul [-pi,pi]
    domain = np.linspace(interval[0], interval[1], 100)  # discretizarea intervalului
    f_exact = func(domain)  # calculul functiei exacte

    for N in [10, 15, 30]:
        """
        Pentru N = 10,30,50 se calculeaza interpolarea prin toate cele 3 metode
        (lagrange, spline liniara si patratica)
        """
        x = np.linspace(interval[0], interval[1], N)
        y = func(x)

        interpolare_lagrange = np.zeros(N)
        interpolare_spline_liniara = np.zeros(N)
        interpolare_spline_patratica = np.zeros(N)
        dt = np.zeros(N)
        for i in range(N):
            interpolare_lagrange[i] = interp_direct(x, y, x[i])
            interpolare_spline_liniara[i] = spline_liniara(x, y, x[i])
            interpolare_spline_patratica[i], dt[i] = spline_patratica(x, y, dfunc(x[0]), x[i])

        # Trasarea graficului
        plt.figure(0)
        plt.plot(domain, f_exact, color='black', label="Functia exacta")
        plt.scatter(x, y, marker='*', s=10, color="red", label="Puncte cunoscute")
        plt.plot(x, interpolare_lagrange, color="green", label="Interpolare Lagrange")
        plt.plot(x, interpolare_spline_liniara, color='orange', label="Interpolare Spline Liniara")
        plt.plot(x, interpolare_spline_patratica, color='green', label="Interpolare Spline Patratica")
        plt.title(f'Pentru N = {N}')
        plt.grid()
        plt.legend()
        plt.show()


if __name__ == '__main__':
    ex()
