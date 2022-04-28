import numpy as np
from scipy.integrate import quad


# Cuadratura dreptunghiului
def int_drept(a, b, f):
    # Pasul 1
    h = b-a

    # Pasul 2
    I = h * f((a+b)/2.)

    # Pasul 3
    return I


# Cuadratura trapezului
def int_trap(a, b, f):
    # Pasul 1
    h = b - a

    # Pasul 2
    I = h/2. * (f(a) + f(b))

    # Pasul 3
    return I


# Cuadratura Simpson
def int_simp(a, b, f):
    # Pasul 1
    h = b - a

    # Pasul 2
    I = h/6. * (f(a) + 4*f((a+b)/2.) + f(b))

    # Pasul 3
    return I


# Functie exemplu ex1
def func1(x):
    y = 3*x / (x**2 - 9.)
    return y


# Exercitiul 1
def ex1():
    # Punctul a
    a = 4
    b = 5
    I_exact, error = quad(func1, a, b)  # Valoarea exacta a integralei
    """
    Puteti calcula integrala exacta fie cu functia de mai sus, fie de mana :)
    """
    print(f'Integrala exacta este I = {I_exact:.6f}')

    # Punctul b
    I_int_drep = int_drept(a, b, func1)  # dreptunghi
    I_int_trap = int_trap(a, b, func1)  # trapez
    I_int_simp = int_simp(a, b, func1)  # simpson

    # Afisarea rezultatelor
    print(f'Integrala calculata cu cuadratura dreptunghiului este I = {I_int_drep:.6f}')
    print(f'Integrala calculata cu cuadratura trapezului este I = {I_int_trap:.6f}')
    print(f'Integrala calculata cu cuadratura simpson este I = {I_int_simp:.6f}')

    # Punctul c
    eroare_int_drep = np.abs(I_exact-I_int_drep)  # eroare dreptunghi
    eroare_int_trap = np.abs(I_exact-I_int_trap)  # eroare trapez
    eroare_int_simp = np.abs(I_exact-I_int_simp)  # eroare simpson

    # Afisarea erorilor
    print(f'\nEroarea cuadraturii dreptunghiului este e = {eroare_int_drep:.6f}')
    print(f'Eroarea cuadraturii trapezului este e = {eroare_int_trap:.6f}')
    print(f'Eroarea cuadraturii simpson este e = {eroare_int_simp:.6f}')


# Cuadratura sumata a dreptunghiului
def int_sum_drept(f, X):
    # Pasul 1
    m = np.int32((np.shape(X)[0] - 1)/2.)
    h = (X[2*m] - X[0]) / (2.*m)

    # Pasul 2
    suma = 0
    for i in range(m):
        suma += f(X[2*i])
    I = 2*h*suma

    # Pasul 3
    return I


# Cuadratura sumata a trapezului
def int_sum_trap(f, X):
    # Pasul 1
    m = np.shape(X)[0] - 1
    h = (X[m] - X[0]) / m

    # Pasul 2
    I = h/2. * (f(X[0]) + 2*np.sum(X[1:]) + f(X[-1]))

    # Pasul 3
    return I


# Cuadratura sumata Simpson
def int_sum_simp(f, X):
    # Pasul 1
    m = np.int32((np.shape(X)[0]-1)/2.)
    h = (X[-1] - X[0]) / (2.*m)

    # Pasul 2
    suma1 = suma2 = 0
    for i in range(m):
        suma1 += f(X[2*i])

    for i in range(m-1):
        suma2 += f(X[2*i+1])

    I = h/3. * (f(X[0]) + 4*suma1 + 2*suma2 + f(X[-1]))

    # Pasul 3
    return I


# Functie exemplu ex2
def func2(x):
    y = 1/(1+x)
    return y


# Exercitiul 2
def ex2():
    # Punctul a
    a = 0
    b = 1
    I_exact, error = quad(func2, a, b)  # Valoarea exacta a integralei
    print(f'Integrala exacta este I = {I_exact:.6f}')

    # Punctul b
    for m in [3, 4, 5]:
        x_drep_sum = np.linspace(a, b, 2*m+1)  # 2m+1 luat din algoritm X apartine R^(2m+1)
        x_trap = np.linspace(a, b, m+1)   # m+1 luat din algoritm X apartine R^(m+1)

        I_sum_drept = int_sum_drept(func2, x_drep_sum)  # sumata dreptunghi
        I_sum_trap = int_sum_trap(func2, x_trap)  # sumata trapez
        I_sum_simp = int_sum_simp(func2, x_drep_sum)  # sumata simpson

        # Afisarea rezultatelor
        print(f'\nIntegrala calculata cu cuadratura sumata a dreptunghiului pentru m = {m} este I = {I_sum_drept:.6f}')
        print(f'Integrala calculata cu cuadratura sumata a trapezului pentru m = {m} este I = {I_sum_trap:.6f}')
        print(f'Integrala calculata cu cuadratura sumata simpson pentru m = {m} este I = {I_sum_simp:.6f}')

    print('\n\n')
    # Punctul c
    for m in [3, 4, 5]:
        eroare_sum_drep = np.abs(I_exact-I_sum_drept)  # eroare sumata dreptunghi
        eroare_sum_trap = np.abs(I_exact-I_sum_trap)  # eroare sumata trapez
        eroare_sum_simp = np.abs(I_exact-I_sum_simp)  # eroare sumata simpson

        # Afisarea erorilor
        print(f'\nEroarea cuadraturii sumate a dreptunghiului pentru m = {m} este e = {eroare_sum_drep:.6f}')
        print(f'Eroarea cuadraturii sumate a trapezului pentru m = {m} este e = {eroare_sum_trap:.6f}')
        print(f'Eroarea cuadraturii sumate simpson pentru m = {m} este e = {eroare_sum_simp:.6f}')


if __name__ == '__main__':
    # ex1()
    ex2()
