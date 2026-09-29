class PlayerController:
    def __init__(self):
        pass
    def choice(self, pokemon):

        print(pokemon.moves)

        selected_move = input("Digite o nome ou o número de um movimento do seu pokemon.")

        if selected_move in pokemon.moves:
            return selected_move
        else:
            while True:
                try:
                    selected_move_number = int(selected_move)
                except ValueError:
                        print("Escolha um número para seu movimento.")

                if 0 < selected_move_number <= len(pokemon.moves): #de 1 a 4, quem controla isso é o appendmove e removemove do player.
                    return pokemon.moves[selected_move_number-1]
                else:
                    print("Escolha um índice de movimento entre 1 e 4.")

    def swap_pokemon(self, trainer):

        while True:
            try:
                selected = int(input("escolha um número do index de algum pokemon do seu time"))
                if 1<= selected <= len(trainer.team):
                    return selected
            except ValueError:
                print("escolha um número inteiro válido")
        

    def respond_request(self):

        response = input("você aceita o pedido de batalha? Se sim, digite 1, se não, digite 0.")
        
        if int(response) == 1:
            return True
        else: 
            return False