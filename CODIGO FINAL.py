from random import randint

t1 = randint(1,4) # 16 variables representando cada sub-cuadrante y generando numeros aleatorios
t2 = randint(1,4) # del 1 al 4
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

if t1 == 1:  # Detectamos si t1 equivale a 1, 2 y si t1 es mayor o igual a 3 saldrá B
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
#-------------------------

# Creamos 3 variables para contar
conteoP = 0
conteoB = 0
conteoA = 0
#--------------------------------------------------------------------------------------------------
if A1 == "P": # Por cada P se agregara 1 a conteoP
    conteoP = conteoP + 1
elif A1 == "B": # Por cada B se agregara 1 a conteoB
    conteoB = conteoB + 1
elif A1 == "A": # por cada A se agregara 1 a conteo A
    conteoA = conteoA + 1
#--------------------------------------------------------------------------------------------------
if A2 == "P": # Por cada P se agregara 1 a conteoP
    conteoP = conteoP + 1
elif A2 == "B": # Por cada B se agregara 1 a conteoB
    conteoB = conteoB + 1
elif A2 == "A": # por cada A se agregara 1 a conteo A
    conteoA = conteoA + 1
#--------------------------------------------------------------------------------------------------
if A3 == "P":
    conteoP = conteoP + 1
elif A3 == "B":
    conteoB = conteoB + 1
elif A3 == "A":
    conteoA = conteoA + 1
#--------------------------------------------------------------------------------------------------
if A4 == "P":
    conteoP = conteoP + 1
elif A4 == "B":
    conteoB = conteoB + 1
elif A4 == "A":
    conteoA = conteoA + 1
#--------------------------------------------------------------------------------------------------
if B1 == "P":
    conteoP = conteoP + 1
elif B1 == "B":
    conteoB = conteoB + 1
elif B1 == "A":
    conteoA = conteoA + 1
#--------------------------------------------------------------------------------------------------
if B2 == "P":
    conteoP = conteoP + 1
elif B2 == "B":
    conteoB = conteoB + 1
elif B2 == "A":
    conteoA = conteoA + 1
#--------------------------------------------------------------------------------------------------
if B3 == "P":
    conteoP = conteoP + 1
elif B3 == "B":
    conteoB = conteoB + 1
elif B3 == "A":
    conteoA = conteoA + 1
#--------------------------------------------------------------------------------------------------
if B4 == "P":
    conteoP = conteoP + 1
elif B4 == "B":
    conteoB = conteoB + 1
elif B4 == "A":
    conteoA = conteoA + 1
#--------------------------------------------------------------------------------------------------
if C1 == "P":
    conteoP = conteoP + 1
elif C1 == "B":
    conteoB = conteoB + 1
elif C1 == "A":
    conteoA = conteoA + 1
#--------------------------------------------------------------------------------------------------
if C2 == "P":
    conteoP = conteoP + 1
elif C2 == "B":
    conteoB = conteoB + 1
elif C2 == "A":
    conteoA = conteoA + 1
#--------------------------------------------------------------------------------------------------
if C3 == "P":
    conteoP = conteoP + 1
elif C3 == "B":
    conteoB = conteoB + 1
elif C3 == "A":
    conteoA = conteoA + 1
#--------------------------------------------------------------------------------------------------
if C4 == "P":
    conteoP = conteoP + 1
elif C4 == "B":
    conteoB = conteoB + 1
elif C4 == "A":
    conteoA = conteoA + 1
#--------------------------------------------------------------------------------------------------
if D1 == "P":
    conteoP = conteoP + 1
elif D1 == "B":
    conteoB = conteoB + 1
elif D1 == "A":
    conteoA = conteoA + 1
#--------------------------------------------------------------------------------------------------
if D2 == "P":
    conteoP = conteoP + 1
elif D2 == "B":
    conteoB = conteoB + 1
elif D2 == "A":
    conteoA = conteoA + 1
#--------------------------------------------------------------------------------------------------
if D3 == "P":
    conteoP = conteoP + 1
elif D3 == "B":
    conteoB = conteoB + 1
elif D3 == "A":
    conteoA = conteoA + 1
#--------------------------------------------------------------------------------------------------
if D4 == "P":
    conteoP = conteoP + 1
elif D4 == "B":
    conteoB = conteoB + 1
elif D4 == "A":
    conteoA = conteoA + 1
#--------------------------------------------------------------------------------------------------
divP = (conteoP/16)*100 # Dividimos la cantidad de estados por 16 y lo multiplicamos por 10
divB = (conteoB/16)*100 # para obtener el porcentaje de aparicion
divA = (conteoA/16)*100 # Y asi obtenemos el porcentaje de Plantas, Agua y Bacterias
#--------------------------------------------------------------------------------------------------
print("Existen todas estas P: ", conteoP) # Expresamos la cantidad de P, B y A
print("Existen todas estas B: ", conteoB)
print("Existen todas estas A: ", conteoA)
#--------------------------------------------------------------------------------------------------
print("El porcentaje de aparicion de P es: ", divP,"%") # Expresamos el porcentaje de cada estado
print("El porcentaje de aparicion de B es: ", divB,"%")
print("El porcentaje de aparicion de A es: ", divA,"%")
#--------------------------------------------------------------------------------------------------
if divP == divB:    # Creamos una secuencia if para indicar similar porcentaje de ocurrencia
    print("Ambas especies tienen el mismo porcentaje de ocurrencia")
elif divP > divB:
    print("Las especies de P tienen mayor ocurrencia que B") # En caso de que el argumento anterior no cumpla, se dira que
else:                                                        # DivP es mayor que DivB y viceversa
    print("Las especies de B tienen mayor ocurrencia que P")
#------------------------------------------------------------------------------------------------------------------
if B2 == "P":
    if A1 == "B" and B1 == "B" and C1 == "B" and A2 == "B" and C2  == "B"and A3 == "B" and B3 == "B" and C3 == "B":
        print("Planta bajo ataque")
        
if B3 == "P":
    if A1 == "B" and B2 == "B" and C2 == "B" and A3 == "B" and C3 == "B"and A4 == "B" and B4 == "B" and C4 == "B":
        print("Planta bajo ataque")
        
if C2 == "P":
    if B1 == "B" and C1 == "B" and D1 == "B" and B2 == "B" and D2  == "B"and B3 == "B" and C3 == "B" and D3 == "B":
        print("Planta bajo ataque")
        
if C3 == "P":
    if B2 == "B" and C2 == "B" and D2 == "B" and B3 == "B" and D3 == "B"and B4 == "B" and C4 == "B" and D4 == "B":
        print("Planta bajo ataque")
#-------------------------------------------------------------------------------------------------------------------
if B2 == "A":
    if A1 == "P" and B1 == "P" and C1 == "P" and A2 == "P" and C2  == "P"and A3 == "P" and B3 == "P" and C3 == "P":
        print("Agua en riesgo de escasez")
        
if B3 == "A":
    if A1 == "P" and B2 == "P" and C2 == "P" and A3 == "P" and C3 == "P"and A4 == "P" and B4 == "P" and C4 == "P":
        print("Agua en riesgo de escasez")
        
if C2 == "A":
    if B1 == "P" and C1 == "P" and D1 == "P" and B2 == "P" and D2  == "P"and B3 == "P" and C3 == "P" and D3 == "P":
        print("Agua en riesgo de escasez")
        
if C3 == "A":
    if B2 == "P" and C2 == "P" and D2 == "P" and B3 == "P" and D3 == "P"and B4 == "P" and C4 == "P" and D4 == "P":
        print("Agua en riesgo de escasez") 
