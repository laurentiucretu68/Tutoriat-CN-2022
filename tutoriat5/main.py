"""
Toate cele 4 exercitii sunt identice, difera doar metoda de interpolare folosita.
Voi detalia doar primul exercitiu.
"""
import numpy as np
import matplotlib.pyplot as plt


def interp_direct(X, Y, z):
    """
    X (numpy vector)
    Y (numpy vector)
    z (float)
    """
    # Pasul 1
    n = np.shape(X)[0]  # Dimensiunea vectorului X
    A = np.vander(X, n, increasing=True)  # Creaza matrice Vandermonde

    # Pasul 2
    a = np.linalg.solve(A, Y)  # Rezolva sistemul A*a=Y

    # Pasul 3
    t = a[:] @ np.power(z, range(n))  # Calculeaza valoarea lui t

    # Pasul 4
    return t


def interp_lagrange(X, Y, z):
    """
    X (numpy vector)
    Y (numpy vector)
    z (float)
    """
    # Pasul 1
    n = np.shape(X)[0]  # Dimensiunea vectorului X
    L = np.zeros(n)  # Se creaza un vector de zerouri de dimensiune n

    for k in range(n):
        # La fiecare pas se determina functiile de baza Ln,k in punctul z
        p = 1
        for j in range(n):
            if j != k:
                p *= (z - X[j]) / (X[k] - X[j])
        L[k] = p

    # Pasul 2
    t = L[:] @ Y[:]  # Determina aproximarea in punctul z

    # Pasul 3
    return t


def interp_newton(X, Y, z):
    """
    X (numpy vector)
    Y (numpy vector)
    z (float)
    """
    # Pasul 1
    n = np.shape(X)[0]  # Dimensiunea vectorului X
    A = np.zeros((n, n))  # Se creaza o matrice de zerouri de dimensiune nxn
    A[:, 0] = 1

    for i in range(1, n):
        for j in range(1, i+1):
            p = 1
            for k in range(j):
                p *= (X[i] - X[k])

            A[i, j] = p

    # Pasul 2
    c = np.linalg.solve(A, Y)  # Se determina coeficientii polinomului Lagrange prin rezolvarea sistemului Ac=Y

    # Pasul 3
    # Se determina aproximarea in punctul z
    t = c[0]
    for i in range(1, n):
        p = 1
        for j in range(i):
            p *= (z - X[j])

        t += c[i] * p

    # Pasul 4
    return t


def interp_newton_dd(X, Y, z):
    """
    X (numpy vector)
    Y (numpy vector)
    z (float)
    """
    # Pasul 1
    n = np.shape(X)[0] - 1  # Dimensiunea vectorului X
    Q = np.zeros((n+1, n+1))  # Se creaza o matrice de zerouri de dimensiune nxn
    Q[:, 0] = Y[:]

    for i in range(1, n+1):
        for j in range(1, i+1):
            Q[i, j] = (Q[i, j-1] - Q[i-1, j-1]) / (X[i] - X[i-j])

    # Pasul 2
    # Se determina aproximarea in punctul t
    t = Q[0, 0]
    for k in range(1, n+1):
        p = 1
        for j in range(k):
            p = p * (z - X[j])

        t += Q[k, k] * p

    # Pasul 3
    return t


def f(x):
    y = np.sin(2*x) - 2*np.cos(3*x)
    return y


def ex1():
    # Punctul a
    x_client = np.linspace(-np.pi, np.pi, 20)  # Discretizarea intervalului [-pi, pi] in 20 de puncte echidistante (Datele clientului)
    y_client = f(x_client)  # Calcularea lui f(x_client)
    # Trasarea graficului
    plt.figure(0)
    plt.plot(x_client, y_client, label="Datele clientului - 20 de puncte - ex1 a")
    plt.grid()
    plt.axvline(0, color='black')
    plt.axhline(0, color='black')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()

    # Punctul b si c
    aprox = np.zeros(100)
    x = np.linspace(-np.pi, np.pi, 100)  # Discretizarea intervalului [-pi, pi] in 100 de puncte echidistante
    y = f(x)  # Calcularea lui f(x)
    """
    Pentru fiecare punct din vectorul x trebuie calculata aproximarea in punctul x[i], i=0,..,99.
    La fiecare apel al functiei interp_direct se trimit ca parametri datele clientului (x_aprox),
    valorile trecute prin functia f (y_aprox) si punctul x[i] curent.
    Valorile sunt salvate intr-un nou vector
    """
    for i in range(100):
        aprox[i] = interp_direct(x_client, y_client, x[i])

    plt.figure(1)
    plt.plot(x, y, label="Datele clientului - 20 puncte")
    plt.plot(x, aprox, linestyle=":", label="Interpolarea - 100 puncte")
    plt.scatter(x_client, y_client, color="red", label="Puncte client")  # Afisarea interpolarii
    plt.title("Metoda directa de interpolare Lagrange")
    plt.grid()
    plt.axvline(0, color='black')
    plt.axhline(0, color='black')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()

    # Punctul d
    """
    Eroarea de interpolare se calculeaza element wise ca diferenta intre vectorul aprox(calculat prin 
    metoda interpolarii) si valorile functiei f in punctele intervalului [-pi, pi] (cele 100 de puncte echidistante)
    """
    plt.figure(1)
    eroare = np.abs(aprox - y)
    plt.plot(x, eroare, label="Eroarea de interpolare - ex1 d")  # Afisarea graficului erorii de interpolare
    plt.legend()
    plt.axvline(0, color='black')
    plt.axhline(0, color='black')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.show()


