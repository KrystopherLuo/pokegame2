class Pokemon: #alive
    def __init__(self):
        self.race = "bulbasaur"
        self.stats = {
            "hp" : 80,
            "attack" : 100,
            "defense" : 50,
            "spattack" : 100,
            "spdefense" : 50,
            "speed" : 120,
            }
        self.level = 80
        self.moves = ["quick attack", "tackle", "", ""]
    def select_attack(self):
        move_command = input("coloque seu move: ")

        try:
            move_command_int = int(move_command) 

            if 0 < move_command_int <= 4:
                move = self.moves[move_command_int - 1]

                return move
        except ValueError:
            pass

        if isinstance(move_command, str):
            #move = self.moves.index()
            
            index = 0
            for i in self.moves:
                if i == move_command:
                    break
                index += 1
            if not index == 4:
                move = self.moves[index]

                return move
        
    def attack(self, rival, move):
        move_power = moves[move]

        attack_power = 2 * self.level / 5 + 2 * move_power * self.stats['attack'] / rival.stats['defense'] / 50 + 2 #falta adicionar modificador

        rival.stats["hp"] -= attack_power
        print(attack_power)

moves = {
    "quick attack" : 50,
    "tackle" : 40,
}

ash = Pokemon()
red = Pokemon()


def battle(pokemon1, pokemon2):
    #if not pokemon2.stats["hp"] == 0 and not pokemon2.stats["hp"] == 0:
    #    alive = True

    def nobody_dies():
        if pokemon1.stats["hp"] <= 0 or pokemon2.stats["hp"] <= 0:
            print(f"fim da partida. pokemon1 hp:{pokemon1.stats["hp"]}. Pokemon2 hp: {pokemon2.stats["hp"]}") #colocar quem morreu no print.
            return False
        else:
            return True

    def order_by_speed(p1, p2):
        return (p1, p2) if p1.stats['speed'] >= p2.stats['speed'] else (p2, p1)

    while True:
        print(f"pokemon1 hp:{pokemon1.stats["hp"]}. Pokemon2 hp: {pokemon2.stats["hp"]}")

        faster, slower = order_by_speed(pokemon1, pokemon2)

        movefaster = faster.select_attack()
        moveslower = slower.select_attack()

        faster.attack(slower, movefaster)
        if nobody_dies():
            slower.attack(faster, moveslower)
        else:
            print(f"fim da partida. pokemon1 hp:{pokemon1.stats["hp"]}. Pokemon2 hp: {pokemon2.stats["hp"]}")
            break


battle(red, ash)