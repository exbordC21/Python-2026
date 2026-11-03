# Ejercicio 1: Se tiene los datos de Pokémons de las 9 generaciones cargados de manera aleatoria (1025 en total) de los 
# cuales se conoce su nombre, número, tipo/tipos, debilidad frente a tipo/tipos, si tiene mega evolucion (bool) y si tiene 
# forma gigamax (bool) para el cual debemos construir tres árboles para acceder de manera eficiente a los datos contemplando lo siguiente:

# los índices de cada uno de los árboles deben ser nombre, número y tipo;

# mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último, la búsqueda debe ser por proximidad, es decir 
# si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–;

# mostrar todos los nombres de los Pokémons de un determinado tipo: fantasma, fuego, acero y eléctrico;

# realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;

# mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum;

# mostrar todos los tipos de Pokémons y cuántos hay de cada tipo;

# determinar cuantos Pokémons tienen megaevolucion.

# determinar cuantos Pokémons tiene forma gigamax.

# cargue al menos 100 Pokémons.



from tree import BinaryTree, Node
from Queue import Queue
from graph import Graph

print()
print("EJERCICIO 1")

class Pokemon:
    def __init__(self, number, name, types, weaknesses, has_mega, has_gigantamax):
        self.number = number                  
        self.name = name                      
        self.types = types                    
        self.weaknesses = weaknesses          
        self.has_mega = has_mega              
        self.has_gigantamax = has_gigantamax  

    def __str__(self):
        tipo_str = ", ".join(self.types)
        deb_str = ", ".join(self.weaknesses)
        mega = "Sí" if self.has_mega else "No"
        giga = "Sí" if self.has_gigantamax else "No"
        return f"#{self.number:04d} | {self.name} | Tipos: [{tipo_str}] | Debilidades: [{deb_str}] | Mega: {mega} | Gigamax: {giga}"

tree_name = BinaryTree()
tree_number = BinaryTree()
tree_type = BinaryTree()

