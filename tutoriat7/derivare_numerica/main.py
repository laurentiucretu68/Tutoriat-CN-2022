import numpy as np
import matplotlib.pyplot as plt


def deriv_num(X, Y, method):
    """
    X: X = [X0, X1, ..., Xn+1]
    Y: [Y0=f(X0), Y1=f(X1), ..., Yn+1=f(Xn+1)]
    metoda (str): Varianta a diferentelor finite ce urmeaza a fi folosita.

    Fiecare lista contine pozitiile vectorilor reprezentati.
    Pentru exemplul nostru [-1-.5 .5 1]
    domain = [0, 1, 2, 3]
    X = [0, 1, 2, 3, 4, 5]
    Y = [0, 1, 2, 3, 4, 5]
    df = [0, 1, 2, 3]
    """
    n = np.shape(X)[0] - 2 # sau len(X) - 2
    df = np.zeros(n)
    # Pasul 1
    if method.lower() == 'ascendente':
        # Pasul 2
        for i in range(1, n+1):
            df[i-1] = (Y[i+1] - Y[i]) / (X[i+1] - X[i])

    # Pasul 3
    if method.lower() == 'descendente':
        for i in range(1, n+1):
            # Pasul 4
            df[i-1] = (Y[i] - Y[i-1]) / (X[i] - X[i-1])

    # Pasul 5
    if method.lower() == 'centrale':
        # Pasul 6
        for i in range(1, n+1):
            df[i-1] = (Y[i+1] - Y[i-1]) / (X[i+1] - X[i-1])

    """
    df: df = [df0, df1, ..., dfn-1]. 
    Reprezinta aproximarea primei derivate pe domeniu cautat, fara punctele
    extra din stanga si dreapta.
    """
    # Pasul 7
    return df


def f(x):
    y = 5*np.sin(2*x) - 2*np.cos(3*x) + 11.5*x
    return y


# Derivata functiei
def df(x):
    dy = 10*np.cos(2*x) + 6*np.sin(3*x) + 11.5
    return dy


def ex1():
    """ Valorile exacte ale primei derivate ce sunt folosite
     pentru a putea compara aproximarea facuta pe grafic.
    """
    interval = [-1, 1]
    domain = np.linspace(interval[0], interval[-1], 100)
    dy_exact = df(domain)

    for N in [20, 40, 70]:
        # Punctul a

        # Discretizarea domeniului x cu puncte extra stanga-dreapta
        x = np.zeros(N+2)  # Vector in care se scrie discretizarea
        x[1:-1] = np.linspace(interval[0], interval[1], N)  # Scrierea slice-ului interior (fara puncte extra)
        h = x[3] - x[2]   # Distanta dintre doua puncte
        x[0] = x[1] - h  # Scriere capat extra stanga
        x[-1] = x[-2] + h  # Scriere capat extra dreapta

        y = f(x)  # Valorile functiei in discretizarea X de mai sus
        dfunc = df(x)  # Valorile derivatei in discretizarea X de mai sus

        # Vectori ce contin aproximarea primei derivate pe domeniu (fara puncte extra stanga-dreapta)
        dfunc_aprox_asc = deriv_num(x,y,method='ascendente')
        dfunc_aprox_desc = deriv_num(x,y,method='descendente')
        dfunc_aprox_cen = deriv_num(x,y,method='centrale')

        # Generare grafic pct a
        plt.figure(0)
        plt.plot(domain, dy_exact, label="Derivata exacta")
        plt.plot(x[1:-1], dfunc_aprox_asc, linewidth=1, linestyle="--", label="Diferente ascendente")
        plt.plot(x[1:-1], dfunc_aprox_desc, linewidth=1, linestyle="--", label="Diferente descendente")
        plt.plot(x[1:-1], dfunc_aprox_cen, linewidth=1, linestyle="--", label="Diferente centrale")
        plt.axvline(0, color='black')
        plt.axhline(0, color='black')
        plt.xlabel("x", color='black')
        plt.ylabel("y", color='black')
        plt.title(f"Pct a N = {N}")
        plt.legend()
        plt.grid()
        plt.show()

        # Punctul b
        # Generare grafic pct b
        plt.figure(1)
        plt.plot(x[1:-1], np.abs(dfunc[1:-1]-dfunc_aprox_asc), linestyle=":", label="Eroare Diferente ascendente")
        plt.plot(x[1:-1], np.abs(dfunc[1:-1]-dfunc_aprox_desc), linestyle="--", label="Eroare Diferente descendente")
        plt.plot(x[1:-1], np.abs(dfunc[1:-1]-dfunc_aprox_cen), linestyle="-.", label="Eroare Diferente centrale")
        plt.xlabel("x", color='black')
        plt.ylabel("y", color='black')
        plt.title(f"Pct b N = {N}")
        plt.legend()
        plt.grid()
        plt.show()


if __name__ == '__main__':
    ex1()
