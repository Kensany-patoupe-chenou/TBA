"""
Ce module contient la classe Room, représentant une pièce dans le jeu.
Chaque pièce a un nom, une description, des objets et des personnages.
"""
# Define the Room class.

class Room:
    """
    Class Room

    Represents a room in the game world. Each room has a name, a description
    and a set of exits that point to other rooms

        Attributs:
            self.name(str): name of room
            self.description(str): Description of room
            self.exits(dict): exit directions

        Methods :
            get_exit(self, direction): Return the room accessible
            in the given direction, or None if no exit exists.
            get_exit_string(self): Return a string listing all
            available exit directions for this room.
            get_long_description(self): Return a detailed description
            of the room, including its description
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
        """
        Initialise une nouvelle instance de Room.

        Args:
            name (str): Le nom de la pièce.
            description (str): La description de la pièce.
        """
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory={}
        self.characters = {}

    # Define the get_exit method.
    def get_exit(self, direction):
        """
        Retourne la pièce dans la direction donnée si elle existe.

        Args:
            direction (str): La direction vers laquelle le joueur veut aller.

        Returns:
            Room: La pièce de destination si elle existe, sinon None.
        """
        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        return None

    # Return a string describing the room's exits.
    def get_exit_string(self):
        """
        Retourne une chaîne décrivant les sorties de la pièce.

        Returns:
            str: Une chaîne listant les directions disponibles.
        """
        exit_string = "Sorties: "
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        """
        Retourne une description détaillée de la pièce, incluant les sorties.

        Returns:
            str: Une chaîne contenant la description de la pièce et des sorties.
        """
        return f"\nVous êtes dans {self.description}\n\n{self.get_exit_string()}\n"

    def get_inventory(self):
        """
        Affiche l'inventaire de la pièce.

        Returns:
        None
        """

        if not self.inventory and not self.characters:
            print("Il n'y a rien ni personne ici.")
        else:
            if  self.inventory:
                print("On voit :")
                for item in self.inventory.values():
                    print(f"    - {item.name} : {item.description} ({item.weight} kg)")
            else:
                print("Il n'y aucun objet ici mais il y'a:")

            if  self.characters:
                for character in self.characters.values():
                    print(f"    - {character.name} : {character.description}")
            else:
                print("Il n'y a personne ici.")
