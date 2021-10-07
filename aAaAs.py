from random import randint

t1 = randint(1,4)
t2 = randint(1,4)
t3 = randint(1,4)
t4 = randint(1,4)
t5 = randint(1,4)
t6 = randint(1,4)
t7 = randint(1,4)
t8 = randint(1,4)
t9 = randint(1,4)
t10 = randint(1,4)
t11 = randint(1,4)
t12 = randint(1,4)
t13 = randint(1,4)
t14 = randint(1,4)
t15 = randint(1,4)
t16 = randint(1,4)

#---------------------------------------------------------------------------#

if t1 == 1:
    A1 = "P"
elif t1 == 2:
    A1 = "A"
elif t1 >= 3:
    A1 = "B"
#-----------------
if t2 == 1:
    B1 = "P"
elif t2 == 2:
    B1 = "A"
elif t2 >= 3:
    B1 = "B"
#-----------------
if t3 == 1:
    C1 = "P"
elif t3 == 2:
    C1 = "A"
elif t3 >= 3:
    C1 = "B"
#-----------------
if t4 == 1:
    D1 = "P"
elif t4 == 2:
    D1 = "A"
elif t4 >= 3:
    D1 = "B"
#-----------------
if t5 == 1:
    A2 = "P"
elif t5 == 2:
    A2 = "A"
elif t5 >= 3:
    A2 = "B"
#-----------------    
if t6 == 1:
    B2 = "P"
elif t6 == 2:
    B2 = "A"
elif t6 >= 3:
    B2 = "B"
#-----------------       
if t7 == 1:
    C2 = "P"
elif t7 == 2:
    C2 = "A"
elif t7 >= 3:
    C2 = "B"
#-----------------       
if t8 == 1:
    D2 = "P"
elif t8 == 2:
    D2 = "A"
elif t8 >= 3:
    D2 = "B"
#-----------------       
if t9 == 1:
    A3 = "P"
elif t9 == 2:
    A3 = "A"
elif t9 >= 3:
    A3 = "B"
#-----------------       
if t10 == 1:
    B3 = "P"
elif t10 == 2:
    B3 = "A"
elif t10 >= 3:
    B3 = "B"
#-----------------       
if t11 == 1:
    C3 = "P"
elif t11 == 2:
    C3 = "A"
elif t11 >= 3:
    C3 = "B"   
#-----------------
if t12 == 1:
    D3 = "P"
elif t12 == 2:
    D3 = "A"
elif t12 >= 3:
    D3 = "B"
#-----------------   
if t13 == 1:
    A4 = "P"
elif t13 == 2:
    A4 = "A"
elif t13 >= 3:
    A4 = "B"
#-----------------       
if t14 == 1:
    B4 = "P"
elif t14 == 2:
    B4 = "A"
elif t14 >= 3:
    B4 = "B"
#-----------------       
if t15 == 1:
    C4 = "P"
elif t15 == 2:
    C4 = "A"
elif t15 >= 3:
    C4 = "B"
#-----------------       
if t16 == 1:
    D4 = "P"
elif t16 == 2:
    D4 = "A"
elif t16 >= 3:
    D4 = "B"
#-----------------    
    
    
print("-----------------")   
print("|", A1, "|", B1, "|", C1, "|",  D1, "|")
print("-----------------")
print("|", A2, "|", B2, "|", C2, "|",  D2, "|")
print("-----------------")
print("|", A3, "|", B3, "|", C3, "|",  D3, "|")
print("-----------------")
print("|", A4, "|", B4, "|", C4, "|",  D4, "|")

print("-----------------")

ConteoP= 0
ConteoB= 0
ConteoA= 0 

#--------------------------
if A1 == "P":
    ConteoP= ConteoP + 1
elif A1 == "B":
    ConteoB= ConteoB + 1
elif A1 == "A":
    ConteoA= ConteoA + 1
#--------------------------
if A2 == "P":
    ConteoP= ConteoP + 1
elif A2 == "B":
    ConteoB= ConteoB + 1
elif A2 == "A":
    ConteoA= ConteoA + 1
#--------------------------
if A3 == "P":
    ConteoP= ConteoP + 1
elif A3 == "B":
    ConteoB= ConteoB + 1
elif A3 == "A":
    ConteoA= ConteoA + 1
#--------------------------
if A4 == "P":
    ConteoP= ConteoP + 1
elif A4 == "B":
    ConteoB= ConteoB + 1
elif A4 == "A":
    ConteoA= ConteoA + 1
#-------------------------
if B1 == "P":
    ConteoP= ConteoP + 1
elif B1 == "B":
    ConteoB= ConteoB + 1
elif B1 == "A":
    ConteoA= ConteoA + 1
#--------------------------
if B2 == "P":
    ConteoP= ConteoP + 1
elif B2 == "B":
    ConteoB= ConteoB + 1
elif B2 == "A":
    ConteoA= ConteoA + 1
#--------------------------    
if B3 == "P":
    ConteoP= ConteoP + 1
elif B3 == "B":
    ConteoB= ConteoB + 1
elif B3 == "A":
    ConteoA= ConteoA + 1
#--------------------------
if B4 == "P":
    ConteoP= ConteoP + 1
elif B4 == "B":
    ConteoB= ConteoB + 1
elif B4 == "A":
    ConteoA= ConteoA + 1
#--------------------------
if C1 == "P":
    ConteoP= ConteoP + 1
elif C1 == "B":
    ConteoB= ConteoB + 1
elif C1 == "A":
    ConteoA= ConteoA + 1
#--------------------------
if C2 == "P":
    ConteoP= ConteoP + 1
elif C2 == "B":
    ConteoB= ConteoB + 1
elif C2 == "A":
    ConteoA= ConteoA + 1
#--------------------------
if C3 == "P":
    ConteoP= ConteoP + 1
elif C3 == "B":
    ConteoB= ConteoB + 1
elif C3 == "A":
    ConteoA= ConteoA + 1
#--------------------------    
if C4 == "P":
    ConteoP= ConteoP + 1
elif C4 == "B":
    ConteoB= ConteoB + 1
elif C4 == "A":
    ConteoA= ConteoA + 1
#--------------------------
if D1 == "P":
    ConteoP= ConteoP + 1
elif D1 == "B":
    ConteoB= ConteoB + 1
elif D1 == "A":
    ConteoA= ConteoA + 1
#--------------------------
if D2 == "P":
    ConteoP= ConteoP + 1
elif D2 == "B":
    ConteoB= ConteoB + 1
elif D2 == "A":
    ConteoA= ConteoA + 1
#--------------------------
if D3 == "P":
    ConteoP= ConteoP + 1
elif D3 == "B":
    ConteoB= ConteoB + 1
elif D3 == "A":
    ConteoA= ConteoA + 1
#--------------------------
if D4 == "P":
    ConteoP= ConteoP + 1
elif D4 == "B":
    ConteoB= ConteoB + 1
elif D4 == "A":
    ConteoA= ConteoA + 1
#--------------------------

divP = (ConteoP/16)*100
divB = (ConteoB/16)*100

print("existen todas estas P: ", ConteoP)
print("existen todas estas B: ", ConteoB)
print("existen todas estas A: ", ConteoA)

print("el porcentaje de aparicion es ", divP,"%")
print("el porcentaje de aparicion es ", divB,"%")

if divP == divB:
    print("Ambas especies tienen el mismo porcentaje de ocurrencia")
if divP > divB:
    print("Las especies de P tienen mayor ocurrencia que B")
else: 
    print("Las especies de B tienen mayor ocurrencia que P")






