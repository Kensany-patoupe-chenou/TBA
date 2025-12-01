# Define the Room class.

class Room:
    """
    Class Room

    Represents a room in the game world. Each room has a name, a description,
    and a set of exits that point to other rooms

        Attributs:
            self.name(str): name of room
            self.description(str): Description of room
            self.exits(dict): exit directions

        Methods :
            get_exit(self, direction): Return the room accessible in the given direction, or None if no exit exists.
            get_exit_string(self): Return a string listing all available exit directions for this room.
            get_long_description(self): Return a detailed description of the room, including its description
            and the list of available exits.

        Examples:

    >>> swamp = Room("Swamp", "Dans un marécage sombre et ténébreux.")
    >>> tower = Room("Tower", "Au pied d'une tour gigantesque en pierre.")
    >>> swamp.exits = {"N": tower}
    >>> swamp.get_exit("N").name
    'Tower'
    >>> swamp.get_exit("S") is None
    True
    >>> swamp.get_exit_string()
    'Sorties: N'
    >>> "marécage" in swamp.get_long_description()
    True

    """

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory={}
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes dans {self.description}\n\n{self.get_exit_string()}\n"
    
    def get_inventory(self):
        """
        Affiche l'inventaire du joueur.

        Returns:
        None
        """
        if len(self.inventory) == 0:
            print("Il n'y a rien ici.")
        else:
            print("La pièce contient :")
            for item in self.inventory.values():
                print(f"    - {item.name} : {item.description} ({item.weight} kg)")
