import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative


# Metoda Bisectiei

def bisectie(f, a, b, epsilon):
    """
    a (float): Capatul din stanga al intervalului.
    b (float): Capatul din dreapta al intervalului.
    f (functie): Functia pentru care se va aplica metoda.
    epsilon (float): Eroarea acceptata.
    """

    # Verifica daca capatul din stanga este mai mic decat cel din dreapta
    assert a < b, "Interval ales necorespunzator"

    # Pasul 1

    # Numarul de pasi necesari pentru a atinge eroarea acceptata
    N = np.int32(np.floor(np.log2((b-a)/epsilon)))

    # Prima aproximare
    x_aprox = (a+b) / 2.

    # Pasul 2
    for _ in range(1, N):  # Variabila '_' nu este folosita
        if f(x_aprox) == 0:  # Verifica daca prima aproximare reprezinta solutia
            break  # Intrerupe bucla 'for'
        elif np.sign(f(a)) * np.sign(f(x_aprox)) < 0:  # Este folosit doar semnul valorilor
            b = x_aprox  # Restrange intervalul -> Muta capatul b
        elif np.sign(f(a)) * np.sign(f(x_aprox)) > 0:
            a = x_aprox  # Restrange intervalul -> Muta capatul a
        x_aprox = (a+b)/2.  # Actualizeaza aproximarea

    """
    x_aprox (float): Solutia numerica.
    N (int): Numarul de iteratii.
    """
    return x_aprox, N


# Metoda Newton Raphson

def newton_raphson(f, df, x0, epsilon, N):
    """
    f (function): Functia pentru care dorim solutia.
    df (function): Derivata functiei pentru care dorim solutia
    x0 (float): Aproximarea initiala a solutiei.
    epsilon (float): Toleranta erorii
    N (int): Numarul maxim de iteratii admis.
    """

    # Pasul 1
    i = 1  # Contorul iteratiilor

    # Pasul 2
    while i <= N:
        # Pasul 3
        x1 = x0 - f(x0)/df(x0)  # Actualizeaza aproximarea
        # Pasul 4
        if np.abs(x1-x0) < epsilon:
            """
            Daca este indeplinita conditia 'if'-ului de mai sus functie returneaza x1 si i 
            si se iese din body-ul functiei.
            """

            """
            x1 (float): Aproximarea solutiei
            i (int): Numarul de iteratii
            """
            return x1, i

        # Pasul 5
        i += 1

        # Pasul 6
        x0 = x1  # Inverseaza valorile aproximarilor pentru a avea sens formula din bucla while

    # Pasul 7
    print(f'Metoda N-R nu a atins convergenta dupa {i+1} iteratii.')
    sys.exit(1)  # Opreste script-ul si returneaza exit code 1 -> Au fost erori in rulare.


# Metoda Secantei

def secanta(f, x0, x1, epsilon, N):
    """
    f (function): Functia pentru care dorim solutia.
    x0 (float): Una din aproximarile initiale.
    x1 (float): Una din aproximarile initiale.
    epsilon (float): Toleranta maxima a erorii
    N (int): Numarul maxim de iteratii admis.
    """
    # Pasul 1
    i = 2  # Initializeaza contorul iteratiilor (2 pentru ca avem deja doua aproximari)
    y0 = f(x0)
    y1 = f(x1)

    # Pasul 2
    while i <= N:
        # Pasul 3
        x_star = x1 - y1*(x1-x0)/(y1-y0)

        # Pasul 4
        if np.abs(x_star-x1) < epsilon:
            """
            x_star (float): Aproximarea solutiei
            i (int): Numarul de iteratii
            """
            return x_star, i

        # Pasul 5
        i += 1

        # Pasul 6
        x0 = x1
        y0 = y1
        x1 = x_star
        y1 = f(x_star)

    # Pasul 7
    print(f'Metoda Secantei nu a atins convergenta dupa {i} iteratii.')
    sys.exit(1)


# Metoda Pozitiei false

def pozitie_falsa(f, x0, x1, epsilon, N):
    """
    f (function): Functia pentru care dorim solutia.
    x0 (float): Una din aproximarile initiale.
    x1 (float): Una din aproximarile initiale.
    epsilon (float): Toleranta maxima a erorii
    N (int): Numarul maxim de iteratii admis.
    """
    # Pasul 1
    i = 2
    y0 = f(x0)
    y1 = f(x1)

    # Pasul 2
    while i <= N:
        # Pasul 3
        x_star = x1 - y1*(x1-x0)/(y1-y0)

        # Pasul 4
        if np.abs(x_star-x1) < epsilon:
            """
            x_star (float): Aproximarea solutiei
            i (int): Numarul de iteratii
            """
            return x_star, i

        # Pasul 5
        i += 1
        y_star = f(x_star)

        # Pasul 6
        if y_star * y1 < 0:
            x0 = x1
            y0 = y1

        # Pasul 7
        x1 = x_star
        y1 = y_star

    # Pasul 8
    print(f'Metoda Pozitiei False nu a atins convergenta dupa {i} iteratii.')
    sys.exit(1)


# Functie exemplu

def f(x):
    y = -x**3 - 2 * np.cos(x)
    return y


