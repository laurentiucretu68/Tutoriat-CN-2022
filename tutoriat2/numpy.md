# Librăria NumPy

NumPy este o librărie ce este folosită în lucrul cu array-uri. Numele acesteia este o abreviere de la "Numerical Python". 

**De ce avem nevoie de NumPy?**
În Python avem deja listele ce țin loc de array-uri, dar acestea sunt destul de lente. Un array Numpy este de aproximativ 50 de ori mai rapid decât o listă tradițională.
<br/>

## Importarea librăriei în script-uri
Pentru a importa librăria NumPy în script-urile noastre folosim:

```python
import numpy as np
```
Am dat un alias librăriei cu ***as np*** pentru a scrie mai puțin cod pe parcursul script-ului, deoarece de fiecare dată când folosim ceva dintr-un pachet, trebuie să specificăm pachetul:
```python
x = numpy.array([1, 2, 3]) # Varianta fara alias
x = np.array([1, 2, 3]) # Varianta cu alias
```
<br/>

## Crearea array-urilor
Pentru a crea un array, folorim funcția **array()** în interiorul căreia specificăm între paranteze **'[]'** elementele acestuia:
```python
x = np.array([1, 2, 3]) # Tablou unidimensional

A = np.array([
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]) # Tablou bidimensional (matrice)
```
<br/>

## Apelarea elementelor
Accesarea elementelor unui tablou unidimensional NumPy se face întocmai ca la o listă clasică din Python.

* **Pentru vector:**
	```python
	x[i]  # elementul de pe pozitia i, unde i = 0,1,2,..., len(x)-1
	
	x[-1]  # elementul de pe pozitia i, numarat in sens invers
	
	b[start:stop]  # un slice al vectorului, avand elemente de la pozitia start (inclusiv) si pana la stop (exclusiv)
	
	b[:stop]  # un slice avand toate elementele incepand de pe pozitia 0 (inclusiv) si pana la pozitia stop (exclusiv)
	
	b[start:]  # un slice avand toate elementele incepand de pe pozitia start (inclusiv) si pana la ultimul element (inclusiv)
	```
	Exemple:
	```python
	x = np.array([1,2,3,4,5])
	print(x[2]) # afiseaza 3
	
	x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
	print(x[2:7:2]) # afiseaza 3 5 7
	```
	
* **Pentru matrice:**
	```python
		A[i, j]  # returneaza elementul de pe linia i si coloana j (indexarea incepe de la 0)

		A[i, :]  # returneaza linia i

		A[:, j]  # returneaza coloana j

		A[i, :j]  # returneaza linia i si toate coloanele incepand cu prima (inclusiv) si pana la j (exclusiv)
	```

	Exemple:
	```python
		A = np.array([
			[1, 2, 3],
			[4, 5, 6],
			[7, 8, 9]
		])
		print(y[2,1]) # afiseaza 8

		x = np.array([
			[1, 2, 3, 4, 5],
			[4, 5, 6, 7, 8],
			[7, 8, 9, 1, 2],
			[3, 4, 5, 6, 7]
		])
		print(x[1:3, 2:]) 

		"""
		Afiseaza:
		6 7 8
		9 1 2
		"""
	```

<br/>

## Tipuri de date
Tipul de date folosit de elementele array-ului este foarte important. De exemplu, array-urile create mai sus sunt interpretate de numpy ca având tipul de date 'int64'.
Pentru a evita erorile provenite din calcule, vom specifica în mod explicit tipul de date ca fiind 'float32'. Pentru a face acest lucru, putem utiliza una din metodele de mai jos
```python
A = np.array([
	[1, 2],
	[3, 4]
], dtype= np.float32)
```
```python
A = np.array([
	[1, 2],
	[3, 4]
]).astype(np.float32)
```
```python
A = np.array([
	[1., 2.],
	[3., 4.]
])
```
<br/>

## Dimensiunea unui array
Pentru a afla dimensiunile array-ului (numărul de linii/coloane), vom folosi metoda **np.shape()**. Această metodă returnează un tuplu în care pe prima poziție se află numărul de linii, iar pe a doua numărul de coloane.
* **Pentru vector:**
	```python
	np.shape(x)  # (x,) unde x este numarul de linii
	np.shape(A)[0]  # numarul de coloane
	len(b)  # numarul de coloane
	```
