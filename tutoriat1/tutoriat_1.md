<img src="https://github.com/laurentiucretu68/Tutoriat-CN-2022/blob/main/tutoriat1/Pasted%20image%2020220304102455.png">

# <p style="color:#4B8BBE">Introducere în Python</p>
Din punct de vedere al sintaxei, Python este un limbaj de programare foarte intuitiv. Python este un limbaj interpretat, adică nu se compilează, acesta rulând în spate, în mare parte, cu cod C.

<br/>

## <span style="color: #4B8BBE">Introducerea comentariilor</span>
În Python putem introduce atât comentarii pe un singur rând cu caracterul #:
```python
# Exemplu de comentariu pe o linie
```
cât și comentarii ce se întind pe mai multe linii de cod:
```python
"""
Comentariu
pe mai multe
linii de cod
"""
```
<br/>

## <span style="color: #4B8BBE">Variabile</span>
Pentru a declara o variabilă în Python nu mai este nevoie să declarăm tipul acesteia (int, float etc) și mai mult, tipul variabilelor poate fi schimbat în timpul programului:
```python
x = 10  # variabila de tip int
"""
serie de instructiuni
"""
x = 'Andrei' # variabila de tip str
```

#### <span style="color: #FFE873">Casting</span>
Pentru a declara variabilele într-un mod mai explicit, sau daca dorim să  schimbăm tipul variabilelor, putem folosi casting-ul:
```python
x = float(5) # x este 3.0
x = int(5) # x este 3
x = str('5') # x este '3'
```

#### <span style="color: #FFE873">Tipul variabilelor</span>
Pentru a obține tipul unei variabile folosim funcția **type()** :
```python
x = 10
y = 'Ana'
print(type(x)) # va afisa <class 'int'>
print(type(y)) # va afisa <class 'str'>
```

#### <span style="color: #FFE873">Atribuirea multiplă</span>
O funcționalitate foarte utilă în Python este atribuirea multiplă, aceasta se realizează ca în exemplul următor:
```python
x, y, z = 3, 4, 5
```

***<span style="color: crimson">Observații:</span>***
* Variabilele de tip string pot fi declarate atât cu " ", cât și cu ' '
* În Python variabilele sunt case-sensitive, adică variabilă x nu este echivalentă cu variabila X
* Pentru atribuirea multiplă, numărul variabilelor din stânga trebuie să fie același cu numărul valorilor din dreapta, în caz contrar codul nu va rula

<br/>

## <span style="color: #4B8BBE">Afișarea în consolă</span>
Afișarea în consolă se realizează cu funcția **print()**:
```python
x = 'mesaj'
print(x) # se afiseaza 'mesaj'
print(x + ' de test') # se afiseaza 'mesaj de test'
print(f'{x} de test') # se afiseaza 'mesaj de test'

x = 10
y = 5
print(x+y) # se afiseaza 15

x = 10
y = 'test'
print(x+y) # veti primi eroare, deoarece nu se poate concatena un int cu un str
```
<br/>

## <span style="color: #4B8BBE">Tipuri de date numerice</span>
Principalele tipuri de date în Python sunt:
* **str** - string-uri
* **int** - numere întregi
* **float** - numere reale
* **complex** - numere complexe
* **bool** - tipuri logice

<br/>

## <span style="color: #4B8BBE">Operatori</span>
Majoritatea operatorilor din C/C++ se regăsește și în limbajul Python, cu câteva excepții:
* Nu mai exista operatorii de incrementare și decrementare prefixați și postfixați **++** și **--**
* Operatorul logic **&&** din C este înlocuit cu *AND*, **||** cu *OR*, iar **!** cu *NOT*

Apar și operatori noi față de C, precum:
<span style="margin-top: 10px"></span>

**<span style="color: #FFE873">1. Operatorii de identitate:</span>** <br>
	a) **is** - returnează True dacă ambele variabile sunt același obiect <br>
	b) **is not** - returnează True dacă ambele variabile nu sunt același obiect
```python
x = ["obiect1", "obiect2"]
y = ["obiect1", "obiect2"]
z = x

print(x is z) # afiseaza TRUE
print(x is not z) # afiseaza FALSE

print(x is y) # afiseaza FALSE
print(x is not y) # afiseaza TRUE
```
<span style="margin-top: 10px"></span>

**<span style="color: #FFE873">2. Operatorii de membru (foarte folosiți în for-uri):</span>**<br>
	a) **in** - returnează True dacă valoarea specificată se găsește în secvență<br>
	b) **not in** - returnează True dacă valoarea specificată nu se găsește în secvență
```python
x = ["obiect1", "obiect2"]

print('obiect1' in x) # afiseaza TRUE
print('obiect1' not in x) # afiseaza FALSE
```

<br/>

