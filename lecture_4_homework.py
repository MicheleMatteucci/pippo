#%%
print("#### ESERCIZIO 1 ####")

nome    = "Michele "
cognome = "Matteucci "
età     = "25 "

print("Buongiorno, mi chiamo " + nome + cognome + "e ho " + età + "anni.")

#%%

print()
print("#### ESERCIZIO 2 ####")

n = 3
m = 0

print()
print("Some integer numbers are:")
print("n =", n)
print("m =", m)
print("n + m =", n+m)

x = 5.1
y = 2**0.5

print()
print("Some real numbers are:")
print("x =", x)
print("y =", y)
print("x / y =", x/y)

z = 1+2j
w = 3-1j

print()
print("Some complex numbers are:")
print("z =", z)
print("w =", w)
print("z^w =", z**w)

P = True
Q = False

print()
print("Two boolean values are:")
print("P =", P)
print("Q =", Q)
print("P and Q =", P and Q)

A = "hello"
B = "world"

print()
print("Some strings are:")
print("A =", A)
print("B =", B)
print("A '+' B =", A+B)

print()
print("Some operations using implicit type casting:")
print("n * z =", n*z)
print("A and P =", A and P)

print()
print("Some operations using explicit type casting:")
print("x * Q =", x * float(Q))
print("B '+' m =", B + str(m))

#%%

print()
print("#### ESERCIZIO 3 ####")

def MRU (s0, dt, v):
    s = s0 + v*dt
    return(s)

def MRUA (s0, dt, v0, a):
    s = s0 + v0*dt + 0.5*a*dt**2
    return(s)

print()
print("Che moto vuoi analizzare?")
print("0 --> moto rettilineo uniforme")
print("1 --> moto rettilineo uniformemente accelerato")
x = input()

if int(x) == 0:
    s0 = float(input("Indicare la posizione iniziale [m]: "))
    dt = float(input("Indicare il tempo del moto [s]:"))
    v  = float(input("Indicare la velocità costante [m/s]:"))
    print()
    print("Lo spazio percorso è ", MRU(s0, dt, v), "m")
elif int(x) == 1:
    s0 = float(input("Indicare la posizione iniziale [m]: "))
    dt = float(input("Indicare il tempo del moto [s]: "))
    v0 = float(input("Indicare la velocità iniziale [m/s]: "))
    a  = float(input("Indicare l'accelerazione costante [m/s^2]: "))
    print()
    print("Lo spazio percorso è ", MRUA(s0, dt, v0, a), "m")
else:
    print("Non so cosa vuoi dire. Termino l'esecuzione.")

#%%

print()
print("#### ESERCIZIO 4 ####")

def f_sum(a, b):
    sum = a + b
    return sum

a = 1
b = 2
sum = 3
f_sum(100, 100)
print()
print(sum)

print("Questo è il risultato del primo codice perché in sostanza viene")
print("unicamente stampato il valore della variabile 'sum', col valore assegnato 3.")


def f_sum(a, b):
    sum = a + b
    return sum

a = 1
b = 2
sum = 3
print()
print(f_sum(100, 100))

print("Questo è il risultato del secondo codice perché viene effettivamente")
print("chiamata la funzione 'f_sum' con input gli interi 100 e 100.")

#%%

print()
print("#### ESERCIZIO 5 ####")

import module as aree

print()
l = float(input("Indicare il lato del quadrato: "))
print("L'area del quadrato è: ", aree.quadrato(l))

print()
a = float(input("Indicare il primo lato del rettangolo: "))
b = float(input("Indicare il secondo lato del rettangolo: "))
print("L'area del rettangolo è: ", aree.rettangolo(a,b))

print()
r = float(input("Indicare il raggio del cerchio: "))
print("L'area del cerchio è: ", aree.cerchio(r))

print()
c1 = float(input("Indicare il primo cateto del triangolo: "))
c2 = float(input("Indicare il secondo cateto del triangolo: "))
print("L'area del triangolo è: ", aree.triangolo(c1,c2))

#%%

print()
print("#### ESERCIZIO 6 ####")

print()
print("La funzione type() restituisce il tipo della variabile in argomento.")
print("Ad esempio, se A = 'hello', type(A) =", type(A), ".")

class point_3D:
    def __init__(position, x, y, z):
        position.x = x
        position.y = y
        position.z = z

print()
print("La funzione dir() restituisce metodi e attributi dell'oggetto in argomento.")
print("Ad esempio, dir(point_3D) =", dir(point_3D), ".")

print("La funzione help() è la help utility di Python.")
print("Si possono inserire diversi input a seconda del tipo di aiuto richiesto.")
#help()