* **Pentru matrice:**
	```python
	np.shape(A)  # (x,y) unde x este numarul de linii si y numarul de coloane
	np.shape(A)[0]  # numarul de linii
	np.shape(A)[1]  # numarul de coloane
	```

<br/>


## Înmulțirea array-urilor
O operație ce o vom folosi în mod frecvent este înmulțirea array-urilor, ce poate fi aplicată atât pe matrice cât și pe vectori.
 
**Pentru matrice:**
Dacă A are dimensiunea (n,m) și B dimensiunea (m,p), atunci:
```python
C = A @ B # reprezinta produsul matricelor si are dimensiunea (n,p)
```

**Pentru vectori:**
În acest caz, operatorul **@** realizează produsul scalar dintre doi vectori.

<br/>


## Concateanarea array-urilor
Pentru concatenarea a 2 array-uri putem folosi mai multe funcții din libraria NumPy:
* **concatenate()**
```python
# Exemplul 1 - concatenarea a doi vectori
x = np.array([1,2,3])
y = np.array([4,5,6])
print(np.concatenate((x,y))) # afiseaza [1,2,3,4,5,6]


# Exemplul 2 - concatenarea a doua matrici pe linii
# Este necesar ca numarul de coloane sa fie acelasi!!
A = np.array([  
    [1,2,3],  
 	[4,5,6],  
 	[7,8,9]  
]).astype(np.float32)  
  
B = np.array([  
    [0,1,7],  
 	[10,5,3]  
]).astype(np.float32)  
  
print(np.concatenate((A,B)))
"""
[[ 1.  2.  3.]
 [ 4.  5.  6.]
 [ 7.  8.  9.]
 [ 0.  1.  7.]
 [10.  5.  3.]]
"""


# Exemplul 3 - concatenarea a doua matrici pe coloane
# Este necesar ca numarul de linii sa fie acelasi!!
A = np.array([  
    [1,2,3],  
 	[4,5,6],  
 	[7,8,9]  
]).astype(np.float32)  
  
B = np.array([  
    [0,1,7],  
 	[10,5,3],  
 	[10,5,3]  
]).astype(np.float32)  
  
print(np.concatenate((A,B), axis=1))

"""
[[ 1.  2.  3.  0.  1.  7.]
 [ 4.  5.  6. 10.  5.  3.]
 [ 7.  8.  9. 10.  5.  3.]]
"""
```

* **hstack()**
Această funcție concatează array-uri de-a lungul liniilor:
```python
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(np.hstack((arr1, arr2))) # afiseaza [1,2,3,4,5,6]
```

* **vstack()**
Funcție utilă dacă dorim să concatenăm de-a lungul coloanelor:
```python
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(np.vstack((arr1, arr2)))

"""
[[1 2 3]
 [4 5 6]]
"""
```

<br/>

## Funcții aritmetice
Funțiile matematice se realizează element cu element și întorc un nou array. De reținut este faptul că dimensiunile celor două array-uri trebuie să fie egale.

* **Suma:**
```python
x = np.array([10, 11, 12, 13, 14, 15])
y = np.array([20, 21, 22, 23, 24, 25])

z = np.add(x, y)

print(z) # afiseaza [30 32 34 36 38 40]
```

* **Diferenta:**
```python
x = np.array([10, 11, 12, 13, 14, 15])
y = np.array([20, 21, 22, 23, 24, 25])

z = np.substract(x, y)

print(z) # afiseaza [-10  -1   8  17  26  35]
```

* **Produsul:**
```python
x = np.array([10, 11, 12, 13, 14, 15])
y = np.array([20, 21, 22, 23, 24, 25])

z = np.multiply(x, y)

print(z) # afiseaza [ 200  420  660  920 1200 1500]
```

* **Câtul:**
```python
x = np.array([10, 20, 30, 40, 50, 60])
y = np.array([3,  5, 10, 8, 2, 33])

z = np.divide(x, y)

print(z) # afiseaza [ 3.33333333  4.  3.  5.  25.  1.81818182]
```

