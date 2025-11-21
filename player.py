# Define the Player class.
class Player():
    """
    Class Player

    Represents the player in the game. The player has a name and is located
    in a current room.
        Attributs:
            self.name(str): name of player
            current_room(Room): Room objetc

        Methods :
            move(self, direction): Return True if the move
            is successful, otherwise print an error message and return False.
        
        >>> from room import Room
        >>> from player import Player
        >>> swamp = Room("Swamp", "Un marécage sombre et ténébreux.")
        >>> tower = Room("Tower", "Une tour gigantesque en pierre.")
        >>> swamp.exits = {"N": tower}
        >>> swamp.get_exit("N").name
        'Tower'
        >>> swamp.get_exit("S") is None
        True
        >>> swamp.get_exit_string()
        'Sorties: N'

    """

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        direction = direction.upper()
        if direction in self.current_room.exits:
            next_room = self.current_room.exits[direction]

            # Set the current room to the next room.
            if next_room is not None:
                self.current_room = next_room
                #On n'ajoute dans l'historique que si la salle suivante est différente
                if not self.history or self.history[-1] != self.current_room:
                    self.history.append(next_room)

                return True
            # If the next room is None, print an error message and return False.
            print("\nAucune porte dans cette direction !\n")
            return False
    #Define the get_history method
    def get_history(self):
        """
        Retourne l'historique des pièces visitées par le joueur.

        Returns:
        str: Une chaîne représentant l'historique des pièces visitées.
        """
        history_str = "Vous avez déjà visité les pièces suivantes:\n"
        if self.history:
            history_str += "\n".join(f"     - {room.name}" for room in self.history[:-1])
        return history_str.strip()
    