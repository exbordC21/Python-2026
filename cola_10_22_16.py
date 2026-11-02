from Queue import Queue
from Stack import Stack
from heap import HeapMax
from heap import HeapMin
# 10. Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
# de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
# resolver las siguientes actividades:

# a. escribir una función que elimine de la cola todas las notificaciones de Facebook;

# b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
# la palabra ‘Python’, sin perder datos en la cola;

# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
# 11:43 y las 15:57, y determinar cuántas son. 

colanoti=Queue()

notificaciones_ejemplo = [
    {'hora': '10:15', 'app': 'Facebook', 'mensaje': 'A Juan le gustó tu foto.'},
    {'hora': '11:50', 'app': 'Twitter', 'mensaje': 'Aprendiendo Python en 2026!'},
    {'hora': '13:00', 'app': 'WhatsApp', 'mensaje': '¿Almorzamos?'},
    {'hora': '14:20', 'app': 'Facebook', 'mensaje': 'Cumpleaños de María hoy.'},
    {'hora': '15:10', 'app': 'Twitter', 'mensaje': 'Mundo Python avanzado.'},
    {'hora': '16:45', 'app': 'Twitter', 'mensaje': 'Buenas tardes a todos.'},
]


def carga_cola(colanoti,notificaciones_ejemplo):
    for elements in notificaciones_ejemplo:
        colanoti.arrive(elements)
     

# a. escribir una función que elimine de la cola todas las notificaciones de Facebook;

def elminar_face(colanoti):
    colaaux=Queue()
    while colanoti.size() > 0:
        notificacion=colanoti.attention()
        if notificacion['app'] !='Facebook':
            colaaux.arrive(notificacion)
        else:
            print(f"Se elimino de la cola --> [{notificacion['hora']}] {notificacion['app']}: {notificacion['mensaje']}")

    while colaaux.size() > 0:
        colanoti.arrive(colaaux.attention())

        
        
# b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
# la palabra ‘Python’, sin perder datos en la cola;  
   
def mostrar_x(colanoti):
   for i in range(colanoti.size()):
       notificacion = colanoti.move_to_end()
       if notificacion['app'] =='Twitter' and 'Python' in notificacion['mensaje']:
            print(f"[{notificacion['hora']}] {notificacion['app']}: {notificacion['mensaje']}")
            
               
# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
# 11:43 y las 15:57, y determinar cuántas son. 
        
def horario(colanoti):
    colaaux=Queue()
    pilaaux=Stack()
    contador=0
    while colanoti.size() > 0:
        noti=colanoti.attention()
        colaaux.arrive(noti)
        if noti['hora'] >= '11:43' and noti['hora'] <= '15:57':
            pilaaux.push(noti)
            contador+=1
            
    while colaaux.size() > 0:
        colanoti.arrive(colaaux.attention())
    
    return contador,pilaaux
        
        
       
carga_cola(colanoti,notificaciones_ejemplo)

print("")

elminar_face(colanoti)

print("")

mostrar_x(colanoti)

print("")

cont,pil=horario(colanoti)

def mostrar(cont,pil):
    aux=Stack()
    while pil.size() > 0:
        sacado=pil.pop()
        print(sacado)
        aux.push(sacado)
    
    while aux.size() > 0:
        pil.push(aux.pop())
        
    print("")   
    print(f'Hay {cont} elementos en la pila temporal')
    
mostrar(cont,pil)



print("") 
print("ejercicio 22") 
print("")

# Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce 
# el nombre del personaje, el nombre del superhéroe y su género (Masculino M y FemeninoF) 
# –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro-
# manoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.

personajes_marvel = [
    {'nombre': 'Tony Stark', 'superheroe': 'Iron Man', 'genero': 'M'},
    {'nombre': 'Steve Rogers', 'superheroe': 'Capitán América', 'genero': 'M'},
    {'nombre': 'Natasha Romanoff', 'superheroe': 'Black Widow', 'genero': 'F'},
    {'nombre': 'Wanda Maximoff', 'superheroe': 'Bruja Escarlata', 'genero': 'F'},
    {'nombre': 'Thor Odinson', 'superheroe': 'Thor', 'genero': 'M'},
    {'nombre': 'Carol Danvers', 'superheroe': 'Capitana Marvel', 'genero': 'F'},
    {'nombre': 'Bruce Banner', 'superheroe': 'Hulk', 'genero': 'M'},
    {'nombre': 'Peter Parker', 'superheroe': 'Spider-Man', 'genero': 'M'},
    {'nombre': 'Scott Lang', 'superheroe': 'Ant-Man', 'genero': 'M'}
]

