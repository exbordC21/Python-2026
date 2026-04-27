#Desarrollar una función que permita convertir un número romano en un número decimal.

romanos = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def RaD ( rom, anterior=0):
    if not rom:
        return 0
    
    letra_actual = rom[-1]
    valor_actual = romanos[letra_actual]
    restante = rom[:-1]
     
    if valor_actual < anterior:
        return -valor_actual + RaD(restante, valor_actual)
    else:
        return valor_actual + RaD(restante, valor_actual)
    
print(f"XIV es: {RaD('XIV')}")   # Debería dar 14
print(f"MCMXCIV es: {RaD('MCMXCIV')}") # Debería dar 1994
print(f"IX es: {RaD('IX')}")     # Debería dar 9



#El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
#otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
#objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
#ayuda de la fuerza” realizar las siguientes actividades:

#a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
#queden más objetos en la mochila;

#b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
#car para encontrarlo;

#c. Utilizar un vector para representar la mochila.

mochila= " botella de agua", "Brújula galáctica", "Colgante de cristal rojo","Sable de luz", "Bastón electrificado"

def usar_la_fuerza(mochila, i=0):
    if len(mochila)==0:
        return print("la mochila esta vacia")
    elif len(mochila)==i:
        return print("no se encontro el sable de luz en la mochila de Luke Skywalker ")
    elif mochila[i]=="Sable de luz":
        return print("se ecnontro el sable de luz y se sacaron",i,"objetos para poder encontrarlo" )
    else:
        return usar_la_fuerza(mochila, i+1)
    
Luke_Skywalker= usar_la_fuerza(mochila)
    
    