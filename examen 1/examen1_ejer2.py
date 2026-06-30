from list_ import List
from super_heroes_data import superheroes
from Queue import Queue

# Ejercicio 2: Dada una lista de personajes de marvel (usar el archivo adjunto) debe tener 100 o mas, resolver:

# Listado ordenado de manera ascendente por nombre de los personajes.

# Determinar en que posicion esta The Thing y Rocket Raccoon.

# Listar todos los villanos de la lista.

# Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.

# Listar los superheores que comienzan con  Bl, G, My, y W.

# Listado de personajes ordenado por nombre real de manera ascendente de los personajes.

# Listado de superheroes ordenados por fecha de aparación.

# Modificar el nombre real de Ant Man a Scott Lang.

# Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.

# Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.


class Personaje:
    def __init__(self, name, alias, real_name, short_bio, first_appearance, is_villain):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.bio = short_bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain

    def __str__(self):
        if self.is_villain:
            tipo = "Villano"
        else:
            tipo = "Héroe"
        return f"{self.name} ({self.alias}) - Real: {self.real_name} - Año: {self.first_appearance} [{tipo}]"


def by_name(item):
    return item.name

def by_real_name(item):
    if item.real_name is None:
        return ""
    return item.real_name

def by_appearance(item):
    return item.first_appearance

list_heroes = List()
list_heroes.add_criterion('name', by_name)
list_heroes.add_criterion('real_name', by_real_name)
list_heroes.add_criterion('year', by_appearance)

for hero in superheroes:
    list_heroes.append(
        Personaje(
            hero['name'], 
            hero['alias'], 
            hero['real_name'], 
            hero['short_bio'], 
            hero['first_appearance'], 
            hero['is_villain']
        )
    )
    
    
# Listado ordenado de manera ascendente por nombre de los personajes.
   
list_heroes.sort_by_criterion('name')
list_heroes.show()


print()

# Determinar en que posicion esta The Thing y Rocket Raccoon.

pos_thing = list_heroes.search("The Thing", 'name')
pos_rocket = list_heroes.search("Rocket Raccoon", 'name')

if pos_thing is not None:
    print(f"The Thing se encuentra en la posicion: {pos_thing}")
else:
    print("The Thing no se encuentra en la lista.")

print()
    
if pos_rocket is not None:
    print(f"Rocket Raccoon se encuentra en la posicion: {pos_rocket}")
else:
    print("Rocket Raccoon no se encuentra en la lista.")
    
    
print()    
    
# Listar todos los villanos de la lista.

for per in list_heroes:
    if per.is_villain:
        print(per)
        

print()

# Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.

cola_villano=Queue()
colaux=Queue()
for per in list_heroes:
    if per.is_villain:
        cola_villano.arrive(per)
        
while cola_villano.size() > 0:
    villano=cola_villano.attention()
    if villano.first_appearance < 1980:
        print(f"{villano.name} ({villano.first_appearance})")
    
    colaux.arrive(villano)

while colaux.size() > 0:
    cola_villano.arrive(colaux.attention())
    

print()

# Listar los superheores que comienzan con  Bl, G, My, y W.

for per in list_heroes:
    if not per.is_villain and per.name.startswith(('Bl', 'G', 'My', 'W')):
        print(per)
        

print()

# Listado de personajes ordenado por nombre real de manera ascendente de los personajes.

list_heroes.sort_by_criterion('real_name')
list_heroes.show()


print()

# Listado de superheroes ordenados por fecha de aparación.
list_heroes.sort_by_criterion('year')
for per in list_heroes:
    if not per.is_villain:
        print(f'{per.first_appearance} {per.name}')
        
        
print()     
        
# Modificar el nombre real de Ant Man a Scott Lang.

pos = list_heroes.search("Ant Man", 'name')
if pos is not None:
    print(list_heroes[pos])
    list_heroes[pos].real_name = "Scott Lang"
    print(f"Se actualizo Ant Man:")
    print(list_heroes[pos])
else:
    print("Ant Man no fue encontrado en la lista.")
    
    
print()  
    
# Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.

list_heroes.filter_contain_on_bio(['time-traveling', 'suit'])


print()

# Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.

electro_eliminado = list_heroes.delete_value("Electro", 'name')
zemo_eliminado = list_heroes.delete_value("Baron Zemo", 'name')

if electro_eliminado:
    print(f"Se elimino: {electro_eliminado}")
else:
    print("Electro no se encontraba en la lista.")

if zemo_eliminado:
    print(f"Se elimino: {zemo_eliminado}")
else:
    print("Baron Zemo no se encontraba en la lista.")


