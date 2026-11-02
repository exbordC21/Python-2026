# 6. Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
# casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesa-
# rias para poder realizar las siguientes actividades:
# a. eliminar el nodo que contiene la información de Linterna Verde;
# b. mostrar el año de aparición de Wolverine;
# c. cambiar la casa de Dr. Strange a Marvel;
# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# “traje” o “armadura”; 
# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# sea anterior a 1963;
# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
# g. mostrar toda la información de Flash y Star-Lord;
# h. listar los superhéroes que comienzan con la letra B, M y S;
# i. determinar cuántos superhéroes hay de cada casa de comic.

from list_ import List

print()
print("Ejercicio 5")
print()

class Superheroe:
    def __init__(self, name, year, house, bio):
        self.name=name
        self.year=year
        self.house=house
        self.bio=bio
        
    def __str__(self):
        return f"Nombre: {self.name} | Año: {self.year} | Casa: {self.house} | Bio: {self.bio}"

def by_name(item):
    return item.name
    
heroes = List()
heroes.add_criterion('name',by_name)

heroes.append(Superheroe("Linterna Verde", 1940, "DC", "Posee un anillo de poder y un traje especial."))
heroes.append(Superheroe("Wolverine", 1974, "Marvel", "Mutante con garras de adamantium y factor de curación."))
heroes.append(Superheroe("Dr. Strange", 1963, "DC", "Hechicero supremo de las artes místicas."))
heroes.append(Superheroe("Capitana Marvel", 1968, "Marvel", "Guerrera Kree con poderes cósmicos."))
heroes.append(Superheroe("Mujer Maravilla", 1941, "DC", "Princesa amazona con armadura y lazo de la verdad."))
heroes.append(Superheroe("Flash", 1940, "DC", "El hombre más rápido vivo."))
heroes.append(Superheroe("Star-Lord", 1976, "Marvel", "Líder intergaláctico de los Guardianes."))
heroes.append(Superheroe("Batman", 1939, "DC", "Vengador nocturno que usa un traje táctico."))
heroes.append(Superheroe("Superman", 1938, "DC", "Último hijo de Krypton."))

# a
eliminado=heroes.delete_value("Linterna Verde",'name')
print(f"Linterna Verde eliminado: {eliminado.name if eliminado else 'No encontrado'}")

print()

# b
pos_wolv=heroes.search("Wolverine",'name')
if pos_wolv is not None:
    print(f"año de aparicion de Wolverine: {heroes[pos_wolv].year}")   
    
# c
pos_strange=heroes.search("Dr. Strange",'name')
if pos_strange is not None:
    heroes[pos_strange].house = "Marvel"
    
print()   
    
# d
print("Superhéroes con 'traje' o 'armadura' en su biografía:")
for h in heroes:
    if "traje" in h.bio.lower() or "armadura" in h.bio.lower():
        print(f"  - {h.name}")
    
print()
    
# e
print("Superhéroes con aparición anterior a 1963:")
for h in heroes:
    if h.year < 1963:
        print(f"  - {h.name} ({h.house}) - Año: {h.year}")

print()
   
# f
print("Casas de Capitana Marvel y Mujer Maravilla:")
for nombre in ["Capitana Marvel", "Mujer Maravilla"]:
    pos = heroes.search(nombre, 'name')
    if pos is not None:
        print(f"  - {heroes[pos].name}: {heroes[pos].house}")

print()

# g
print("Información completa de Flash y Star-Lord:")
for nombre in ["Flash", "Star-Lord"]:
    pos = heroes.search(nombre, 'name')
    if pos is not None:
        print(f"  - {heroes[pos]}")

print()

# h
print("Superhéroes que comienzan con B, M o S:")
for h in heroes:
    if h.name.startswith(('B', 'M', 'S')):
        print(f"  - {h.name}")
        
print()
        
# i
count_marvel = 0
count_dc = 0
for h in heroes:
    if h.house.lower() == "marvel":
        count_marvel += 1
    elif h.house.lower() == "dc":
        count_dc += 1

print(f"Conteo por casa de cómic:")
print(f" Marvel: {count_marvel}")
print(f" DC: {count_dc}")


print()
print("Ejercicio 15")
print()

# 15. Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, can-
# tidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y ade-
# más la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver
# las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
# a. obtener la cantidad de Pokémons de un determinado entrenador;
# b. listar los entrenadores que hayan ganado más de tres torneos;
# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
# d. mostrar todos los datos de un entrenador y sus Pokémos;
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# (tipo y subtipo);
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# i. mostrar los entrenadores que tienen Pokémons repetidos;
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Te-
# rrakion o Wingull;
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;

from list_ import List

class Pokemon:
    def __init__(self, name, level, tipo, subtipo):
        self.name = name
        self.level = level
        self.tipo = tipo
        self.subtipo = subtipo
    def __str__(self):
        return f" -> Pokémon: {self.name} | Nivel: {self.level} | Tipo: {self.tipo}/{self.subtipo}"

class Entrenador:
    def __init__(self, name, torneos_ganados, batallas_perdidas, batallas_ganadas):
        self.name = name
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas
        self.pokemons = List()  
    def __str__(self):
        return f" Entrenador: {self.name} | Torneos: {self.torneos_ganados} | Ganadas: {self.batallas_ganadas} | Perdidas: {self.batallas_perdidas}"

def by_trainer_name(item):
    return item.name

def by_pokemon_name(item):
    return item.name

