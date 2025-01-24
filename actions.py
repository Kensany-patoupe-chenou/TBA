"""
Ce module contient les actions pour un jeu d'aventure textuel. Il définit les actions
que le joueur peut effectuer, telles que se déplacer, parler, regarder et interagir avec des objets.
"""
# Description: The actions module.
# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.
# The error message is stored in the MSG0 and MSG1 variables and formatted
# with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
import game
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"
class Actions:
    """    
    Gère les actions qu'un joueur peut effectuer dans le jeu.
    Cela inclut des actions comme déplacer le joueur,
    interagir avec l'environnement et gérer l'état du jeu.
    """
    def go(self,game, list_of_words, number_of_parameters):
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
        if player.current_room.name == "Manor_exit":
        # Vérifier l'inventaire du joueur pour les deux clés nécessaires.
            if "exit_key" in player.inventory and "car_key" in player.inventory:
                print("\nFélicitations ! Vous avez les deux clés et vous pouvez quitter le manoir.")
                print("Vous avez gagné le jeu !")
                game.finished = True  # Fin du jeu si les deux clés sont présentes.
                return True
            else:
                print("\nVous n'avez pas les deux clés nécessaires pour quitter le manoir.")
                print("Vous avez été tué... Le jeu est terminé.")
                game.finished = True  # Fin du jeu si les clés sont manquantes.
                return False
        return True
    def quit(self,game, list_of_words, number_of_parameters):
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
        pass
    def help(self,game, list_of_words, number_of_parameters):
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
    def back(self,game, list_of_words, number_of_parameters):
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
            print("\nImpossible de revenir en arrière,"
                  " vous n'avez visité qu'une seule pièce ou aucune.\n")
            return False
        #Removing the room from the history and going back to the room before
        player.history.pop()
        previous_room_name = player.history[-1]
        previous_room = next(room for room in game.rooms if room.name == previous_room_name)
        player.current_room = previous_room
        print(previous_room.get_long_description())
        print("\n" + player.get_history())
        return True
    def look(self,game, list_of_words, number_of_parameters):
        """
        Affiche les items présents dans la pièce actuelle,
        les objets et les personnages présents.
        """
        current_room = game.player.current_room
        if len(current_room.inventory_items) == 0:
            print("Il n'y a rien d'intéressant dans cette pièce.")
        else:
            print("La pièce contient les objets suivants :")
            for item in current_room.inventory_items.values():
                print(f"    - {item.name} : {item.description} ({item.weight}g)")
        if current_room.characters:
            print("\nPersonnages présents :")
            for character in current_room.characters.values():
                print(f"    - {character.name} : {character.description}")
        else:
            print("Il n'y a personne ici.")
            return True
    def take(self, game, list_of_words, number_of_parameters):
         """Permet au joueur de prendre un item."""
         if len(list_of_words) > number_of_parameters:
            item_name = list_of_words[1]  # Premier paramètre : nom de l'objet
            current_room = game.player.current_room
         if item_name in current_room.inventory_items:
            item = current_room.inventory_items.pop(item_name)
            game.player.add_item_to_inventory(item)
            print(f"\nVous avez pris {item_name}.")
         else:
            print("\nCet objet n'est pas présent dans cette pièce.")
        
    def drop(self,game, list_of_words, number_of_parameters):
        """Permet au joueur de déposer un item dans la pièce actuelle."""
        if len(list_of_words) != number_of_parameters + 1:
            print("Erreur dans le nombre de paramètres.")
            return False
        name_item = list_of_words[1].lower()
        name_item = list_of_words[1].lower()
        player = game.player
        current_room = player.current_room
        if name_item in player.inventory:
            item = player.inventory[name_item]
            current_room.inventory_items[name_item] = item  # Ajoute l'item à la pièce
            del player.inventory[name_item]  # Retire l'item de l'inventaire du joueur
            print(f"Vous avez déposé {item.name}.")
            return True
        else:
            print(f"Vous avez retiré {name_item} de votre inventaire.")
            return False
    def check(self,game, list_of_words, number_of_parameters):
        """Affiche l'inventaire du joueur."""
        player = game.player
        if len(player.inventory) == 0:
            print("Il n'y a rien dans votre inventaire.")
        else:
            print("Vous avez dans votre inventaire :")
            for item in player.inventory.values():
                print(f"    - {item.name} : {item.description} ({item.weight})")
    def talk(self,game, list_of_words, number_of_parameters):
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
    