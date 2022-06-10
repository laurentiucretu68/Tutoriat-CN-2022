"""
Universitatea din Bucuresti
Facultatea de Matematica si Informatica
Domeniul Calculatoare si Tehnologia Informatiei

Test Calcul Numeric
Data: 08.06.2021
Student: Cretu Laurentiu Vasile
Grupa: 161
"""

import numpy as np
import matplotlib.pyplot as plt


# Exercitiul 1 - metoda de rezolvare a ecuatiei x^2 - 17 = 0  => Metoda Bisectiei
def bisectie(f, a, b, epsilon):
    # Verificare
    assert a <= b, "Interval ales necorespunzator"

    # Pasul 1
    N = np.int32(np.floor(np.log2((b-a)/epsilon)))
    x_aprox = (a+b) / 2.

    # Pasul 2
    for _ in range(1, N):
        if f(x_aprox) == 0:
            break
        elif np.sign(f(a)) * np.sign(f(x_aprox)) < 0:
            b = x_aprox
        elif np.sign(f(a)) * np.sign(f(x_aprox)) > 0:
            a = x_aprox
        x_aprox = (a+b)/2.

    return x_aprox,N


# Functia de la exercitiul 1
def func1(x):
    y = x**2 - 17
    return y


def ex1():
    """Punctul a

    # Functia x^2 - 17 = 0 <=> x1 = sqrt(17) si x2 = -sqrt(17), unde sqrt reprezinta radicalul
    # Pentru acest tip de ecuatie este convenabila folosirea Metodei Bisectiei deoarece putem incadra foarte usor
    # pe sqrt(17) intr-un interval, respectiv -sqrt(17)
    # Am incadrat sqrt(17) in intervalul [4,5], respectiv -sqrt(17) in [-5,-4]"""

    a = np.floor(np.sqrt(17))  # Reprezinta capatul din stanga pentru primul interval
    b = np.ceil(np.sqrt(17))  # Reprezinta capatul din dreapta pentru primul interval
    epsilon = 10e-7  # Eroarea de calcul 10e^(-6)

    x, steps = bisectie(func1, a, b, epsilon)
    print(f'Solutiile ecuatiei sunt x1 = {x:.6f} si x2 = {-x:.6f} gasite cu Metoda Bisectiei dupa {steps} pasi')

    # Punctul b
    domain = np.linspace(-10, 10, 100)  # Discretizarea domeniului in 100 de puncte echidistante
    y_domain = func1(domain)
    plt.figure(0)
    plt.plot(domain, y_domain, label='f(x) = x^2 - 17')

    plt.scatter(x, 0, label="x1")
    plt.scatter(-x, 0, label="x2")

    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

    plt.xlabel("OX")
    plt.ylabel("OY")
    plt.title("Graficul functiei f(x) = x^2-17 - exercitiul 1c")
    plt.legend()
    plt.grid()
    plt.show()


# Implementarea algoritmului de la exeritiul 2 punctul a
def interp_neville(X, Y, z):
    # Pasul 1
    n = np.shape(X)[0]
    Q = np.zeros((n, n))
    Q[:, 0] = Y[:]

    for i in range(1, n):
        for j in range(1, i+1):
            Q[i, j] = (Q[i, j-1] * (z - X[i-j]) - Q[i-1][j-1] * (z - X[i])) / (X[i] - X[i-j])

    # Pasul 2
    t = Q[n-1, n-1]

    # Pasul 3
    return t


def func2(x):
    y = np.e ** (2*x)
    return y


def ex2():
    # Datele clientului - punctul a
    x_client = np.linspace(-1, 1, 23)
    y_client = func2(x_client)

    # Punctul b
    x_discret = np.linspace(-1, 1, 75)
    y_discret = func2(x_discret)

    x_aprox = np.zeros(75)
    for z in range(75):
        x_aprox[z] = interp_neville(x_client, y_client, x_discret[z])

    plt.figure(0)
    plt.scatter(x_client, y_client, label="Date client", color='black')
    plt.plot(x_discret, y_discret, label="Functia exacta", color='orange')
    plt.plot(x_discret, x_aprox, label="Aproximarea cu metoda Neville", linestyle=':', color='green')
    plt.title("Exercitiul 2b")
    plt.xlabel("Points")
    plt.ylabel("Domain")
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.grid()
    plt.legend()
    plt.show()


    # Punctul c - Generarea graficului erorii
    plt.figure(1)
    plt.plot(x_discret, np.abs(x_aprox-y_discret), label="Eroarea")
    plt.title("Exercitiul 2c - Eroarea")
    plt.xlabel("Points")
    plt.ylabel("Domain")
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.grid()
    plt.legend()
    plt.show()


def subs_desc(A,b):
    # Verifica daca A este matrice patratica
    assert np.shape(A)[0] == np.shape(A)[1], "Matricea A nu este patratica"

    # Verifica daca A este superior triunghiulara
    assert np.allclose(np.triu(A),A), "Matricea A nu este superior triunghiulara"

    # Verifica daca A si vectorul b sunt compatibili
    assert np.shape(A)[1] == np.shape(b)[0], "Matricea A si vectorul b nu sunt compatibili"

    # Verifica daca A este inversabile
    assert np.product(np.diag(A)) != 0, "Matrice A nu este inversabila"

    n = np.shape(A)[0]
    x = np.zeros(n).astype(np.float32)

    for i in range(n-1, -1, -1):
        x[i] = (b[i] - A[i, (i+1):] @ x[(i+1):]) / A[i, i]

    return x



def fact_qr_new(A):
    # Verificari

    # Verificare A este patratica
    assert np.shape(A)[0] == np.shape(A)[1], "Matricea A nu este patratica"

    # Verificare A este inversabila
    assert np.linalg.det(A) != 0, "Matricea A nu este inversabila"

    # Pasul 1
    n = np.shape(A)[0]
    Q = np.zeros((n, n))
    R = np.zeros((n, n))

    # r11
    suma = 0
    for i in range(n):
        suma += A[i, 0] * A[i, 0]
    R[0,0] = np.sqrt(suma)

    # qi1
    for i in range(n):
        Q[i, 0] = A[i, 0]/R[0, 0]

    # r1j
    for j in range(1, n):
        suma = 0
        for s in range(n):
            suma += Q[s, 0] * A[s, j]
        R[0, j] = suma


    # Pasul 2
    for k in range(1, n):
        # rkk
        suma1 = 0
        suma2 = 0
        for i in range(n):
            suma1 += A[i, k] * A[i, k]
        for s in range(k):
            suma2 += R[s, k] * R[s, k]
        R[k, k] = np.sqrt(suma1-suma2)

        # qik
        for i in range(n):
            suma = 0
            for s in range(k):
                suma += Q[i, s] * R[s, k]
            Q[i, k] = (A[i, k] - suma) / R[k, k]

        #rkj
        for j in range(k, n):
            suma = 0
            for s in range(n):
                suma += Q[s, k] * A[s, j]
            R[k, j] = suma


    # Pasul 3
    return Q, R



def ex3():
    A = np.array([
        [0, 1, 5, 1],
        [-10, 4, 0, 6],
        [4, -5, -10, -5],
        [1, 5, -7, 7]
    ]).astype(np.float32)

    b = np.array([
        [28],
        [22],
        [-72],
        [24]
    ]).astype(np.float32)

    Q, R = fact_qr_new(A)
    x_aprox = subs_desc(R, Q.T @ b)
    print(f'Solutia sistemului Ax=b gasita cu metoda QR este {x_aprox}')


if __name__ == '__main__':
    ex1()
    ex2()
    ex3()