# Derivata functiei

def df(x):
    """
    Calculam derivata cu ajutorul functiei derivative() din pachetul scipy.misc
    Pentru instalare, urmariti instructiunile din tutoriatul 2, difera doar numele pachetului
    Also, puteti calcula derivata si de mana :)
    """
    y = derivative(f, x)
    return y


# Functie de trasare a graficelor

def draw_graphic(interval, points, functions, metoda=None):
    """
    interval (list): Lista cu doua valori, continand capetele intervalului pe care dorim plot-area.
    points (list): Lista care contine obiecte de tip tuplu. Fiecare tuplu are doua pozitii. Pe prima pozitie se
                   afla un numar de tip float, reprezentand coordonata in x a solutiei gasite pentru functia
                   studiata. Metoda este 'hard-codata' in sensul ca valoarea in y a punctului este data drept 0.
                   Acest lucru este fortat pentru a afisa punctul fix pe axa OX.
    functions (list): Lista care contine obiecte de tip tuplu. Fiecare tuplu are doua pozitii. Pe prima pozitie
                      se afla referinta catre functie pe care dorim sa o afisam. Pe a doua pozitie se afla
                      un str care va fi folosit in legenda graficului.
    metoda (str): Titlul figurii
    """

    plt.figure(0)  # Initializeaza figura

    if points is not None:  # Verifica daca avem puncte de afisat.
        for x in points:
            plt.scatter(x[0], 0, label=x[1])  # Afiseaza punctul in figura.

    for func in functions:
        """ Itereaza prin fiecare tuplu din lista si afiseaza graficul fiecarei functii in figura. 
            Pune, totodata si label-ul care va fi afisat in legenda.
        """
        domain = np.linspace(interval[0], interval[1], 100)  # Discretizarea domeniului in 50 de puncte
        func = func[0](domain)  # Valorile functiei in punctele din domeniu.
        plt.plot(domain, func, label=func[1])

    plt.axvline(0, color='black')  # Afiseaza axa OX
    plt.axhline(0, color='black')  # Afiseaza axa OY
    plt.xlabel('points')  # Afiseaza label pe axa OX
    plt.ylabel('values')  # Afiseaza label pe axa OY

    if metoda:  # Verifica daca avem titlul setat
        plt.title(metoda.upper(), color='darkred')  # Afiseaza titlul

    plt.legend()  # Afiseaza legenda
    plt.grid()  # Afiseaza grid
    plt.show()  # Afiseaza graficul


# Functie exemplu pentru Metoda Bisectiei

def ex_bisectie():
    a = -3  # Capatul din stanga al intervalului
    b = 3  # Capatul din dreapta al intervalului
    epsilon = 10e-6  # 1e-6 -> 10**(-6). Eroarea maxima acceptata
    x_aprox, steps = bisectie(f=f, a=a, b=b, epsilon=epsilon)  # Apelarea functiei
    print(f'Solutia ecuatiei f(x)=0 este {x_aprox:.5f} gasita in {steps} pasi')  # Afisarea solutiei si a numarului de pasi

    draw_graphic(interval=[a,b],
                 points=[(a,'a'), (b,'b'), (x_aprox, 'x_aprox')],
                 functions=[(f,'f(x)')],
                 metoda="metoda bisectiei")


# Functie exemplu pentru Newton Raphson

def ex_newton_raphson():
    x0 = -3
    epsilon = 10e-6
    N = 1000
    x_aprox, steps = newton_raphson(f, df, x0, epsilon, N)
    print(f'Metoda Newton-Raphson are solutia {x_aprox:.5f} gasita dupa {steps} iteratii')

    draw_graphic(interval=[-3, 3],
                 points=[(x_aprox, 'x_aprox')],
                 functions=[(f, 'f(x)'), (df, "f'(x)")],
                 metoda="metoda newton raphson")


# Functie exemplu pentru Metoda Secantei

def ex_secanta():
    x0 = -1.6
    x1 = -1.4
    N = 1000
    epsilon = 10e-6
    x_aprox, steps = secanta(f, x0, x1, epsilon, N)
    print(f'Solutia ecuatiei calculata cu Metoda Secantei este {x_aprox:.5f} gasita in {steps} pasi')

    draw_graphic(interval=[-3, 3],
                 points=[(x_aprox, 'x_aprox')],
                 functions=[(f, 'f(x)')],
                 metoda="metoda secantei")


# Functie exemplu pentru Metoda Pozitiei False

def ex_pozitie_falsa():
    x0 = -1.6
    x1 = -1.4
    N = 1000
    epsilon = 10e-6
    x_aprox, steps = pozitie_falsa(f, x0, x1, epsilon, N)
    print(f'Solutia ecuatiei calculata cu Metoda Pozitiei False este {x_aprox:.5f} gasita in {steps} pasi')

    draw_graphic(interval=[-3, 3],
                 points=[(x_aprox, 'x_aprox')],
                 functions=[(f, 'f(x)')],
                 metoda="metoda falsei pozitii")


if __name__ == '__main__':
    ex_bisectie()
    # ex_newton_raphson()
    # ex_secanta()
    # ex_pozitie_falsa()
