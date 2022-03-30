import numpy as np


# Metoda Substitutiei Descendente
def subs_desc(A, b):
    """
    A (numpy square matrix) = Matrice superior triunghiulara.
    b (numpy column vector) = Coloana termenilor liberi.
    """

    # Verifica daca A este matrice patratica
    assert np.shape(A)[0] == np.shape(A)[1], "Matricea A nu este patratica"

    # Verifica daca A este superior triunghiulara
    assert np.all(np.triu(A)==A), "Matricea A nu este superior triunghiulara"

    # Verifica daca A si vectorul b sunt compatibili
    assert np.shape(A)[1] == np.shape(b)[0], "Matricea A si vectorul b nu sunt compatibili"

    # Verifica daca A este inversabila
    assert np.product(np.diag(A)) != 0, "Matrice A nu este inversabila"

    n = np.shape(A)[0]  # Salvam in variabila 'n' dimensiunea matricei
    x = np.zeros(n).astype(np.float32)  # Initializeaza vectorul x ca vector coloana numpy

    for i in range(n-1, -1, -1):
        x[i] = (b[i] - A[i, i+1:] @ x[i+1:]) / A[i, i]

    # x (numpy column vector) = Solutia sistemului.
    return x


# Metoda de eliminare Gauss fara pivotare
def meg_fp(A, b):
    """
    A (numpy square matrix): Matricea sistemului.
    b: (numpy column vector): Coloana termenilor liberi.
    """

    # Verifica daca A este patratica
    assert np.shape(A)[0] == np.shape(A)[1], "Matricea A nu este patratica"

    # Verifica daca A si b sunt compatibili
    assert np.shape(A)[0] == np.shape(b)[0], "Matricea A si vectorul b nu sunt compatibili"

    # Verifica daca A este inversabila
    assert np.prod(np.diag(A)) != 0, "Matricea A nu este inversabila"

    # Pasul 1
    E = np.concatenate((A, b), axis=1)

    # Numarul de linii/coloane (pentru identarea in python)
    n = np.shape(A)[0]  # Cu '1' mai putin pentru ca in numpy plecam de la 0

    # Pasul 2
    for i in range(n-1):
        # Pasul 3 (aflam pozitia pivotului de pe coloana k)
        if not E[i:, i].any():  # Verifica daca sunt zerouri in vectorul de sub pivot (inclusiv)
            raise AssertionError('Sistem incompatibil sau compatibil determinat!')
        else:
            p = np.argmin(E[i:, i] == 0)  # Pozitia primului element nenul din slice-ul coloanei i
            p += i  # Ne intereseaza linia din matricea 'a'. Pozitia 'p' este cea din slice. Compensam cu numarul de

        # Pasul 4 (schimba linia 'i' cu 'p' daca pivotul nu se afla pe diagonala principala)
        if p != i:
            """ a[[j, k], :] = a[[k, j], :] -> Rocada intre linia 'j' si 'k'. """
            E[[p, i], :] = E[[i, p], :]

        # Pasul 5 (zero pe coloana sub pozitia pivotului)
        for j in range(i+1, n):
            # Pasul 6
            m = E[j, i] / E[i, i]

            # Pasul 7
            E[j, :] -= m * E[i, :]

    # Pasul 8 (verifica si ultimul element de pe diagonala principala daca este zero)
    if E[-1, -1] == 0:
        raise AssertionError('Nu exista solutie unica!')

    # Pasul 9 (gaseste solutia numerica folosind metoda substitutiei descendente)
    x = subs_desc(E[:, :-1], E[:, -1])

    # Pasul 10
    return x  # x (numpy column vector): Solutia sistemului.


# Metoda de eliminare Gauss cu pivotare partiala
def meg_pp(A, b):
    """
    A (numpy square matrix): Matricea sistemului.
    b: (numpy column vector): Coloana termenilor liberi.
    """

    # Verifica daca A este patratica
    assert np.shape(A)[0] == np.shape(A)[1], "Matricea A nu este patratica"

    # Verifica daca A si b sunt compatibili
    assert np.shape(A)[0] == np.shape(b)[0], "Matricea A si vectorul b nu sunt compatibili"

    # Verifica daca A este inversabila
    assert np.prod(np.diag(A)) != 0, "Matricea A nu este inversabila"

    # Pasul 1
    E = np.concatenate((A, b), axis=1)
    n = np.shape(A)[0]

    # Pasul 2
    for i in range(n-1):
        # Pasul 3
        if not A[i:, i].any():
            raise AssertionError('Nu exista solutie unica!')
        else:
            p = np.argmax(A[i:, i] == 0)
            p += i

        # Pasul 4
        if p != i:
            E[[p, i], :] = E[[i, p], :]

        # Pasul 5
        for j in range(i+1, n):
            # Pasul 6
            m = E[j, i] / E[i, i]

            # Pasul 7
            E[j, :] -= m * E[i, :]

    # Pasul 8
    if E[-1, -1] == 0:
        raise AssertionError('Nu exista solutie unica!')

    # Pasul 9
    x = subs_desc(E[:, :-1],E[:, -1])

    # Pasul 10
    return x  # x (numpy column vector): Solutia sistemului.


