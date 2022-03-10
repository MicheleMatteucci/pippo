
a = [1, 3, "ciao"]
print(a)

b = 5

# at this point print(a+b) doens't work

c = [b,0]

print(a+c)
print(a+c*2)

c.append(7)
print(c)

# measuring efficiency
import time
l=[range(5,100000000)]
v=[range(1000000)]
T1=time.perf_counter()
s=l+v
T2=time.perf_counter()
print(" + execution time: :" , T2-T1, "s")
T3=time.perf_counter()
l.extend(v)
T4=time.perf_counter()
print("extend execution time:", T4-T3 , "s")


# printing the first 11 positive integers using while loop and if statement
condition = True
i = 0

while condition:
    i = i + 1
    print(i)
    
    if i == 11:
        condition = False
        print("end while cycle", "\n")        
        
# printing the first 11 integers usign for loop
for i in range(1,12):
    print(i)
    
    if i == 12:
        print("end for cycle")
    



