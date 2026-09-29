def battle(pokemon1, pokemon2): #acho que esse nome genérico não vai dar problema agora mas depois vou deletar de qualquer forma.
    #if not pokemon2.stats["hp"] == 0 and not pokemon2.stats["hp"] == 0:
    #    alive = True

    def nobody_dies():
        if pokemon1.stats["hp"] <= 0 or pokemon2.stats["hp"] <= 0:
            print(f"fim da partida. pokemon1 hp:{pokemon1.stats["hp"]}. Pokemon2 hp: {pokemon2.stats["hp"]}") #colocar quem morreu no print.
            return False
        else:
            return True
    
    def attack(attacker, rival, move):
        move_power = moves[move]

        attack_power = 2 * attacker.level / 5 + 2 * move_power * attacker.stats['attack'] / rival.stats['defense'] / 50 + 2 #falta adicionar modificador

        rival.stats["hp"] -= attack_power
        print(attack_power)

    while True:
        print(f"pokemon1 hp:{pokemon1.stats["hp"]}. Pokemon2 hp: {pokemon2.stats["hp"]}")

        faster, slower = order_by_speed(pokemon1, pokemon2)

        movefaster = faster.select_attack()
        moveslower = slower.select_attack()

        attack(faster, slower, movefaster)
        if nobody_dies():
            attack(slower, faster, moveslower)
        else:
            print(f"fim da partida. pokemon1 hp:{pokemon1.stats["hp"]}. Pokemon2 hp: {pokemon2.stats["hp"]}")
            break