pokemons_data = [
    (1, "Bulbasaur", ["Planta", "Veneno"], ["Fuego", "Hielo", "Volador", "Psíquico"], False, False),
    (2, "Ivysaur", ["Planta", "Veneno"], ["Fuego", "Hielo", "Volador", "Psíquico"], False, False),
    (3, "Venusaur", ["Planta", "Veneno"], ["Fuego", "Hielo", "Volador", "Psíquico"], True, True),
    (4, "Charmander", ["Fuego"], ["Agua", "Tierra", "Roca"], False, False),
    (5, "Charmeleon", ["Fuego"], ["Agua", "Tierra", "Roca"], False, False),
    (6, "Charizard", ["Fuego", "Volador"], ["Agua", "Eléctrico", "Roca"], True, True),
    (7, "Squirtle", ["Agua"], ["Eléctrico", "Planta"], False, False),
    (8, "Wartortle", ["Agua"], ["Eléctrico", "Planta"], False, False),
    (9, "Blastoise", ["Agua"], ["Eléctrico", "Planta"], True, True),
    (10, "Caterpie", ["Bicho"], ["Fuego", "Volador", "Roca"], False, False),
    (11, "Metapod", ["Bicho"], ["Fuego", "Volador", "Roca"], False, False),
    (12, "Butterfree", ["Bicho", "Volador"], ["Roca", "Fuego", "Eléctrico", "Hielo", "Volador"], False, True),
    (13, "Weedle", ["Bicho", "Veneno"], ["Fuego", "Volador", "Psíquico", "Roca"], False, False),
    (14, "Kakuna", ["Bicho", "Veneno"], ["Fuego", "Volador", "Psíquico", "Roca"], False, False),
    (15, "Beedrill", ["Bicho", "Veneno"], ["Fuego", "Volador", "Psíquico", "Roca"], True, False),
    (16, "Pidgey", ["Normal", "Volador"], ["Eléctrico", "Hielo", "Roca"], False, False),
    (17, "Pidgeotto", ["Normal", "Volador"], ["Eléctrico", "Hielo", "Roca"], False, False),
    (18, "Pidgeot", ["Normal", "Volador"], ["Eléctrico", "Hielo", "Roca"], True, False),
    (19, "Rattata", ["Normal"], ["Lucha"], False, False),
    (20, "Raticate", ["Normal"], ["Lucha"], False, False),
    (21, "Spearow", ["Normal", "Volador"], ["Eléctrico", "Hielo", "Roca"], False, False),
    (22, "Fearow", ["Normal", "Volador"], ["Eléctrico", "Hielo", "Roca"], False, False),
    (23, "Ekans", ["Veneno"], ["Tierra", "Psíquico"], False, False),
    (24, "Arbok", ["Veneno"], ["Tierra", "Psíquico"], False, False),
    (25, "Pikachu", ["Eléctrico"], ["Tierra"], False, True),
    (26, "Raichu", ["Eléctrico"], ["Tierra"], False, False),
    (27, "Sandshrew", ["Tierra"], ["Agua", "Planta", "Hielo"], False, False),
    (28, "Sandslash", ["Tierra"], ["Agua", "Planta", "Hielo"], False, False),
    (29, "Nidoran♀", ["Veneno"], ["Tierra", "Psíquico"], False, False),
    (30, "Nidorina", ["Veneno"], ["Tierra", "Psíquico"], False, False),
    (31, "Nidoqueen", ["Veneno", "Tierra"], ["Agua", "Hielo", "Tierra", "Psíquico"], False, False),
    (32, "Nidoran♂", ["Veneno"], ["Tierra", "Psíquico"], False, False),
    (33, "Nidorino", ["Veneno"], ["Tierra", "Psíquico"], False, False),
    (34, "Nidoking", ["Veneno", "Tierra"], ["Agua", "Hielo", "Tierra", "Psíquico"], False, False),
    (35, "Clefairy", ["Hada"], ["Veneno", "Acero"], False, False),
    (36, "Clefable", ["Hada"], ["Veneno", "Acero"], False, False),
    (37, "Vulpix", ["Fuego"], ["Agua", "Tierra", "Roca"], False, False),
    (38, "Ninetales", ["Fuego"], ["Agua", "Tierra", "Roca"], False, False),
    (39, "Jigglypuff", ["Normal", "Hada"], ["Veneno", "Acero"], False, False),
    (40, "Wigglytuff", ["Normal", "Hada"], ["Veneno", "Acero"], False, False),
    (41, "Zubat", ["Veneno", "Volador"], ["Eléctrico", "Hielo", "Psíquico", "Roca"], False, False),
    (42, "Golbat", ["Veneno", "Volador"], ["Eléctrico", "Hielo", "Psíquico", "Roca"], False, False),
    (43, "Oddish", ["Planta", "Veneno"], ["Fuego", "Hielo", "Volador", "Psíquico"], False, False),
    (44, "Gloom", ["Planta", "Veneno"], ["Fuego", "Hielo", "Volador", "Psíquico"], False, False),
    (45, "Vileplume", ["Planta", "Veneno"], ["Fuego", "Hielo", "Volador", "Psíquico"], False, False),
    (46, "Paras", ["Bicho", "Planta"], ["Fuego", "Volador", "Veneno", "Roca", "Bicho", "Hielo"], False, False),
    (47, "Parasect", ["Bicho", "Planta"], ["Fuego", "Volador", "Veneno", "Roca", "Bicho", "Hielo"], False, False),
    (48, "Venonat", ["Bicho", "Veneno"], ["Fuego", "Volador", "Psíquico", "Roca"], False, False),
    (49, "Venomoth", ["Bicho", "Veneno"], ["Fuego", "Volador", "Psíquico", "Roca"], False, False),
    (50, "Diglett", ["Tierra"], ["Agua", "Planta", "Hielo"], False, False),
    (51, "Dugtrio", ["Tierra"], ["Agua", "Planta", "Hielo"], False, False),
    (52, "Meowth", ["Normal"], ["Lucha"], False, True),
    (53, "Persian", ["Normal"], ["Lucha"], False, False),
    (54, "Psyduck", ["Agua"], ["Planta", "Eléctrico"], False, False),
    (55, "Golduck", ["Agua"], ["Planta", "Eléctrico"], False, False),
    (56, "Mankey", ["Lucha"], ["Volador", "Psíquico", "Hada"], False, False),
    (57, "Primeape", ["Lucha"], ["Volador", "Psíquico", "Hada"], False, False),
    (58, "Growlithe", ["Fuego"], ["Agua", "Tierra", "Roca"], False, False),
    (59, "Arcanine", ["Fuego"], ["Agua", "Tierra", "Roca"], False, False),
    (60, "Poliwag", ["Agua"], ["Planta", "Eléctrico"], False, False),
    (61, "Poliwhirl", ["Agua"], ["Planta", "Eléctrico"], False, False),
    (62, "Poliwrath", ["Agua", "Lucha"], ["Planta", "Eléctrico", "Volador", "Psíquico", "Hada"], False, False),
    (63, "Abra", ["Psíquico"], ["Bicho", "Fantasma", "Siniestro"], False, False),
    (64, "Kadabra", ["Psíquico"], ["Bicho", "Fantasma", "Siniestro"], False, False),
    (65, "Alakazam", ["Psíquico"], ["Bicho", "Fantasma", "Siniestro"], True, False),
    (66, "Machop", ["Lucha"], ["Volador", "Psíquico", "Hada"], False, False),
    (67, "Machoke", ["Lucha"], ["Volador", "Psíquico", "Hada"], False, False),
    (68, "Machamp", ["Lucha"], ["Volador", "Psíquico", "Hada"], False, True),
    (69, "Bellsprout", ["Planta", "Veneno"], ["Fuego", "Hielo", "Volador", "Psíquico"], False, False),
    (70, "Weepinbell", ["Planta", "Veneno"], ["Fuego", "Hielo", "Volador", "Psíquico"], False, False),
    (71, "Victreebel", ["Planta", "Veneno"], ["Fuego", "Hielo", "Volador", "Psíquico"], False, False),
    (72, "Tentacool", ["Agua", "Veneno"], ["Eléctrico", "Tierra", "Psíquico"], False, False),
    (73, "Tentacruel", ["Agua", "Veneno"], ["Eléctrico", "Tierra", "Psíquico"], False, False),
    (74, "Geodude", ["Roca", "Tierra"], ["Agua", "Planta", "Lucha", "Tierra", "Acero", "Hielo"], False, False),
    (75, "Graveler", ["Roca", "Tierra"], ["Agua", "Planta", "Lucha", "Tierra", "Acero", "Hielo"], False, False),
    (76, "Golem", ["Roca", "Tierra"], ["Agua", "Planta", "Lucha", "Tierra", "Acero", "Hielo"], False, False),
    (77, "Ponyta", ["Fuego"], ["Agua", "Tierra", "Roca"], False, False),
    (78, "Rapidash", ["Fuego"], ["Agua", "Tierra", "Roca"], False, False),
    (79, "Slowpoke", ["Agua", "Psíquico"], ["Planta", "Eléctrico", "Bicho", "Fantasma", "Siniestro"], False, False),
    (80, "Slowbro", ["Agua", "Psíquico"], ["Planta", "Eléctrico", "Bicho", "Fantasma", "Siniestro"], True, False),
    (81, "Magnemite", ["Eléctrico", "Acero"], ["Tierra", "Fuego", "Lucha"], False, False),
    (82, "Magneton", ["Eléctrico", "Acero"], ["Tierra", "Fuego", "Lucha"], False, False),
    (83, "Farfetch'd", ["Normal", "Volador"], ["Eléctrico", "Hielo", "Roca"], False, False),
    (84, "Doduo", ["Normal", "Volador"], ["Eléctrico", "Hielo", "Roca"], False, False),
    (85, "Dodrio", ["Normal", "Volador"], ["Eléctrico", "Hielo", "Roca"], False, False),
    (86, "Seel", ["Agua"], ["Planta", "Eléctrico"], False, False),
    (87, "Dewgong", ["Agua", "Hielo"], ["Planta", "Eléctrico", "Lucha", "Roca"], False, False),
    (88, "Grimer", ["Veneno"], ["Tierra", "Psíquico"], False, False),
    (89, "Muk", ["Veneno"], ["Tierra", "Psíquico"], False, False),
    (90, "Shellder", ["Agua"], ["Planta", "Eléctrico"], False, False),
    (91, "Cloyster", ["Agua", "Hielo"], ["Planta", "Eléctrico", "Lucha", "Roca"], False, False),
    (92, "Gastly", ["Fantasma", "Veneno"], ["Fantasma", "Siniestro", "Psíquico", "Tierra"], False, False),
    (93, "Haunter", ["Fantasma", "Veneno"], ["Fantasma", "Siniestro", "Psíquico", "Tierra"], False, False),
    (94, "Gengar", ["Fantasma", "Veneno"], ["Fantasma", "Siniestro", "Psíquico", "Tierra"], True, True),
    (95, "Onix", ["Roca", "Tierra"], ["Agua", "Planta", "Lucha", "Tierra", "Acero", "Hielo"], False, False),
    (96, "Drowzee", ["Psíquico"], ["Bicho", "Fantasma", "Siniestro"], False, False),
    (97, "Hypno", ["Psíquico"], ["Bicho", "Fantasma", "Siniestro"], False, False),
    (98, "Krabby", ["Agua"], ["Planta", "Eléctrico"], False, False),
    (99, "Kingler", ["Agua"], ["Planta", "Eléctrico"], False, True),
    (100, "Voltorb", ["Eléctrico"], ["Tierra"], False, False),
    (101, "Electrode", ["Eléctrico"], ["Tierra"], False, False),
    (102, "Exeggcute", ["Planta", "Psíquico"], ["Bicho", "Fuego", "Hielo", "Volador", "Veneno", "Fantasma", "Siniestro"], False, False),
    (103, "Exeggutor", ["Planta", "Psíquico"], ["Bicho", "Fuego", "Hielo", "Volador", "Veneno", "Fantasma", "Siniestro"], False, False),
    (104, "Cubone", ["Tierra"], ["Agua", "Planta", "Hielo"], False, False),
    (105, "Marowak", ["Tierra"], ["Agua", "Planta", "Hielo"], False, False),
    (106, "Hitmonlee", ["Lucha"], ["Volador", "Psíquico", "Hada"], False, False),
    (107, "Hitmonchan", ["Lucha"], ["Volador", "Psíquico", "Hada"], False, False),
    (108, "Lickitung", ["Normal"], ["Lucha"], False, False),
    (109, "Koffing", ["Veneno"], ["Tierra", "Psíquico"], False, False),
    (110, "Weezing", ["Veneno"], ["Tierra", "Psíquico"], False, False)
]

