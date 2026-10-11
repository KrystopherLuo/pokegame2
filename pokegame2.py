from battle import battle
from pokemoncentral import create_pk #esses vão permancer, deixei até separado.

#from trainer import Trainer
from trainer import Player
from trainer import trainers
from trainer import trainers_nick
#from pokemon import Pokemon #isso era pra sumir ao longo que as classes vão ficando independentes tipo o player convoca os pokemon

#talevz pra programar os moves e habilidades eu tenha que colocar pra cada um um parâmetro "posmove" "posstart" "posdead" que todos tenham mas nem todos usem
shop = {
    "pokeball" : 200
}

class Game:
    def __init__(self):
        self.gamerules = {

        }
        self.player = Player("ash")

    def wild_battle(self):
        battle(self.player, create_pk())

    def trainer_battle(self,):
        gym_leader = self.player.get_valid_input(["quit", *trainers_nick])

        battle(self.player, trainers[gym_leader])


    def start(self): # o jogo tem que rodar aqui.
        #o jogo é pra ser singleplayer, sei nem porque adicionei coisa de duelo, mas vai servir pra fazer os npc de qualquer forma.
        self.player.start_adventure()
        #venusaur = create_pk(1, 80, [31, 31, 31, 31, 31, 31], [0, 0, 0, 0, 0, 0], "hardy")
        #charizard = create_pk(3, 80, [31, 31, 31, 31, 31, 31], [0, 0, 0, 0, 0, 0], "hardy")

        #player.receive_pokemon(charizard)
        #player.receive_pokemon(venusaur) 

        #npc = Trainer("gary", self.battlecentral, self.pokemoncentral) #era pra ter um playermanager pra cuidar disso.
        #npc.receive_pokemon(3, 80, [31, 31, 31, 31, 31, 31], [0, 0, 0, 0, 0, 0], "hardy")
        #npc.receive_pokemon(6, 80, [31, 31, 31, 31, 31, 31], [0, 0, 0, 0, 0, 0], "hardy")  

        commands = ["wild_battle", "trainer_battle"]
        commands_functions = {
            "wild_battle" : self.wild_battle,
            "trainer_battle" : self.trainer_battle
        }

        #self.wild_battle(player)

        while True:
            if not self.player.able_to_battle():
                self.player.heal()

            command = self.player.get_valid_input(commands)

            if command in commands:
                commands_functions[command]()
            elif command == "quit": 
                break
            else:
                print("comando inválido")


        #while True:
        #    command = player.command

    #def artificial_create
    
game = Game()
game.start()

globals_dict = globals().copy()

for key, item in globals_dict.items():
    print(f"{key} : {item}")