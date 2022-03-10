#%%

print("#### ESERCIZIO 1 ####")

class point_3D:
    def __init__(position, x, y, z):
        position.x = x
        position.y = y
        position.z = z

    def coordinates(abc):
        print( "Point coordinates are: (" + str(abc.x) + ", " + str(abc.y) + ", " + str(abc.z) + ")" )
        
def distance(A, B):
    dis = ( (A.x - B.x)**2 + (A.y - B.y)**2 + (A.z - B.z)**2 )**0.5
    print("Distance between two points is: " + str(dis))
    

p1 = point_3D(1, 3, 2)
p2 = point_3D(7, 5, 3)

p1.coordinates()
p2.coordinates()

distance(p1, p2)        

#%%

print()
print("#### ESERCIZI 2, 3 ####")

import numpy as np

class point_2D:
    def __init__(position, x, y):
        position.x = x
        position.y = y

    def coordinates(abc):
        print( "Point coordinates are: (" + str(abc.x) + ", " + str(abc.y) + ")" )
        
def CM(punti, n):
    x_CM = 0
    y_CM = 0
    
    for i in range(0,n):
        x_CM = punti[i,0] + x_CM
        y_CM = punti[i,1] + y_CM

    print("Center of mass position is: (" + str(x_CM/n) + ", " + str(y_CM/n) + ")" )


var = input("Please type in data file name: ")
file = open(var, 'r')
    
n = sum(1 for line in open('Dati.txt'))
punti = np.zeros((n,2))

for i in range(0,n):
    temp = file.readline()
    punti[i,0] = temp.split()[0]
    punti[i,1] = temp.split()[1]
    #temp_x = temp.split()[0]
    #temp_y = temp.split()[1]
    
file.close()

CM(punti, n)

#%%

print()
print("#### ESERCIZIO 4 ####")

class campionato:
    
    def __init__(lista_squadre, nomi, punteggi, numero_squadre):
        lista_squadre.nomi = nomi
        lista_squadre.punt = punteggi
        lista_squadre.tot  = numero_squadre
        
    def squadre(abc):
        print("The teams are:", abc.nomi)
        
    def punteggi(abc):
        print("Their respective scores are:", abc.punt)
        
    def aggiungi_squadra(abc, squadra):
        abc.append(squadra)
    
    def aggiunggi_punteggio(abc, punteggio):
        abc.append(punteggio)

n = input("Please insert total teams number: ")
n = int(n)

nomi = list()
punt = list()

for i in range(0,n):
    temp_1 = input("Please insert name of team #" + str(i+1) + ": ")
    nomi.append(temp_1)
    temp_2 = int(input("Please insert team #" + str(i+1) + " points: "))
    punt.append(temp_2)
    
lista_squadre = campionato(nomi, punt, n)
lista_squadre.squadre()
lista_squadre.punteggi()    
    
squadra_x = input("Insert a team's name to know its score: ")

i = 0
j = 0
b = "ciao"

for x in nomi:
    if x != squadra_x:
        i = i + 1
    if x == squadra_x:
        print(squadra_x + " score is: " + str(punt[i]))
        break
    
for i in range(0,n):
    if punt[i] == max(punt):
        print("winner team is: " + str(nomi[i]))
        punt[i] = 0
        nomi[i] = 0
        break
    
for i in range(0,n):
    if punt[i] == max(punt):
        print(str(nomi[i]) + " came 2nd")
        punt[i] = 0
        nomi[i] = 0
        break
    
for i in range(0,n):
    if punt[i] == max(punt):
        print(str(nomi[i]) + " came 3rd")
        punt[i] = 0
        nomi[i] = 0
        break

#%%

print()
print("#### ESERCIZIO 5 ####")
print()
print("List product")
print()

import numpy as np
import sys

def prod_scal(A, B):
    if len(A) != len(B):
        print("Error: scalar product not allowed!")
    elif len(A) == len(B):
        prod = 0
        for i in range(0,len(A)):
            prod = prod + A[i]*B[i]
        return(prod)
    
A = [1,2,3,4,5]
B = [5,8,7,7,3]

print("A =", A)
print("B =", B)
print("A*B =", prod_scal(A,B))

print("Rows-columns product")
print()

n = int(input("Enter # of rows in matrix A: "))
m = int(input("Enter # of columns in matrix A: "))
p = int(input("Enter # of rows in matrix B: "))
q = int(input("Enter # of columns in matrix B: "))

if m != p:
    sys.exit("Error: rows-columns product not allowed!")
        
A = np.zeros((n,m))
B = np.zeros((p,q))
C = np.zeros((n,q))
    
def prod_mat(A, B):
    if m==p:
       for i in range(0,n):
           for j in range(0,q):
               for k in range(0,m):
                    C[i,j] = C[i,j] + A[i,k] * B[k,j]
                    
    return(C)

for i in range(0,n):
    for j in range(0,m):
        A[i,j] = 0.1*i + 0.2*j
        
for i in range(0,p):
    for j in range(0,q):
        B[i,j] = 0.3*i + 0.4*j

print("A =", A)
print("B =", B)
print("A*B =", prod_mat(A,B))


#%%

print()
print("#### ESERCIZIO 6 ####")      

print("La funzione LAMBDA ha in input uno o più argomenti e restituisce il")
print("risultato dell'operazione indicata. Nel primo caso l'operazione ha un numero")
print("come input e quel numero, sommato a 10, come output. Nel secondo caso occorre")
print("indicare come argomento 1 unica entrata (stringa) della lista 'animali' per")
print("ottenere in output lo stesso elemento, scritto con la prima lettera maiuscola.")      

avg = lambda x, y : (x+y)/2
x = float(input("Please insert x = "))
y = float(input("Please insert y = "))
print()
print("average(x,y) =", avg(x,y))
        

        
        
        

        


















    
    
    
    
    
    
    
    
    
    
 
    
 
    
 
    