# Carga en los tres árboles
for num, name, types, weaknesses, has_mega, has_gigantamax in pokemons_data:
    poke = Pokemon(num, name, types, weaknesses, has_mega, has_gigantamax)
    tree_name.insert_node(name, poke)
    tree_number.insert_node(num, poke)
    for t in types:
        found_node = tree_type.search(t)
        if found_node:
            found_node.other_values.append(poke)
        else:
            tree_type.insert_node(t, [poke])
        
print()

# mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último, la búsqueda debe ser por proximidad, es decir 
# # si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–;
# tuve que cambiar la parte de la funcion de proxy_search ya que antes tenia values, pero necesitaba que use other values
# if prefix in root.value.lower():
#     print(root.other_values)
print("Búsqueda por Número")
resultado_num = tree_number.search(25)
if resultado_num:
    print(resultado_num.other_values)
print()
print("Búsqueda por Proximidad (Nombre) ")
tree_name.proxy_search("bul")

print()

# mostrar todos los nombres de los Pokémons de un determinado tipo: fantasma, fuego, acero y eléctrico;
tipos_buscados = ["Fantasma", "Fuego", "Acero", "Eléctrico"]
print("Pokémons por Tipo (Fantasma, Fuego, Acero, Eléctrico)")
for tipo in tipos_buscados:
    nodo = tree_type.search(tipo)
    if nodo:
        print(f"Tipo: {tipo}")
        for poke in nodo.other_values:
            print(f" - {poke.name}")
    else:
        print(f"Tipo: {tipo} (No hay Pokémon registrados)")

