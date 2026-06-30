# Ejercicio 1: Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:
# funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
# funcion recursiva para listar los superheroes de la lista.
superheroes = [
    {
        "name": "Kang",
        "alias": "Kang the Conqueror",
        "real_name": "Nathaniel Richards",
        "short_bio": "Kang the Conqueror is a time-traveling warlord who has battled many heroes, especially the Avengers. He is known for his mastery of advanced technology and his ability to manipulate time.",
        "first_appearance": 1964,
        "is_villain": True
    },
    {
        "name": "Hulk",
        "alias": "The Hulk",
        "real_name": "Bruce Banner",
        "short_bio": "Hulk is a gamma-powered superhero with incredible strength and durability. He transforms into a green giant when angered or stressed.",
        "first_appearance": 1962,
        "is_villain": False
    },
    {
        "name": "Black Widow",
        "alias": "Natasha Romanoff",
        "real_name": "Natasha Romanoff",
        "short_bio": "Black Widow is a highly trained spy and former assassin with exceptional skills in hand-to-hand combat and espionage.",
        "first_appearance": 1964,
        "is_villain": False
    },
    {
        "name": "Black Cat",
        "alias": "Felicia Hardy",
        "real_name": "Felicia Hardy",
        "short_bio": "Black Cat is a skilled burglar with a unique power that brings bad luck to her enemies. She often operates in the gray area between hero and villain.",
        "first_appearance": 1979,
        "is_villain": True
    },
    {
        "name": "Iron Man",
        "alias": "Iron Man",
        "real_name": "Tony Stark",
        "short_bio": "A billionaire inventor who built a powered suit of armor to save his life and became a founding Avenger.",
        "first_appearance": 1963,
        "is_villain": False
    },
    {
        "name": "Magneto",
        "alias": "Master of Magnetism",
        "real_name": "Max Eisenhardt",
        "short_bio": "A powerful mutant with control over magnetic fields, often portrayed as an adversary to the X-Men, though with complex motivations.",
        "first_appearance": 1963,
        "is_villain": True
    },
    {
        "name": "Storm",
        "alias": "Storm",
        "real_name": "Ororo Munroe",
        "short_bio": "A mutant with the ability to manipulate weather, known for her leadership in the X-Men and her strong moral compass.",
        "first_appearance": 1975,
        "is_villain": False
    },
    {
        "name": "Venom",
        "alias": "Venom",
        "real_name": "Eddie Brock",
        "short_bio": "A journalist who bonds with an alien symbiote to become the anti-hero Venom, often torn between vengeance and justice.",
        "first_appearance": 1988,
        "is_villain": True
    },
    {
        "name": "Scarlet Witch",
        "alias": "Scarlet Witch",
        "real_name": "Wanda Maximoff",
        "short_bio": "A mutant with chaos magic and reality-warping powers, known for her complex role as both hero and threat.",
        "first_appearance": 1964,
        "is_villain": False
    },
    {
        "name": "Abomination",
        "alias": "Abomination",
        "real_name": "Emil Blonsky",
        "short_bio": "A former KGB agent who transforms into a gamma-powered monster and becomes one of Hulk's main enemies.",
        "first_appearance": 1967,
        "is_villain": True
    },
    {
        "name": "Adam Warlock",
        "alias": "Adam Warlock",
        "real_name": "Adam Warlock",
        "short_bio": "An artificially created perfect human who becomes a cosmic protector and wielder of the Soul Gem.",
        "first_appearance": 1967,
        "is_villain": False
    },
    {
        "name": "Angel",
        "alias": "Angel",
        "real_name": "Warren Worthington III",
        "short_bio": "A founding member of the X-Men with large feathered wings that allow him to fly.",
        "first_appearance": 1963,
        "is_villain": False
    },
    {
        "name": "Annihilus",
        "alias": "Annihilus",
        "real_name": "Annihilus",
        "short_bio": "A powerful insectoid ruler from the Negative Zone, obsessed with extending his lifespan.",
        "first_appearance": 1968,
        "is_villain": True
    },
    {
        "name": "Ant Man",
        "alias": "Ant Man",
        "real_name": "Hank Pym",
        "short_bio": "A brilliant scientist who discovered Pym Particles and became a size-changing superhero.",
        "first_appearance": 1962,
        "is_villain": False
    },
    {
    "name": "Apocalypse",
    "alias": "Apocalypse",
    "real_name": "En Sabah Nur",
    "short_bio": "One of the first mutants, Apocalypse believes in survival of the fittest and has enhanced his body over millennia with alien technology.",
    "first_appearance": 1986,
    "is_villain": True
    },
    {
        "name": "Baron Zemo",
        "alias": "Baron Zemo",
        "real_name": "Helmut Zemo",
        "short_bio": "A brilliant and ruthless strategist, Baron Zemo is a longtime foe of Captain America and leader of various villainous groups.",
        "first_appearance": 1973,
        "is_villain": True
    },
    {
    "name": "Captain America",
    "alias": "Captain America",
    "real_name": "Steve Rogers",
    "short_bio": "A super-soldier from World War II, Captain America is a symbol of heroism, justice, and patriotism in the Marvel Universe.",
    "first_appearance": 1941,
    "is_villain": False
    }]


# funcion recursiva  para buscar, determinar si Capitan America esta en la lista.

def recur_1(superheroes,i=0):
    if len(superheroes) == 0:
        return print("La lista esta vacia")
    elif len(superheroes) == i:
        return print("No se encontro al Capitan america en la lista")
    elif superheroes[i]['name'] == 'Captain America':
        return print("El Capitan America si se encontro en la lista")
    else:
        return recur_1(superheroes,i+1)
    
recur_1(superheroes,i=0)  


# funcion recursiva para listar los superheroes de la lista.

def listar_superheroes(lista, i=0) -> None:
    if i>= len(lista):
        return 
    heroe = lista[i]
    print(f"Nombre: {heroe['name']} / Alias: {heroe['alias']} / Año: {heroe['first_appearance']}")
    listar_superheroes(lista, i + 1)
print("")

listar_superheroes(superheroes)

