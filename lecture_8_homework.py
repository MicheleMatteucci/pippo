import matplotlib.pyplot as plt
import numpy as np

#%%

print("#### ESERCIZIO 1 ####")

def isto_ast(data_file):
    file        = open(data_file, 'r')
    n           = sum(1 for line in open(data_file))
    isto        = np.zeros((n,1))

    for i in range (0,n):
        isto[i] = file.readline()
        temp = int(isto[i])
        for j in range(0,temp):
            print("*", end = ' ')
        print("\n")
    file.close()

def isto_gra(data_file):
    file        = open(data_file, 'r')
    n           = sum(1 for line in open(data_file))
    isto = np.ones((n) * 1)
    x    = np.ones((n) * 1)

    for i in range (0,n):
        x[i] = str(i)
        isto[i] = file.readline()
    
    plt.bar(x,isto)
    plt.show()
    file.close()


print()
data_file   = input("Please type in data file name: ")
#data_file = "dati.txt"
print()
isto_ast(data_file)
isto_gra(data_file)

#%%

print()
print("#### ESERCIZIO 2 ####")
   
print()
data_file   = input("Please type in data file name: ")
#data_file = "Dati_8.txt"

file    = open(data_file, 'r')
n       = sum(1 for line in open(data_file))
#print(n)

anni    = np.zeros((n,1))
Tmin    = np.zeros((n,1))
Tmax    = np.zeros((n,1))

for i in range(0,n):
    temp    = file.readline()
    if i == 0:
        anni[0] = 0
        Tmin[0] = 0
        Tmax[0] = 0
    else:
        anni[i] = temp.split()[0]
        Tmin[i] = temp.split()[1]
        Tmax[i] = temp.split()[3]
    #print(Tmin[i], Tmax[i])

file.close()

anni = anni[anni != 0]
Tmin = Tmin[Tmin != 0]
Tmax = Tmax[Tmax != 0]
n = n-1

avg_min = sum(Tmin)
avg_max = sum(Tmax)
avg_min = avg_min / n
avg_max = avg_max / n
var_min = 0
var_max = 0

for i in range(0,n):
    var_min = var_min + ( Tmin[i] - avg_min )**2
    var_max = var_max + ( Tmax[i] - avg_max )**2
    
var_min = var_min / n
var_max = var_max / n

print()
print("Dev.st. Tmin =", var_min**0.5)
print("Dev.st. Tmax =", var_max**0.5)
print()
print("Lib. dev.st. Tmin =", np.std(Tmin))
print("Lib. dev.st. Tmax =", np.std(Tmax))

plt.plot(anni, Tmin, color='blue', label='Tmin')
plt.plot(anni, Tmax, color='red', label='Tmax')
plt.xlabel("Years")
plt.ylabel("Temperature")
plt.grid()
plt.legend()

#%%

print()
print("#### ESERCIZIO 3 ####")

n = 10
A = np.zeros((n,1))

for i in range(0,n):
    A[i] = i
    
print()
print("A =", A)
print()
print("Array indexing")
print("A[0] =", A[0])
print("A[1] =", A[1])
print("A[2] =", A[2])
print()
print("Array slicing")
print("A[2:7] =", A[2:7])
print("A[2:] =", A[2:])
print("A[:7] =", A[:7])

print()
print("COPIA PER RIFERIMENTO")
print("Un elemento copiato per riferimento viene posto uguale a")
print("un'area di memoria 'puntata'.")
print()
print("COPIA PER VALORE")
print("Una copia per valore crea una nuova area di memoria e le")
print("assegna valore uguale a quella 'puntata'.")

B = np.zeros((n,1))

for i in range(0,n):
    B[i] = i**2
    
print()
print("B =", B)
print()
print("La somma di tutti gli elementi dei due array è ", np.sum(A)+np.sum(B))
print()
print("La somma dei due array termine a termine è ", np.add(A,B))
print()
print("Il prodotto dei due array termine a termine è ", np.multiply(A,B))

#%%

print()
print("#### ESERCIZIO 4 ####")

print()
print("La funzione eig() della libreria linalg di numpy calcola autovalori")
print("e autovettori, mentre eigval() calcola solo gli autovalori.")

print()
data_file   = input("Please type in data file name to read matrix: ")
#data_file = "mat.txt"

file    = open(data_file, 'r')
n       = sum(1 for line in open(data_file))

A = np.zeros((n,n))

for i in range(0,n):
    temp = file.readline()
    for j in range(0,n):
        A[i,j] = temp.split()[j]
    #print(Tmin[i], Tmax[i])

file.close()

print("A =", A)

l, v = np.linalg.eig(A)
print()
print("Eingenvalues =", l)
print("Eingenvectors =", v)

#%%

print()
print("#### ESERCIZIO 5 ####")

def sigmoide(x):
    sigma = 1 / (1+np.e**(-x))
    return(sigma)

print()
x = float(input("Please type in a real number x: "))
print()
print("F(x) =", sigmoide(x))
    

def normalized_sigmoid_fkt(a, b, x):
    '''
    Returns array of a horizontal mirrored normalized sigmoid function
    output between 0 and 1
    Function parameters a = center; b = width
    '''
    s= 1/(1+np.exp(b*(x-a)))
    return 1*(s-min(s))/(max(s)-min(s)) # normalize function to 0-1

def draw_function_on_2x2_grid(x):
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    plt.subplots_adjust(wspace=.5)
    plt.subplots_adjust(hspace=.5)
    ax1.plot(x, normalized_sigmoid_fkt( .5, 18, x))
    ax1.set_title('1')
    ax2.plot(x, normalized_sigmoid_fkt(0.518, 10.549, x))
    ax2.set_title('2')
    ax3.plot(x, normalized_sigmoid_fkt( .7, 11, x))
    ax3.set_title('3')
    ax4.plot(x, normalized_sigmoid_fkt( .2, 14, x))
    ax4.set_title('4')
    plt.suptitle('Different normalized (sigmoid) function',size=10 )
    return fig

x = np.linspace(0,1,100)
Travel_function = draw_function_on_2x2_grid(x)

#%%

import time as t

print()
print("#### ESERCIZIO 6 ####")

n = int(input("Please type in matrix dimension: "))
A = np.zeros((n,n))

t1 = float(t.time())
for i in range(0,n):
    for j in range(0,n):
        A[i,j] = np.random.randint(10)
t2 = float(t.time())

t3 = float(t.time())
A  = np.random.randint(10, size=(n,n))
t4 = float(t.time())

print()
print("Time to initialize nxn matrix:")
print("- 'for' cycle init.: t =", t2-t1, "s")
print("- built in functions init.: t =", t4-t3, "s")
#print("tempo =", t.time())





