* **Restul împărțirii:**
```python
x = np.array([10, 20, 30, 40, 50, 60])
y = np.array([3,  5, 10, 8, 2, 33])

z = np.mod(x, y)

print(z) # afiseaza [ 1  6  3  0  0 27]
```

* **Ridicarea la putere:**
```python
x = np.array([10, 20, 30, 40, 50, 60])
y = np.array([3,  5, 10, 8, 2, 33])

z = np.power(x, y)

print(z) # afiseaza [1000  3200000  729000000  6553600000000  2500  0]
```

* **Modulul:**
```python
x = np.array([-1, -2, 1, 2, 3, -4])

z = np.abs(x)

print(z) # afiseaza [1 2 1 2 3 4]
```

<br/>

## Funcții pe matrice
* **np.linalg.det()** - calculează determinantul matricei
```python
A = np.array([  
    [1,2,3],  
 	[4,5,6],  
 	[7,8,3]  
])  
z = np.linalg.det(A)

print(z) # afiseaza 17.999999999999996
```

* **np.triu()** - crează matricea superior triunghiulară a unei matrice date ca argument
```python
A = np.array([  
    [1,2,3],  
 	[4,5,6],  
 	[7,8,3]  
])  
B = np.triu(A)  
print(B)

"""
[[1 2 3]
 [0 5 6]
 [0 0 3]]
 """
```

* **np.tril()** - crează matricea inferior triunghiulară a unei matrice date ca argument
```python
A = np.array([  
    [1,2,3],  
 	[4,5,6],  
 	[7,8,3]  
])  
B = np.triu(A)  
print(B)

"""
[[1 0 0]
 [4 5 0]
 [7 8 3]]
"""
```

* **np.diag()** - întoarce o listă ce reprezintă elementele diagonalei matricei date ca argument
```python
A = np.array([  
    [1,2,3],  
 	[4,5,6],  
 	[7,8,3]  
])  
B = np.triu(A)  
print(B) # afiseaza [1 5 3]
```

* **np.eye()** - construiește matricea identitate cu dimensiunea specificată
```python
I = np.eye(3)  
print(I)

"""
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
"""
```

* **np.vander()** - construiește matricea Vandermonde cu dimensiunea specificată
```python
x = np.array([1,2,3,4])  
B = np.vander(x, 5, increasing=False)  
print(B)

"""
[[  1   1   1   1   1]
 [ 16   8   4   2   1]
 [ 81  27   9   3   1]
 [256  64  16   4   1]]
"""


x = np.array([1,2,3,4])  
B = np.vander(x, 5, increasing=True)  
print(B)

"""
[[  1   1   1   1   1]
 [  1   2   4   8  16]
 [  1   3   9  27  81]
 [  1   4  16  64 256]]
"""
```

<br/>

## Funcții utile
* **np.linspace(start, stop, number_of_elem)** - returnează un array de **number_of_elem** elemente, în care primul element este **start**, ultimul este **stop**, iar toate elementele sunt echidistante între ele
```python
x = np.linspace(1, 10, 5)
print(x) # afiseaza [ 1.  3.25  5.5  7.75  10.]
```

* **np.sign()** - returnează -1 dacă numărul este negativ și 1 dacă este pozitiv
```python
x = np.array([-10, 17, 34, -2])  
print(np.sign(x)) # afiseaza [-1  1  1 -1]
```

* **np.zeros()** - crează un array de zero-uri, cu dimensiunea specificată
```python
x = np.zeros(7)  
print(x) # afiseaza [0. 0. 0. 0. 0. 0. 0.]
```

* **np.ones()** - crează un array în care toate elementele sunt 1, având dimensiunea specificată
```python
x = np.ones(7)  
print(x) # afiseaza [1. 1. 1. 1. 1. 1. 1.]
```

* **np.sum()** - returnează suma unui array
```python
x = np.array([-10, 17, 34, -2])  
print(np.sum(x)) # afiseaza 39
```

* **np.product()** - returnează produsul unui array
```python
x = np.array([-10, 17, 34, -2])  
print(np.product(x)) # afiseaza 11560
```

* **np.max()** - returnează elementul maxim al unui array
```python
x = np.array([-10, 17, 34, -2])  
print(np.max(x)) # afiseaza 34
```