def ex2():
    # Punctul a
    x_client = np.linspace(-np.pi, np.pi, 20)
    y_client = f(x_client)
    plt.figure(0)
    plt.plot(x_client, y_client, label="Datele clientului - 20 de puncte - ex2 a")
    plt.grid()
    plt.axvline(0, color='black')
    plt.axhline(0, color='black')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()

    # Punctul b si c

    aprox = np.zeros(100)
    x = np.linspace(-np.pi, np.pi, 100)
    y = f(x)
    for i in range(100):
        aprox[i] = interp_lagrange(x_client, y_client, x[i])

    plt.figure(1)
    plt.plot(x, y, label="Datele clientului - 100 puncte")
    plt.plot(x, aprox, linestyle=":", label="Interpolarea - 100 puncte")
    plt.scatter(x_client, y_client, color="red", label="Puncte client")
    plt.title("Metoda Lagrange de interpolare Lagrange")
    plt.grid()
    plt.axvline(0, color='black')
    plt.axhline(0, color='black')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()

    # Punctul d
    plt.figure(1)
    eroare = np.abs(aprox - y)
    plt.plot(x, eroare, label="Eroarea de interpolare - ex2 d")
    plt.legend()
    plt.axvline(0, color='black')
    plt.axhline(0, color='black')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.show()


def ex3():
    # Punctul a
    x_client = np.linspace(-np.pi, np.pi, 20)
    y_client = f(x_client)
    plt.figure(0)
    plt.plot(x_client, y_client, label="Datele clientului - 20 de puncte - ex3 a")
    plt.grid()
    plt.axvline(0, color='black')
    plt.axhline(0, color='black')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()

    # Punctul b si c

    aprox = np.zeros(100)
    x = np.linspace(-np.pi, np.pi, 100)
    y = f(x)
    for i in range(100):
        aprox[i] = interp_newton(x_client, y_client, x[i])

    plt.figure(1)
    plt.plot(x, y, label="Datele clientului - 100 puncte")
    plt.plot(x, aprox, linestyle=":", label="Interpolarea - 100 puncte")
    plt.scatter(x_client, y_client, color="red", label="Puncte client")
    plt.title("Metoda Newton de interpolare Lagrange")
    plt.grid()
    plt.axvline(0, color='black')
    plt.axhline(0, color='black')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()

    # Punctul d
    plt.figure(1)
    eroare = np.abs(aprox - y)
    plt.plot(x, eroare, label="Eroarea de interpolare - ex3 d")
    plt.legend()
    plt.axvline(0, color='black')
    plt.axhline(0, color='black')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.show()


def ex4():
    # Punctul a
    x_client = np.linspace(-np.pi, np.pi, 20)
    y_client = f(x_client)
    plt.figure(0)
    plt.plot(x_client, y_client, label="Datele clientului - 20 de puncte - ex4 a")
    plt.grid()
    plt.axvline(0, color='black')
    plt.axhline(0, color='black')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()

    # Punctul b si c

    aprox = np.zeros(100)
    x = np.linspace(-np.pi, np.pi, 100)
    y = f(x)
    for i in range(100):
        aprox[i] = interp_newton_dd(x_client, y_client, x[i])

    plt.figure(1)
    plt.plot(x, y, label="Datele clientului - 100 puncte")
    plt.plot(x, aprox, linestyle=":", label="Interpolarea - 100 puncte")
    plt.scatter(x_client, y_client, color="red", label="Puncte client")
    plt.title("Metoda Newton cu diferente divizate de interpolare Lagrange")
    plt.grid()
    plt.axvline(0, color='black')
    plt.axhline(0, color='black')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()

    # Punctul d
    plt.figure(1)
    eroare = np.abs(aprox - y)
    plt.plot(x, eroare, label="Eroarea de interpolare - ex4 a")
    plt.legend()
    plt.axvline(0, color='black')
    plt.axhline(0, color='black')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.show()


if __name__ == '__main__':
    ex1()
    # ex2()
    # ex3()
    # ex4()