entrenadores = List()
entrenadores.add_criterion('name', by_trainer_name)

ash = Entrenador("Ash", 4, 10, 40)
ash.pokemons.add_criterion('name', by_pokemon_name)
ash.pokemons.append(Pokemon("Pikachu", 85, "Electrico", "Ninguno"))
ash.pokemons.append(Pokemon("Charizard", 90, "Fuego", "Volador"))
ash.pokemons.append(Pokemon("Bulbasaur", 70, "Planta", "Veneno"))
entrenadores.append(ash)

misty = Entrenador("Misty", 2, 5, 25)
misty.pokemons.add_criterion('name', by_pokemon_name)
misty.pokemons.append(Pokemon("Starmie", 65, "Agua", "Psiquico"))
misty.pokemons.append(Pokemon("Wingull", 40, "Agua", "Volador"))
entrenadores.append(misty)

brock = Entrenador("Brock", 1, 8, 20)
brock.pokemons.add_criterion('name', by_pokemon_name)
brock.pokemons.append(Pokemon("Onix", 60, "Roca", "Tierra"))
brock.pokemons.append(Pokemon("Tyrantrum", 75, "Roca", "Dragon"))
entrenadores.append(brock)


# a.
nombre_buscado = "Ash"
pos = entrenadores.search(nombre_buscado, 'name')
if pos is not None:
    print(f"Cantidad de Pokémon de {nombre_buscado}: {entrenadores[pos].pokemons.size()}")

print()

# b.
print("Entrenadores con más de 3 torneos ganados:")
for e in entrenadores:
    if e.torneos_ganados > 3:
        print(f" - {e.name} ({e.torneos_ganados} torneos)")

print()

# c.
max_torneos = -1
entrenador_top = None
for e in entrenadores:
    if e.torneos_ganados > max_torneos:
        max_torneos = e.torneos_ganados
        entrenador_top = e

if entrenador_top and entrenador_top.pokemons.size() > 0:
    poke_mayor = entrenador_top.pokemons[0]
    for p in entrenador_top.pokemons:
        if p.level > poke_mayor.level:
            poke_mayor = p
    print(f"Pokémon de mayor nivel del entrenador con más torneos ({entrenador_top.name}):")
    print(f" - {poke_mayor.name} (Nivel {poke_mayor.level})")

print()

# d.
print("Datos completos de todos los entrenadores y sus Pokémon:")
for e in entrenadores:
    print(f"  {e}")
    for p in e.pokemons:
        print(f"  {p}")

print()

# e.
print("Entrenadores con > 79% de batallas ganadas:")
for e in entrenadores:
    total_batallas = e.batallas_ganadas + e.batallas_perdidas
    if total_batallas > 0:
        porcentaje = (e.batallas_ganadas / total_batallas) * 100
        if porcentaje > 79:
            print(f" - {e.name} ({porcentaje:.1f}%)")

print()

# f.
print("Entrenadores con Fuego y Planta o (Agua y Volador):")
for e in entrenadores:
    tiene_fuego = any(p.tipo.lower() == "fuego" for p in e.pokemons)
    tiene_planta = any(p.tipo.lower() == "planta" for p in e.pokemons)
    tiene_agua_volador = any(p.tipo.lower() == "agua" and p.subtipo.lower() == "volador" for p in e.pokemons)
    if (tiene_fuego and tiene_planta) or tiene_agua_volador:
        print(f" - {e.name}")

print()

# g.
nombre_g = "Ash"
pos_g = entrenadores.search(nombre_g, 'name')
if pos_g is not None and entrenadores[pos_g].pokemons.size() > 0:
    ent_g = entrenadores[pos_g]
    suma_niveles = sum(p.level for p in ent_g.pokemons)
    promedio = suma_niveles / ent_g.pokemons.size()
    print(f"Promedio de nivel de los Pokémon de {nombre_g}: {promedio:.1f}")

print()

# h.
poke_buscado = "Pikachu"
contador_entrenadores = 0
for e in entrenadores:
    for p in e.pokemons:
        if p.name.lower() == poke_buscado.lower():
            contador_entrenadores += 1
            break
print(f"Entrenadores que tienen a {poke_buscado}: {contador_entrenadores}")

print()

# i.
print("Entrenadores con Pokémon repetidos:")
for e in entrenadores:
    nombres_pokes = [p.name for p in e.pokemons]
    if len(nombres_pokes) != len(set(nombres_pokes)):
        print(f" - {e.name}")

print()

# j.
buscados = ["tyrantrum", "terrakion", "wingull"]
print("Entrenadores con Tyrantrum, Terrakion o Wingull:")
for e in entrenadores:
    encontro = any(p.name.lower() in buscados for p in e.pokemons)
    if encontro:
        print(f" - {e.name}")

print()

# k.
entrenador_x = "Ash"
pokemon_y = "Charizard"

pos_x = entrenadores.search(entrenador_x, 'name')
if pos_x is not None:
    ent_x = entrenadores[pos_x]
    poke_encontrado = None
    for p in ent_x.pokemons:
        if p.name.lower() == pokemon_y.lower():
            poke_encontrado = p
            break
            
    if poke_encontrado:
        print(f"El entrenador {entrenador_x} tiene al Pokémon {pokemon_y}:")
        print(f" - {ent_x}")
        print(f" - {poke_encontrado}")
    else:
        print(f"El entrenador {entrenador_x} no tiene al Pokémon {pokemon_y}.")