print()

# realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;
print("listado acendente por numero")
tree_number.inorden()
print()
print("listado acendente por nombre")
tree_name.inorden()
print()
print("listado por nivel(por nombre)")
tree_name.by_level()

print()

# mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum;
tipos_atacantes = ["Eléctrico", "Roca", "Dragón"]
print("Pokémon débiles frente a Jolteon, Lycanroc y Tyrantrum")
def mostrar_debiles(nodo):
    if nodo is not None:
        mostrar_debiles(nodo.left)
        poke = nodo.other_values
        if poke is not None:
            es_debil = False
            for debilidad in poke.weaknesses:
                if debilidad in tipos_atacantes:
                    es_debil = True
                    break 
            if es_debil:
                print(f" - {poke.name} (Debilidades: {poke.weaknesses})")
        mostrar_debiles(nodo.right)
mostrar_debiles(tree_name.root)

print()

# mostrar todos los tipos de Pokémons y cuántos hay de cada tipo;
print("Cantidad de Pokémon por cada tipo")
def mostrar_cantidad_por_tipo(nodo):
    if nodo is not None:
        mostrar_cantidad_por_tipo(nodo.left)
        tipo_nombre = nodo.value
        cantidad = len(nodo.other_values)
        print(f" - Tipo {tipo_nombre}: {cantidad} Pokémon")
        mostrar_cantidad_por_tipo(nodo.right)
