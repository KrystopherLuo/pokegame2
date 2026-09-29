import csv


class Pokedex:
    def __init__(self):
        self.pokedex = []
        self.pokedex_dict = {} #prefiro não usar esse dict no momento.
    def start(self):
        with open("gen01.csv", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for item in leitor:
                self.pokedex.append(item)

                

                self.pokedex_dict[item["name"].lower()] = item

    def import_race(self, id_or_name):
        with open("gen01.csv", encoding="utf-8") as pokedex_archive:
            pokedex = csv.DictReader(pokedex_archive)

            if isinstance(id_or_name, int):
                identifier_type = "id"
                identifier_format = int
            elif isinstance(id_or_name, str):
                identifier_type = "name"
                identifier_format = str

            for pokemon in pokedex:
                if identifier_format(pokemon[identifier_type]) == id_or_name: #não funciona pra formas alternativas. Ele precisa buscar pelo id e não pelo index direto.
                    return pokemon #no momento essa busca ocorre em busca linear. O que deve ser mudado.

            print("Não foi encontrado nenhum pokemon com esse identificador")
            return None

pokedex = Pokedex()

pokedex.start()