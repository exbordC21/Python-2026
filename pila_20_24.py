#Realizar un algoritmo que registre los movimientos de un robot, los datos que se guardan son
#cantidad de pasos y dirección –suponga que el robot solo puede moverse en ocho direcciones:
#norte, sur, este, oeste, noreste, noroeste, sureste y suroeste–. Luego desarrolle otro algoritmo
#que genere la secuencia de movimientos necesarios para hacer volver al robot a su lugar de
#partida, retornando por el mismo camino que fue.
from Stack import Stack

pila=Stack()
pilaux=Stack()

DIRECCIONES_OPUESTAS = {
    "norte": "sur",
    "sur": "norte",
    "este": "oeste",
    "oeste": "este",
    "noreste": "suroeste",
    "suroeste": "noreste",
    "noroeste": "sureste",
    "sureste": "noroeste"
}

movimientos = [
        (5, "norte"),
        (10, "este"),
        (3, "noreste")
    ]

for pasos, direccion in movimientos:
    pila.push((pasos,direccion))
     
def volver(pil, opu,pil2):
    retorno=[]
    while pil.size() > 0:
        pasos, direccion = pil.pop()
        vuelta=opu[direccion]
        retorno.append((pasos, vuelta))
        pil2.push((pasos, direccion))
    return retorno

while pilaux.size() >0:
    pila.push(pilaux.pop())
    
print("--- Secuencia de Retorno ---")

La_vuelta=volver(pila,DIRECCIONES_OPUESTAS,pilaux)
for pasos, direccion in La_vuelta:
    print(f"El roboto se movio {pasos} pasos, hacia {direccion} para regresar")
    

# 24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
# su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
# necesarias para resolver las siguientes actividades:

# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posi-
# ción uno la cima de la pila;

# b. determinar los personajes que participaron en más de 5 películas de la saga, además indi-
# car la cantidad de películas en la que aparece;

# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);

# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.
print()
print("ejercicio 24")

pila_personajes = Stack()
pilaaux = Stack()
Personajes=[('Iron Man',5),("Rocket Raccoon",6),('Capitan America',9),('Groot',2),('Black Widow',8)]
buscado="Black Widow"
buscado_groot = ('Groot',2)
buscado_rocket = ("Rocket Raccoon",6)

for element in Personajes:
    pila_personajes.push(element) 


def encontrar_groot(pila_personajes, buscado_groot):
    for i in range (pila_personajes.size()):
        if buscado_groot != pila_personajes.on_top():
            data=pila_personajes.pop()
            pilaaux.push(data)
        elif buscado_groot == pila_personajes.on_top():
            data=pila_personajes.pop()
            pilaaux.push(data)
            posicion = i
    return(posicion)

def encontrar_rocket(pila_personajes,buscado_rocket):
    for i in range (pila_personajes.size()):
        if buscado_rocket != pila_personajes.on_top():
            data=pila_personajes.pop()
            pilaaux.push(data)
        elif buscado_rocket == pila_personajes.on_top():
            data=pila_personajes.pop()
            pilaaux.push(data)
            posicion_2 = i
    return (posicion_2)


print(buscado_rocket, "esta en la posicion: ", encontrar_rocket(pila_personajes, buscado_rocket))
while pilaaux.size() >0:
    pila_personajes.push(pilaaux.pop())

print(buscado_groot,"esta en la posicion", encontrar_groot(pila_personajes, buscado_groot))
while pilaaux.size() >0:
    pila_personajes.push(pilaaux.pop())


while pila_personajes.size()>0:
        cuebana3=pila_personajes.on_top()[-1]
        if cuebana3<5:
            data2=pila_personajes.pop()
            pilaaux.push(data2)
        elif cuebana3>5:
            print(pila_personajes.on_top()[-2],"aparece en mas de 5 peliculas y tiene:",cuebana3,"peliculas")
            data2=pila_personajes.pop()
            pilaaux.push(data2)
        else:
            data2=pila_personajes.pop()
            pilaaux.push(data2)

while pilaaux.size() >0:
    pila_personajes.push(pilaaux.pop())


while pila_personajes.size()>0:
    peliswidow=pila_personajes.on_top()[-1]
    nombre=pila_personajes.on_top()[-2]
    if nombre == buscado:
        print(buscado,"tiene",peliswidow,"peliculas")
        data3=pila_personajes.pop()
        pilaaux.push(data3)
    else:
        data3=pila_personajes.pop()
        pilaaux.push(data3)

while pilaaux.size() >0:
    pila_personajes.push(pilaaux.pop())


while pila_personajes.size()>0:
    nombre2=pila_personajes.on_top()[-2]
    if (nombre2[:1] == "C" ):
        print("El nombre de ",nombre2,"empieza por: C")
        data4=pila_personajes.pop()
        pilaaux.push(data4)
    elif (nombre2[:1]=="D"):
        print("El nombre de ",nombre2,"empieza por: D") 
        data4=pila_personajes.pop()
        pilaaux.push(data4)
    elif (nombre2[:1]=="G"):
        print("El nombre de ",nombre2,"empieza por: G")
        data4=pila_personajes.pop()
        pilaaux.push(data4)
    else:
        data4=pila_personajes.pop()
        pilaaux.push(data4)
        
while pilaaux.size() >0:
    pila_personajes.push(pilaaux.pop())

print(pila_personajes)