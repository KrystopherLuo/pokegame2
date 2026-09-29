from pokemon import Pokemon

import random

from moves import moves
from trainer import Trainer

#colocar print pro jogador saber o que tá acontecendo na batalha tipo que movimento foi escolhido e tals

def battle( fighter1, fighter2): #preciso terminar esse reformulation battle
    

    print(f"{fighter1.nick} desafiou {fighter2.nick} para uma batalha.")
    endbattle = False
    assert isinstance(fighter1, Pokemon) or isinstance(fighter1, Trainer) and isinstance(fighter2, Pokemon) or isinstance(fighter2, Trainer), "erro, tentativa de iniciar batalhas com objetos que não podem batalhar"

    #depois eu dou del no fighteractindex só de raiva pro ter fudido com a legibilidade dessa parte do código. Talvez eu tire o loop for só por isso. Da pra usar continue também pra pular o que não é trainer e adicioanr tudo em uma lista.

    def orderspeed(pokemon1, pokemon2, pokemon1priority, pokemon2priority):
        assert isinstance(pokemon1priority, int) and isinstance(pokemon2priority, int), "erro, prioridade não é um inteiro"

        if pokemon1priority == pokemon2priority:
            if pokemon1.stats['speed'] > pokemon2.stats["speed"]:
                return (pokemon1, pokemon2) #eu poderia retornar duas tupla e usar isso no script de executar também.
            elif pokemon1.stats['speed'] < pokemon2.stats["speed"]:
                return(pokemon2, pokemon1)
            else:
                return random.choice(((pokemon1, pokemon2), (pokemon2, pokemon1)),)
        else:
            if pokemon1priority > pokemon2priority:
                return (pokemon1, pokemon2)
            elif pokemon1priority < pokemon2priority:
                return (pokemon2, pokemon1)


    def define_priority(pokemon, turn_action):
        #definir o de moves
        if turn_action["action"] == "attack":
            move_priority = 0 #depois eu mudo isso pra pegar a informação do move do pokemon.
            ability_priority = 0
            return move_priority + ability_priority
        actions_priority = { 
            "attack" : 0,
            "run" : 6,
            "capture" : 6,
            "switch" : 6
        }
        return actions_priority[turn_action[0]]

    def on_turn_end(chekingtrainer): #o death protocol recebe player. funciona pra verificar se o pokemon em batalha morreu e, se sim, requisitar uma troca e encerrar a batalha se estiver todo mundo morto.
        chekingpk = chekingtrainer.get_first_pk()
        if not chekingpk.isalive():
            if isinstance(chekingtrainer, Trainer) and chekingtrainer.able_to_battle():
                chekingtrainer.battle_swap_pokemon() #aqui necessariamente é um treinador
                print(f"{chekingtrainer.nick} trocou para {chekingtrainer.get_first_pk().race_name}")
            else: 
                print("on turn end determina que a batalha deve ser encerrada.")

        else:
            print(f"chekingtrainer's hp: {chekingpk.stats["hp"]}") #e se tiver vivo executa as skills.

    def attack( attackercharacter, move, rivalcharacter): #não sei se o ideal é isso estar aqui ou no battlemanager.
        attacker = attackercharacter.get_first_pk()
        rival = rivalcharacter.get_first_pk()

        assert attacker.able_to_battle(), "O pokemon que deveria atacar não está vivo."

        #move = attacker_trainer.choice_move(attacker_trainer.team[0]) #tirar esse choice daqui.
        move_power = moves[move] #eu deveria mudar o nome desse dict pra "moves_powerS"

        attack_power = int(2 * attacker.level / 5 + 2 * move_power * attacker.stats['attack'] / rival.stats['defense'] / 50 + 2) #falta adicionar modificador

        if attack_power > rival.stats["hp"]:
            print(f"{attacker.race_name} deu {rival.stats["hp"]} de dano em {rival.race_name}")
            rival.stats["hp"] = 0
        else:
            rival.stats["hp"] -= attack_power
            print(f"{attacker.race_name} deu {attack_power} de dano em {rival.race_name}")
                #if challenger.pokemon #como se referir ao pokemon que está na batalha?

            print(f"hp do rival depois do ataque: {rival.stats["hp"]}")

    def execute_attack(trainer, rival, turn_action): #aqui não necessariamente é um trainer tirando no useitem
        attack(trainer.get_first_pk(), turn_action["move"], rival.get_first_pk())

    def execute_run(trainer, rival, turn_action):
        num = random.random()
        if num <= 0.5:
            print(f"{trainer.nick} fugiu covardemente.")

            nonlocal endbattle
            endbattle = True

    def execute_item(trainer, rival, turn_action):
        assert isinstance(rival, Pokemon), "tentativa de capturar algo que não é um pokemon"


        rivalpk = rival.get_first_pk()
        if rivalpk.iswild: #se não for, aqui você perde turno.
            num = random.randint(1, 100)
            if num <= 50:
                print(f"{trainer.nick} capturou com sucesso {rival.race_name}")

                trainer.receive_pokemon(rival)

                nonlocal endbattle
                endbattle = True
            else:
                print(f"A pokebola falhou.")
        else:
            print("Você não pode capturar o pokemon de um treinador.")

    def execute_switch(trainer, rival, turn_action):
        assert trainer.isalive()[1], "trainer não está vivo para trocar de pokemon"
        assert isinstance(trainer, Trainer)
        trainer.battle_swap_pokemon()

    actions = {
        "attack" : execute_attack,
        "run" : execute_run,
        "capture" : execute_item, #troco o nome "capture" quando adicionar outros itens.
        "switch" : execute_switch
    }

    def execute_action(fighter, rival, fighter_turn_action): #execute tá sendo usada só pra pokemon mas capture precisa de um treinador.
        actions[fighter_turn_action["action"]](fighter, rival, fighter_turn_action)

    while fighter1.able_to_battle() and fighter2.able_to_battle() and endbattle == False:
        print(f"Lutadores hp: {fighter1.nick} hp: {fighter1.get_first_pk().stats["hp"]}. {fighter2.nick} hp: {fighter2.get_first_pk().stats["hp"]}")

        #on_enter_battle(pokemon1, pokemon2)
        fighter1_action = fighter1.choice_turn_action()
        fighter2_action = fighter2.choice_turn_action()

        fighter1_priority = define_priority(fighter1.get_first_pk(), fighter1_action)#colocar coisa pra puxar a prioridade dos moves depois de fazer o reformulation moves
        fighter2_priority = define_priority(fighter2.get_first_pk(), fighter2_action) 

        rank_speed = orderspeed(fighter1.get_first_pk(), fighter2.get_first_pk(), fighter1_priority, fighter2_priority)

        for pokemon in rank_speed:
            if not endbattle:
                if pokemon == fighter1.get_first_pk(): #tá muito manual, pode ser trocado, mas agora não.
                    fighter_turn_action = fighter1_action
                    fighter = fighter1
                    fighter_rival = fighter2
                else:
                    fighter_turn_action = fighter2_action
                    fighter = fighter2
                    fighter_rival = fighter1

                if pokemon.isalive():
                    execute_action(fighter, rank_speed[1], fighter_turn_action) #execute tá sendo usada só pra pokemon mas capture precisa de um treinador.

                on_turn_end(fighter_rival) #if o cara morreu, break. falta isso pra não o cara que morreu aproveitar o turno.

                rank_speed = (rank_speed[1], rank_speed[0])

        print(f"turno acabado")

    #se ele continuou foi pq alguém morreu
    print(f"Batalha encerrada. lutadores info: {fighter1.nick} hp: {fighter1.get_first_pk().stats["hp"]}. {fighter2.nick} hp: {fighter2.get_first_pk().stats["hp"]}")