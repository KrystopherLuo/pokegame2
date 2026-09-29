from pokemon import Pokemon
from pokedex import pokedex
import random

#pokemon central cuida dos wilds.
#raceid, level, iv, ev, nature
#todo pokemon é inicialmente wild até ser adicionado ao time ou pc de alguém.
dexlimit = 151
allnatures = [
            "hardy",
            "lonely",
            "brave",
            "adamant",
            "naughty",
            "bold",
            "docile",
            "relaxed",
            "impish",
            "lax",
            "timid",
            "hasty",
            "serious",
            "jolly",
            "naive",
            "bashful",
            "rash",
            "quiet",
            "quirky",
            "modest",
            "calm",
            "gentle",
            "sassy",
            "careful",
            "mild"
        ]

def random_nature():
    return random.choice(allnatures)

def random_iv():
    random_iv_tab = []
    for i in range(6): 
        random_iv_tab.append(random.randint(0, 31))
    return random_iv_tab
    #return tuple(random_iv_tab) depois eu coloco porque quando colocar vou ter que revisar as verificações pra aceitarem tuplas.

def random_ev(): #eu não sei se essa é a forma mais eficiente de calcular uma distribuição aleatória, mas acho que funciona
    random_ev_tab = [0, 0, 0, 0, 0, 0] #da pra modificar os parametros pra ficar mais utilizável tipo adicionar maxev, statev, mas não preciso disso agora.
    random_ev_sum = random.randint(0, 510)

    def distribute(value, intlist): #acho que não vai diminuir a variável passada.

        sum_list = []

        for i in range(len(intlist)):
            random_value = random.randint(0, value)
            sum_list.append(random_value)

            value -= random_value 

        for i in random.sample(sum_list, len(sum_list)):
            sum_list.append(i)
        sum_list = sum_list[6:]

        for i in range(len(sum_list)):
            intlist[i] += sum_list[i]

    distribute(random_ev_sum, random_ev_tab)

    while not verify_ev(random_ev_tab):
        index = 0
        for i in random_ev_tab:
            if i >= 252:
                distribute(i-252, random_ev_tab)
                random_ev_tab[index] = 252

            index += 1

    return(random_ev_tab)



def create_random_params(): #completamente aleatório, quero colocar parâmetros opcionais.
    dex_number = random.randint(1,151)

    wild_race = int(pokedex.import_race(dex_number)["id"])
    wild_level = random.randint(1, 100)
    wild_iv = random_iv()
    wild_ev = []
    for i in range(6): 
        wild_ev.append(0) #posso tirar isso também.

    wild_nature = random.choice(allnatures)

    return [wild_race, wild_level, wild_iv, wild_ev, wild_nature]
#def create_wild_battle(): #adicionar nature

def verify_ev(evs): #falta verificar se é uma list

    if len(evs) == 6:
        for ev in evs:
            if not 0 <= ev <= 252:
                return False
        return True
    return False

def verify_pk(id, level, iv, ev, nature): #eu devia usar mais assert do que if's

    valid_params = {}

    def verify_id(id):
        if isinstance(id, int):
            if 0 < id < dexlimit:
                return True
        return False

    def verify_level(level):
        if isinstance(level, int):
            if 0 < level < 100:
                return True
        return False

    def verify_iv(ivs):
        if isinstance(ivs, list):
            if len(ivs) == 6:
                valid_iv = 0
                for iv in ivs:
                    if 0 <= iv <= 31:
                        valid_iv += 1
                if valid_iv == 6:
                    return True
        return False
    
    def verify_nature(nature):
        if nature in allnatures:
            return True
        return False

    valid_params["id"] = verify_id(id)
    valid_params["level"] = verify_level(level)
    valid_params["iv"] = verify_iv(iv)
    valid_params["ev"] = verify_ev(ev)
    valid_params["nature"] = verify_nature(nature)

    for i in valid_params:
        if not i:
            return False
        return True
                    
def import_pk_id(idorname): #eu poderia colocar isso direto no createpk.
    if isinstance(idorname, str):
        return int(pokedex.import_race(idorname)["id"])
    elif isinstance(idorname, int):
        return idorname
    assert isinstance(idorname, int) or isinstance(idorname, str), "erro, idorname não é nem int nem str."

def create_pk(raceid=random.randint(1, dexlimit), level=random.randint(1, 100), iv=random_iv(), ev=random_ev(), nature=random_nature()): #utilitário para criar pokemon.
    
    if verify_pk(import_pk_id(raceid), level, iv, ev, nature):
        pokemon = Pokemon(import_pk_id(raceid), level, iv, ev, nature)
        pokemon.update_stats()
        return pokemon
    else: 
        print("pokemon inválido")
        print(import_pk_id(raceid), level, iv, ev, nature)

def create_wild_pk(): #agora isso é obsoleto porque o createpk faz essa aleatoriedade sozinho. Mas vai ser importante porque esse que vai receber as zones
    random_pk = create_pk(*create_random_params())
    random_pk.update_stats()
    return random_pk




    
        #criar um def learn que armazena dentro da classe as informações apenas dos moves usados pelo pokemon