mostrar_cantidad_por_tipo(tree_type.root)

print()

# determinar cuantos Pokémons tienen megaevolucion.
print("Cantidad de Pokémon con Megaevolución")
def contar_megas(nodo):
    if nodo is None:
        return 0
    actual = 0
    poke = nodo.other_values
    if poke and poke.has_mega:
        actual = 1
    return contar_megas(nodo.left) + actual + contar_megas(nodo.right)
total_megas = contar_megas(tree_name.root)
print(f"Total de Pokémon con Megaevolución: {total_megas}")

print()

# determinar cuantos Pokémons tiene forma gigamax.
print("Cantidad de Pokémon con forma Gigamax")
def contar_gigantamax(nodo):
    if nodo is None:
        return 0
    actual = 0
    poke = nodo.other_values
    if poke and poke.has_gigantamax:
        actual = 1
    return contar_gigantamax(nodo.left) + actual + contar_gigantamax(nodo.right)
total_gigantamax = contar_gigantamax(tree_name.root)
print(f"Total de Pokémon con forma Gigamax: {total_gigantamax}")



# Ejercicio 2: Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios para resolver las 
# siguientes tareas:

# cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los
# que aparecieron juntos ambos personajes que se relacionan;

# hallar el árbol de expansión mínimo desde el vértice que contiene a: C-3PO, Yoda y Leia;

# determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los
# pares de personajes que coinciden con dicho número;

# cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba F
# ett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8;

# calcule el camino mas ccorto desde: C-3PO a R2-D2 y desde Yoda a Darth Vader;

# indicar qué personajes aparecieron en los nueve episodios de la saga.

print()

print("EJERCICIO 2")

# cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los
# que aparecieron juntos ambos personajes que se relacionan;
sw_graph = Graph(is_dir=False)
personajes = [
    "Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", 
    "C-3PO", "Leia", "Rey", "Kylo Ren", 
    "Chewbacca", "Han Solo", "R2-D2", "BB-8"
]
# cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba F
# ett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8;
for p in personajes:
    sw_graph.add_vertex(p)