## <span style="color: #4B8BBE">Tipuri de date: </span>
Pe lângă tipurile numerice și string, în Python mai există 4 tipuri de date:
* lista
* tuplul
* setul
* dicționarul 

În cadrul acestui curs vom folosi array-uri din *Numpy* (detalii tutoriatul următor) și liste.

### <span style="color: #FFE873">Liste : </span> 
O listă este o structură de date în cadrul căreia elementele sunt ordonate, pot fi schimbate și pot apărea duplicate.

***<span style="color: crimson">Exemplu de listă:</span>***
```python
ex_list = ['object1', 'object2', 'object3']
```

***<span style="color: crimson">Observații:</span>***
* Pentru a obține dimensiunea unei liste, folosim funcția **len()**.
* O listă poate conține și tipuri de date diferite:
```python
lista = ['Ana', 34, 'are', True, 40]
```

* Putem crea o listă și cu ajutorul constructorului **list()**:
```python
lista = list((12, 13, 45))
```

***<span style="color: crimson">Accesarea elementelor:</span>***
* Elementele unei liste sunt stocate de la 0 și pot fi accesate prin []:
```python
lista = [12, 13, 45, 4, -2, 7, 17]
print(lista[1]) # afiseaza 13
```
* Se pot accesa indexuri negative:
```python
lista = [12, 13, 45, 4, -2, 7, 17]
print(lista[-2]) # afiseaza 7
```
* Se pot accesa prin slicing (**lista[start : end]**):
```python
lista = [12, 13, 45, 4, -2, 7, 17]
print(lista[1:3]) # afiseaza 13 45
print(lista[:4]) # afiseaza 12 13 45 4
print(lista[3:]) # afiseaza 4 -2 7 17
print(lista[-4:-1]) # afiseaza 4 -2 7
```

***<span style="color: crimson">Modificarea elementelor:</span>***
* Pentru a modifica elementele unei liste se selectează index-ul elemetului sau un slice de index-uri:
```python
lista = ['ob1', 'ob2', 'ob3', 'ob4', 'ob5']
lista[1] = 'mod1' # lista devine 'ob1', 'mod1', 'ob3', 'ob4', 'ob5'

lista = ['ob1', 'ob2', 'ob3', 'ob4', 'ob5']
lista[1:3] = ['mod1', 'mod2'] # lista devine 'ob1', 'mod1', 'mod2', 'ob4', 'ob5'

lista = ['ob1', 'ob2', 'ob3', 'ob4', 'ob5']
lista[1:2] = ['mod1', 'mod2'] # lista devine 'ob1', 'mod1', 'mod2', 'ob4', 'ob5'

lista = ['ob1', 'ob2', 'ob3', 'ob4', 'ob5']
lista[1:7] = ['mod1', 'mod2'] # lista devine 'ob1', 'mod1', 'mod2'
```


***<span style="color: crimson">Inserarea de elemente:</span>***
* Pentru a insera elemente într-o listă se folosește metoda **insert()** ce are 2 parametri (primul specifică poziția unde vom insera elementul și al doilea elementul):
```python
lista = ['ob1', 'ob2', 'ob3', 'ob4', 'ob5']
lista.insert(2, 'mod1') # lista devine 'ob1', 'ob2', 'mod1', 'ob3', 'ob4', 'ob5'
```
* Putem să inserăm și la finalul listei prin metoda **append()**:
```python
lista = ['ob1', 'ob2', 'ob3']
lista.append('mod1') # lista devine 'ob1', 'ob2', 'ob3', 'mod1',
```
* Dacă avem 2 liste și dorim să le concatenăm, folosim metoda **extend()**:
```python
lista1 = ['ob1', 'ob2', 'ob3']
lista2 = ['ob4', 'ob5']
lista1.extend(lista2) # lista devine 'ob1', 'ob2', 'ob3', 'ob4', 'ob5'
```

***<span style="color: crimson">Ștergerea elementelor:</span>***
* Pentru a șterge un element folosește metoda **remove()**:
```python
lista = ['ob1', 'ob2', 'ob3']
lista.remove('ob2') # lista devine 'ob1', 'ob3'
```
* Dacă dorim să ștergem un element aflat la o anumită poziție, folosim metoda **pop**:
```python
lista = ['ob1', 'ob2', 'ob3']
lista.pop(1) # lista devine 'ob1', 'ob3'
```
* Pentru a ștege întreaga lista, folosim funcția **del**:
```python
lista = ['ob1', 'ob2', 'ob3']
del lista
```
* Ștegerea întregului conținut al listei se realizează cu metoda **clear()**:
```python
lista = ['ob1', 'ob2', 'ob3']
lista.clear() # lista devine vida
```

