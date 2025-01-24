"""
Ce module contient la classe Player, qui représente le joueur dans le jeu.

La classe Player gère les éléments suivants :
- Le nom du joueur.
- La pièce actuelle du joueur.
- L'historique des pièces visitées par le joueur.
- L'inventaire des objets du joueur.

La classe permet au joueur de se déplacer, de consulter son historique,
 de gérer son inventaire, etc.
"""
class Player():
    """
    Classe représentant le joueur dans le jeu.
    Le joueur a un nom, une pièce actuelle,
    un historique de pièces visitées et un inventaire d'objets.
    """
    def __init__(self, name):
        """
        Initialise un nouveau joueur.

        Args:
            name (str): Le nom du joueur.
        """
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory={}
    # Define the move method.
    def add_item_to_inventory(self, item):
        """Ajoute un objet à l'inventaire du joueur."""
        self.inventory[item.name] = item
        print(f"Vous avez ajouté {item.name} à votre inventaire.")
    def move(self, direction):
        """
        Déplace le joueur dans la direction spécifiée.

        Args:
        direction (str): La direction dans laquelle le joueur doit se déplacer.

        Returns:
        bool: True si le déplacement a réussi, False sinon.
        """
        direction = direction.upper()
        if direction in self.current_room.exits:
            next_room = self.current_room.exits[direction]
            if next_room is not None:
                self.current_room = next_room
                self.history.append(self.current_room.name)
                return True
            print("\nAucune porte dans cette direction !\n")
            return False
        print(f"\nDirection '{direction}' non valide dans cette pièce.\n")
        return False
    def get_history(self):
        """
        Retourne l'historique des pièces visitées par le joueur.

        Returns:
        str: Une chaîne représentant l'historique des pièces visitées.
        """
        history_str = "Vous avez déjà visité les pièces suivantes:\n"
        if self.history:
            history_str += "\n".join(f"     - {room_name}" for room_name in self.history[:-1])
        return history_str.strip()
    def get_inventory(self):
        """
        Affiche l'inventaire du joueur.

        Returns:
        None
        """
        if len(self.inventory) == 0:
            print("Il n'y a rien dans votre inventaire.")
        else:
            print("Vous avez dans votre inventaire :")
            for item in self.inventory.values():
                print(f"    - {item.name} : {item.description} ({item.weight})")