sw_graph.add_edge(9, "C-3PO", "R2-D2")
sw_graph.add_edge(5, "C-3PO", "Leia")
sw_graph.add_edge(5, "C-3PO", "Luke Skywalker")
sw_graph.add_edge(4, "C-3PO", "Yoda")
sw_graph.add_edge(6, "Leia", "Luke Skywalker")
sw_graph.add_edge(5, "Leia", "Han Solo")
sw_graph.add_edge(5, "Leia", "Chewbacca")
sw_graph.add_edge(3, "Yoda", "Darth Vader")
sw_graph.add_edge(4, "Yoda", "Luke Skywalker")
sw_graph.add_edge(3, "Darth Vader", "Luke Skywalker")
sw_graph.add_edge(2, "Boba Fett", "Darth Vader")
sw_graph.add_edge(3, "Han Solo", "Chewbacca")
sw_graph.add_edge(3, "Han Solo", "Luke Skywalker")
sw_graph.add_edge(3, "Rey", "Kylo Ren")
sw_graph.add_edge(3, "Rey", "BB-8")
sw_graph.add_edge(3, "Kylo Ren", "Darth Vader")
sw_graph.add_edge(2, "BB-8", "R2-D2")
print()
print("El grafo esta cargado")

print()

# hallar el árbol de expansión mínimo desde el vértice que contiene a: C-3PO, Yoda y Leia;
print("Arbol de expansion minimo(use kruskal)")
print()
for origen in ["C-3PO", "Yoda", "Leia"]:
    min_tree = sw_graph.kruskal(origen) 
    print(f"Arbol de Expansión Mínimo desde {origen}:")
    print(min_tree)
    peso_total = 0
    if min_tree:
        for edge in min_tree.split(';'):
            if '-' in edge:
                partes = edge.split('-')
                weight = partes[-1]
                conexion = "-".join(partes[:-1])
                print(f" - Conexión: {conexion} (Episodios: {weight})")
                if weight.isdigit():
                    peso_total += int(weight)
        print(f" > Peso total del MST desde {origen}: {peso_total}")
        
print()

# determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los
# pares de personajes que coinciden con dicho número;
print("Maximo episodios compartidos y sus pares")
max_episodios = 0
pares_maximos = []
for vertex in sw_graph:
    for edge in vertex.edges:
        if edge.weight > max_episodios:
            max_episodios = edge.weight
            pares_maximos = [[vertex.value, edge.destination]]
        elif edge.weight == max_episodios:
            par_actual = [vertex.value, edge.destination]
            par_inverso = [edge.destination, vertex.value]
            if par_actual not in pares_maximos and par_inverso not in pares_maximos:
                pares_maximos.append(par_actual)
print(f"El numero máximo de episodios compartidos es: {max_episodios}")
print("Pares de personajes que coinciden con dicho número:")
for p1, p2 in pares_maximos:
    print(f" - {p1} y {p2}")
    
print()    

# calcule el camino mas corto desde: C-3PO a R2-D2 y desde Yoda a Darth Vader;
print("Camino mas corto (dijkstra)")
def calcular_camino_corto(origen, destino):
    if sw_graph.exist_path(origen, destino):
        paths = sw_graph.dijkstra(origen)
        peso_total = None
        camino_completo = []
        curr_dest = destino
        while paths.size() > 0:
            value = paths.pop()
            if value[0] == curr_dest:
                if peso_total is None:
                    peso_total = value[1]
                camino_completo.append(value[0])
                curr_dest = value[2]
        camino_completo.reverse()
        print(f"El camino más corto de {origen} a {destino} es: {'-'.join(camino_completo)} con un costo de {peso_total}")
    else:
        print(f"No hay camino posible entre {origen} y {destino}")
calcular_camino_corto("C-3PO", "R2-D2")
calcular_camino_corto("Yoda", "Darth Vader")

print()

# indicar qué personajes aparecieron en los nueve episodios de la saga.
print("personajes que aparecieron en los 9 episodios")
print("Los personajes que comparten el máximo de 9 episodios son:")
for p1, p2 in pares_maximos:
    if max_episodios == 9:
        print(f" - {p1}")
        print(f" - {p2}")