# Metoda Substitutiei Ascendente
def subs_asc(A, b):
    """
    A (numpy square matrix) = matrice inferior triunghiulara
    b (numpy column vector) = coloana termenilor liberi
    """

    # Verifica daca A este patratica
    assert np.shape(A)[0] == np.shape(A)[1], "Matricea A nu este patratica"

    # Verifica daca a este inferior triunghiulara
    assert np.allclose(np.tril(A),A), "Matricea A nu este inferior triunghiulara"

    # Verifica daca A si vectorul b sunt compatibi
    assert np.shape(A)[0] == np.shape(b)[0], "Matricea A si vectorul b nu sunt compatibili"

    # Verifica daca A este inversabila
    assert np.prod(np.diag(A)) != 0, "Matricea A nu este inversabila"

    n = np.shape(A)[0]  # Salvam in variabila n dimensiunea matricei
    x = np.zeros(n)  # Initializeaza vectorul x ca vector coloana numpy

    for i in range(n):
        x[i] = (b[i] - A[i, :n-1] @ x[:n-1]) / A[i, i]

    return x  # x (numpy column vector) = solutia sistemului


# Factorizarea LU (Metoda Gauss cu pivotare partiala)
def fact_lu(A):

    # Verifica daca A este patratica
    assert np.shape(A)[0] == np.shape(A)[1], "Matricea A nu este patratica"

    # Verifica daca A este inversabila
    assert np.linalg.det(A) != 0, "Matricea A nu este inversabila"

    n = np.shape(A)[0]  # Salvan numarul de linii/coloane in variabila n

    # Pasul 1
    L = np.eye(n)
    w = np.array(range(n))

    # Pasul 2
    for i in range(n-1):
        # Pasul 3
        if np.abs(np.max(A[i:, i])) > 0:  # Verifica daca sunt zerouri in vectorul de sub pivot (inclusiv) (incepand cu pivotul, in jos)
            p = np.argmax(A[i:, i])   # Pozitia primului element nenul din slice-ul coloanei i
            p += i  # Ne intereseaza linia din matricea 'a'. Pozitia 'p' este cea din slice. Compensam cu numarul de
        else:
            raise AssertionError('Matricea A nu admite factorizare LU!')

        # Pasul 4
        if p != i:
            A[[p, i], :] = A[[i, p], :]  # Schimba linia 'i' cu linia 'p'
            w[[p, i]] = w[[i, p]]  # Memoreaza schimbarea de mai sus

            # Pasul 5
            if i != 0:
                L[[p, i], :i] = L[[i, p], :i]  # Schimbarea subliniilor 'i' si 'p' din matricea L

        # Pasul 6
        for j in range(i+1, n):
            # Pasul 7
            L[j, i] = A[j, i] / A[i, i]  # Salvarea multiplicatorilor in matricea L

            # Pasul 8
            A[j, :] = A[j, :] - L[j, i] * A[i, :]  # Zero sub pivot, pe coloana

    # Pasul 9
    if A[-1, -1] == 0:  # Extra-verificare daca matricea are rang maxim!
        raise AssertionError('Matricea A nu admite factorizare LU!')

    # Pasul 10
    U = A  # Salveaza in variabila 'U' matricea 'A'

    # Pasul 11  # Returnarea variabilelor cerute
    return L, U, w


# Factorizarea QR (Metoda Givens)
def fac_qr(A):

    # Verifica daca A este patratica
    assert np.shape(A)[0] == np.shape(A)[1], "Matricea A nu este patratica"

    # Verifica daca A este inversabila
    assert np.linalg.det(A) != 0, "Matricea A nu este inversabila"

    n = np.shape(A)[0]  # Salvan numarul de linii/coloane in variabila n

    # Pasul 1
    Q = np.eye(n)

    # Pasul 2
    for i in range(n):
        # Pasul 3
        for j in range(i+1, n):
            sigma = np.sqrt(A[i, i]*A[i, i] + A[j, i]*A[j, i])
            c = A[i, i]/sigma
            s = A[j, i]/sigma

            # Pasul 4
            for k in range(n):
                u = c*A[i, k] + s*A[j, k]
                v = -s*A[i, k] + c*A[j, k]
                A[i, k] = u
                A[j, k] = v

                u = c*Q[i, k] + s*Q[j, k]
                v = -s*Q[i, k] + c*Q[j, k]
                Q[i, k] = u
                Q[j, k] = v

    # Pasul 5
    R = A
    Q = Q.T

    # Pasul 6
    return Q, R



def ex_subs_asc():
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

    x_aprox = subs_asc(A,b)
    print(f'Am implementat corect Metoda Substitutiei Ascendente? {x_aprox}')


def ex_fac_lu():
    A = np.array([
        [3, 0, 1],
        [-4, 1, 2],
        [1, 4, 1]
    ]).astype(np.float32)

    b = np.array([
        [18],
        [76],
        [4]
    ]).astype(np.float32)


    L,U,w = fact_lu(A)
    b_prim = b[w]
    print(f'{L} \n\n {U}')
    y = subs_asc(L,b_prim)
    x_aprox = subs_desc(U,y)

    print(f'Am implementat corect factorizarea LU? {x_aprox}')


def ex_fac_qr():
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


    Q,R = fac_qr(A)
    print(f'{Q}\n\n {R}')
    x_aprox = subs_desc(R,Q.T@b)
    print(f'Am implementat corect Factorizarea QR? {x_aprox}')


def ex_meg_pp():
    A = np.array([
        [2,3,0],
        [3,4,2],
        [1,3,1]
    ]).astype(np.float32)

    b = np.array([
        [8],
        [17],
        [10]
    ]).astype(np.float32)

    x = meg_pp(A,b)
    print(x)


if __name__ == '__main__':
    ex_subs_asc()
    # ex_fac_lu()
    # ex_fac_qr()
    # ex_meg_pp()