* **np.min()** - returnează elementul minim al unui array
```python
x = np.array([-10, 17, 34, -2])  
print(np.min(x)) # afiseaza -10
```

* **any()** - verifică dacă există cel puțin un element nenul în array
```python
x = np.array([-10, 0, 0, 0])  
print(np.any(x)) # afiseaza True
```

* **np.argmin()** - întoarce index-ul elementului minim din array
```python
x = np.array([-10, 17, 34, -2])  
print(np.argmin(x)) # afiseaza 0
```

* **np.argmax()** - întoarce index-ul elementului maxim din array
```python
x = np.array([-10, 17, 34, -2])  
print(np.argmax(x)) # afiseaza 2
```

* **np.allclose()** - întoarce True dacă două array-uri sunt egale cu o toleranță stabilită
```python
x = np.allclose([1e10,1e-8], [1.00001e10,1e-9])  
print(x) # afiseaza True
```

* **np.linalg.solve()** - rezolvă un sistem de ecuații
```python
A = np.array([  
    [1, 2],  
 	[3, 5]  
])  
b = np.array([1, 2])  
x = np.linalg.solve(A, b)  # rezolva sistemul Ax=b
print(x) # afiseaza [-1.  1.]
```

<br/>

## Exerciții
**1. a) Crează o matrice A, având 4 linii și 3 coloane cu elemente de tip float32.**
```python
A = np.array([  
    [1,2,3],  
	[5,2,4],  
	[6,8,7],  
	[12,8,9],  
]).astype(np.float32)
```

**b) Află dimensiunile matricei folosind o metodă din numpy și printează rezultatul la consolă.**
```python
print(A.shape)
```

**c) Convertește tipul de date al matricei la int64 și printează matricea rezultat la consolă.**
```python
A = A.astype(np.int64)  
print(A)
```

**d) Crează o matrice C, având 3 linii și 3 coloane cu elemente de tip float32.**
```python
C = np.array([  
    [1,2,3],  
	[4,5,6],  
	[7,8,9]  
], dtype=np.float32)
```

**e) Crează un vector b, având 3 linii și o coloană cu elemente de tip float32.**
```python
b = np.array([  
    [7],  
	[3],  
	[2]  
]).astype(np.float32)
```

**f) Înmulțește matricele A și C și printează rezultatul la consolă.**
```python
print(A @ C)
```

**g) Înmulțește matricea C și vectorul b.**
```python
print(C @ b)
```

<br/>	

**2.  a) Crează un vector coloană b, cu elemente de tip float32, având 5 linii și printează rezultatul la consolă.**
```python
b = np.array([  
    [4],  
	[8],  
	[2],  
	[-3],  
	[7]  
]).astype(np.float32)  
print(b)
```
	
**b) Printează la consolă primul și ultimul element al vectorului b.**
```python
print(f'{b[0]} {b[-1]}')
```

**c) Printează la consolă penultimul element al vectorului b.**
```python
print(b[-2])
```

**d) Extrage elementele vectorului b fără primul și ultimul element și printează.**
```python
print(b[1:-1])
```

<br/>

**3. a) Crează o matrice A, cu elemente de tip float32, având 4 linii și 4 coloane.**
```python
A = np.array([  
    [1,2,3,7],  
	[5,2,4,1],  
	[6,8,7,10],  
	[12,8,9,-3],  
]).astype(np.float32)
```

**b) Extrage a doua linia a matricei A și printează rezultatul la consolă.**
```python
print(A[1,:])
```

**c) Extrage a treia coloană a matricei A și printează rezultatul la consolă.**
```python
print(A[:,2])
```

<br/>

**4. Crează un vector x, apoi folosind librăria NumPy crează un alt vector cu elementele lui x luate în ordine inversă.**
```python
x = np.array([1,2,3,7,5])  
y = x[::-1]  
print(y)
```

<br/>

**6. Crează o matrice 5x5 în care toate elementele sunt 0, cu excepția bordurilor acesteia ce sunt 1.**
```python
A = np.zeros((5,5))  
A[0,:] = A[-1,:] = 1  
A[:,0] = A[:,-1] = 1  
print(A)
```