# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
import game


MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:
    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O, U, D, or alias ).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
        
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        # Liste des directions valides
        direction = {"n": ["n", "nord"],
                     "e": ["e", "est"],
                     "s": ["s", "sud"],
                     "o": ["o", "ouest"],
                     "u": ["u", "haut"],
                     "d": ["d", "bas"] }

        # Get the direction from the list of words.
        direction_input = list_of_words[1].lower()
    

        # Check if the direction is valid (by checking the aliases).
        valid_direction = None
        for main_direction, alias in direction.items():
            if direction_input in alias:
                valid_direction = main_direction
                break

        # If the direction is not recognized, print an error message
        if valid_direction is None:
            print(f"\nDirection: '{direction_input}' non reconnue.\n")
            return False
        # Move the player in the direction specified by the parameter.
        player.move(valid_direction)
        print(player.current_room.get_long_description())
        print("\n" + player.get_history())
         # Vérifier si le joueur est dans la pièce de sortie
        if player.current_room.name == "Exit":
            Actions.present_riddle(game)
            return True

    def present_riddle(game):
        print("\nVous êtes face à la sortie.\n \n Il ne manquais plus que ça, une énigme. Il faut vite la ressoudre.")
        print("Une enigme apparait devant vous :")
        print("Je meurs chaque nuit pour renaître à l'aube. Qui suis-je ?")

        chances = 2
        while chances > 0:
            answer = input("Votre réponse : ").lower()
            if answer in ["l'espoir"]:
                print("\nBravo!Vous ètés sortie de la maison et avez prie la voiture\n \n ENFIN HORS DE CETTE FORET !!!\n")
                game.finished = True
                return
            else:
                chances -= 1
                if chances > 0:
                    print(f"Mauvaise réponse. Il vous reste {chances} chance.\n\n Anthony ce rapproche\n")
                else:
                    print("\nOHH MINCE!!!\n\n Anthony vous a r'attrapé.\n\n VOUS ETES MORT")
                    game.finished = True
                    return
            
    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True
    
    def back(game, list_of_words, number_of_parameters):
        """
    Move the player back to the previous room.

    Args:
        game (Game): The game object.
        list_of_words (list): The list of words in the command.
        number_of_parameters (int): The number of parameters expected by the command.

    Returns:
        bool: True if the command was executed successfully, False otherwise.

    Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> back(game, ["back"], 1)
        True
        >>> back(game, ["back", "N", "E"], 1)
        False
        >>> back , (game, ["back"], 1)
        False

        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        player=game.player

        # Verifying if it is possible to go back
        if len(player.history) < 2:
            print("\nImpossible de revenir en arrière, vous n'avez visité qu'une seule pièce ou aucune.\n")
            return False

        #Removing the room from the history and going back to the room before
        player.history.pop() 
        previous_room_name = player.history[-1]  
        previous_room = next(room for room in game.rooms if room.name == previous_room_name) 
        player.current_room = previous_room  
        print(previous_room.get_long_description())
        print("\n" + player.get_history())
        return True
    

    def look(game, list_of_words, number_of_parameters):
        """Affiche les items présents dans la pièce actuelle."""
        game.player.current_room.look()
    
    def take(game, list_of_words, number_of_parameters):
       """Permet au joueur de prendre un item."""
       
       if len(list_of_words) != number_of_parameters + 1:
           print("Erreur dans le nombre de paramètres.")
           return False
        
       name_item = list_of_words[1].lower()
       game.player.current_room.take(name_item, game.player)
       
       return True


    def drop(game, list_of_words, number_of_parameters):
       if len(list_of_words) != number_of_parameters + 1:
           print("Erreur dans le nombre de paramètres.")
           return False
        
       name_item = list_of_words[1].lower()
       game.player.current_room.drop(name_item, game.player)
       
       return True

    def check(game, list_of_words, number_of_parameters):
        """Affiche l'inventaire du joueur."""
        player = game.player
        if len(player.inventory) == 0:
            print("Il n'y a rien dans votre inventaire.")
        else:
            print("Vous avez dans votre inventaire :")
            for item in player.inventory.values():
                print(f"    - {item.name} : {item.description} ({item.weight})")

    def talk(game, list_of_words, number_of_parameters):
        if len(list_of_words) != number_of_parameters + 1:
            print("Erreur dans le nombre de paramètres.")
            return False
    
        character_name = list_of_words[1].lower()
        current_room = game.player.current_room
    
        if character_name in current_room.characters:
            character = current_room.characters[character_name]
            print(f"{character.name} dit : {character.get_msg(game)}")
        else:
            print(f"Il n'y a pas de personnage nommé {character_name} ici.")
    
        return True