***<span style="color: crimson">Parcurgerea unei liste:</span>***
* Putem parcurge o listă prin mai multe moduri, dar cele mai folosite sunt următoarele două:
```python
lista = ['ob1', 'ob2', 'ob3']

# Metoda 1
for x in lista:
	print(x)
	
# Metoda 2
for x in range(len(lista)):
	print(lista[x])
```
* O metodă interesantă este următoarea (mai multe detalii <a href="https://www.w3schools.com/python/python_lists_comprehension.asp">aici</a>):
```python
lista = ['ob1', 'ob2', 'ob3']

[print(x) for x in lista]
```

***<span style="color: crimson">Alte metode utile :</span>***
* **sort()**
* **copy()**
* **count()**
* **reverse()**
<br>

## <span style="color: #4B8BBE">Instrucțiuni de control </span>
### <span style="color: #FFE873">Instrucțiunea *if else* : </span> 
Varianta standard are următoarea sintaxă:
```python
if conditie:
	
	instructiuni1
	
elif conditie:
	
	instructiuni2
	
else:
	
	instructiuni3
```

Varianta short hand are sintaxa:
```python
instructiune_if if conditie else instructiune_else
```

***<span style="color: crimson">Exemplu:</span>***
```python
x = 10  
y = 15  
print("x mai mare") if x > y else print("Egalitate") if x == y else print("y mai mare")
```
<br>

### <span style="color: #FFE873">Instrucțiunea *while* : </span> 
Sintaxă:
```python
while conditie:
	instructiuni
	
```

***<span style="color: crimson">Exemplu:</span>***
```python
x = 1  

while x < 10:
	print(x)
	x += 1
```
<br>

### <span style="color: #FFE873">Instrucțiunea *for* : </span> 
Sintaxă:
```python
for var in object:
	instructiuni
	
```
***<span style="color: crimson">Exemplu:</span>***
```python
x = ['obiect1', 'obiect2', 'obiect3']  

for i in x:
	print(i)
```

Pentru a simula comportamentul unui *for* tradițional din C, ne folosim de funcția **range()**. Aceasta are următorii parametri: **range(start, end, step)**. Dacă **start** nu este specificat se va pleca de la 0, iar daca **step** nu este specificat, pasul va fi de 1.

***<span style="color: crimson">Exemplu:</span>***
```python
for i in range(2,17,3):
	print(i)

# se va afisa 2 5 8 11 14
# nu va fi afisat si 17, deoarece for-ul va merge pana la end-1, deci pana la 16 in acest exemplu
```
<br/>

## <span style="color: #4B8BBE">Funcții </span>
Pentru a crea o funcție se folosește cuvântul **def**:
```python
def functie():
	print('test')
	
functie() # apelul functiei
```
***<span style="color: crimson">Argumentele unei funcții:</span>***
* Argumentele funcției sunt plasate între parantezele () și specificate prin virgulă:
```python
def functie(string):
	print(string + ' afisare')
	
functie('apel1')
functie('apel2')
```
* Dacă dorim să primim un număr arbitrar de argumente folosim specificatorul *:
```python
def functie(*param):
	print(f'{param[0]} {param[2]}')
	
functie('Email', 2, 3, 'Test') 
```
* La apelul funcției putem specifica parametri în mod explicit:
```python
def functie(ob2, ob3, ob1):
	print(ob2)
	
functie(ob1=1, ob2=2, ob3=3) 
```
* Parametri cu valoare default:
```python
def functie(param = 'Valoare'):
	print(param)
	
functie('Test') # va afisa Test
functie()
```
<<<<<<< HEAD

<br/>

## <span style="color: #4B8BBE">Exerciții: </span>
#### 1. Spuneți se va afișa la execuția următoarelor script-uri: 
```python
## Exercitiul nr 1
def function():
	return "string " + 'chr'

print(function()) # string chr
```

```python
## Exercitiul nr 2
def function():
	return [i for i in range(0, 3, 3)]

print(function()) # 0
```

```python
## Exercitiul nr 3
def function():
	a = 1/3
	b = 3/1
	return (a*b)

print(function())
```

```python
## Exercitiul nr 4
x, y = 30, 59
x, y, z = 1, 2, 3

print(x, y, z) # 1 2 3
```

```python
## Exercitiul nr 5
i = 0  
while i < 7:  
   	print(f'{i}')  
   	i += 1  
	if i == 5:  
		break  
	else:  
		i += 2
		
# 0 3 6
```

```python
## Exercitiul nr 6
l = [4, 3, 2, 1]
elem = l.pop(1)
print(elem) # 3
```

```python
## Exercitiul nr 7
rows = 6  
  
for i in range(0, rows):  
     
	for j in range(rows-1, i, -1):  
      	print(j, '', end='')  
  
   	for l in range(i+1, rows):  
      	print(l, '', end='')  
  
   	print('\n')
	
"""
5 4 3 2 1 1 2 3 4 5 

5 4 3 2 2 3 4 5 

5 4 3 3 4 5 

5 4 4 5 

5 5 
"""
```
=======
>>>>>>> d261710 (Update tutoriat_1.md)
