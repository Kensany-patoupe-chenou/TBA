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
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True

    