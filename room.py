"""
Ce module contient la classe Room, représentant une pièce dans le jeu.
Chaque pièce a un nom, une description, des objets et des personnages.
"""
class Room:
    """
    Représente une pièce dans le jeu, avec des sorties, des objets et des personnages.

    Attributs :
        name (str): Le nom de la pièce.
        description (str): La description de la pièce.
        exits (dict): Un dictionnaire des sorties de la pièce (direction -> Room).
        inventory_items (dict): Un dictionnaire des objets présents dans la pièce.
        characters (dict): Un dictionnaire des personnages présents dans la pièce.
    """
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
        self.inventory_items={}
        self.characters = {}
    def get_exit(self, direction):
        """
        Retourne la pièce dans la direction donnée si elle existe.

        Args:
            direction (str): La direction vers laquelle le joueur veut aller.

        Returns:
            Room: La pièce de destination si elle existe, sinon None.
        """
        if direction in self.exits:
            return self.exits[direction]
        return None
    def get_exit_string(self):
        """
        Retourne une chaîne décrivant les sorties de la pièce.

        Returns:
            str: Une chaîne listant les directions disponibles.
        """
        exit_string = "Sorties: "
        for direction,room in self.exits.items():
            if room:
                exit_string += direction + ", "
        exit_string = exit_string.strip(", ")
        return exit_string
    def get_long_description(self):
        """
        Retourne une description détaillée de la pièce, incluant les sorties.

        Returns:
            str: Une chaîne contenant la description de la pièce et des sorties.
        """
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
    def get_inventory_items(self):
        """
        Affiche les objets présents dans la pièce.

        Si la pièce ne contient aucun objet, un message l'indique.
        """
        if len(self.inventory_items) == 0:
            print("Il n'y a rien ici dans cette pièce")
        else:
            print("La pièce contient :")
            for item in self.inventory_items.values():
                print(f"    - {item.name} : {item.description} ({item.weight})") 
            