cola_marvel=Queue()

def cargar(cola_marvel,personajes_marvel):
    for element in personajes_marvel:
        cola_marvel.arrive(element)
    

# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;

def nom_cap_marvel(cola_marvel):
    for i in range(cola_marvel.size()):
        personaje=cola_marvel.move_to_end()
        if personaje['superheroe'] == 'Capitana Marvel':   
            nombre=personaje['nombre']
            print(f'El nombre de la Capitana Marvel es {nombre}')


# b. mostrar los nombre de los superhéroes femeninos;

def nom_femeninos(cola_marvel):
    for i in range(cola_marvel.size()):
        personaje_femenino=cola_marvel.move_to_end()
        if personaje_femenino['genero'] == 'F':   
            nombre=personaje_femenino['nombre']
            print(f'Los nombres de los personajes femeninos son --> {nombre}')


# c. mostrar los nombres de los personajes masculinos;

def nom_masculinos(cola_marvel):
    for i in range(cola_marvel.size()):
        personaje_masculinos=cola_marvel.move_to_end()
        if personaje_masculinos['genero'] == 'M':   
            nombre=personaje_masculinos['nombre']
            print(f'Los nombres de los personajes masculinos son --> {nombre}')


# d. determinar el nombre del superhéroe del personaje Scott Lang;

def nom_Scott(cola_marvel):
    for i in range(cola_marvel.size()):
        personaje_scott=cola_marvel.move_to_end()
        if personaje_scott['nombre'] == 'Scott Lang':   
            nombre_super=personaje_scott['superheroe']
            print(f'El nombre del superheroe de Scott Lang es {nombre_super}')


# e. mostrar todo los datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S;

def nom_s(cola_marvel):
    for i in range(cola_marvel.size()):
        per_s=cola_marvel.move_to_end()
        if 'S' in per_s['superheroe']:
            print(per_s)
            

# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.

def nom_carol(cola_marvel):
    for i in range(cola_marvel.size()):
        personaje_carol=cola_marvel.move_to_end()
        if personaje_carol['nombre'] == 'Carol Danvers':   
            nombre_super=personaje_carol['superheroe']
            print(f'Carol Danvers se encuentra en la cola y el nombre de superheroe es {nombre_super}')

cargar(cola_marvel,personajes_marvel)  
   
nom_cap_marvel(cola_marvel)

print("")

nom_femeninos(cola_marvel)

print("")

nom_masculinos(cola_marvel)

print("")

nom_Scott(cola_marvel)

print("")

nom_s(cola_marvel)

print("")

nom_carol(cola_marvel)



print("")
print("ejercicio 16")
print("")
# Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
# criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la
# siguiente situación:
# a. cargue tres documentos de empleados (cada documento se representa solamente con
# un nombre).
# b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
# c. cargue dos documentos del staff de TI.
# d. cargue un documento del gerente.
# e. imprima los dos primeros documentos de la cola.
# f. cargue dos documentos de empleados y uno de gerente.
# g. imprima todos los documentos de la cola de impresión.

cola_impresion = HeapMin()

# a
cola_impresion.arrive("documento_juan",1)
cola_impresion.arrive("documento_roman",1)
cola_impresion.arrive("documento_nestor",1)

# b
print(cola_impresion.attention()[1])
print("")
# c
cola_impresion.arrive("documento_ramiro",2)
cola_impresion.arrive("documento_jose",2)

# d
cola_impresion.arrive("documento_kratos",3)

# e
print(cola_impresion.attention()[1])
print(cola_impresion.attention()[1])
print("")
# f
cola_impresion.arrive("documento_trhal",1)
cola_impresion.arrive("documento_artas",1)
cola_impresion.arrive("documento_rey lich",3)

while cola_impresion.size()>0:
    print(cola_impresion.attention()[1])
    


