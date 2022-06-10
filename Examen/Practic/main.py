"""
Universitatea din Bucuresti
Facultatea de Matematica si Informatica
Domeniul Calculatoare si Tehnologia Informatiei

Examen Calcul Numeric - Proba practica
Data: 18.06.2021
Student: Cretu Laurentiu-Vasile
Grupa: 161
"""

# Librariile folosite
import numpy as np  # pentru array-uri si operatii cu acestia
import matplotlib.pyplot as plt  # pentru grafice
from scipy.integrate import quad # pentru calculul integralei


# Metoda Romberg - exercitiul 1
def int_romberg(a, b, f, n):
    # Pasul 1
    h = np.abs(b - a)  # Determina lungimea intervalului

    # Pasul 2
    Q = np.zeros((n, n))  # Creeaza matricea Q de lungime (n,n)
    Q[0, 0] = h/2. * (f(a) + f(b))  # Formula trapezului

    for i in range(1, n):
        # Calculam suma separat
        putere = 2**i  # 2^i deoarece i pleaca de la 1, nu de la 2 ca in algoritm
        suma = 0
        for k in range(1, putere):
            suma += f(a + k * h/putere)

        Q[i, 0] = h/(2**(i+1)) * (f(a) + 2*suma + f(b))  # 2^(i+1) deoarece i pleaca de la 1, nu de la 2

    for i in range(1, n):
        for j in range(1, i+1):
            Q[i, j] = (4**j * Q[i, j-1] - Q[i-1, j-1]) / (4**j - 1)  # 4^j deoarece j pleaca de la 1, nu de la 2 ca si in algoritm

    # Pasul 3
    I = Q[-1,-1]

    # Pasul 4
    return I


# Functia de la exercitiul 1
def func1(x):
    y = 1/(1+x**2)
    return y


# Exercitiul 1
def ex1():
    # Punctul b - calculul integralei exacte cu ajutorul librariei scimpy
    a = -6
    b = 6
    I_exact, error = quad(func1, a, b)  # calculeaza integrala exacta, iar in variabila error se retine eroarea de calcul
    print('Exercitiul 1\n')
    print(f'Integrala exacta este I = {I_exact:.6f}')

    # Punctul c - calculul integralei cu metoda Romberg
    n = 4
    I_aprox = int_romberg(a, b, func1, n)  # calculeaza aproximarea integralei folosind metoda Romberg
    print(f'Integrala calculata cu metoda Romberg este I = {I_aprox:.6f}')

    # Punctul d - calculul erorii
    e = np.abs(I_exact - I_aprox)
    print(f'Eroarea este e = {e:.6f}\n\n')


# Metoda Lagrange de interpolare Lagrange
def interp_lagrange(X, Y, z):
    # Pasul 1
    n = np.shape(X)[0] - 1  # Stocheaza in n dimensiunea vectorului X
    L = np.zeros(n+1)  # Creaza un vector L de dimensiune n+1

    for k in range(n+1):
        produs = 1
        for j in range(n+1):
            # Verific daca k!=j
            if k != j:
                produs *= (z-X[j]) / (X[k] - X[j])
        L[k] = produs

    # Pasul 2
    t = L[:] @ Y[:]  # Determina aproximarea in punctul z

    # Pasul 3
    return t


# Functia de la exercitiul 2
def func2(x):
    y = np.cos(2*x)
    return y


# Exercitiul 2
def ex2():
    # Punctul b - generare date si afisare la consola
    x_cunoscut = np.linspace(0, np.pi, 21)  # discretizarea intervalului
    y_cunoscut = func2(x_cunoscut)
    print('Exercitiul 2\n')
    print(f'X cunoscut este {x_cunoscut} \n\n Y cunoscut este {y_cunoscut}')

    # Punctul c - generare grafic date cunoscute
    plt.figure(0)
    plt.scatter(x_cunoscut,y_cunoscut,label='Date cunoscute',color='black')
    plt.title('Grafic exercitiul 2 punctul c+e')
    plt.axhline(0,color='black')
    plt.axvline(0,color='black')
    plt.xlabel('Ox')
    plt.ylabel('Oy')
    # Nu afisez graficul deoarece il voi continua la punctul e

    # Punctul d
    x_aprox = np.linspace(0, np.pi, 110)
    y_aprox = func2(x_aprox)
    y_lagrange = np.zeros(110)

    # Calculez interpolarea
    for z in range(110):
        y_lagrange[z] = interp_lagrange(x_cunoscut, y_cunoscut, x_aprox[z])

    # Punctul e
    plt.plot(x_aprox, y_aprox, label='Functia exacta', color='green')  # Graficul functiei exacte
    plt.plot(x_aprox, y_lagrange, label='Aproximarea Lagrange', color='crimson', linestyle=':')  # Graficul interpolarii
    plt.grid()
    plt.legend()
    plt.show()

    # Punctul f
    eroare = np.abs(y_aprox - y_lagrange)  # Eroarea de interpolare
    plt.figure(1)
    plt.plot(x_aprox, eroare, label='Eroarea de interpolare', color='orange')
    plt.title('Grafic exercitiul 2 punctul f')
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.xlabel('Ox')
    plt.ylabel('Oy')
    plt.grid()
    plt.legend()
    plt.show()


if __name__ == '__main__':
    ex1()
    ex2()
